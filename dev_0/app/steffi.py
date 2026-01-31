import markus

# Variablen

nums_steffi = [100,99,98,97,96,95]

def demo_lists_noob():
    print("\nPYTHON LISTS - DEMO BY STEFFI")


    # 2 Listen mit Elementen gleichen Datentyps verbinden - 1 // + operator
    print("\nListen mit '+' verbinden, gleicher Datentyp:")
    nums_steffi_markus = nums_steffi + markus.nums
    print(nums_steffi_markus)

    # 2 Listen mit Elementen gleichen Datentyps verbinden - 2 //append: genau 1! Element (gesamte Liste = 1 Element)
    print("\nListen mit 'append' verbinden (bzw. Listenelement anhängen), gleicher Datentyp:")
    nums_steffi.append(markus.nums)
    print(nums_steffi)

    # 1 Angehängte Liste wieder entfernen
    print("\nAngehängtes Element (=Liste) mit remove wieder entfernen:")
    nums_steffi.remove(markus.nums)
    print(nums_steffi)

    # 2 Listen mit Elementen gleichen Datentyps verbinden - 3 //extend: erweitert Liste um alle Elemente
    print("\nListe mit extend um Elemente erweitern:")
    nums_steffi.extend(markus.nums)
    print(nums_steffi_markus)

    # Liste automatisch numerisch (absteigend) sortieren
    print("\nListe mit sort (und reverse) sortieren:")
    nums_steffi.sort(reverse=True)
    print(nums_steffi)\

    # Mit Funktion gemergte Liste "+" File-Liste
    print("\nNeue Liste: File Liste + return von Funktion test_merge")
    new_list = nums_steffi + markus.test_merge()
    print(new_list)

