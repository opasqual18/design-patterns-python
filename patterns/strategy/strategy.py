from abc import ABC, abstractmethod

# Interface Strategy
class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Estratégias concretas
class SomaStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class MultiplicaStrategy(Strategy):
    def execute(self, a, b):
        return a * b

# Contexto que usa Strategy
class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def calcular(self, a, b):
        return self._strategy.execute(a, b)

# Exemplo de uso
if __name__ == "__main__":
    ctx = Context(SomaStrategy())
    print("Soma: 2 + 3 =", ctx.calcular(2, 3))

    ctx.set_strategy(MultiplicaStrategy())
    print("Multiplicação: 2 * 3 =", ctx.calcular(2, 3))
