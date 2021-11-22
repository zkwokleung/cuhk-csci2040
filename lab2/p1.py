def check_sublist(list1, d1,d2,d3):
    lista = [x for x in list1 if x > max (d1,d2,d3)]
    listb = [x for x in list1 if x > (d1 * (d2+d3))]
    listc = [x for x in list1 if x < (d1+d2+d3)]
    return lista, listb, listc