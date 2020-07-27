import json
import analise

class product(object):
    # campos como o allbundle
    def __init__(self,sku,codigo_ddd,name=None,description=None,price_virtual=None,full_price=None,price=None,group=None,dependentes=None,
                dependentes_gratis=None,grupo_cidade_uf=None,prod_internet_net=None,adesao=None,adesao_parcelas=None,
                adesao_pre_paga=None,adesao_nao_fidelidade=None,adesao_acrescimo_nao_dcc=None,acrescimo_nao_dcc=None,
                acrescimo_nao_fd=None,acrescimo_nao_dccfd=None,taxa_instalacao=None,short_description=None,modality=None,
                nomenclatura_sap=None,dados_valor=None,ddd_descricao=None,ddd_valor=None,options=None,
                minutos_offnet_descricao=None,minutos_offnet_valor=None,minutos_onnet_descricao=None,
                minutos_onnet_valor=None,sms_descricao=None,special_price=None,resumo_plano=None,sms_valor=None,
                sms_on_net=None,sms_off_net=None,sms_onnet_charge=None,sms_offnet_charge=None,minute_base=None,
                minute_landline=None,ativo=False,complemento=None):
        
        self._sku = sku
        self._codigo_ddd = codigo_ddd
        self._name = name
        self._description = description
        self._price_virtual = price_virtual
        self._full_price = full_price
        self._price = price
        self._group = group
        self._dependentes = dependentes
        self._dependentes_gratis = dependentes_gratis
        self._grupo_cidade_uf = grupo_cidade_uf
        self._prod_internet_net = prod_internet_net
        self._adesao = adesao
        self._adesao_parcelas = adesao_parcelas
        self._adesao_pre_paga = adesao_pre_paga
        self._adesao_nao_fidelidade = adesao_nao_fidelidade
        self._adesao_acrescimo_nao_dcc = adesao_acrescimo_nao_dcc
        self._acrecimo_nao_dcc = acrescimo_nao_dcc
        self._acrecimo_nao_fd = acrescimo_nao_fd
        self._acrecimo_nao_dccfd = acrescimo_nao_dccfd
        self._taxa_de_instalacao = taxa_instalacao
        self._short_description = short_description
        self._modalidy = modality
        self._nomenclatura_sap = nomenclatura_sap
        self._dados_valor = dados_valor
        self._ddd_descricao = ddd_descricao
        self._ddd_valor = ddd_valor
        self._options = options
        self._minutos_offnet_descricao = minutos_offnet_descricao
        self._minutos_offnet_valor = minutos_offnet_valor
        self._minutos_onnet_descricao = minutos_onnet_descricao
        self._minutos_onnet_valor = minutos_onnet_valor
        self._sms_descricao = sms_descricao
        self._special_price = special_price
        self._resumo_plano = resumo_plano
        self._sms_valor = sms_valor
        self._sms_on_net = sms_on_net
        self._sms_off_net = sms_off_net
        self._sms_onnet_charge = sms_offnet_charge
        self._sms_offnet_charge = sms_offnet_charge
        self._minute_base = minute_base
        self._minute_landline = minute_landline
        self._ativo = ativo
        self._complemento = self.compl()
    
    
    def compl(self):
        str = f'{{"dados_valor":"{self._dados_valor}","ddd_descricao":"{self._ddd_descricao}","ddd_valor":"{self._ddd_valor}",' +\
              f'"minutos_offnet_valor":"{self._minutos_offnet_valor}","minutos_offnet_decricao":"{self._minutos_offnet_descricao}",'+\
              f'"minutos_onnet_valor":"{self._minutos_onnet_valor}","sms_descricao":"{self._sms_descricao}","sms_valor":"{self._sms_valor}",'+\
              f'"sms_on_net":"{self._sms_on_net}","sms_off_net":"{self._sms_off_net}","sms_onnet_charge":"{self._sms_onnet_charge}",'+\
              f'"sms_offnet_charge":"{self._sms_offnet_charge}","minute_base": "{self._minute_base}","minute_landline":"{self._minute_landline}"}}'
        return str


    def load_data_from_allbundle(json_path):
        with open(json_path,'r',encoding='UTF-8') as file:
            _codigo_ddd = str(json_path.split('/')[-1].split('_')[-1].split('.')[0])
            print(_codigo_ddd)
            result = []
            obj = json.loads(file.read())[0]
            
            #for o in (obj['options_simple']['products']):
            #    result.append(product(#id=o['id'],
            #        sku=o['sku'],
            #        codigo_ddd=_codigo_ddd,
            #        name=o['name'],
            #        price=o['price_simple']
            #    ).__dict__)
               
            for o in (obj['options_virtual']['products']['Planos']['itens']):
                result.append(product(
                    sku=o['sku'],
                    codigo_ddd=_codigo_ddd,
                    name=o['name'],
                    description=o['description'],
                    #price_virtual=o['price_virtual'],
                    full_price=o['full_price'],
                    price=o['price'],
                    group=o['group'],
                    #dependentes=o['dependentes'],
                    #dependentes_gratis=o['dependentes_gratis'],
                    #grupo_cidade_uf=o['grupo_cidade_uf'],
                    #prod_internet_net=o['prod_internet_net'],
                    #adesao=o['adesao'],
                    #adesao_parcelas=o['adesao_parcelas'],
                    #adesao_pre_paga=o['adesao_pre_paga'],
                    #adesao_nao_fidelidade=o['adesao_nao_fidelidade'],
                    #adesao_acrescimo_nao_dcc=o['adesao_acrescimo_nao_dcc'],
                    #acrescimo_nao_dcc=o['acrescimo_nao_dcc'],
                    #acrescimo_nao_fd=o['acrescimo_nao_fd'],
                    #acrescimo_nao_dccfd=o['acrescimo_nao_dccfd'],
                    #taxa_instalacao=o['taxa_instalacao'],
                    short_description=o['short_description'],
                    #modality=o['modality'],
                    #nomenclatura_sap=o['nomenclatura_sap'],
                    dados_valor=o['dados_valor'],
                    ddd_descricao=o['ddd_descricao'],
                    ddd_valor=o['ddd_valor'],
                    options=o['options'],
                    minutos_offnet_descricao=o['minutos_offnet_descricao'],
                    minutos_offnet_valor=o['minutos_offnet_valor'],
                    minutos_onnet_descricao=o['minutos_onnet_descricao'],
                    minutos_onnet_valor=o['minutos_onnet_valor'],
                    sms_descricao=o['sms_descricao'],
                    #special_price=o['special_price'],
                    resumo_plano=o['resumo_plano'],
                    sms_valor=o['sms_valor'],
                    sms_on_net=o['sms_on_net'],
                    sms_off_net=o['sms_off_net'],
                    sms_onnet_charge=o['sms_onnet_charge'],
                    sms_offnet_charge=o['sms_offnet_charge'],
                    minute_base=o['minute_base'],
                    minute_landline=o['minute_landline'],
                    ativo=True
                ).__dict__)
            return(result)


    def load_data_from_db(list_obj_skus):
        result = []
        for o in list_obj_skus:
            complemento = json.loads(o['Complemento'])
            result.append(product(
                sku=o['CodigoSku'],
                codigo_ddd=str(o['CodigoDdd']),
                name=o['Nome'],
                description=o['Descricao'],
                #price_virtual=o['price_virtual'],
                full_price=o['Valor'],
                price=o['ValorComDesconto'],
                group=o['Grupo'],
                dependentes=o['MaximoDependentes'],
                #dependentes_gratis=o['dependentes_gratis'],
                #grupo_cidade_uf=o['grupo_cidade_uf'],
                #prod_internet_net=o['prod_internet_net'],
                #adesao=o['adesao'],
                #adesao_parcelas=o['adesao_parcelas'],
                #adesao_pre_paga=o['adesao_pre_paga'],
                #adesao_nao_fidelidade=o['adesao_nao_fidelidade'],
                #adesao_acrescimo_nao_dcc=o['adesao_acrescimo_nao_dcc'],
                #acrescimo_nao_dcc=o['acrescimo_nao_dcc'],
                #acrescimo_nao_fd=o['acrescimo_nao_fd'],
                #acrescimo_nao_dccfd=o['acrescimo_nao_dccfd'],
                #taxa_instalacao=o['taxa_instalacao'],
                short_description=o['DescricaoCurta'],
                #modality=o['modality'],
                #nomenclatura_sap=o['nomenclatura_sap'],
                dados_valor=complemento['dados_valor'],
                ddd_descricao=complemento['ddd_descricao'],
                ddd_valor=complemento['ddd_valor'],
                options=o['Opcoes'],
                #minutos_offnet_descricao=complemento['minutos_offnet_descricao'],
                minutos_offnet_valor=complemento['minutos_offnet_valor'],
                #minutos_onnet_descricao=complemento['minutos_onnet_descricao'],
                minutos_onnet_valor=complemento['minutos_onnet_valor'],
                sms_descricao=complemento['sms_descricao'],
                #special_price=o['special_price'],
                resumo_plano=o['ResumoPlano'],
                sms_valor=complemento['sms_valor'],
                sms_on_net=complemento['sms_on_net'],
                sms_off_net=complemento['sms_off_net'],
                sms_onnet_charge=complemento['sms_onnet_charge'],
                sms_offnet_charge=complemento['sms_offnet_charge'],
                minute_base=complemento['minute_base'],
                minute_landline=complemento['minute_landline'],
                ativo=True
            ).__dict__)
        return(result)


        def update_query():
            header = 'UPDATE FROM '
            result = []
         
            set = f"""
                [CodigoSku] = {_sku}
                ,[Nome] = {_name}
                ,[Descricao] = {_description}
                ,[Valor] = {_price}
                ,[Ativo] = {_ativo}
                ,[MaximoDependentes] = {_dependentes}
                ,[SkuTipoPessoa]
                ,[SkuTipoPessoaDescricao]
                ,[ValorComDesconto]
                ,[Complemento]
                ,[SkuTipoPagamento]
                ,[SkuTipoPagamentoDescricao]
                ,[ValorSemDesconto]
                ,[MaximoDependentesGratis]
                ,[ValorAparelho]
                ,[DescricaoCurta]
                ,[Opcoes]
                ,[Grupo]
                ,[ResumoPlano]
                ,[IdUpSell]
            """


