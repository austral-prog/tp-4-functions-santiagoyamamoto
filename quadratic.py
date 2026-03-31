# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    r1 = (-b + (b**2 - 4 * a * c)**0.5) / 2 * a
    r2 = (-b - (b**2 - 4 * a * c)**0.5) / 2 * a
    discriminante=  b**2 - 4 * a * c

    if discriminante >= 0 :
        if r1 != r2 :
            return (f"({r1}, {r2})")
        elif r1 == r2:
            return f"({r1})"
    else:
        return "( )"

def value_y(a, b, c, x):
    y= a * x ** 2 + b * x + c
    return y

def to_string(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return (" ")
    elif b == 0 and c == 0:
        return (f"f(x) = {a} * X^2")
    elif a == 0 and b == 0:
        return (f"f(x) = {c}")
    elif a == 0 and c == 0:
        return (f"f(x) = {b} * X")
    elif a == 0:
        return (f"f(x) = {b} * X + {c}")
    elif b == 0:
        return (f"f(x) = {a} * X^2 + {c}")
    elif c == 0:
        return (f"f(x) = {a} * X^2 + {b} * X")
    else:
        return (f"f(x) = {a} * X^2 + {b} * X + {c}")

def derivation(a, b, c):
    a1=int(a)

    if a == 0:
        return (f"f'(x) = {b}")
    elif b == 0:
        return (f"f'(x) = {2*a1} * X")
    else:
        return (f"f'(x) = {2*a1} * X + {b}")
