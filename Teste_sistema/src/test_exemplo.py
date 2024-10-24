def soma (a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multipicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

def teste_soma():
    assert soma (8,9) == 17
    assert soma (10,5) == 15
    assert soma (8,5) == 13

def teste_subtracao():
    assert subtracao (5,3) == 2
    assert subtracao (3,3) == 0
    assert subtracao (5,4) == 1

def teste_multiplicacao():
    assert multipicacao (2,5) == 10
    assert multipicacao (5,5) == 25
    assert multipicacao (3,10) == 30

def teste_divisao():
    assert divisao (10,2) == 5
    assert divisao (50,5) == 10
    assert divisao (100,2) == 50