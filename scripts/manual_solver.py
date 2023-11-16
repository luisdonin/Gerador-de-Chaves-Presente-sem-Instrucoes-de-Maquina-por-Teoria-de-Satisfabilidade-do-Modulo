from tkinter import *
from tkinter import ttk
from z3 import *

def solve():
    digito1 = BitVec('digito1', 4)
    digito2 = BitVec('digito2',4)
    digito3 = BitVec('digito3',4)
    digito4 = BitVec('digito4',4)
    digito5 = BitVec('digito5',4)

    solver = Solver()

    solver.add(((digito1)+(digito2)) %2 != 0 )
    solver.add(((digito3)+(digito4)) %2 != 0 )
    solver.add(((digito4)+(digito5)) %2 != 0 )
    solver.add((digito1) != 1)
    solver.add((digito2) != 1)
    solver.add((digito3) != 1)
    solver.add((digito4) != 1)
    solver.add((digito5) != 1)
    solver.add((digito1) != 0)
    solver.add((digito2) != 0)
    solver.add((digito3) != 0)
    solver.add((digito4) != 0)
    solver.add((digito5) != 0)

    if solver.check() == sat:
        model = solver.model()

        digito_1 = model[digito1].as_long()
        digito_2 = model[digito2].as_long()
        digito_3 = model[digito3].as_long()
        digito_4 = model[digito4].as_long()
        digito_5 = model[digito5].as_long()

        resultado.set(f"Chave: {digito_1} {digito_2} {digito_3} {digito_4} {digito_5}")
    else:
        resultado.set("Solução não encontrada!")

janela = Tk()
janela.geometry("300x200")
janela.title("Keygen")
style = ttk.Style(janela)
style.theme_use("clam")
resultado = StringVar()

Button(janela, text="Checar Satisfabilidade", command=solve).pack()
Label(janela, textvariable=resultado).pack()
janela.mainloop()