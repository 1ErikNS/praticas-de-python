'''Implemente o jogo da adivinhação. Neste jogo, um número é sorteado e o usuário
tenta adivinhar esse número por meio de uma sequência de palpites, ao passo que
vai recebendo feedbacks indicando se o número alvo é "maior" ou "menor" que o
último palpite dado. Para sortear um número inteiro, podemos usar a função
randint do módulo random.'''

from random import randint

loop = False
while not loop:
    numero_aleatorio = randint(1,100)
    print(numero_aleatorio)

    adivinhacao = False
    while not adivinhacao:
        numero_usuario = int(input('Digite um número: '))

        if(numero_usuario == numero_aleatorio):
            print('Parabéns você conseguiu adivinhar!!!!')
            adivinhacao = True
        else:
            print('Não foi dessa vez tente novamente!')

