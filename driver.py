import tkinter as tk
#from grid import Grid
class MainWin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Welcome to the game')
        tk.Label(self, text = "High scores:\n\n\n\n\n").pack()
        self.minsize(400,200)
        #self.grid = Grid()
        tk.Button(self, text = "Start the game", command = print("hi")).pack()
app = MainWin()
app.mainloop()