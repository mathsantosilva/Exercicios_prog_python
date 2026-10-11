# Melhorias — Ordem Decrescente

**Solução de referência:** [Criar uma lofica para deixar um inteiro em ordem decrescente](Descrição_desafio.md)

> **Escopo:** registrar somente o problema identificado, a alteração e o resultado. Não recontar o algoritmo inteiro.

## Melhoria 1 — limite de lista

### Qual era o problema?

- A lista era comparada inteira mesmo que a ultima posição já estivesse corretamente alocada

### O que alterei?
- Ao rodar o proximo looping do while eu incremento uma variavel que vai reduzir o tamanho do range do for

**Antes:**

```python
for i in range(len(list_nums) - 1):
```

**Depois:**

```python
for i in range(len(list_nums) - limite_reducao):


limite_reducao += 1
```

### Por que essa mudança funciona?
- o Range da lista já tem que receber uma diminuição para não acessar indices inexistentes, a unica diferença é que ao inves dessa diminuição ser fixa, ela é incrementada a cada looping do while 

### Qual foi o efeito?

- **Antes:** Realizada 20 comparações para a entrada 12345
- **Depois:** Realiza somente 10 comparação para a entrada
- **Benefício:** Um algoritmo mais eficiente 
- **Limitação ou custo:** A última execução do while pode ocorrer sem comparações, pois o for recebe range(0). Isso não gera erro, mas representa uma execução desnecessária.

---

## Melhoria 2 — Segunda condição no while 

### Qual era o problema?

- O while tinha que executar um looping morto para validar efetivamente que não tinha mais mudanças e manter a variavel troca como false

### O que alterei?

**Antes:**

```python
while troca:
```

**Depois:**

```python
while troca and limite_reducao < len(list_nums):
```

### Por que essa mudança funciona?

- Quando o limite de redução chega no mesmo valor ou maior que o tamanho da lista, o while já perde a condição de looping, parando a execução mesmo que o troca ainda seja true

### Qual foi o efeito?

- **Antes:** Precisava de um ultimo looping para deixar a variavel troca false 
- **Depois:** Quando os valores de redução atingem o tamanho da lista o looping finaliza
- **Benefício:** um looping a menos na execução
- **Limitação ou custo:** A execução pode terminar com a variavel troca como true

---

## Melhoria 3 — Menos codigo

### Qual era o problema?

- Variavel para guardar a string para depois ser transformada em int

### O que alterei?

**Antes:**

```python
lista_string = ''.join(list_nums)
return int(lista_string)
```

**Depois:**

```python
return int(''.join(list_nums))
```

### Por que essa mudança funciona?

- Agora o python realiza as conversões sem a necessidade de uma variavel itermediaria pra isso 

### Qual foi o efeito?

- **Antes:** Duas linhas e uma variavel para formatar o result
- **Depois:** nenhuma variavel e o python resolve as conversões antes do return
- **Benefício:** Melhor legibilidade e menos codigo 
- **Limitação ou custo:** Nenhum

## Resumo das mudanças (opcional)

| Melhoria                  | Problema que resolve                                                                                                                   | Resultado observado           |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| limite de lista           | A lista era comparada inteira mesmo que a ultima posição já estivesse corretamente alocada                                             | Eficiencia no algoritmo       |
| Segunda condição no while | O while tinha que executar um looping morto para validar efetivamente que não tinha mais mudanças e manter a variavel troca como false | Uma execução a menos no while |
| Menos codigo              | Encurtar o comando e deixar ele mais facil de entender                                                                                 | Melhor legibilidade           |

> **Pergunta de revisão:** consigo explicar *o que mudou e por quê* sem consultar o código?
