from contextlib import nullcontext

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class chessboard(object):
    chessBoard = GridLayout(rows=8, cols=8)
    def __init__(self):
        # Adding buttons to the inner layout
        for i in range(8 * 8):  # 8x8 grid = 64 buttons
            button = Button(text=f"Button {i + 1}")
            self.chessBoard.add_widget(button)
