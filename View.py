import re
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Touch(Button):
    """Chaque touche de la calculatrice"""
    def __init__(self, text="%",background_color="#353b48"):
        Button.__init__(self)
        self.text = text
        self.size_hint = (.2, .2)
        self.font_size = 45
        self.background_normal = ""
        self.background_color = background_color
        self.color = "#8c7ae6"


class Print(TextInput):
    """L'écran de la calculatrice"""
    def __init__(self, text="#"):
        TextInput.__init__(self)
        self.text = text
        self.multiline = False
        self.halign = "right"
        self.font_size = 65
        self.size_hint = (1, .19)
        self.background_color = "#786fa6"
        self.foreground_color = "#f5f6fa"


class Screen(BoxLayout):
    """l'écran ou affichage principal"""
    def __init__(self):
        BoxLayout.__init__(self)
        self.orientation = "vertical"
        self.size = (self.width, self.height)
        self.print = Print(text="0")
        self.add_widget(self.print)
        self.pad = GridLayout(cols=4, rows=5)
        self.add_widget(self.pad)
        # le pavé numérique de la calculatrice
        self.percent = Touch(text="%")
        self.percent.bind(on_press=self.calculate)
        self.pad.add_widget(self.percent)
        self.to_erase = Touch(text="C")
        self.to_erase.bind(on_press=self.clear)
        self.pad.add_widget(self.to_erase)
        self.ce = Touch(text=u"\u00AB")
        self.ce.bind(on_press=self.remote_a_number)
        self.pad.add_widget(self.ce)
        self.to_divide = Touch(text="/", background_color="#222f3e")
        self.to_divide.bind(on_press=self.calculate)
        self.pad.add_widget(self.to_divide)
        self.button_7 = Touch(text="7")
        self.button_7.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_7)
        self.button_8 = Touch(text="8")
        self.button_8.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_8)
        self.button_9 = Touch(text="9")
        self.button_9.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_9)
        self.to_multiply = Touch(text="*", background_color="#222f3e")
        self.to_multiply.bind(on_press=self.calculate)
        self.pad.add_widget(self.to_multiply)
        self.button_4 = Touch(text="4")
        self.button_4.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_4)
        self.button_5 = Touch(text="5")
        self.button_5.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_5)
        self.button_6 = Touch(text="6")
        self.button_6.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_6)
        self.to_subtract = Touch(text="-", background_color="#222f3e")
        self.to_subtract.bind(on_press=self.calculate)
        self.pad.add_widget(self.to_subtract)
        self.button_1 = Touch(text="1")
        self.button_1.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_1)
        self.button_2 = Touch(text="2")
        self.button_2.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_2)
        self.button_3 = Touch(text="3")
        self.button_3.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_3)
        self.to_add = Touch(text="+", background_color="#222f3e")
        self.to_add.bind(on_press=self.calculate)
        self.pad.add_widget(self.to_add)
        self.to_convert = Touch(text="+/-")
        self.to_convert.bind(on_press=self.convert_a_number)
        self.pad.add_widget(self.to_convert)
        self.button_0 = Touch(text="0")
        self.button_0.bind(on_press=self.type_number)
        self.pad.add_widget(self.button_0)
        self.dot = Touch(text=".")
        self.dot.bind(on_press=self.add_a_dot)
        self.pad.add_widget(self.dot)
        self.equal = Touch(text="=", background_color="#222f3e")
        self.equal.bind(on_press=self.is_equal_to)
        self.pad.add_widget(self.equal)

    def clear(self, widget):
        self.print.text = "0"

    def type_number(self, widget):
        previous_number = self.print.text
        if "IMPOSSIBLE" in previous_number:
            previous_number = ""

        if previous_number == '0':
            self.print.text = ""
            self.print.text = f"{widget.text}"
        else:
            self.print.text = f"{previous_number}{widget.text}"

    def calculate(self, widget):
        previous_number = self.print.text
        self.print.text = f"{previous_number}{widget.text}"

    def remote_a_number(self, widget):
        previous_number = self.print.text
        previous_number = previous_number[:-1]
        self.print.text = previous_number

    def is_equal_to(self, widget):
        previous_number = self.print.text
        try:
            result = eval(previous_number)
            self.print.text = str(result)
        except ZeroDivisionError:
            self.print.text = "IMPOSSIBLE"

    def convert_a_number(self, widget):
        previous_number = self.print.text
        if "-" in previous_number:
            self.print.text = f"{previous_number.replace('-','')}"
        else:
            self.print.text = f"-{previous_number}"

    def add_a_dot(self, widget):
        previous_number = self.print.text
        list_of_numbers = re.split("\+/-/\*///%", previous_number)
        if ("+" in previous_number or "-" in previous_number or "*" in previous_number or "/" in previous_number or "%" in previous_number) and "." not in list_of_numbers[-1]:
            previous_number = f"{previous_number}."
            self.print.text = previous_number
        elif "." in previous_number:
            pass
        else:
            previous_number = f"{previous_number}."
            self.print.text = previous_number


class CalculatorView(App):
    def build(self):
        self.title = "Calculator"
        return Screen()


if __name__ == '__main__':
    Window.size = (350, 550)
    CalculatorView().run()
