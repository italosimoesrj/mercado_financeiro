import requests
from datetime import datetime
import sqlite3
import time
import schedule


def extract():
    url = "http://api.coinbase.com/v2/prices/spot"
    resp = requests.get(url)
    return resp.json()

def transform(dados):
    data = datetime.now().strftime('%d/%m/%Y')
    valor = float(dados['data']['amount'])
    cripto = dados['data']['base']
    moeda = dados['data']['currency']
    
    inform = {"Data":data, "Valor": valor, "Criptomoeda":cripto,'Moeda': moeda}

    return inform

def carrega(informacao):
    db = '/home/italosimoes/Documentos/Projetos/Machine_Learning/db/databank.db'
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    cur.execute("""INSERT INTO bitcoin(data, valor,cripto,moeda)VALUES(?,?,?,?)""",(informacao['Data'],informacao['Valor'],informacao['Criptomoeda'],informacao['Moeda']))
   
    conn.commit()
    print("Dados adicionados.")
    conn.close()
    
def tarefa():
    dados = extract()
    inform = transform(dados)
    carrega(inform)
    print(inform)
    carrega(inform)
    
if __name__=='__main__':
    print('Iniciando a coleta a cada minuto')
    schedule.every(1).minute.do(tarefa)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
