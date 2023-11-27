import csv
import pandas as pd

def ceps_in_list(cep):
    switcher ={
        
    }

def sanitize(cpf):
    clean = []
    for i in cpf:
        i = str(i)
        n_cpf = i.replace('.','').replace('-','').replace('/','')
        try:
            while len(n_cpf) < 11:
                n_cpf = '0'+n_cpf            
            if len(n_cpf) == 11:
                clean.append(str(str)(n_cpf))
            else:
                clean.append(str(str)(n_cpf))
        except:
            clean.append(str(0))
    return clean

encart =pd.read_excel(r"C:/Users/leonardo_zamarchi/Sicredi/Equipe BI - Desenvolvimento Power BI - General/PROJETOS/ENCARTEIRAMENTO/SAIDA/BASE_ASSOCIADOS_TOTAL.xlsx")
encart['CPF_CNPJ'] = sanitize(encart['CPF_CNPJ'])

font0 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y0.D21217.ESTABELE'
font1 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y1.D21217.ESTABELE'
font2 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y2.D21217.ESTABELE'
font3 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y3.D21217.ESTABELE'
font4 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y4.D21217.ESTABELE'
font5 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y5.D21217.ESTABELE'
font6 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y6.D21217.ESTABELE'
font7 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y7.D21217.ESTABELE'
font8 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y8.D21217.ESTABELE'
font9 = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/K3241.K03200Y9.D21217.ESTABELE'

