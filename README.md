# Código para Análise de Dados Eleitorais

Este repositório contém um script em Python projetado para analisar e combinar dados eleitorais de duas fontes diferentes. O objetivo do código é proporcionar insights valiosos a partir dos dados eleitorais, permitindo uma análise aprofundada das informações. A biblioteca `pandas` é utilizada para manipulação e processamento dos dados.

## Funcionamento

O código opera da seguinte maneira:

1. Importação de Bibliotecas:
   O código começa importando a biblioteca `pandas` para a manipulação dos dados.

```python
import pandas as pd
```

2. Carregamento dos Dados:
   O código carrega dois conjuntos de dados: um arquivo CSV contendo informações sobre o perfil do eleitorado em 2020 e outro arquivo CSV contendo resultados eleitorais do primeiro turno em São Paulo.

```python
tabela = pd.read_csv('C:/Users/adm/OneDrive/Área de Trabalho/task/eleitorado/perfil_eleitorado_2020/perfil_eleitorado_2020.csv', sep=';', encoding='ISO-8859-1')
tabela2 = pd.read_csv('C:/Users/adm/OneDrive/Área de Trabalho/task/resultados/resultadosSP_turno_1.csv', sep=';', encoding='ISO-8859-1')
```


## Como Usar

1. Certifique-se de ter o Python instalado em sua máquina.

2. Instale a biblioteca `pandas` caso ainda não tenha instalado:
   ```
   pip install pandas
   ```

3. Faça o download deste script e dos arquivos de dados que serão utilizados.

4. Edite as linhas que contêm os caminhos dos arquivos CSV para corresponder aos caminhos dos arquivos em seu sistema:

```python
tabela = pd.read_csv('caminho/do/arquivo/perfil_eleitorado_2020.csv', sep=';', encoding='ISO-8859-1')
tabela2 = pd.read_csv('caminho/do/arquivo/resultadosSP_turno_1.csv', sep=';', encoding='ISO-8859-1')
```

5. Execute o script e observe os resultados da análise.

## Conclusão

Este código é uma ferramenta útil para combinar e analisar dados eleitorais de diferentes fontes. Ele demonstra como usar a biblioteca `pandas` para carregar, processar e combinar dados, proporcionando insights valiosos para análises posteriores. Sinta-se à vontade para adaptar e expandir este código de acordo com suas necessidades específicas.
