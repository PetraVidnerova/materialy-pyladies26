def pokracovat():
    while True:
        vstup = input("Pro pokračování stiskni Enter, pro konec hry n/ne \n")
        vstup = vstup.strip().lower()
        if not vstup.strip():
            return True
        elif vstup in ("n", "ne"):
            return False

def retezec_procento(p):
    retezec = (int(p) // 10 ) * "■"
    return f"{retezec:<10}"

def menu(moznosti):
    for i, moznost in enumerate(moznosti):
        print(i, moznost)
    volba = int(input("?"))
    if volba < 0 or volba >= len(moznosti):
        return None
    return moznosti[volba]