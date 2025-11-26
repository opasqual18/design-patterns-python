# Interface esperada pelo cliente
class Target:
    def request(self):
        return "Target: comportamento padrão"

# Classe existente com interface diferente
class Adaptee:
    def specific_request(self):
        return "Adaptee: comportamento existente"

# Adapter converte a interface
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: traduzindo -> ({self.adaptee.specific_request()})"

# Cliente
def client_code(target: Target):
    print(target.request())

# Exemplo de uso
if __name__ == "__main__":
    print("Cliente com Target normal:")
    client_code(Target())

    print("\nCliente usando Adapter:")
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)
