import random

def vytvor_priklad():
    a = random.randrange(1, 10)
    b = random.randrange(1, 10) 
    
    return {
        "a": a,
        "b": b,
        "vysledek": a*b
    }

def priklad_na_retezec(priklad):
    return f"{priklad['a']} * {priklad['b']} = "