from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class ChessAI(App):
    def build(self):
        # Outer BoxLayout (Vertical orientation)
        outer_layout = BoxLayout(orientation='horizontal')

        # First inner BoxLayout (Horizontal orientation)
        inner_layout_1 = GridLayout(rows=8,cols=8)
        inner_layout_1.add_widget(Button(text="Button 1"))
        inner_layout_1.add_widget(Button(text="Button 2"))

        return outer_layout
if __name__ == "__main__":
    ChessAI().run()




