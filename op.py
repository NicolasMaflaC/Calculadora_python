
class Operacion:
    def hacer_operacion(self, e_texto):
        ecuacion = e_texto.get()
        resultado = eval(ecuacion)
        e_texto.delete(0, 'end')
        e_texto.insert(0, resultado)