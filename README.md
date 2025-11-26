# Design Patterns em Python

Este repositório apresenta implementações simples de três padrões de projeto, cada um pertencente a uma categoria diferente:

- Strategy (Comportamental)
- Abstract Factory (Criacional)
- Adapter (Estrutural)

As implementações foram feitas em Python e acompanhadas de explicações sobre o problema que o padrão resolve, sua solução e um diagrama UML representando a estrutura conceitual.

---

## Referência

O conteúdo conceitual foi baseado no catálogo de padrões de projeto:

Refactoring Guru — Design Patterns  
https://refactoring.guru/pt-br/design-patterns

---

## Uso de LLM

ChatGPT 

---

# 1. Strategy — Padrão Comportamental

### Ideia principal
O padrão Strategy permite trocar algoritmos em tempo de execução.  
A lógica muda sem alterar a estrutura do código cliente.

### Problema que resolve
Quando o software realiza uma mesma tarefa de diferentes maneiras (por exemplo, múltiplos métodos de pagamento), o uso de estruturas condicionais como `if`, `match`, `switch` dificulta:

- manutenção
- inclusão de novos comportamentos
- respeito ao princípio aberto/fechado (OCP)

O código se torna rígido e pouco extensível.

### Solução
Criar:

1. Uma interface comum (Strategy)
2. Implementações individuais (estratégias concretas)
3. Um contexto que recebe a estratégia e delega a execução

Não há impacto no restante do sistema quando novas estratégias forem adicionadas.

### Diagrama UML (Strategy)

```
┌──────────────────┐
│     Context      │
│------------------│
│ - strategy       │
│ + setStrategy()  │
│ + execute()      │
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│    Strategy      │ <<interface>>
│------------------│
│ + execute()      │
└─────────┬────────┘
     ┌────┴────────────┐
     ▼                 ▼
┌───────────────┐ ┌───────────────┐
│ ConcreteA      │ │ ConcreteB      │
│----------------│ │----------------│
│ + execute()    │ │ + execute()    │
└───────────────┘ └───────────────┘
```

### Local do código
Arquivo: `patterns/strategy/strategy.py`

---

# 2. Abstract Factory — Padrão Criacional

### Ideia principal
Cria famílias de objetos relacionados sem acoplar o código às classes concretas.

### Problema que resolve
Quando uma aplicação precisa gerar múltiplos objetos compatíveis entre si, o código pode começar a depender diretamente de implementações específicas.

Exemplo:
- Interface Windows com botão Windows e checkbox Windows
- Interface Mac com botão Mac e checkbox Mac

Sem o padrão, o código acaba repleto de condicionais e viola o OCP.

### Solução
O padrão Abstract Factory propõe:

- Uma fábrica abstrata
- Fábricas concretas
- Cliente que cria os objetos apenas através da fábrica

Assim, todos os objetos criados permanecem consistentes e o cliente nunca conhece as classes reais.

### Diagrama UML (Abstract Factory)

```
┌──────────────────────────┐
│        GUIFactory        │ <<interface>>
│--------------------------│
│ + createButton()         │
│ + createCheckbox()       │
└───────────┬──────────────┘
            │
    ┌───────┴────────────────┐
    ▼                        ▼
┌──────────────┐     ┌──────────────┐
│ WindowsFactory│     │ MacFactory   │
└──────┬────────┘     └──────┬───────┘
       │ creates            │ creates
       ▼                    ▼
   Button Windows       Button Mac
   Checkbox Windows     Checkbox Mac
```

### Local do código
Arquivo: `patterns/abstract_factory/abstract_factory.py`

---

# 3. Adapter — Padrão Estrutural

### Ideia principal
Permite que objetos com interfaces incompatíveis trabalhem juntos.

### Problema que resolve
Quando um sistema depende de uma interface definida, mas existe uma biblioteca ou código legado que usa uma interface diferente.

Exemplo:
- O sistema moderno espera MediaPlayer.play()
- Uma biblioteca antiga usa play_file()

Sem o Adapter, o código cliente teria que conhecer a forma antiga e adaptar manualmente.

### Solução
Criar uma classe intermediária (Adapter) que:

- implementa a interface esperada
- converte chamadas para a interface antiga

O cliente não é modificado.

### Diagrama UML (Adapter)

```
┌──────────────────┐
│     Client       │
└──┬───────────────┘
   │
   ▼
┌──────────────────┐
│   Target         │ <<interface>>
│ + request()      │
└──┬───────────────┘
   │
   ▼
┌──────────────────┐
│     Adapter      │
│ adaptee.request  │
└──┬───────────────┘
   │
   ▼
┌──────────────────┐
│     Adaptee      │
│ + specific()     │
└──────────────────┘
```

### Local do código
Arquivo: `patterns/adapter/adapter.py`

---

# Como executar

É necessário possuir Python 3 instalado.

```
python3 patterns/strategy/strategy.py
python3 patterns/abstract_factory/abstract_factory.py
python3 patterns/adapter/adapter.py
```

---

# Conclusão

Cada padrão resolve um tipo de problema recorrente no desenvolvimento de software:

- Strategy: permite trocar algoritmos de forma flexível e extensível.
- Abstract Factory: separa a criação de objetos da lógica da aplicação.
- Adapter: permite reaproveitar código incompatível sem alterar o cliente.

Os exemplos apresentados aqui são simplificados, com o objetivo de demonstrar o funcionamento básico de cada padrão.

---

# Direitos autorais

Conceitos e explicações baseados no catálogo:

Refactoring Guru — https://refactoring.guru/pt-br/design-patterns
