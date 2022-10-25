from math import *
import numpy as np
import matplotlib.pyplot as plt


def FuncX(fx, x):
    resultado = fx.replace('x', str(x))
    return float(eval(resultado))


def FuncDeriv(fx, x):
    h = 0.00001
    return (FuncX(fx, x + h) - FuncX(fx, x)) / h


def TxVar(fxA, fxB, a, b):
    return float((fxB - fxA) / (b - a))


def Main(fx, a, b):
    fxA = FuncX(fx, a)
    fxB = FuncX(fx, b)
    listaAprox = []
    listaIntervalo = np.arange(a, b, 0.001)

    print('f(x) no ponto A = ', fxA)
    print('f(x) no ponto B = ', fxB)
    print('Taxa de variação = ', TxVar(fxA, fxB, a, b))

    for i in listaIntervalo:
        if round(FuncDeriv(fx, i), 2) == TxVar(fxA, fxB, a, b):
            print('Pontos aproximados', round(FuncDeriv(fx, i), 5))
            listaAprox.append(i)
        else:
            pass

    plt.text(a+1, 1.0, fx, horizontalalignment='center',
             fontsize=12, color='blue')

    # Gráfico derivada
    plt.plot(listaIntervalo, [round(FuncDeriv(fx, i), 2)
             for i in listaIntervalo], color='blue', label='Derivada')
    # Ponto da Media da variação
    if len(listaAprox) >= 1:
        plt.plot(listaAprox, [FuncDeriv(fx, i)
                              for i in listaAprox], 'ro', label='Variacao Media')
    else:
        print('Não foi possível encontrar um ponto aproximado')
    # Grafico f(x) da função
    plt.plot(listaIntervalo, [FuncX(fx, i)
             for i in listaIntervalo], color='purple', label='Funcao de X')
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()

# Entradas


f = input('Digite a função:\t')

a = float(input("Digite o ponto a: "))
b = float(input("Digite o ponto b: "))


Main(f, a, b)
