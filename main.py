import pandas as pd
import numpy as np

tabela = pd.read_csv('C:\\Users\\adm\OneDrive\\Área de Trabalho\\developments\\trarefaUsandoPandas\\introducao-ao-Pandas-python--main\\eleitorado\\perfil_eleitorado_2020\\perfil_eleitorado_2020.csv', sep=';', encoding='ISO-8859-1')
tabela2 = pd.read_csv('C:\\Users\\adm\OneDrive\\Área de Trabalho\developments\\trarefaUsandoPandas\\introducao-ao-Pandas-python--main\\resultados\\resultadosSP_turno_1.csv', sep=';', encoding='ISO-8859-1')

#print(tabela)
#print(tabela2)


tabelasJuntadas = pd.concat([tabela, tabela2], ignore_index=True)

# Substituindo todos os valores -1 por NULO e NaN por '-' (sei lá estetica viu haha)
tabelasJuntadas = tabelasJuntadas.replace(-1, 'NULO')
tabelasJuntadas = tabelasJuntadas.replace(np.nan , '-')

# Imprime tabela com eles modificados modificado
print(tabelasJuntadas)

candidato = input('selecione o canditado')

candidato_df = tabelasJuntadas[tabelasJuntadas['NM_VOTAVEL'] == candidato]

if not candidato_df.empty:
    qt_eleitores = candidato_df.iloc[0]['QT_ELEITORES']
    qt_eleitores = candidato_df.iloc[0]['QT_ELEITORES']
    
    print(f'O candidato {candidato} teve {qt_eleitores} mil eleitores.')
else:
    print(f'O candidato {candidato} não foi encontrado.')



