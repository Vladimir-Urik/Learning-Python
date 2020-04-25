def add(c1, c2):
    return c1 + c2

def rem(c1, c2):
    return c1 - c2

def krat(c1, c2):
    return c1 * c2

def deleno(c1, c2):
    return c1 / c2

volba = input("Vyber si operáciu(plus,minus,krat,deleno)")
cislo1 = float(input("Zadaj čislo: "))
cislo2 = float(input("Zadaj čislo: "))

if(volba == "plus"):
    print('----------------------------------')
    print('Príklad: ', cislo1 ,' + ', cislo2 ,' = ?')
    print('Výsledok: ', add(cislo1, cislo2))
    print('----------------------------------')

elif(volba == "minus"):
    print('----------------------------------')
    print('Príklad: ', cislo1 ,' - ', cislo2 ,' = ?')
    print('Výsledok: ', rem(cislo1, cislo2))
    print('----------------------------------')

elif(volba == "krat"):
    print('----------------------------------')
    print('Príklad: ', cislo1 +' x '+ cislo2 ,' = ?')
    print('Výsledok: ', krat(cislo1, cislo2))
    print('----------------------------------')

elif(volba == "deleno"):
    print('----------------------------------')
    print('Príklad: ', cislo1 ,' : ', cislo2 ,' = ?')
    print('Výsledok: ', deleno(cislo1, cislo2))
    print('----------------------------------')

else:
    print('Kamo ty si kolko litrov vodky vypil?')