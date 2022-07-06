import random
import hoofdstuk1
import hoofdstuk2
import hoofdstuk3
import hoofdstuk4
import hoofdstuk6
import oefening1
import oefening2
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import oefening3
import oefening4
import oefening5
import python1_expressies
import hoofdstuk5
import python2_selectiestructuren
import python3_lussen
import python4_functies
import python5_lijsten_en_tuples
from oefening7 import BankRekening
from python7_klassen import Dog


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #oefening1.boekenBestellen()
    #oefening1.somVanTweeGetallen()
    #oefening1.krekelAlsThermometer()
    #oefening1.isbn()
    #oefening1.thePuddingGuy()
    #oefening1.eentweedriedrietweeeen()
    #oefening1.appelsSchikken()
    #oefening1.autoverhuur()
    #oefening2.isbn()
    #oefening2.blad_steen_schaar()
    #oefening2.apgar()
    #oefening2.vierkantsvergelijking()
    #oefening2.vierkaarten()
    #oefening2.valsmunterij()
    #oefening2.babysit()
    #oefening2.botsing()
    #oefening3.getalladder()
    #oefening3.apenEnKokosnoten()
    #oefening3.baselProbleem()
    #oefening3.biljarttafel()
    #oefening3.blackjack()
    #oefening3.beleefdheid()
    #oefening3.bevriendeGetallen()
    #oefening3.boeketRozen()
    #oefening3.drieWijzen()
    #print(oefening4.maximale_blootstelling(120))
    #print(oefening4.bovensteboven(90306))
    #print(oefening4.volgende(98765))
    #print(oefening4.waardering(3.44, 0.70))
    #print(oefening4.wisselkoersanalyse('3.44 pond sterling', 0.70))
    #print(oefening4.evenOneven(886328712442992))
    #print(oefening4.stappen(1))
    #print(oefening5.alfabetisch('je ziet een boel vliegen vliegen maar er is geen een bij bij'))
    #print(oefening5.driehoek(3.14))
    #print(oefening5.zeshoek(3,3))
    #print(oefening5.kwadraat(16, 7))
    #index = hoofdstuk1.zoekBinair([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 70)
    #print(f"index = {index}")
    #a = [int(_) for _ in input().split()]
    #hoofdstuk1.selection_sort_vooraan(a)
    #a = [int(_) for _ in input().split()]
    #hoofdstuk1.bubble_sort(a)
    #print(hoofdstuk2.rekenmachine("3 + 5 * 2"))
    #print(hoofdstuk2.evalueer_postfix(["3", "5", "*", "2", "-"]))
    #print(hoofdstuk2.infix_naar_postfix(["3", "*", "5"]))
    #print(f'{python1_expressies.boeken_bestellen():.2f}')
    #print(python1_expressies.som_van_twee_getallen())
    #python1_expressies.de_krekel_als_thermometer()
    #print(python1_expressies.isbn())
    #print(python1_expressies.the_pudding_guy())
    #print(python1_expressies.eentweedrie())
    #python1_expressies.appels_schikken()
    #print(hoofdstuk5.precies_een_verschillend("span", "zpin"))
    #python2_selectiestructuren.isbn()
    #python2_selectiestructuren.apgar()
    #python3_lussen.toevoegenachteraan()
    #python3_lussen.getalladder()
    #python3_lussen.Euler()
    #python3_lussen.beleefdheid()
    #print(python4_functies.lawaaidoofheid(105))
    #print(python4_functies.bovensteboven(90306))
    #print(python4_functies.waardering(3.44, 0.70))
    #print(python4_functies.wisselkoersanalyse('3.44 euro', 0.70))
    #print(python4_functies.csom(377096267))
    #python5_lijsten_en_tuples
    #print(hoofdstuk3.twoSum([1, 5, 16, 17, 18, 20, 21,22,23,24,25,26,19], 20))
    #print(hoofdstuk3.twoSumHash([1, 5, 16, 17, 18, 20, 21,22,23,24,25,26,19], 20))
    # b4 = hoofdstuk4.BinaryHeap(max_size=10000)
    # elems = list(range(10000))
    # random.shuffle(elems)
    # for elem in elems:
    #     b4.insert_elem(elem)
    # toto = b4.get_min_elem()
    # print(toto)
    #d = Dog('Frolic')
    #print(d)
    #print(d.__repr__())
    #b1 = BankRekening('Jan Jansen', '001457894501', 10000)
    #b2 = BankRekening('Peter Peeters', '842457894511', 10000)
    #b1.storten(250)
    #b1.afhalen(1000)
    #b2.afhalen(300)
    #str(b1)
    #print(b2)
    #repr(b2)
    # words = ["aa", "ab", "ac", "ad", "ba", "bb", "bc", "bd", "ca", "cb", "cc", "cd", "da", "db", "dc", "dd"]
    # graaf = hoofdstuk5.maak_graaf(words)
    # print(graaf)
    # print(graaf['ab'])
    # pred = hoofdstuk5.korste_pad(graaf,'cd')
    # print(pred)
    # print(hoofdstuk5.geef_pad(pred, "ba"))
    # s = hoofdstuk6.AchtPuzzel()
    # print(s)
    # print(sorted(s.opvolgers()))
    # s1 = hoofdstuk6.AchtPuzzel("724506831")
    # s2 = hoofdstuk6.AchtPuzzel("012345678")
    # s1.manhattan_heuristiek(s2)
    doel_puzzel = hoofdstuk6.AchtPuzzel("123456780")
    start_puzzel = hoofdstuk6.AchtPuzzel("120453786")
    is_doel = lambda p: p == doel_puzzel
    heuristiek0 = lambda p: 0
    print(start_puzzel)
    print(doel_puzzel)
    (acties, kost) = hoofdstuk6.a_ster_zoeken(start_puzzel, is_doel, heuristiek0)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
