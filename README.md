**Readme: Explicação do Funcionamento do Código**

**Descrição:**
Este código em Python utiliza a biblioteca Pandas para realizar algumas operações com tabelas de dados. Ele carrega informações sobre o eleitorado e resultados de uma eleição em São Paulo, tenta mesclar essas tabelas e, em seguida, permite ao usuário selecionar um candidato para obter o número de eleitores que o apoiaram.

**Passos do Código:**

1. **Importação de Bibliotecas:**
   As bibliotecas Pandas e NumPy são importadas para realizar operações relacionadas a análise de dados.

2. **Carregamento de Dados:**
   Duas tabelas de dados são carregadas a partir de arquivos CSV usando a função `pd.read_csv()`. Essas tabelas contêm informações sobre o eleitorado e os resultados de uma eleição em São Paulo.

3. **Concatenação de Tabelas:**
   As duas tabelas carregadas são concatenadas usando a função `pd.concat()`. O argumento `ignore_index=True` é usado para reindexar as linhas. Isso cria uma única tabela combinando os dados de ambas as tabelas.

4. **Substituição de Valores:**
   A função `replace()` é usada para substituir todos os valores -1 por 'NULO' e valores NaN por '-' na tabela combinada. Isso é feito para melhorar a estética e legibilidade dos dados.

5. **Seleção de Candidato:**
   O usuário é solicitado a inserir o nome de um candidato. Com base na entrada do usuário, a tabela combinada é filtrada para encontrar todas as linhas onde o nome do candidato corresponde à coluna 'NM_VOTAVEL'.

6. **Verificação e Impressão:**
   Verifica-se se o DataFrame resultante da seleção não está vazio (ou seja, se o candidato foi encontrado na tabela). Se o candidato for encontrado, o código extrai o número de eleitores (QT_ELEITORES) associados a esse candidato e o imprime. Caso contrário, uma mensagem informando que o candidato não foi encontrado é exibida.

**Observações:**
- O código assume que os arquivos CSV contêm colunas específicas ('NM_VOTAVEL' e 'QT_ELEITORES') para o nome do candidato e a quantidade de eleitores, respectivamente.
- A concatenação de tabelas foi realizada mesmo que os dados das colunas não fossem iguais, o que pode não resultar em uma combinação precisa dos dados. No entanto, isso foi feito devido a conhecimentos básicos em Pandas.

**Melhorias Possíveis:**
1. **Verificação de Correspondência de Dados:**
   Seria ideal verificar se há uma coluna comum entre as tabelas para realizar uma junção (merge) mais precisa, em vez de apenas concatenar. Isso garantiria que os dados correspondessem corretamente.

2. **Manipulação de Dados Ausentes:**
   Em vez de substituir valores NaN por '-', você poderia explorar opções como preencher valores ausentes com algum valor padrão ou estratégia de imputação mais adequada.

3. **Melhor Mensagem de Saída:**
   Ao informar que um candidato não foi encontrado, você poderia fornecer mais detalhes sobre os nomes dos candidatos disponíveis na tabela ou verificar possíveis erros de digitação.

4. **Manipulação de Entrada do Usuário:**
   Pode ser útil adicionar tratamento de entrada do usuário, como tornar a entrada do nome do candidato em letras maiúsculas ou minúsculas para evitar discrepâncias de caixa.

Lembre-se de que a exploração e manipulação de dados com Pandas podem se tornar mais complexas à medida que você avança para cenários de dados mais detalhados e exigentes.
