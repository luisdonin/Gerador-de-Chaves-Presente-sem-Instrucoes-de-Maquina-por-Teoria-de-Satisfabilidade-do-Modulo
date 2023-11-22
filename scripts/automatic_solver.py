import tkinter as tk
from tkinter import filedialog
from barf import BARF
from barf.arch.disassembler import DisassemblerError
from z3 import *
from z3 import BitVec


def analyze_file(filepath):
   
    barf = BARF(filepath)

 

    
    
    for addr, asm_instr, reil_instrs in barf.disassemble():
        text_box.insert(tk.END, f"0x{addr:x} {asm_instr}\n")
        #print(asm_instr)
        #print(reil_instrs)
    for addr, asm_instr, reil_instrs in barf.translate():
        for reil_instr in reil_instrs:
            translate_box.insert(tk.END,reil_instr)
        #print(asm_instr)
        #print(reil_instrs)

    asm_instructions = {"EAX", "eax"}
    try:
        for addr, asm_instr, reil_instrs in barf.translate():
            if asm_instr.mnemonic in asm_instructions:
                for reil_instr in reil_instrs:
                    if reil_instr.mnemonic != "UNKN":
                        barf.code_analyzer.add_instruction(reil_instr)
                        print(reil_instr)
                    else:
                        text_box.insert(tk.END, f"Pulando instruções em: 0x{addr:x}\n")
    except DisassemblerError:
        analyzed_file_box.insert(tk.END, "Erro, reveja o endereço de entrada  ou arquivo binário.\n")


    eax = barf.code_analyzer.get_register_expr("eax", mode="post")
    
    #analyzed_file_box.insert(tk.END, eax)
    #print(eax)

    eax_z3 = BitVec("eax", 64)
    #text_box.insert(tk.END, f"eax: {eax}\n")
    #print(eax_z3)

    solver = Solver()

    solver.add(And(eax_z3 >= 10000, eax_z3 <= 99999))

    if solver.check() == sat:
        modelo = solver.model()

        eax_val = modelo[eax_z3].as_long()

        analyzed_file_box.insert(tk.END, f"Chave: {eax_val}\n")
    else:
        analyzed_file_box.insert(tk.END, "Solução não encontrada!\n")

def load_file():
    
    filepath = filedialog.askopenfilename()
    
    if filepath:
        analyze_file(filepath)
        file_loader_box.insert(tk.END, filepath)
    else:
        file_loader_box.insert(tk.END, "Nenhum arquivo selecionado\n")

janela = tk.Tk()

janela.title("Gerador de chaves")
janela.geometry("1024x900")

file_loader_box = tk.Text(janela, height=2, width=60)
file_loader_box.pack()


text_box = tk.Text(janela, height=20, width=100, spacing2=1)
text_box.pack()



translate_box = tk.Text(janela, height=20, width=100)
translate_box.pack()



analyzed_file_box = tk.Text(janela, height=2, width=60)
analyzed_file_box.pack()

load_button = tk.Button(janela, text="escolha um arquivo", command=load_file)
load_button.pack()

janela.mainloop()
