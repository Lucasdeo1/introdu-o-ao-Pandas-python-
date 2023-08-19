import pandas as pd

tabela = pd.read_csv('C:/Users/adm/OneDrive/Área de Trabalho/task/eleitorado/perfil_eleitorado_2020/perfil_eleitorado_2020.csv', sep=';', encoding='ISO-8859-1')
tabela2 = pd.read_csv('C:/Users/adm/OneDrive/Área de Trabalho/task/resultados/resultadosSP_turno_1.csv', sep=';', encoding='ISO-8859-1')

#print(tabela)
#print(tabela2)



#tabelasJuntadas = pd.concat([tabela, tabela2], ignore_index=True , keys=['tabela', 'tabela2'])
#tabelasJuntadas = pd.concat([tabela, tabela2], keys=['tabela', 'tabela2'])
#print(tabelasJuntadas)
tabelaMerge = pd.merge(tabela, tabela2)

print(tabelaMerge)