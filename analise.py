import allbundle as b
import context as c
import json
import csv as reader
import os
import config_tools as ct
import datetime as dt
import models
from os.path import isfile , join

import pandas as pd
# Make the graphs a bit prettier, and bigger
#pd.set_option('display.mpl_style', 'default') 
#pd.set_option('display.line_width', 5000) 
pd.set_option('display.max_columns', 60) 

sku = c.select_execute_dict(ct.read('queries')['retriave_skus_ddd'])
ddd_list = c.select_execute_dict(ct.read("queries")["retriave_ddd_codigoddd"])
#operator = 'nextel'

def create_files(type_client,ddd,operator,aba):
    for d in ddd:
        try:
            ddd_cod = d['CodigoDdd']
            #print(ddd_cod)
            bun = b.get(type_client, operator, ddd_cod, aba).json()
            create_json_file(bun, f'{operator}_{type_client}_{aba}_{ddd_cod}')
        except() as error:
            print(error)


def create_json_file(json_file, filename):
    path = f'./json/{filename.split("_")[0].lower()}/'
    if os.path.exists(path):
        filename = os.path.join(path,f'{filename}.json')
    else:
        os.makedirs(path)
    with open(filename, 'w') as outfile:
       json.dump(json_file,outfile)


def all_json_paths_by_operator(operator):
    path  = f'./json/{operator.lower()}'
    return([f'{path}/{f}' for f in os.listdir(path) if isfile(join(path,f))])


def list_products_from_path(operator):
    all_json_paths_by_operator(operator)


def dataframe_difference(df1, df2, operator, which=None):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(df2,
                              indicator=True,
                              how='outer',
                              suffixes=['_allbundle','_database'],
                              on=['_sku','_codigo_ddd','_name'])
    
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
        diff_df.to_csv(f'data/{operator}_diff.csv')
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
        diff_df.to_csv(f'data/{operator}_both.csv')
    
    return diff_df


def df_groupby(df):
    df = df.reset_index(drop=True)
    df_gpby = df.groupby(list(df.columns))
    idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
    result = df.reindex(idx)
    return result


def analise_operator(operator):
    #operator = 'nextel'
    #create_files(ddd_list,operator)
    allbundle = []
    database = []
    for path in all_json_paths_by_operator(operator):
        allbundle += models.product.load_data_from_allbundle(path)
    database = models.product.load_data_from_db(sku)
    if database and allbundle:
            #print(f'database -> {str(len(database))}')
            #print(f'allbundle -> {str(len(allbundle))}')

            df_database = pd.DataFrame(database)
            df_allbundle = pd.DataFrame(allbundle)

            df_database = df_groupby(df_database)
            df_allbundle = df_groupby(df_allbundle)

            df_both = dataframe_difference(df_allbundle,df_database,operator,which='both')
            df_diff = dataframe_difference(df_allbundle,df_database,operator)

            print(df_both)
            print(df_diff)
        

def create_update_sql(operator,filter_skus):
    
    #filter_skus += lambda x: [str(sku)+'|' for sku in filter_skus]
    #print(filter_skus)
    allbundle = []
    
    for path in all_json_paths_by_operator(operator):
        allbundle += models.product.load_data_from_allbundle(path)

    if allbundle:
        #print(allbundle)
        df_allbundle = pd.DataFrame(allbundle)
        #print(df_allbundle)
        #df_allbundle = df_groupby(df_allbundle)
        #print(df_allbundle)
        
        df_filter = df_allbundle.loc[df_allbundle['_sku'].str.contains(filter_skus,regex=True)]
 
        s = tuple(df_filter['_sku'].unique())
        print(s)
        skus = c.select_execute_dict(ct.read('queries')['retreave_sku_db']+f"where CodigoSku in {tuple(s)}")
        #print(skus)
        df_skus_id = pd.DataFrame(skus)
        #print(df_skus_id)

        df_sku = df_filter.drop(['_codigo_ddd'], axis=1)
        df_sku = df_sku.drop_duplicates()
        df_sku = df_sku.merge(df_skus_id)

        #print(df_skus_id)
        
        sub_sku = df_sku[['_id_sku','_sku','_name','_description','_full_price','_complemento','_short_description']]

        sku_tuples =  [tuple(x) for x in sub_sku.values]
        print(sku_tuples)

        

        #falta carregar na interface sku_db e atualizar a base com os valores do allbundle 

        #print(df_filter.columns)
        #print(f"{df_filter[['_sku','_codigo_ddd','_full_price']]}")
        #print(df_filter.groupby('_sku'))
        #df_filter.to_csv(f'data/{operator}_allbundle.csv')


def create_update_sql_correios(operator):
    
    
    allbundle = [] #cria uma lista vazia
    
    for path in all_json_paths_by_operator(operator):
        allbundle += models.product.load_data_from_allbundle(path)

    if allbundle:
        df_allbundle = pd.DataFrame(allbundle) #lista allbundle e transforma em um dataframe(df)

        df_sku_ddd = df_allbundle[['_sku','_codigo_ddd']] #filtra dois seguentes campos do df

        sku_ddd =  [tuple(x) for x in df_sku_ddd.values] #lista de tuplas
        
        df_sku = df_allbundle.drop(['_codigo_ddd'], axis=1) #excluinda a coluna codigo ddd

        df_sku = df_sku.drop_duplicates()
        
        # força tipagem do dados
        df_sku = df_sku.astype({'_price':'float'})
        df_sku = df_sku.astype({'_ativo':'int'})
        df_sku = df_sku.astype({'_price_virtual':'float'})
        df_sku = df_sku.astype({'_full_price':'float'})

        df_sku["_produto_id"] = 1
        #df_sku['_full_price'] = 0 # precisei preencher por falta de valores no allbundle
        #df_sku['_price_virtual'] = 0


        df_sub_sku = df_sku[['_produto_id','_sku','_name','_description','_price','_ativo','_dependentes','_price_virtual','_complemento','_full_price',
        '_short_description','_options','_group']]

        sku_tuples =  [tuple(x) for x in df_sub_sku.values]

        query = f"""
        INSERT INTO [cd_catalogo_correios].[dbo].[Sku] 
        ([IdProduto],[CodigoSku],[Nome],[Descricao],[Valor],[Ativo],[MaximoDependentes],[ValorComDesconto] 
        ,[Complemento],[ValorSemDesconto],[DescricaoCurta],[Opcoes],[Grupo])
        values {str(sku_tuples)[1:-1]}"""
       
        query = query.replace('None', "''").replace('nan','null')
        print(query)
        #print(sku_ddd)

if __name__ == "__main__":
    print(f'Init->{dt.datetime.now()}')
    #analise_operator('nextel')

    #create_files('gestao',ddd_list,'Tim','voz')

    create_update_sql('tim','TNFE918|TNFE919|TPTF948')

    #create_update_sql_correios('tim')

    print(f'End->{dt.datetime.now()}')
    
    
    
    
