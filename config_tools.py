import os
import json

def read(attr):
    with open(file='./config.json',mode='r',encoding='UTF-8') as conf:
        cfg = json.loads(conf.read())
        return cfg[f'{attr}']

if __name__ == "__main__":
    print(read('connect_string'))