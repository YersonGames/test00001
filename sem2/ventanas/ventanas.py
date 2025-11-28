import tkinter as tk

root = tk.Tk()
root.title("Titulo 1")
#Ancho,Alto+PosX,PosY
root.geometry("640x400+120+120")
root.resizable(False,False)
root.configure(bg="red")
root.iconbitmap("sem2/ventanas/icon.ico")
root.mainloop()