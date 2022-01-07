from typing import NewType
from datetime import datetime
from Informacoes import Informacoes
import csv

def pega_informacoes():
   lista_informacoes = []
   with open('gerint_solicitacoes_mod.csv', encoding ="utf8") as csvfile:
      next(csvfile, None)
      tabela = csv.reader(csvfile, delimiter = ';')
      for linha in tabela:
         informacoes_lendo = Informacoes(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18])
         lista_informacoes.append(informacoes_lendo)
   return lista_informacoes


def verificar_cidade(lista_de_info):
    cidade = input("Digite um município: ").upper()
    soma_idades_F = 0
    soma_idades_M = 0
    contador_idade_m = 0
    contador_idade_f = 0 
    for informacoes in lista_de_info:
        if informacoes.get_municipio_residencia() == cidade:
       
            if informacoes.get_sexo() == "MASCULINO": 
               soma_idades_M += float(informacoes.get_idade())
               contador_idade_m += 1
         
            elif informacoes.get_sexo() == "FEMININO": 
                soma_idades_F += float(informacoes.get_idade())
                contador_idade_f += 1

    if(contador_idade_f == 0 and contador_idade_m == 0):
        print("\nCidade não encontrada\n")
    else:
        print("\n\nA: Número total de pacientes do municipio: ", contador_idade_m + contador_idade_f, "\n\nB: 1. Média de idade Masculina:",soma_idades_M / contador_idade_m,"|||| 2. Média de idade Feminina: ", soma_idades_F / contador_idade_f, "\n\nC: Idade média de todos os pacientes: ", soma_idades_F + soma_idades_M / contador_idade_f + contador_idade_m, "\n\n")


def exibir_listas(lista_de_info):

    cidade = input("Digite um município: ").upper()
    cont2018 = 0
    cont2019 = 0
    cont2020 = 0
    cont2021 = 0
    for informacoes in lista_de_info:
        if informacoes.get_municipio_residencia() == cidade:
            data = datetime.strptime(informacoes.get_data_internacao(), '%Y-%m-%d %H:%M:%S.%f')
            if data.year == 2018:
                cont2018 += 1
            if data.year == 2019:
                cont2019 += 1
            if data.year == 2020:
                cont2020 += 1
            if data.year == 2021:
                cont2021 += 1
    if(cont2018 == 0 and cont2019 == 0 and cont2020 == 0 and cont2021 == 0):
        print("Cidade não encontrada")
        
    if(cont2018 > 0 or cont2019 > 0 or cont2020 > 0 or cont2021 > 0):
        print("Número de pacientes em: ", "\n2018: ", cont2018, "\n2019: ", cont2019, "\n2020: ", cont2020, "\n2021: ", cont2021, "\n")
                      

def consultar_hospitais(lista_de_info):
    intvalidate = 0
    executante = input("Digite o nome de um executante: ").upper()
    for informacoes in lista_de_info:
        if executante == informacoes.get_executante():
           intvalidate += 1  
           print("\n\n============================================================================", "\nIdade: ", informacoes.get_idade(),"\nMunicipio Residencial: ", informacoes.get_municipio_residencia(),"\nSolicitante: ", informacoes.get_solicitante(),"\nData da autorizacao: ", informacoes.get_data_autorizacao(),"\nData da internacao: ", informacoes.get_data_internacao(),"\nData da alta: ", informacoes.get_data_alta(),"\nNome do executante: ", informacoes.get_executante(), "\n============================================================================\n\n")
    if intvalidate == 0: 
        print("\nExecutante não encontrado.\n") 
        

def calculo(lista_de_info):
    intvalidate = 0
    solicitante = input("Digite um Estabelecimento de Saúde: ").upper()
    for informacoes in lista_de_info:
        if informacoes.get_solicitante() == solicitante:
           intvalidate += 1 
           d1 = datetime.strptime(informacoes.get_data_solicitacao(), '%d/%m/%Y') 
           d2 = datetime.strptime(informacoes.get_data_alta(), '%Y-%m-%d %H:%M:%S.%f')
           sub = abs((d2 - d1).days)
           print("\n\nUsuário: ", informacoes.get_id_usuario(), "\nExecutante: ", informacoes.get_executante(), "\nTempo: ", sub, "dia(s)\n\n")
    if intvalidate == 0:
        print("\nSolicitante não encontrado\n")

def determinar_tempo(lista_de_info):
    hora1 = hora2 = hora3 = hora4 = hora5 = 0
    info1 = info2 = info3 = info4 = info5 = Informacoes(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

    for informacoes in lista_de_info:
       horacheck = int(informacoes.get_horas_na_fila())
       if horacheck > hora1 or horacheck > hora2 or horacheck > hora3 or horacheck > hora4 or horacheck > hora5:
           if hora1 <= hora2 and hora1 <= hora3 and hora1 <= hora4 and hora1 <= hora5:
               hora1 = horacheck
               info1 = informacoes 

           elif hora2 <= hora1 and hora2 <= hora3 and hora2 <= hora4 and hora2 <= hora5: 
               hora2 = horacheck
               info2 = informacoes 

           elif hora3 <= hora1 and hora3 <= hora2 and hora3 <= hora4 and hora3 <= hora5:
               hora3 = horacheck
               info3 = informacoes

           elif hora4 <= hora1 and hora4 <= hora2 and hora4 <= hora3 and hora4 <= hora5:    
               hora4 = horacheck
               info4 = informacoes

           else:    
               hora5 = horacheck
               info5 = informacoes
           
    
    print("\n\nCaso 1: ", info1.ToString(), "\n\nCaso 2: ", info2.ToString(), "\n\nCaso 3: ", info3.ToString(), "\n\nCaso 4: ", info4.ToString(), "\n\nCaso 5: ", info5.ToString()) 



def main():

    lista_de_info = pega_informacoes()

    while True:

        print(" ===MENU===")
        print("\n 1.Consultar média de idade dos pacientes.\n 2.Consultar internações por ano.\n 3.Consultar hospitais.\n 4.Calcular tempo de internação.\n 5.Determinar tempo de espera na fila.\n 6.Terminar o programa.")
        opcao = int(input("\nEscolha uma das opções:\n"))
        
        if opcao == 1:     
            verificar_cidade(lista_de_info)
                   
        elif opcao == 2:
            exibir_listas(lista_de_info)
           
        elif opcao == 3:
            consultar_hospitais(lista_de_info)

        elif opcao == 4:
            calculo(lista_de_info)

        elif opcao == 5:
            determinar_tempo(lista_de_info)

        elif opcao == 6:
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida.\nPor favor, digite um valor de 1 a 6.")

main()