import re
import requests 
import time
import csv
import pandas as pd
import os
import datetime


def consultaReceita():
  CNPJ = input('Digite um CNPJ:')
  CNPJ = re.sub('[0-9]', '', CNPJ)

  URL = ('https://www.receitaws.com.br/v1/cnpj/' + CNPJ)

  r = requests.get(url = URL)
  data = r.json()
  status = data['status']
  f = open("RelCNPJ.txt", "a")
  if status == 'OK':
    situacao = data['situacao']
    if situacao == 'ATIVA':
      print('A situação do CNPJ '+CNPJ+' é '+ str(situacao))      
    else:
      f.write('\n A situação do CNPJ '+CNPJ+' é '+ str(situacao))
  elif status == 'ERROR':
    mensagem = data['message']
    if (len(mensagem) > 20):
      f.write('\n'+CNPJ+ ' CNPJ Rejeitado pela Receita')
    else:
      f.write('\n'+CNPJ+ ' CNPJ Inválido')    
  f.close()



#consultaReceita()

def geraCsv(filename):
    df = pd.read_excel(filename, sheet_name=None)
    for key, value in df.items():
        return df[key].to_csv('%s.csv' % key)


def valida_base_cnpj(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
        base = []
        for cnpj in csv_list:     
            try:
                #entre [] deve ser informado o indice da coluna que contém o numero de CNPJ no arquivo .csv
                CNPJ = re.sub('[^0-9]+', '', str(cnpj[0]))

                while len(CNPJ) < 14:
                    CNPJ =  "0"+str(CNPJ)
                #tempo 21 segundos mínimo entre cada pesquisa para manter a regra de plano gratuito da plataforma
                time.sleep(21)
                print(datetime.datetime.now())
                URL = ('https://www.receitaws.com.br/v1/cnpj/' + CNPJ)
                r = requests.get(url = URL)
                data = r.json()
                print(str(data))
                base.append(data)
            except:
               time.sleep(21)
        
        base.to_clipboard()
               


valida_base_cnpj('C:/Users/leonardo_zamarchi/Desktop/cnpj_inap.csv')
