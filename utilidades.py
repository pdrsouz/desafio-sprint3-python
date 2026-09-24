def celsius_para_fahrenheit(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return celsius * 9 / 5 + 32


def validar_senha(senha):
    """Retorna True se a senha tiver 8 ou mais caracteres."""
    return len(senha) >= 8


def caixa(*precos):
    """Retorna o total, o item mais caro e a média dos preços."""
    if not precos:
        return 0.0, 0.0, 0.0
    total = sum(precos)
    item_mais_caro = max(precos)
    media = total / len(precos)
    return total, item_mais_caro, media


def ficha_aluno(**dados):
    """Imprime os dados do aluno, uma informação por linha."""
    for campo, valor in dados.items():
        print(f"{campo.capitalize()}: {valor}")


def adicionar_item_seguro(item, lista_original=None):
    """Retorna uma nova lista com o item, sem alterar a original."""
    if lista_original is None:
        lista_original = []
    nova_lista = lista_original[:]
    nova_lista.append(item)
    return nova_lista


if __name__ == "__main__":
    print(f"25 °C = {celsius_para_fahrenheit(25):.1f} °F")
    print(f"'abc123' é válida? {validar_senha('abc123')}")
    print(f"'senha12345' é válida? {validar_senha('senha12345')}")
    total, mais_caro, media = caixa(10.0, 25.5, 7.0)
    print(f"Total: {total:.2f} | Mais caro: {mais_caro:.2f} | "
          f"Média: {media:.2f}")
    ficha_aluno(nome="Ana", curso="ADS", nota=9.5)
    compras = ["arroz"]
    print(f"{adicionar_item_seguro('feijão', compras)} | original: {compras}")


# Versão em Portugol
#
# programa {
#     inclua biblioteca Texto --> txt
#
#     funcao real celsius_para_fahrenheit(real celsius) {
#         retorne celsius * 9.0 / 5.0 + 32.0
#     }
#
#     funcao logico validar_senha(cadeia senha) {
#         retorne txt.numero_caracteres(senha) >= 8
#     }
#
#     funcao caixa(real precos[], inteiro quantidade) {
#         real total = 0.0
#         real item_mais_caro = precos[0]
#         para (inteiro i = 0; i < quantidade; i++) {
#             total = total + precos[i]
#             se (precos[i] > item_mais_caro) {
#                 item_mais_caro = precos[i]
#             }
#         }
#         escreva("Total: ", total, "\n")
#         escreva("Mais caro: ", item_mais_caro, "\n")
#         escreva("Média: ", total / quantidade, "\n")
#     }
#
#     funcao ficha_aluno(cadeia nome, cadeia curso, real nota) {
#         escreva("Nome: ", nome, "\n")
#         escreva("Curso: ", curso, "\n")
#         escreva("Nota: ", nota, "\n")
#     }
#
#     funcao adicionar_item_seguro(cadeia original[], inteiro tamanho,
#                                  cadeia item, cadeia nova[]) {
#         para (inteiro i = 0; i < tamanho; i++) {
#             nova[i] = original[i]
#         }
#         nova[tamanho] = item
#     }
#
#     funcao inicio() {
#         real precos[3] = {10.0, 25.5, 7.0}
#         cadeia compras[1] = {"arroz"}
#         cadeia nova_lista[2]
#
#         escreva("25 °C = ", celsius_para_fahrenheit(25.0), " °F\n")
#         escreva("'abc123' é válida? ", validar_senha("abc123"), "\n")
#         escreva("'senha12345' é válida? ", validar_senha("senha12345"))
#         escreva("\n")
#         caixa(precos, 3)
#         ficha_aluno("Ana", "ADS", 9.5)
#         adicionar_item_seguro(compras, 1, "feijão", nova_lista)
#         escreva(nova_lista[0], ", ", nova_lista[1])
#         escreva(" | original: ", compras[0], "\n")
#     }
# }
