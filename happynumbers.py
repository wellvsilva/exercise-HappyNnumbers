"""
Um número feliz é definido pelo seguinte processo:
Começando com qualquer número inteiro positivo, substitua o número pela soma dos
quadrados de seus dígitos e repita o processo até que o número seja igual a   1
(onde permanecerá) ou faça um loop infinito em um ciclo que não inclui   1 .
Os números para os quais esse processo termina em   1   são números felizes,
enquanto os que não terminam em   1   são números infelizes.
Exiba um exemplo de sua saída aqui.
"""
def happy(number):
    next_ = sum(int(char) ** 2 for char in str(number))
    return number in (1, 7) if number < 10 else happy(next_)


assert all([happy(n) for n in (1, 10, 100, 130, 97)])
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
