def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a, b):
    """Retorna a diferença entre a e b."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto de a e b."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de a por b, ou None se b for zero."""
    if b == 0:
        print("Erro: não é possível dividir por zero.")
        return None
    return a / b


if __name__ == "__main__":
    print(f"somar(10, 5) = {somar(10, 5)}")
    print(f"subtrair(10, 5) = {subtrair(10, 5)}")
    print(f"multiplicar(10, 5) = {multiplicar(10, 5)}")
    print(f"dividir(10, 5) = {dividir(10, 5)}")
    print(f"dividir(10, 0) = {dividir(10, 0)}")


# Versão em Portugol
#
# programa {
#     funcao real somar(real a, real b) {
#         retorne a + b
#     }
#
#     funcao real subtrair(real a, real b) {
#         retorne a - b
#     }
#
#     funcao real multiplicar(real a, real b) {
#         retorne a * b
#     }
#
#     funcao real dividir(real a, real b) {
#         se (b == 0.0) {
#             escreva("Erro: não é possível dividir por zero.\n")
#             retorne 0.0
#         }
#         retorne a / b
#     }
#
#     funcao inicio() {
#         escreva("somar(10, 5) = ", somar(10.0, 5.0), "\n")
#         escreva("subtrair(10, 5) = ", subtrair(10.0, 5.0), "\n")
#         escreva("multiplicar(10, 5) = ", multiplicar(10.0, 5.0), "\n")
#         escreva("dividir(10, 5) = ", dividir(10.0, 5.0), "\n")
#         escreva("dividir(10, 0) = ", dividir(10.0, 0.0), "\n")
#     }
# }
