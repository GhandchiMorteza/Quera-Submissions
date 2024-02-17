from math import comb
import re

def replace_pattern(term):
    pattern = r"\^1([0-9])"
    replacement = r"^{1\1}"
    replaced_term = re.sub(pattern, replacement, term)
    return replaced_term

n = int(input())
terms = []
for i in range(n + 1):
    coefficient = comb(n, i)
    x_term = f"x^{n-i}" if (n - i) > 1 else "x" if (n - i) == 1 else ""
    y_term = f"y^{i}" if i > 1 else "y" if i == 1 else ""
    term = f"{coefficient}{x_term}{y_term}" if coefficient != 1 else f"{x_term}{y_term}"
    term = replace_pattern(term).replace("^20", "^{20}").replace("^1", "").replace("^1", "").replace("x^0", "").replace("y^0", "")
    if x_term == "" and y_term == "":  
            term = "1"
    terms.append(term)  
print('+'.join(terms))
