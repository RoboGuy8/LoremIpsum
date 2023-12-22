import os
import random

pismena = ['a', 'b', 'c', 'č', 'd', 'e', 'é', 'ě', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 'ř', 's', 'š', 't', 'u', 'ů', 'v', 'y', 'ý', 'z', 'ž']

pocet_vet = int(input("Kolik vět byste si přál vygenerovat? "))
seznam_vet = []
souhlasky = ['b', 'c', 'č', 'd', 'h', 'ch', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 'ř', 's', 'š', 't', 'v', 'z', 'ž']
samohlasky = ['a', 'á', 'e', 'é', 'ě', 'i', 'í', 'o', 'u', 'ů', 'y', 'ý']
jednopismenove_spojeni = ["a", "i", "o", "u", "s", "z", "v", "k"]
dvoupismenove_spojeni = ['na', 'do', 'od', 'do', 'po', 'za', 'ne', 'se', 'si', 'te', 'ti', 'to', 'ty', 'už', 'ví', 'za', 'ze']

while pocet_vet != 0:
    pocet_slov = random.randint(3, 10) 
    veta = []

    for x in range(pocet_slov):
        delka = random.randint(1, 8)
        if delka == 1:
            slovo = random.choice(jednopismenove_spojeni)
        elif delka == 2:
            slovo = random.choice(dvoupismenove_spojeni)
        else:
            prvni_pismeno = random.choice(pismena)
            if prvni_pismeno in ["y", "ý"]:
                prvni_pismeno = random.choice(pismena)
            else:
                pass
            slovo = prvni_pismeno.capitalize() if x == 0 else prvni_pismeno.lower()
            minule_pismeno = prvni_pismeno


            for i in range(delka - 1):
                if minule_pismeno in samohlasky:
                    y = random.randint(1, 20)
                    if y == 1:
                        pismeno = random.choice(samohlasky)
                        if pismeno == minule_pismeno:
                            pismeno = ""
                    else:
                        pismeno = random.choice(souhlasky)
                        if pismeno == minule_pismeno:
                            pismeno = ""
                else:
                    y = random.randint(1, 5)
                    if y == 1:
                        pismeno = random.choice(souhlasky)
                        if pismeno == minule_pismeno:
                            pismeno = ""
                    else:
                        pismeno = random.choice(samohlasky)
                        if pismeno == minule_pismeno:
                            pismeno = ""

                slovo += pismeno
                minule_pismeno = pismeno

        veta.append(slovo)

    seznam_vet.append(' '.join(veta).capitalize())
    pocet_vet -= 1

lorem_ipsum = '. '.join(seznam_vet) + '.'

#vytváření .txt souboru pomocí gpt
cesta_na_plose = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
soubor_na_plose = os.path.join(cesta_na_plose, "vygenerovany_lorem_ipsum.txt")
with open(soubor_na_plose, "w", encoding="utf-8") as soubor:
    soubor.write(lorem_ipsum)

print(f"Text byl úspěšně zapsán do souboru {soubor_na_plose}.")