class sku_db(object):
    def __init__(self, id_produto, id_sku, codigo_sku, nome, descricao, valor, ativo, maximo_dependentes,
                sku_tipo_pessoa, sku_tipo_pessoa_descricao, valor_com_desconto, complemento, sku_tipo_pagamento,
                sku_tipo_pagamento_descricao, valor_sem_desconto, maximo_dependentes_gratis, valor_aparelho,
                descricao_curta, opcoes, grupo, resumo_plano, id_up_sell):
        self._id_sku = id_sku
        self._id_produto = id_produto
        self._codigo_sku = codigo_sku
        self._nome = nome
        self._descricao = descricao
        self._valor = valor
        self._ativo = ativo
        self._maximo_dependentes = maximo_dependentes
        self._sku_tipo_pessoa = sku_tipo_pessoa
        self._sku_tipo_pessoa_descricao = sku_tipo_pessoa_descricao
        self._valor_com_desconto = valor_com_desconto
        self._complemento = complemento
        self._sku_tipo_pagamento = sku_tipo_pagamento
        self._sku_tipo_pagamento_descricao = sku_tipo_pagamento_descricao
        self._valor_sem_desconto = valor_sem_desconto
        self._maximo_dependentes_gratis = maximo_dependentes_gratis
        self._valor_aparelho = valor_aparelho
        self._descricao_curta = descricao_curta
        self._opcoes = opcoes
        self._grupo = grupo
        self._resumo_plano = resumo_plano
        self._id_up_sell =id_up_sell
  

