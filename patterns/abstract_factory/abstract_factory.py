from abc import ABC, abstractmethod

# Produtos abstratos
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Produtos concretos
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

# Fábricas abstratas
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Fábricas concretas
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

# Cliente
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())

# Exemplo de uso
if __name__ == "__main__":
    print("Usando WindowsFactory:")
    client_code(WindowsFactory())

    print("\nUsando MacFactory:")
    client_code(MacFactory())