#fields = ['CNPJ', 'NOME', 'LOGRADOURO', 'ENDERECO', 'NUMERO', 'BAIRRO','CIDADE', 'CEP', 'ESTADO','DDD','TELEFONE','EMAIL']
fields = ['CNPJ']
fonts = [font0,font1,font2,font3,font4,font5,font6,font7,font8,font9]
content_pr = []
content_sc = []
content_sp = []
content_tst = []
n=0
for i in fonts:
    file_font = i
    with open(file_font,'r',encoding='latin-1') as f:
        for row in f:
            row = row.replace('"','')
            row = row.split(';')
            if row[19] == 'SP': 
                res = 0
                try:
                    row[18] = int(row[18])
                    if(row[18] >= 14200000 and row[18] <= 14209999):
                        cidade = 'São Simão'
                        res=1
                    elif(row[18] >= 14210000 and row[18] <= 14229999):
                        cidade = 'Luís Antônio'
                        res=1
                    elif(row[18] >= 14140000 and row[18] <= 14149999):
                        cidade = 'Cravinhos'
                        res=1
                    elif(row[18] >= 13670000 and row[18] <= 13689999):
                        cidade = 'Santa Rita do Passa Quatro'
                        res=1
                    elif(row[18] >= 89848000 and row[18] <= 89849999):
                        cidade = 'Jardinópolis'
                        res=1
                    elif(row[18] >= 14350000 and row[18] <= 14389999):
                        cidade = 'Altinópolis'
                        res=1
                    elif(row[18] >= 14340000 and row[18] <= 14349999):
                        cidade = 'Brodowski'
                        res=1
                    elif(row[18] >= 14120000 and row[18] <= 14139999):
                        cidade = 'Dumont'
                        res=1
                    elif(row[18] >= 14180000 and row[18] <= 14199999):
                        cidade = 'Pontal'
                        res=1
                    elif(row[18] >= 14390000 and row[18] <= 14399999):
                        cidade = 'Santo Antônio da Alegria'
                        res=1
                    elif(row[18] >= 14260000 and row[18] <= 14269999):
                        cidade = 'Cássia dos Coqueiros'
                        res=1
                    elif(row[18] >= 14270000 and row[18] <= 14299999):
                        cidade = 'Santa Rosa de Viterbo'
                        res=1
                    elif(row[18] >= 14150000 and row[18] <= 14159999):
                        cidade = 'Serrana'
                        res=1
                    elif(row[18] >= 14240000 and row[18] <= 14249999):
                        cidade = 'Cajuru'
                        res=1
                    elif(row[18] >= 14300001 and row[18] <= 14339999):
                        cidade = 'Batatais'
                        res=1
                    elif(row[18] >= 14860000 and row[18] <= 14869999):
                        cidade = 'Barrinha'
                        res=1
                    elif(row[18] >= 14230000 and row[18] <= 14239999):
                        cidade = 'Serra Azul'
                        res=1
                    elif(row[18] >= 14160001 and row[18] <= 14179999):
                        cidade = 'Sertãozinho'
                        res=1
                    elif(row[18] >= 14250000 and row[18] <= 14259999):
                        cidade = 'Santa Cruz da Esperança'
                        res=1
                    elif(row[18] >= 14000001 and row[18] <= 14114999):
                        cidade = 'Ribeirão Preto'
                        res=1
                    else:
                        res = 0

                    if res == 1:
                        #app = [str(row[0])+str(row[1])+str(row[2]),row[4],row[13],row[16],row[15],row[17],cidade,row[18],row[19],row[21],row[22],row[27]]
                        app = [str(row[0])+str(row[1])+str(row[2])]
                        #if encart['CPF_CNPJ'].str.contains(str(app)).any() == False:
                        content_sp.append(str(app))
                        n+=1
                        print(str(n))
                        print(app)
                except:
                    pass
            if row[19] == 'SC': 
                res = 0
                try:
                    row[18] = int(row[18])
                    if(row[18] >= 89862000 and row[18] <= 89864999):
                        cidade = 'Entre Rios'
                        res = 1
                    elif(row[18] >= 89850000 and row[18] <= 89853999):
                        cidade = 'Quilombo'
                        res = 1
                    elif(row[18] >= 89550000 and row[18] <= 89557999):
                        cidade = 'Rio das Antas'
                        res = 1
                    elif(row[18] >= 89690000 and row[18] <= 89693999):
                        cidade = 'Vargeão'
                        res = 1
                    elif(row[18] >= 89590000 and row[18] <= 89594999):
                        cidade = 'Arroio Trinta'
                        res = 1
                    elif(row[18] >= 89558000 and row[18] <= 89559999):
                        cidade = 'Iomerê'
                        res = 1
                    elif(row[18] >= 89824000 and row[18] <= 89824999):
                        cidade = 'Bom Jesus'
                        res = 1
                    elif(row[18] >= 89618000 and row[18] <= 89619999):
                        cidade = 'Monte Carlo'
                        res = 1
                    elif(row[18] >= 89832000 and row[18] <= 89833999):
                        cidade = 'Ipuaçu'
                        res = 1
                    elif(row[18] >= 89675000 and row[18] <= 89676999):
                        cidade = 'Vargem Bonita'
                        res = 1
                    elif(row[18] >= 89518000 and row[18] <= 89519999):
                        cidade = 'Macieira'
                        res = 1
                    elif(row[18] >= 89650000 and row[18] <= 89651999):
                        cidade = 'Treze Tílias'
                        res = 1
                    elif(row[18] >= 89834000 and row[18] <= 89834999):
                        cidade = 'Ouro Verde'
                        res = 1
                    elif(row[18] >= 89652000 and row[18] <= 89653999):
                        cidade = 'Ibiam'
                        res = 1
                    elif(row[18] >= 89839000 and row[18] <= 89839999):
                        cidade = 'Jupiá'
                        res = 1
                    elif(row[18] >= 89854000 and row[18] <= 89854999):
                        cidade = 'Santiago do Sul'
                        res = 1
                    elif(row[18] >= 89580000 and row[18] <= 89589999):
                        cidade = 'Fraiburgo'
                        res = 1
                    elif(row[18] >= 89654000 and row[18] <= 89659999):
                        cidade = 'Água Doce'
                        res = 1
                    elif(row[18] >= 89642000 and row[18] <= 89649999):
                        cidade = 'Tangará'
                        res = 1
                    elif(row[18] >= 89515000 and row[18] <= 89517999):
                        cidade = 'Lebon Régis'
                        res = 1
                    elif(row[18] >= 89835000 and row[18] <= 89836999):
                        cidade = 'São Domingos'
                        res = 1
                    elif(row[18] >= 89595000 and row[18] <= 89599999):
                        cidade = 'Salto Veloso'
                        res = 1
                    elif(row[18] >= 89500001 and row[18] <= 89514999):
                        cidade = 'Caçador'
                        res = 1
                    elif(row[18] >= 89837000 and row[18] <= 89837999):
                        cidade = 'Coronel Martins'
                        res = 1
                    elif(row[18] >= 89998000 and row[18] <= 89999999):
                        cidade = 'Novo Horizonte'
                        res = 1
                    elif(row[18] >= 89830000 and row[18] <= 89831999):
                        cidade = 'Abelardo Luz'
                        res = 1
                    elif(row[18] >= 89859000 and row[18] <= 89859999):
                        cidade = 'Formosa do Sul'
                        res = 1
                    elif(row[18] >= 89530000 and row[18] <= 89532999):
                        cidade = 'Frei Rogério'
                        res = 1
                    elif(row[18] >= 89838000 and row[18] <= 89838999):
                        cidade = 'Galvão'
                        res = 1
                    elif(row[18] >= 89570000 and row[18] <= 89579999):
                        cidade = 'Pinheiro Preto'
                        res = 1
                    elif(row[18] >= 89694000 and row[18] <= 89699999):
                        cidade = 'Faxinal dos Guedes'
                        res = 1
                    elif(row[18] >= 89687000 and row[18] <= 89689999):
                        cidade = 'Passos Maia'
                        res = 1
                    elif(row[18] >= 89640000 and row[18] <= 89641999):
                        cidade = 'Ibicaré'
                        res = 1
                    elif(row[18] >= 89683000 and row[18] <= 89686999):
                        cidade = 'Ponte Serrada'
                        res = 1
                    elif(row[18] >= 89860000 and row[18] <= 89861999):
                        cidade = 'Marema'
                        res = 1
                    elif(row[18] >= 89560001 and row[18] <= 89569999):
                        cidade = 'Videira'
                        res = 1
                    else:
                        res = 0
                    
                    if res == 1:
                        #app = [str(row[0])+str(row[1])+str(row[2]),row[4],row[13],row[16],row[15],row[17],cidade,row[18],row[19],row[21],row[22],row[27]]
                        app = [str(row[0])+str(row[1])+str(row[2])]
                        #if encart['CPF_CNPJ'].str.contains(str(app)).any() == False:
                        content_sc.append(str(app))
                        n+=1
                        print(str(n))
                        print(app)
                except:
                    pass
            if row[19] == 'PR': 
                res = 0
                try:
                    row[18] = int(row[18])
                    if(row[18] >= 85540000 and row[18] <= 85547999):
                        cidade = 'Mangueirinha'
                        res = 1
                    elif(row[18] >= 85520000 and row[18] <= 85524999):
                        cidade = 'Vitorino'
                        res = 1
                    elif(row[18] >= 85555000 and row[18] <= 85556999):
                        cidade = 'Palmas'
                        res = 1
                    elif(row[18] >= 85525000 and row[18] <= 85529999):
                        cidade = 'Mariópolis'
                        res = 1
                    elif(row[18] >= 85500001 and row[18] <= 85514999):
                        cidade = 'Pato Branco'
                        res = 1
                    elif(row[18] >= 85557000 and row[18] <= 85559999):
                        cidade = 'Coronel Domingos Soares'
                        res = 1
                    elif(row[18] >= 85530000 and row[18] <= 85539999):
                        cidade = 'Clevelândia'
                        res = 1
                    elif(row[18] >= 85548000 and row[18] <= 85549999):
                        cidade = 'Honório Serpa'
                        res = 1
                    elif(row[18] >= 85550000 and row[18] <= 85554999):
                        cidade = 'Coronel Vivida'
                        res = 1
                    else:
                        res = 0

                    if res == 1:
                        #app = [str(row[0])+str(row[1])+str(row[2]),row[4],row[13],row[16],row[15],row[17],cidade,row[18],row[19],row[21],row[22],row[27]]
                        app = [str(row[0])+str(row[1])+str(row[2])]
                        #if encart['CPF_CNPJ'].str.contains(str(app)).any() == False:
                        content_pr.append(str(app))
                        n+=1
                        print(str(n))
                        print(app)
                except:
                    pass

            if row[19] == 'SC': 
                res = 0
                try:
                    if(row[18] >= 88000001 and row[18] <= 88099999):
                        res = 1
                    elif(row[18] >= 88450000 and row[18] <= 88459999):
                        res = 1
                    elif(row[18] >= 88460000 and row[18] <= 88469999):
                        res = 1
                    elif(row[18] >= 88470000 and row[18] <= 88474999):
                        res = 1
                    elif(row[18] >= 88475000 and row[18] <= 88484999):
                        res = 1
                    elif(row[18] >= 88180000 and row[18] <= 88189999):
                        res = 1
                    elif(row[18] >= 88125000 and row[18] <= 88129999):
                        res = 1
                    elif(row[18] >= 88150000 and row[18] <= 88159999):
                        res = 1
                    elif(row[18] >= 88485000 and row[18] <= 88489999):
                        res = 1
                    elif(row[18] >= 88140000 and row[18] <= 88149999):
                        res = 1
                    elif(row[18] >= 88490000 and row[18] <= 88494999):
                        res = 1
                    elif(row[18] >= 88200000 and row[18] <= 88209999):
                        res = 1
                    elif(row[18] >= 88190000 and row[18] <= 88199999):
                        res = 1
                    elif(row[18] >= 88160001 and row[18] <= 88179999):
                        res = 1
                    elif(row[18] >= 88100001 and row[18] <= 88124999):
                        res = 1
                    elif(row[18] >= 88130001 and row[18] <= 88139999):
                        res = 1
                    elif(row[18] >= 88495000 and row[18] <= 88499999):
                        res = 1

                    else:
                        res = 0
                    
                    if res == 1:
                        #app = [str(row[0])+str(row[1])+str(row[2]),row[4],row[13],row[16],row[15],row[17],cidade,row[18],row[19],row[21],row[22],row[27]]
                        app = [str(row[0])+str(row[1])+str(row[2])]
                        #if encart['CPF_CNPJ'].str.contains(str(app)).any() == False:
                        content_tst.append(str(app))
                        n+=1
                        print(str(n))
                        print(app)
                except:
                    pass
