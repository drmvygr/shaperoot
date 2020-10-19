import math
import cmath

print("N-GON ROOT CALCULATOR - by dreamVoyager \n A generalized root formula for the length of the side of an "
      "n-sided regular "
      "polygon with area x. \n Also works with complex numbers. (Use j instead of i)")
while True:
    try:
        x = complex(input(">Input 1 (n-gon):"))
        y = complex(input(">Input 2 (Area):"))
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
    if 0 <= shaperoot.imag:
        op = "+"
    else:
        op = "-"
    print(f"The {x}-gon root of {y} is {round(shaperoot.real, 10)}{op}{abs(round(shaperoot.imag, 10))}j")
