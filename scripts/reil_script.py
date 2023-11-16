from barf import BARF

# Open ELF file
barf = BARF("main")

# Add instructions to analyze.
for addr, asm_instr, reil_instrs in barf.translate(0x80483ed, 0x8048401):
    for reil_instr in reil_instrs:
        try:
            barf.code_analyzer.add_instruction(reil_instr)
        except Exception as e:
            print(f"Skipping unsupported instruction at address {addr}: {e}")

ebp = barf.code_analyzer.get_register_expr("ebp", mode="post")

# Preconditions: set range for variable a and b
a_addr = barf.code_analyzer.evaluate(ebp-0x8).as_long()
b_addr = barf.code_analyzer.evaluate(ebp-0xc).as_long()

a = barf.code_analyzer.get_memory_expr(a_addr, 4, mode="pre")
b = barf.code_analyzer.get_memory_expr(b_addr, 4, mode="pre")

for constr in [a >= 2, a <= 100, b >= 2, b <= 100]:
    barf.code_analyzer.add_constraint(constr)

# Postconditions: set desired value for the result
c = barf.code_analyzer.get_memory_expr(ebp-0x4, 4, mode="post")

for constr in [c >= 26, c <= 28]:
    barf.code_analyzer.add_constraint(constr)

if barf.code_analyzer.check() == 'sat':
    print("[+] Satisfiable! Possible assignments:")

    # Get concrete value for expressions
    a_val = barf.code_analyzer.get_expr_value(a)
    b_val = barf.code_analyzer.get_expr_value(b)
    c_val = barf.code_analyzer.get_expr_value(c)

    # Print values
    print("- a: {0:#010x} ({0})".format(a_val))
    print("- b: {0:#010x} ({0})".format(b_val))
    print("- c: {0:#010x} ({0})".format(c_val))

    assert a_val + b_val + 5 == c_val
else:
    print("[-] Unsatisfiable!")