with  open('C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/CNPJs/lista_pr_all.csv', 'w') as f:      
    # using csv.writer method from CSV package
    write = csv.writer(f)      
    write.writerow(fields)
    write.writerows(content_pr)

with open('C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/CNPJs/lista_sc_all.csv', 'w') as f:      
    # using csv.writer method from CSV package
    write = csv.writer(f)      
    write.writerow(fields)
    write.writerows(content_sc)

with open('C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/CNPJs/lista_sp_all.csv', 'w') as f:      
    # using csv.writer method from CSV package
    write = csv.writer(f)      
    write.writerow(fields)
    write.writerows(content_sp)

with open('C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/CNPJs/lista_tst_all.csv', 'w') as f:      
    # using csv.writer method from CSV package
    write = csv.writer(f)      
    write.writerow(fields)
    write.writerows(content_tst)
    
'''
CEPS A CONSIDERAR
89830000 a 89831999
89590000 a 89594999
89824000 a 89824999
89500001 a 89514999
89500001 a 89514999
89837000 a 89837999
89862000 a 89864999
89694000 a 89699999
89859000 a 89859999
89580000 a 89589999
89530000 a 89532999
89838000 a 89838999
89652000 a 89653999
89640000 a 89641999
89558000 a 89559999
89832000 a 89833999
89839000 a 89839999
89515000 a 89517999
89518000 a 89519999
89860000 a 89861999
89618000 a 89619999
89998000 a 89999999
89834000 a 89834999
89687000 a 89689999
89570000 a 89579999
89683000 a 89686999
89850000 a 89853999
89550000 a 89557999
89595000 a 89599999
89854000 a 89854999
89835000 a 89836999
89642000 a 89649999
89650000 a 89651999
89675000 a 89676999
89690000 a 89693999
89654000 a 89659999

14350000 a 14389999
14860000 a 14869999
14300001 a 14339999
14300001 a 14319999
14340000 a 14349999
14240000 a 14249999
14140000 a 14149999
14260000 a 14269999
14120000 a 14139999
14680000 a 14699999
14210000 a 14229999
14180000 a 14199999
14000001 a 14114999
14000001 a 14109999
14250000 a 14259999
13670000 a 13689999
14270000 a 14299999
14390000 a 14399999
14230000 a 14239999
14150000 a 14159999
14160001 a 14179999
14160001 a 14179999
14200000 a 14209999


85530000 a 85539999
85557000 a 85559999
85550000 a 85554999
85548000 a 85549999
85540000 a 85547999
85525000 a 85529999
85555000 a 85556999
85500001 a 85514999
85500001 a 85513999
85520000 a 85524999
'''


