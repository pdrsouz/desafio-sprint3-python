def media(*valores):
    """Retorna a média aritmética dos valores."""
    return sum(valores) / len(valores)


def mediana(*valores):
    """Retorna o valor central dos valores ordenados."""
    ordenados = sorted(valores)
    meio = len(ordenados) // 2
    if len(ordenados) % 2 == 0:
        return (ordenados[meio - 1] + ordenados[meio]) / 2
    return ordenados[meio]


def moda(*valores):
    """Retorna o valor que mais se repete."""
    return max(valores, key=valores.count)


if __name__ == "__main__":
    notas = (7, 8, 8, 9, 10)
    print(f"Média: {media(*notas):.2f}")
    print(f"Mediana: {mediana(*notas)}")
    print(f"Moda: {moda(*notas)}")


# Versão em Portugol
#
# programa {
#     funcao real media(real valores[], inteiro quantidade) {
#         real soma = 0.0
#         para (inteiro i = 0; i < quantidade; i++) {
#             soma = soma + valores[i]
#         }
#         retorne soma / quantidade
#     }
#
#     funcao real mediana(real valores[], inteiro quantidade) {
#         real auxiliar
#         para (inteiro i = 0; i < quantidade - 1; i++) {
#             para (inteiro j = 0; j < quantidade - 1 - i; j++) {
#                 se (valores[j] > valores[j + 1]) {
#                     auxiliar = valores[j]
#                     valores[j] = valores[j + 1]
#                     valores[j + 1] = auxiliar
#                 }
#             }
#         }
#         se (quantidade % 2 == 0) {
#             retorne (valores[quantidade / 2 - 1]
#                      + valores[quantidade / 2]) / 2.0
#         }
#         retorne valores[quantidade / 2]
#     }
#
#     funcao real moda(real valores[], inteiro quantidade) {
#         real valor_moda = valores[0]
#         inteiro maior_contagem = 0
#         inteiro contagem
#         para (inteiro i = 0; i < quantidade; i++) {
#             contagem = 0
#             para (inteiro j = 0; j < quantidade; j++) {
#                 se (valores[j] == valores[i]) {
#                     contagem = contagem + 1
#                 }
#             }
#             se (contagem > maior_contagem) {
#                 maior_contagem = contagem
#                 valor_moda = valores[i]
#             }
#         }
#         retorne valor_moda
#     }
#
#     funcao inicio() {
#         real notas[5] = {7.0, 8.0, 8.0, 9.0, 10.0}
#         escreva("Média: ", media(notas, 5), "\n")
#         escreva("Mediana: ", mediana(notas, 5), "\n")
#         escreva("Moda: ", moda(notas, 5), "\n")
#     }
# }
