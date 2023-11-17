import tkinter as tk
from tkinter import filedialog
from barf import BARF
from elftools.elf.elffile import ELFFile
from barf.arch.disassembler import DisassemblerError
from z3 import *
from z3 import BitVec


def analyze_file(filepath):
   
    barf = BARF(filepath)

 

    with open(filepath, "rb") as file:
        elffile = ELFFile(file)
       
        
    jump_instructions = {"JMP", "JA", "JAE", "JB", "JBE", "JC", "JE", "JG", "JGE", "JL", "JLE", "JNA", "JNAE", "JNB", "JNBE", "JNC", "JNE", "JNG", "JNGE", "JNL", "JNLE", "JNO", "JNP", "JNS", "JNZ", "JO", "JP", "JPE", "JPO", "JS", "JZ"}
    
    for addr, asm_instr, reil_instrs in barf.disassemble():
        text_box.insert(tk.END, f"0x{addr:x} {asm_instr}\n")
    


    try:
        for addr, asm_instr, reil_instrs in barf.translate():
            if asm_instr.mnemonic in jump_instructions:
                for reil_instr in reil_instrs:
                    if reil_instr.mnemonic != "UNKN":
                        barf.code_analyzer.add_instruction(reil_instr)
                    else:
                        text_box.insert(tk.END, f"Pulando instruções em: 0x{addr:x}\n")
    except DisassemblerError:
        analyzed_file_box.insert(tk.END, "Erro, reveja o endereço de entrada  ou arquivo binário.\n")


    eax = barf.code_analyzer.get_register_expr("eax", mode="post")
    #analyzed_file_box.insert(tk.END, eax)

    eax_z3 = BitVec("eax", 32)
    #text_box.insert(tk.END, f"eax: {eax}\n")

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

load_button = tk.Button(janela, text="Load File", command=load_file)
load_button.pack()

text_box = tk.Text(janela)

file_loader_box = tk.Text(janela, height=2, width=60)
file_loader_box.pack()

analyzed_file_box = tk.Text(janela, height=2, width=60)
analyzed_file_box.pack()

text_box.pack()
janela.mainloop()