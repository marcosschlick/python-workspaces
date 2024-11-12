import math

def raiz_arredondada(n):
    raiz = math.sqrt(n)
    if raiz.is_integer():
        return int(raiz)  # Retorna o valor inteiro se for exato
    else:
        return math.ceil(raiz)  # Arredonda para cima se não for inteiro

# Testando a função
print(raiz_arredondada(2))  # Saída esperada: 5
print(raiz_arredondada(16))  # Saída esperada: 4

