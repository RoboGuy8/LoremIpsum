# Lorem ipsum generátor připomínající kombinaci češtiny, slovenštiny a maďarštiny.

- používá knihovny random a os
- generuje výsledný text do .txt souboru na plochu

- posloupnost kódu:
    - určení potřebných proměnných / seznamů
    - dokud počet vět se nerovná zadání, generuje náhodné věty o délce 3-10 slov. Slova mají délku 1-8 písmen.
    - generuje se náhodné první písmeno, které je velké, pokud je na začátku věty
    - pro slova o délce 1 a 2 písmena se přiřadí náhodný výběr již zadaných slov
    - náhodná generace písmen podle předešlého písmene. Pokud je minulé písmeno souhláska, je 80% šance, že další písmeno je        samohláska. Pokud je poslední písmeno samohláska, šance že další bude též je jen 5%.
    - sloučení písmen do slov a slov do vět
    - zápis výsledku do .txt souboru na plochu
