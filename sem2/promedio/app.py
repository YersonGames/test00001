import tkinter as tk

def main():
    root = tk.Tk()
    root.resizable(False,False)
    root.title("Calculador de promedio")
    root.geometry("640x480+800+150")


    marco = tk.Frame(root,padx=10,pady=10)
    marco.pack(fill="both",expand=True)

    #Nota 1
    lbl_nota1 = tk.Label(marco,text="Nota 1:")
    lbl_nota1.grid(row=0,column=0,padx=5,pady=5,sticky="we")

    entry_nota1 = tk.Entry(marco,width=10)
    entry_nota1.grid(row=0,column=1,padx=5,pady=5,sticky="we")

    #Nota 2
    lbl_nota2 = tk.Label(marco,text="Nota 2:")
    lbl_nota2.grid(row=1,column=0,padx=5,pady=5,sticky="we")

    entry_nota2 = tk.Entry(marco,width=10)
    entry_nota2.grid(row=1,column=1,padx=5,pady=5,sticky="we")

    #Nota 3
    lbl_nota3 = tk.Label(marco,text="Nota 3:")
    lbl_nota3.grid(row=2,column=0,padx=5,pady=5,sticky="we")

    entry_nota3 = tk.Entry(marco,width=10)
    entry_nota3.grid(row=2,column=1,padx=5,pady=5,sticky="we")

    #Nota 1
    lbl_nota4 = tk.Label(marco,text="Nota 4:")
    lbl_nota4.grid(row=3,column=0,padx=5,pady=5,sticky="we")

    entry_nota4 = tk.Entry(marco,width=10)
    entry_nota4.grid(row=3,column=1,padx=5,pady=5,sticky="we")

    #Promedio
    lbl_promedio = tk.Label(marco,text="Promedio: --",font=("Arial",12,"bold"))
    lbl_promedio.grid(row=5,column=0,padx=5,pady=5,columnspan=3,sticky="we")

    #Error
    lbl_mensaje = tk.Label(marco,text="",foreground="red")
    lbl_mensaje.grid(row=6,column=0,padx=5,pady=5,columnspan=3,sticky="we")


    def calcular_promedio():
        try:
            n1 = float(entry_nota1.get())
            n2 = float(entry_nota2.get())
            n3 = float(entry_nota3.get())
            n4 = float(entry_nota4.get())

            prom = (n1+n2+n3+n4)/4
            lbl_promedio.configure(text=f"Promedio: {prom:.1f}")
            lbl_mensaje.configure(text="")
        except ValueError:
            lbl_promedio.configure(text=f"Promedio: --")
            lbl_mensaje.configure(text="Error: Ingrese solo numeros en las 4 notas")
    
    #Boton Calcular
    btn_calcular = tk.Button(marco,text="Calcular",command=calcular_promedio)
    btn_calcular.grid(row=4,column=0,padx=5,pady=5,sticky="we")


    def limpiar_entradas():
        entry_nota1.delete(0,tk.END)
        entry_nota2.delete(0,tk.END)
        entry_nota3.delete(0,tk.END)
        entry_nota4.delete(0,tk.END)
        lbl_mensaje.configure(text="")
        lbl_promedio.configure(text=f"Promedio: --")

    #Boton limpiar
    btn_limpiar = tk.Button(marco,text="Limpiar",command=limpiar_entradas)
    btn_limpiar.grid(row=4,column=1,padx=5,pady=5,sticky="we")


    #Boton salir
    btn_salir = tk.Button(marco,text="salir",command=exit)
    btn_salir.grid(row=4,column=2,padx=5,pady=5,sticky="we")


    marco.grid_columnconfigure([0,1,2], weight=1)
    marco.grid_rowconfigure([0,1,2,3,4,5,6], weight=1)

    root.mainloop()

main()