from tkinter import*
from op import Operacion


ventana = Tk()
ventana.title("Calculadora")
ventana.configure(bg="black")

#Entrada
e_texto = Entry(ventana, font=("Calibri 20"), bg="black", fg="white")
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#funciones

def click_boton(valor):
  e_texto.insert(END,valor)


def borrar():
  e_texto.delete(0,END)

operacion = Operacion()

#Botones
boton1= Button(ventana, text="1", width=5, height=2, command=lambda:click_boton(1), bg="#404040", fg="white")
boton2= Button(ventana, text="2", width=5, height=2, command=lambda:click_boton(2), bg="#404040", fg="white")
boton3= Button(ventana, text="3", width=5, height=2, command=lambda:click_boton(3), bg="#404040", fg="white")
boton4= Button(ventana, text="4", width=5, height=2, command=lambda:click_boton(4), bg="#404040", fg="white")
boton5= Button(ventana, text="5", width=5, height=2, command=lambda:click_boton(5), bg="#404040", fg="white")
boton6= Button(ventana, text="6", width=5, height=2, command=lambda:click_boton(6), bg="#404040", fg="white")
boton7= Button(ventana, text="7", width=5, height=2, command=lambda:click_boton(7), bg="#404040", fg="white")
boton8= Button(ventana, text="8", width=5, height=2, command=lambda:click_boton(8), bg="#404040", fg="white")
boton9= Button(ventana, text="9", width=5, height=2, command=lambda:click_boton(9), bg="#404040", fg="white")
boton0= Button(ventana, text="0", width=15, height=2, command=lambda:click_boton(0), bg="#404040", fg="white")

boton_borrar= Button(ventana, text="AC", width=5, height=2, command=lambda:borrar(), bg="#C0C0C0", fg="white")
boton_parentesis1= Button(ventana, text="(", width=5, height=2, command=lambda:click_boton("("), bg="#C0C0C0", fg="white")
boton_parentesis2= Button(ventana, text=")", width=5, height=2, command=lambda:click_boton(")"), bg="#C0C0C0", fg="white")
boton_punto= Button(ventana, text=".", width=5, height=2, command=lambda:click_boton("."), bg="#C0C0C0", fg="white")

boton_div= Button(ventana, text="/", width=5, height=2, command=lambda:click_boton("/"), bg="#C0C0C0", fg="white")
boton_mult= Button(ventana, text="X", width=5, height=2, command=lambda:click_boton("*"), bg="#C0C0C0", fg="white")
boton_sum= Button(ventana, text="+", width=5, height=2, command=lambda:click_boton("+"), bg="#C0C0C0", fg="white")
boton_rest= Button(ventana, text="-", width=5, height=2, command=lambda:click_boton("-"), bg="#C0C0C0", fg="white")
boton_igual = Button(ventana, text="=", width=5, height=2, command=lambda: operacion.hacer_operacion(e_texto), bg="#C0C0C0", fg="white")

#agregar botones

boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_rest.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)


ventana.mainloop()