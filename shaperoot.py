import math
import cmath

print("N-GON ROOT CALCULATOR - by dreamVoyager \n A generalized root formula for the length of the side of an "
      "n-sided regular "
      "polygon with area x. \n Also works with complex numbers.")
while True:
    try:
        x = complex(input(">Input 1 (n-gon):").replace("i","j"))
        y = complex(input(">Input 2 (Area):").replace("i","j"))
    except ValueError:
        print("Invalid input.")
        continue
    top = 4 * complex(y)
    try:
        tang = cmath.tan(cmath.pi / complex(x))
    except ZeroDivisionError:
        print("Error: Division by 0.")
        continue
    bot = complex(x) / complex(tang)
    fraction = complex(top) / complex(bot)
    shaperoot = cmath.sqrt(complex(fraction))
    z=str(x).replace("j","i")
    w = str(y).replace("j", "i")
    if 0 <= shaperoot.imag:
        op = "+"
    else:
        op = "-"
    print(f"The {z}-gon root of {w} is {round(shaperoot.real, 10)}{op}{abs(round(shaperoot.imag, 10))}i")
