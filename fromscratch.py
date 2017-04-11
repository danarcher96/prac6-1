from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


__author__ = 'Daniel Archer'


class convertmtokmApp(App):

    def build(self):
        Window.size = (200, 100)
        self.title = "M to KM Converter"
        self.root = Builder.load_file('fromscratch.kv')
        return self.root

    def handle_convert(self, value):
        result = value / 1000
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):

        newNum = self.get_validated_miles() + increment

        self.root.ids.input_number.text = str(newNum)


    def get_validated_miles(self):

        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


convertmtokmApp().run()