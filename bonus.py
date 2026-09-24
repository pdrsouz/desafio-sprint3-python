def fatorial(numero):
    """Retorna o fatorial de numero de forma recursiva."""
    if numero <= 1:
        return 1
    return numero * fatorial(numero - 1)


def relatorio(titulo, *linhas, **config):
    """Imprime um relatório com título, linhas e configurações."""
    largura = config.get("largura", 30)
    simbolo = config.get("simbolo", "=")
    print(simbolo * largura)
    print(titulo.upper().center(largura))
    print(simbolo * largura)
    for numero_linha, linha in enumerate(linhas, start=1):
        print(f"{numero_linha}. {linha}")
    print(simbolo * largura)


if __name__ == "__main__":
    print(f"5! = {fatorial(5)}")
    relatorio("Vendas", "Arroz: R$ 25,00", "Feijão: R$ 8,50", largura=24)


# Versão em Portugol (fatorial com repetição)
#
# programa {
#     funcao inteiro fatorial(inteiro numero) {
#         inteiro resultado = 1
#         para (inteiro i = 2; i <= numero; i++) {
#             resultado = resultado * i
#         }
#         retorne resultado
#     }
#
#     funcao relatorio(cadeia titulo, cadeia linhas[], inteiro quantidade,
#                      inteiro largura) {
#         para (inteiro i = 0; i < largura; i++) {
#             escreva("=")
#         }
#         escreva("\n", titulo, "\n")
#         para (inteiro i = 0; i < quantidade; i++) {
#             escreva(i + 1, ". ", linhas[i], "\n")
#         }
#         para (inteiro i = 0; i < largura; i++) {
#             escreva("=")
#         }
#         escreva("\n")
#     }
#
#     funcao inicio() {
#         cadeia linhas[2] = {"Arroz: R$ 25,00", "Feijão: R$ 8,50"}
#         escreva("5! = ", fatorial(5), "\n")
#         relatorio("VENDAS", linhas, 2, 24)
#     }
# }
