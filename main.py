from kivy.core.window import Window
from View import CalculatorView


if __name__ == '__main__':
    Window.size = (500, 700)
    CalculatorView().run()
