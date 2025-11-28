import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Titulo 1")
    #Ancho,Alto+PosX,PosY
    root.geometry("640x400+120+120")
    root.resizable(True,True)
    root.configure(bg="black")
    root.iconbitmap("sem2/ventanas/icon.ico")

    label = tk.Label(root,text="Hola amigos del youtus",bg="red",font=("Arial",14))
    label.pack()

    button = tk.Button(root,text="Cerrar",command=exit)
    button.pack()
    tk.Message(root,text="Hola").pack()
    root.mainloop()
main()