conjunto1 = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
print("Conjunto1: {}".format(conjunto1))
print("Conjunto2: {}".format(conjunto2))

conjunto_union = conjunto1.union(conjunto2)
print("\nUnião: {}".format(conjunto_union))

conjunto_interseccao = conjunto1.intersection(conjunto2)
print("Intersecção: {}".format(conjunto_interseccao))

conjunto_diferenca1 = conjunto1.difference(conjunto2)
print("Diferença: {}".format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print("Diferença: {}".format(conjunto_diferenca2))

conjunto_diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferença Simétrica: {}".format(conjunto_diferenca_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4}
print("\n\nconjunto_a: {}".format(conjunto_a))
print("conjunto_b: {}".format(conjunto_b))
print("\na issubset b: {}".format(conjunto_a.issubset(conjunto_b)))
print("b issubset a: {}".format(conjunto_b.issubset(conjunto_a)))
print("a issuperset b: {}".format(conjunto_a.issuperset(conjunto_b)))
print("b issuperset a: {}".format(conjunto_b.issuperset(conjunto_a)))

lista_animais = ["cachorro", "cachorro", "gato", "gato", "cavalo"]
print("\n\nLista animais: {}".format(lista_animais))
conjunto_animais = set(lista_animais)
print("Conjunto animais: {}".format(conjunto_animais))
lista_animais = list(conjunto_animais)
print("Lista animais: {}".format(lista_animais))

#conjunto = {1,2,3,4}
#conjunto.add(5)
#conjunto.discard(2)
#print(conjunto)