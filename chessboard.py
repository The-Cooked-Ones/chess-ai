from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class ChessBoard(GridLayout):
    def __init__(self, **kwargs):
        # Initialize the parent GridLayout with 8 rows and 8 columns
        super().__init__(**kwargs)
        self.rows = 8
        self.cols = 8

        # Adding buttons to the layout
        for i in range(8):
            for j in range(8):
                test = 1 if j % 2 == 0 else 0
                if i % 2 == test:
                    button = Button(text=f"Button {i*8+(j) + 1}", background_color=(100, 100, 100), color=(0, 0, 0))
                else:
                    button = Button(text=f"Button {i*8+(j) + 1}", background_color=(0, 0, 0), color=(100, 100, 100))
                self.add_widget(button)