from priklad import vytvor_priklad, priklad_na_retezec
from utility import pokracovat, retezec_procento

def hraj():
    hrajeme = True 
    kolo = 0 
    spravne = 0
    spatne = 0 

    while hrajeme:
        kolo += 1 
        priklad = vytvor_priklad()
        vstup = int(input(priklad_na_retezec(priklad)))

        if priklad["vysledek"] == vstup:
            spravne += 1
            print("OK")
        else:
            spatne += 1
            print("CHYBA")

        if kolo % 5 == 0:
            hrajeme = pokracovat()


    spravne = 100*spravne/kolo

    print(f"Správně {retezec_procento(spravne)} {spravne}%")

    if spravne > 75:
        print("Díky za hru, vedl sis dobře.")
    elif spravne > 50:
        print("Díky, dobrá práce, ale ještě by se to dalo vylepšit.")
    elif spravne > 25:
        print("Díky za hru a nezapomeň zítra zase cvičit.")
    else:
        print("Asi si raději kup kalkulačku.")    

    return spravne