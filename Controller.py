from Model import CalculatorModel
from View import CalculatorView


class CalculatorController():
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView()

    def main(self):
        self.view.build()


if __name__ == '__main__':
    calculator = CalculatorController()
    calculator.main()
