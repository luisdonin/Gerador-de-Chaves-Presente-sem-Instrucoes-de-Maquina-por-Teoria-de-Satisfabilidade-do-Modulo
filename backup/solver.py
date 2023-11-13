from z3 import *


digit1 = BitVec('digit1', 4)
digit2 = BitVec('digit2',4)
digit3 = BitVec('digit3',4)
digit4 = BitVec('digit4',4)
digit5 = BitVec('digit5',4)


solver = Solver()



solver.add(((digit1)+(digit2)) %2 != 0 )
solver.add(((digit3)+(digit4)) %2 != 0 )
solver.add(((digit4)+(digit5)) %2 != 0 )
solver.add((digit1) != 1)
solver.add((digit2) != 1)
solver.add((digit3) != 1)
solver.add((digit4) != 1)
solver.add((digit5) != 1)
solver.add((digit1) != 0)
solver.add((digit2) != 0)
solver.add((digit3) != 0)
solver.add((digit4) != 0)
solver.add((digit5) != 0)

#solver.add((digit3) %2 != 0 )
#solver.add((digit4) %2 != 0 )

if solver.check() == sat:

    model = solver.model()

    digit_1 = model[digit1].as_long()
    digit_2 = model[digit2].as_long()
    digit_3 = model[digit3].as_long()
    digit_4 = model[digit4].as_long()
    digit_5 = model[digit5].as_long()


    print(f"Key: {digit_1} {digit_2} {digit_3} {digit_4} {digit_5}")
else:

    print("Couldn't find a solution!.")