class complement(object):
    def __init__(self,dados_valor,ddd_descricao,ddd_valor,
              minutos_offnet_valor,minutos_offnet_descricao,
              minutos_onnet_valor,sms_descricao,sms_valor,
              sms_on_net,sms_off_net,sms_onnet_charge,
              sms_offnet_charge,minute_base,minute_landline
             ):
        self._dados_valor = dados_valor
        self._ddd_descricao = ddd_descricao
        self._ddd_valor = ddd_valor
        self._minutos_offnet_valor = minutos_offnet_valor
        self._minutos_offnet_descricao = minutos_offnet_descricao
        self._minitos_offnet_valor = minutos_offnet_valor
        self._minutos_onnet_valor = minutos_onnet_valor
        self._sms_descricao = sms_descricao
        self._sms_valor = sms_valor
        self._sms_on_net = sms_on_net
        self._sms_off_net = sms_off_net
        self._sms_offnet_charge = sms_offnet_charge
        self._minute_base = minute_base
        self._minute_landline = minute_landline

    def as_dict():
        return self.__dict__()

if __name__ == "__main__":
    #json_path = "./json/nextel/nextel_11.json"

    db = product.load_data_from_db(analise.sku)
    print(db[0])

    a = product.load_data_from_allbundle('./json/nextel/nextel_11.json')
    print(a[0])