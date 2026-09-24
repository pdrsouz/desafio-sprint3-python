import calculadora
import utilidades
import estatistica as est
from bonus import fatorial, relatorio


def main():
    """Executa as funções dos módulos criados."""
    print("--- Calculadora ---")
    print(f"10 + 5 = {calculadora.somar(10, 5)}")
    print(f"10 - 5 = {calculadora.subtrair(10, 5)}")
    print(f"10 x 5 = {calculadora.multiplicar(10, 5)}")
    print(f"10 / 5 = {calculadora.dividir(10, 5)}")
    print(f"10 / 0 = {calculadora.dividir(10, 0)}")

    print("\n--- Conversor de temperatura ---")
    temperatura_celsius = 36.5
    temperatura_fahrenheit = utilidades.celsius_para_fahrenheit(
        temperatura_celsius
    )
    print(f"{temperatura_celsius} °C = {temperatura_fahrenheit:.1f} °F")

    print("\n--- Validador de senha ---")
    for senha in ("abc123", "senhaforte2026"):
        print(f"'{senha}' é válida? {utilidades.validar_senha(senha)}")

    print("\n--- Caixa ---")
    total, item_mais_caro, media_precos = utilidades.caixa(
        12.90, 45.00, 7.50, 30.00
    )
    print(f"Total: R$ {total:.2f}")
    print(f"Item mais caro: R$ {item_mais_caro:.2f}")
    print(f"Média: R$ {media_precos:.2f}")

    print("\n--- Ficha do aluno ---")
    utilidades.ficha_aluno(nome="Pedro", curso="ADS", semestre=2, nota=9.0)

    print("\n--- Lista segura ---")
    lista_compras = ["arroz", "feijão"]
    nova_lista = utilidades.adicionar_item_seguro("café", lista_compras)
    print(f"Lista original: {lista_compras}")
    print(f"Nova lista: {nova_lista}")

    print("\n--- Estatística (bônus) ---")
    notas = (7, 8, 8, 9, 10)
    print(f"Média: {est.media(*notas):.2f}")
    print(f"Mediana: {est.mediana(*notas)}")
    print(f"Moda: {est.moda(*notas)}")

    print("\n--- Fatorial e relatório (bônus) ---")
    print(f"5! = {fatorial(5)}")
    relatorio("Resumo", "Módulos importados", "Funções reaproveitadas",
              largura=26, simbolo="-")


if __name__ == "__main__":
    main()


# Versão em Portugol
#
# programa {
#     inclua biblioteca calculadora
#     inclua biblioteca utilidades
#
#     funcao inicio() {
#         real precos[4] = {12.90, 45.00, 7.50, 30.00}
#         cadeia lista_compras[2] = {"arroz", "feijão"}
#         cadeia nova_lista[3]
#
#         escreva("10 + 5 = ", calculadora.somar(10.0, 5.0), "\n")
#         escreva("10 - 5 = ", calculadora.subtrair(10.0, 5.0), "\n")
#         escreva("10 x 5 = ", calculadora.multiplicar(10.0, 5.0), "\n")
#         escreva("10 / 5 = ", calculadora.dividir(10.0, 5.0), "\n")
#         escreva("10 / 0 = ", calculadora.dividir(10.0, 0.0), "\n")
#
#         escreva("36.5 °C = ")
#         escreva(utilidades.celsius_para_fahrenheit(36.5), " °F\n")
#
#         escreva("'abc123' é válida? ")
#         escreva(utilidades.validar_senha("abc123"), "\n")
#
#         utilidades.caixa(precos, 4)
#         utilidades.ficha_aluno("Pedro", "ADS", 9.0)
#
#         utilidades.adicionar_item_seguro(lista_compras, 2, "café",
#                                          nova_lista)
#         escreva("Original: ", lista_compras[0], ", ", lista_compras[1])
#         escreva("\nNova: ", nova_lista[0], ", ", nova_lista[1], ", ")
#         escreva(nova_lista[2], "\n")
#     }
# }
