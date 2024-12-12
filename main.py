from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import yaml

# Load the yamls
with open("ChessAI.yaml", "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

class ChessAI(App):
    def build(self):
        # Outer BoxLayout (Horizontal orientation)
        outer_layout = BoxLayout(orientation='vertical')  # Changed to 'vertical' for better stacking of widgets

        outer_layout.add_widget(chessBoard)

        return outer_layout


if __name__ == "__main__":
    ChessAI().run()




