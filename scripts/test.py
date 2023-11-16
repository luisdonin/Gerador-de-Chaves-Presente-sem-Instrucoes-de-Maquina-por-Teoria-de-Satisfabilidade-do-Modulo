import tkinter as tk
from tkinter import filedialog
from barf import BARF

def analyze_file(filepath):
   
    barf = BARF(filepath)


    for addr, asm_instr, reil_instrs in barf.translate(0x80483ed, 0x8048401):
        # Add each REIL instruction to the code analyzer
        for reil_instr in reil_instrs:
            barf.code_analyzer.add_instruction(reil_instr)


    eax = barf.code_analyzer.get_register_expr("eax", mode="post")
    print(eax)

def load_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        analyze_file(filepath)
        print(f"Loaded and analyzed file: {filepath}")
    else:
        print("No file selected")

root = tk.Tk()

load_button = tk.Button(root, text="Load File", command=load_file)
load_button.pack()

root.mainloop()