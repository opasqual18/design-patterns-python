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

Explicação do código
Este código implementa o padrão Strategy, permitindo trocar o algoritmo usado pela aplicação sem alterar o restante do código.

Interface Strategy

Define um método comum (execute(a, b)) que todas as estratégias devem implementar.

    class Strategy(ABC):
    
    @abstractmethod
    
    def execute(self, a, b):
        pass

Estratégias concretas

Cada classe implementa o método de forma diferente.

    class SomaStrategy(Strategy):
    
    def execute(self, a, b):
        return a + b

    class MultiplicaStrategy(Strategy):
    
    def execute(self, a, b):
        return a * b

Context

Recebe uma estratégia e delega a ela a operação.

    class Context:
    
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy
    
    def calcular(self, a, b):
        return self._strategy.execute(a, b)

Exemplo

Trocar a estratégia muda o comportamento sem alterar o código do contexto.

    ctx = Context(SomaStrategy())
    ctx.calcular(2, 3)  # soma

    ctx.set_strategy(MultiplicaStrategy())
    ctx.calcular(2, 3)  # multiplicação

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

<img width="377" height="358" alt="SoWkIImgAStDuUNAp2j9BKfBJ4vL22ufIYn9JQzKgERbKW02xPHy_u9Ke5XcVfw69YzNBIyNBrToJc9niO9pVbvoKMf9AaoBeq9cRa5EQcvgNaan9UOuaMzEIMf52KobRZ5KgnNS4AWHnQabC16DOeIi9bGwjI8rkHJX7BWjCFDrTUsGJCGC1Jsz6dmAdD0LEAJcfO1Z0G00" src="https://github.com/user-attachments/assets/fe56f4e3-f43d-4d15-b739-8801c196a209" />

### Local do código
Arquivo: `patterns/strategy/strategy.py`

---

# 2. Abstract Factory — Padrão Criacional
Explicação do código
Este código implementa o padrão Abstract Factory, que permite criar famílias de objetos relacionados (ex.: componentes UI) sem acoplar o código às classes concretas.

Produtos abstratos

Interfaces que definem o que os produtos devem fazer.

    class Button(ABC):
    @abstractmethod
    
    def paint(self):
        pass

    class Checkbox(ABC):
    @abstractmethod
    
    def paint(self):
        pass


Button e Checkbox são contratos: definem o método paint(), mas não a implementação.

Produtos concretos

Implementações específicas para cada sistema.

    class WindowsButton(Button):
    
        def paint(self):
            return "Botão estilo Windows"

    class MacButton(Button):
   
        def paint(self):
            return "Botão estilo Mac"

    class WindowsCheckbox(Checkbox):
   
        def paint(self):
            return "Checkbox estilo Windows"

    class MacCheckbox(Checkbox):
    
        def paint(self):
            return "Checkbox estilo Mac"


Cada produto segue a interface correspondente, mas pertence a uma família (Windows ou Mac).

Abstract Factory

Define a família de objetos a serem criados.

    class GUIFactory(ABC):
        @abstractmethod
        def create_button(self):
            pass

        @abstractmethod
        def create_checkbox(self):
            pass


A Abstract Factory especifica quais produtos podem ser criados, sem decidir como.

Concrete Factories

Implementam a Abstract Factory criando produtos da mesma família.

    class WindowsFactory(GUIFactory):
    
        def create_button(self):
            return WindowsButton()

        def create_checkbox(self):
            return WindowsCheckbox()

    class MacFactory(GUIFactory):
    
        def create_button(self):
            return MacButton()

        def create_checkbox(self):
            return MacCheckbox()


Cada fábrica garante compatibilidade entre os produtos criados.

Cliente

    def client_code(factory: GUIFactory):
    
        button = factory.create_button()
        checkbox = factory.create_checkbox()
        print(button.paint())
        print(checkbox.paint())


O cliente depende apenas da Abstract Factory e das interfaces dos produtos, mantendo o código desacoplado.

Exemplo
   
    client_code(WindowsFactory())   # UI estilo Windows
    client_code(MacFactory())       # UI estilo Mac

Trocar a família de objetos é feito apenas trocando a factory passada para o cliente.

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


<img width="479" height="526" alt="abstract" src="https://github.com/user-attachments/assets/aa18a055-ae81-4f1c-82fa-50fd96c4725a" />



### Local do código
Arquivo: `patterns/abstract_factory/abstract_factory.py`

---

# 3. Adapter — Padrão Estrutural

Explicação do código
Este código implementa o padrão Adapter, que permite fazer duas classes incompatíveis trabalharem juntas convertendo a interface de uma para a interface esperada pela outra.

Target

Interface que o cliente espera usar.

    class Target:
    
        def request(self):
            return "Target: comportamento padrão"


O cliente conhece e usa apenas o método request.

Adaptee

Classe existente com uma interface diferente.

    class Adaptee:
    
        def specific_request(self):
            return "Adaptee: comportamento existente"


Ela faz algo útil, mas seu método (specific_request) não é compatível com o que o cliente espera.

Adapter

Traduz a interface do Adaptee para a interface Target.

    class Adapter(Target):
    
        def __init__(self, adaptee: Adaptee):
            self.adaptee = adaptee

        def request(self):
            return f"Adapter: traduzindo -> ({self.adaptee.specific_request()})"


O Adapter recebe uma instância de Adaptee e implementa request() chamando specific_request() internamente.
O cliente continua usando Target, mas o comportamento vem do Adaptee.

Cliente

    def client_code(target: Target):
        print(target.request())


O cliente funciona com qualquer objeto que implemente a interface Target.

Exemplo
   
    client_code(Target())         # comportamento padrão
    client_code(Adapter(adaptee)) # comportamento adaptado


Sem modificar o cliente nem a classe existente, o Adapter resolve a incompatibilidade entre interfaces.

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

<img width="164" height="342" alt="ZOzD2i8m48Nt0tE7B1Lf3-2Yr2k85nZILmaa8MQcA_Nkbj8gTELR3j_xcLvDgaqfCeLigADuk9lKEymzcToiKyLZWjhXoFHcOl9HLDrba38RN4Wb8Y6RxdoDB0JEAue_ul0jrG8Vnk2lEtghRPhkbxiTs_RLhIkOUkHXUUm3" src="https://github.com/user-attachments/assets/86ff524d-db2d-4bb0-bf6b-1002bfb7cd26" />


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
