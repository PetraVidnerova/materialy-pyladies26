# PROJEKT PROCVIČOVÁNÍ NÁSOBILKY

1. Napiš funkci `vyvor_priklad` a ulož ji do souboru `priklad.py`

Funkce nebude mít žádné parametry a měla by vracet slovník, který bude obsahovat klíče: `"a"`, `"b"` a `"vysledek"`, a hodnoty budou pro `"a"` a `"b"` náhodná celá čísla a pro `"vysledek"` součin těchto čísel.

Pokud funkce funguje správně, spuštění `krok1.py` by mělo vypsat slovník podobný jako tento:
```
{'a': 4, 'b': 6, 'vysledek': 24}
```

(čísla se mohou lišit, jsou náhodná, ale výsledek by měl být součinem a a b)

2. Do souboru `priklad.py` přidej funkci `priklad_na_retezec`, která bude mít jeden parametr. V parametru bude očekávat slovník obsahující klíče `"a"`, `"b"` a bude vracet řetězec s příkladem bez výsledku. 

Spuštění `krok2.py` by mělo vypsat např.
```
4 * 6 = 
```
(čísla ve výpisu jsou náhodná, mohou se lišit). 

3. Vyzkoušej si `krok3.py` a zkoupíruje si z něj kód do souboru `hra.py`. Dopiš jej tak, aby program po zadání vstupu uživatelem, vypsal `OK` nebo `CHYBA`. Hlášku si můžeš opravit dle svého vkusu.

*Na jednom příkladu moc neprocvičíme. Umožníme uživateli hru opakovat.*

4. Založ soubor `utility.py` a napiš do něj funkci `pokracovat`, která se zeptá uživatele, zda chce ve hře pokračovat. Pokud uživatel zadá `"NE"`, `"ne"`, `"n"` nebo `"N"` vrátí `False`, pokud uživatel zadá Enter (prázdný řetězec), vrátí `True`, jinak se zeptá znovu. 

5. Přidej cyklus a po každém přikladu se zeptej uživatele, jestli chce pokračovat (zavolej funkci `pokracovat`). Před ukončením programu se nezapomeň rozloučit a poděkovat za hru.
    
**Enter po každém příkladu nás zdržuje.**

6. Uprav hru tak, aby umožňovala ukončení jen po každém pátém příkladu. Nápověda: můžeš využit operátor `%`.

7. Přidej statistiky. Počítej počty správných a špatných odpovědí a na závěr vypiš tyto dvě čísla převedená na procenta.

8. Rozloučení před koncem hry uprav podle toho, kolik procent uživatel zodpověděl správně. Např. `"vedl sis dobře"`, `"dnes nic moc"`, .... kreativitě se meze nekladou.

9. Do souboru `utility.py` přidej funkci `retezec_procenta`, která bude mít jeden parametr `procento` a vrátí řetězec znaků `■` (znak si zkopíruj, nebo použij např. X) délky `procento // 10`. 

Např. `retezec_procenta(30)`, vrátí `■■■`.

10. Využij funkci `retezec_procenta` k zobrazení výsledku.

11. Celý kód v souboru hra zabal do jedné funkce `hra` (je na čase naučit se klávesovou zkratku pro odsazení celého bloku kódu) a založ soubor `app.py`, kde bude pouze:
```
from hra import hra

hra()
```
Vyzkoušej si, že program funguje a přidej do funce `hra` ještě `return`, který bude vrace počet procent správných odpovědí. 

12. Přidej na začátku dotaz na jméno hráče a počet správných odpovědí ulož do souboru se jménem `f"{jmeno_hrace}.txt"`. Pro otevření souboru použij `"a"`, tím připojíš výsledek na konec existujícího souboru, pokud již soubor existuje. 
```
with open(f"{jmeno_hrace}.txt", "a", encoding="utf-8") as f:
    print(spravne, file=f)
```