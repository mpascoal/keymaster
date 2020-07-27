import json 
import requests


def get(type_client,operator,ddd,aba):
    r = requests.get(
        #type_client:
        # gestao = pf e pj
        # corp = pf
        f'http://{type_client}.qa01.celulardireto.com.br/api_cd/vendas/select_product.php?operator={operator.lower()}&ddd={ddd}&aba={aba}&type=allbundle'
           
    )
    return r

if __name__ == "__main__":
    print(get("gestao","nextel","11","voz"))