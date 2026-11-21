from hra import hraj
from utility import menu, retezec_procento

jmeno_hrace = input("Login: ").strip()

while True:
    volba = menu(["Hra", "Statistika", "Konec"])
    if volba == "Konec":
        break
    elif volba == "Statistika":
        with open(f"{jmeno_hrace}.txt", "r", encoding="utf-8") as f:
            for line in f:
                spravne = int(line)
                print(retezec_procento(spravne), f"{spravne}%")
    elif volba == "Hra":
        spravne = hraj()
        with open(f"{jmeno_hrace}.txt", "a", encoding="utf-8") as f:
            print(int(spravne), file=f)


print("To je opravdu konec.")