# Guia de Programação para Iniciantes — Python

> Nível: 2/10 → em evolução 🚀

---

## Passo 1 — Escolha da Linguagem

**Python** é a melhor escolha para iniciantes:
- Sintaxe simples, parece quase inglês
- Usado em IA, dados, automação e web
- Evite começar com C, C++ ou Java — são mais complexas

---

## Passo 2 — Ferramentas (gratuitas)

| Ferramenta | Link | Para que serve |
|---|---|---|
| Python 3.12+ | python.org | A linguagem em si |
| VS Code | code.visualstudio.com | Editor de código |
| Extensão Python | Dentro do VS Code | Destaca erros, autocomplete |
| Replit | replit.com | Programar no navegador, sem instalar nada |

---

## Passo 3 — Onde Aprender (grátis, em PT-BR)

- **Curso em Vídeo** — cursoEmVideo.com.br (melhor opção em português)
- **CS50P** — cs50.harvard.edu/python (Harvard, com legendas PT)
- **YouTube** — canais "Programação Dinâmica" e "Eduardo Mendes"

---

## Passo 4 — Conceitos Aprendidos

### `print()` — Mostrar texto na tela
```python
print("Olá, mundo!")
print("Meu nome é João")
```

---

### `input()` — Receber informação do usuário
```python
nome = input("Qual é o seu nome? ")
print("Seja bem-vindo,", nome)
```

---

### Variáveis — Guardar valores
```python
nome = "João"        # texto (str)
idade = 25           # número inteiro (int)
altura = 1.75        # número decimal (float)
```

---

### `int()` e `float()` — Converter texto em número
```python
idade = int(input("Quantos anos você tem? "))    # número inteiro
peso = float(input("Qual o seu peso? "))          # número com decimal
```

---

### Operações Matemáticas
```python
soma        = n1 + n2
subtracao   = n1 - n2
multiplicacao = n1 * n2
divisao     = n1 / n2
potencia    = n1 ** n2   # ex: 2 ** 3 = 8
```

---

### f-string — Texto com variáveis (jeito moderno)
```python
nome = "João"
idade = 25
print(f"Olá {nome}, você tem {idade} anos!")
```
> Coloca `f` antes das aspas e a variável dentro de `{}`

---

### `if`, `elif`, `else` — Condições
```python
idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você é maior de idade")
elif idade >= 16:
    print("Você pode votar!")
else:
    print("Você é menor de idade")
```

- `if` → "se"
- `elif` → "senão se" (para múltiplas condições)
- `else` → "senão" (captura tudo que não se encaixou)
- `==` compara valores | `=` atribui valores

---

### `while` + `break` — Loop (repetição)
```python
while True:
    resposta = input("Digite sim ou não: ")

    if resposta == "sim":
        print("Você disse sim!")
        break
    elif resposta == "não":
        print("Você disse não!")
        break
    else:
        print("Resposta inválida! Tente novamente.")
```

- `while True` → repete para sempre até encontrar um `break`
- `break` → sai do loop

---

## Projeto da Aula — Cadastro Completo

```python
nome = input("Qual o seu nome? ")
sobrenome = input("Qual o seu sobrenome? ")
idade = int(input("Quantos anos voce tem? "))

ano_atual = 2026
ano_nascimento = ano_atual - idade

print(f"Ola {nome} {sobrenome}")
print(f"Voce nasceu em {ano_nascimento}")

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

while True:
    qtde = input("Quantos animais voce tem? (0, 1 ou 2) ")

    if qtde == "0":
        print("Você não tem animais")
        break
    elif qtde == "1":
        animal1 = input("Qual o nome do seu animal? ")
        print(f"Seu animal se chama {animal1}")
        break
    elif qtde == "2":
        animal1 = input("Qual o nome do primeiro animal? ")
        animal2 = input("Qual o nome do segundo animal? ")
        print(f"Seus animais se chamam {animal1} e {animal2}")
        break
    else:
        print("Opção inválida! Tente novamente.")
```

---

## Próximos Passos

- [ ] Funções — `def` (organizar o código em blocos reutilizáveis)
- [ ] Listas — guardar vários valores numa variável só
- [ ] Loops com `for` — repetir para cada item de uma lista
- [ ] Importar bibliotecas — usar código pronto de terceiros

---

## Como Compartilhar seu Código

| Situação | Solução |
|---|---|
| Pessoa tem Python instalado | Manda o arquivo `.py` |
| Pessoa não tem nada instalado | Usa o Replit e manda o link |
| Quer um `.exe` clicável | Aprenderemos mais pra frente |

---

*Guia criado durante aula prática — atualizado conforme o aprendizado evolui.*
