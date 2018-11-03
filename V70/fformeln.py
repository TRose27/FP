import sympy

def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()

    if err_vars == None:
        err_vars = f.free_symbols

    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '(\\Delta ' + latex(v) +')'

    return latex(sympy.sqrt(s), symbol_names=latex_names)

#E, q, r = sympy.var('E_x q r')
di,l1,l2 = sympy.var('{d_{innen}} l_1 l_2')
#f = E + q**2 * r
f = sympy.pi * (di/2)**2 * (l1+2*l2)

print(f)
print(error(f))
print()
