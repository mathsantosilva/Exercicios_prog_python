# Ordem decrescente - Bubble sort

### Como funciona? Explique a sequência de operações.
- O valor chega como int
- O valor é transformado em Str
- OBS: Não e possivel interar sobre um valor inteiro
- Essa str é iterado e os valores viram um list
- E criada uma variavel de controle chamada trocas
- Essa variavel vai controlar o While por isso a variavel nasce com valor True
- Após entrar no While o valor da variavel e alterado para False
- O list e iterado por um FOR
- Ao criar o FOR é passado o range (len(list) - 1), porque em toda passada do for o if esta comparando o indice atual (list[i]) com +1 (list[i +1]) isso poderia gerar acesso a indices que não existem como indice[5] o que causaria erro no programa
- Usando os indices para acessar os valores do list
- E comparando se o valor do numero no indice atual e menor que o valor presente no proximo indice
- Se a condição for verdadeira os numeros invertem a posição entre eles
- E é sinalizado pela variavel "troca" que houve manipulação no list
- O FOR prossegue e compara a proxima dupla
- Quando o for termina, o While repete o processo caso a variavel troca seja true
- Após concluir o looping toda a lista é unida utilizando o join, com isso a lista passa a ser uma str
- E por ultimo o return transforma a str em int antes de enviar 

### Por que funciona? Explique o raciocínio por trás das decisões, principalmente as condições e repetições.
- Porque ele compara todas as posições, com as proximas, garantindo que em todas as passadas os valores menores serão deslocados para o proximo caso haja necessidade
- Na primeira passagem do for, ele já garante que o menor numero já se encontre na ultima posição, então no caso do numero 1, quando o for terminar de iterar ele estará na ultima casa da list
- A variavel de controle me garante uma nova execução do for sempre que houver mudanças nas posições

### Quando termina ou falha? Explique a condição de parada e os casos especiais.
- O controle de execução fica a cargo do while, mas especificadamente da variavel troca
- Enquanto ela for true o while ira repetir o processo
- Ela sempre será true caso haja necessidade de trocar numeros de posições
- Na iteração do FOR a variavel troca só será alterada para True caso alguma troca de posição dos numeros tenta sido realizada
- Sendo assim mantendo a variavel de controle como false e terminando o while na proxima tentativa

# Simulação de execução:
### inicio do codigo
- Int: 42153
- Str: '42153'
- list: ['4','2','1','5','3']
- troca: True

1. WHILE troca: True:
   - Inicia o WHILE
   - list: ['4','2','1','5','3']
   - troca: False

   1. FOR:
      - indice Atual: 0 - Valor: 4 | proximo indice: 1 - Valor: 2
      - troca: False
      - list: ['4','2','1','5','3']
   2. FOR:
      - indice Atual: 1 - Valor: 2 | proximo indice: 2 - Valor: 1
      - troca: False
      - list: ['4','2','1','5','3']
   3. FOR:
      - indice Atual: 2 - Valor: 1 | proximo indice: 3 - Valor: 5
      - troca: True
      - list: ['4','2','5','1','3']
   4. FOR:
      - indice Atual: 3 - Valor: 1 | proximo indice: 4 - Valor: 3
      - troca: True
      - list: ['4','2','5','3','1']

2. WHILE troca: True:
   - Inicia o WHILE
   - list: ['4','2','5','3','1']
   - troca: False

   1. FOR:
      - indice Atual: 0 - Valor: 4 | proximo indice: 1 - Valor: 2
      - troca: False
      - list: ['4','2','5','3','1']
   2. FOR:
      - indice Atual: 1 - Valor: 2 | proximo indice: 2 - Valor: 5
      - troca: True
      - list: ['4','5','2','3','1']
   3. FOR:
      - indice Atual: 2 - Valor: 2 | proximo indice: 3 - Valor: 3
      - troca: True
      - list: ['4','5','3','2','1']
   4. FOR:
      - indice Atual: 3 - Valor: 2 | proximo indice: 4 - Valor: 1
      - troca: True
      - list: ['4','5','3','2','1']

3. WHILE troca: True:
   - Inicia o WHILE
   - list: ['4','5','3','2','1']
   - troca: False

   1. FOR:
      - indice Atual: 0 - Valor: 4 | proximo indice: 1 - Valor: 5
      - troca: True
      - list: ['5','4','3','2','1']
   2. FOR:
      - indice Atual: 1 - Valor: 4 | proximo indice: 2 - Valor: 3
      - troca: True
      - list: ['5','4','3','2','1']
   3. FOR:
      - indice Atual: 2 - Valor: 3 | proximo indice: 3 - Valor: 2
      - troca: True
      - list: ['5','4','3','2','1']
   4. FOR:
      - indice Atual: 3 - Valor: 2 | proximo indice: 4 - Valor: 1
      - troca: True
      - list: ['5','4','3','2','1']


4. WHILE troca: True:
   - Inicia o WHILE
   - list: ['5','4','3','2','1']
   - troca: False

   1. FOR:
      - indice Atual: 0 - Valor: 5 | proximo indice: 1 - Valor: 4
      - troca: False
      - list: ['5','4','3','2','1']
   2. FOR:
      - indice Atual: 1 - Valor: 4 | proximo indice: 2 - Valor: 3
      - troca: False
      - list: ['5','4','3','2','1']
   3. FOR:
      - indice Atual: 2 - Valor: 3 | proximo indice: 3 - Valor: 2
      - troca: False
      - list: ['5','4','3','2','1']
   4. FOR:
      - indice Atual: 3 - Valor: 2 | proximo indice: 4 - Valor: 1
      - troca: False
      - list: ['5','4','3','2','1']

5. WHILE troca: False:
   - Não inicia o WHILE

- lista_string = '54321'
- return 54321























