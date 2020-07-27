import pymssql
import config_tools
#import log

cfg_server = config_tools.read("connect_string")['server']
cfg_database = config_tools.read('connect_string')["correios"]
cfg_user = config_tools.read("connect_string")["user"]
cfg_password = config_tools.read("connect_string")["password"]


def get_connection():
    conn = pymssql.connect(
        server=cfg_server,
        database=cfg_database,
        user=cfg_user,
        password=cfg_password
    )
    return conn


def select_execute(query):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(query)
                result = cursor.fetchone()[0]
                return str(result)
            except:
                return ''


def select_execute_list(query):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Exception as error:
                return [str(error)]


def select_execute_dict(query):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(query)
                columns = [column[0] for column in cursor.description]
                #print(columns)
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
                return results
            except Exception as error:
                return [str(error)]


def obj_recovery(obj):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            query = obj.recovery_query
            if query:
                try:
                    cursor.execute(query)
                    result = cursor.fetchone()[0]
                    return result
                except Exception as error:
                    #log.write_log(repr(error))
                    return None


def update_obj(obj, key):
    query = obj.update_query(key)
    try:
        execute_query(query)
    except Exception as error:
        raise error


def insert_objs(list_objs):
    for o in list_objs:
        key = obj_recovery(o)
        query = o.insert_query
        print(query)
        if key is None:
            try:
                execute_query(query)
            except Exception as error:
                #log.write_log(repr(error)+" <-> "+query)
                pass
        else:
            try:
                update_obj(o, key)
            except Exception as error:
                #log.write_log(repr(error)+" <-> "+key)
                pass


def insert_objs_query(query):

    try:
        execute_query(query)
    except Exception as error:
        #log.write_log(repr(error)+" <-> "+query)
        pass


def execute_query(query):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()
    except Exception as error:
        print(error)
        print(query)
        raise Exception('Execute Query: Sql Inválido')


if __name__ == '__main__':
    #query = config_tools.read('queries')['retriave_skus']
    
    query1 = """ SELECT * FROM cd_catalogo_correios.dbo.Ddd"""

    r = select_execute_dict(query1)
    print(r)
