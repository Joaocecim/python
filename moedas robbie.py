def checa_primo(res):
    # variável que irá guardar o valor de: se é ou não é número primo

    flag = True

    # se o valor for maior que 1...

    if res > 1:

        # começamos de 2, porque é só divisível por ele mesmo, portanto não é primo.

        for i in range(2, res):

            # se o resto de algum valor do loop for 0 então esse numéro não é primo

            if (res % i) == 0:
                # False = não primo

                flag = False

                break

                # verificamos se a flag é False ou se o valor é igual a 1

    # e retorna o resultado esperado

    if flag == False or res == 1:
        return 'Bad boy! I’ll hit you.'

    # se nenhum das verificações forem reais... então retorna esse resultado
    return 'You’re a coastal aircraft, Robbie, a large silver aircraft.'

    while True:

        # Na definição do problema, ele nos diz que só vai parar quando houver um EOF

        # então usamos o tratamento de exceções

        # tente fazer o algoritmo abaixo

        try:

            # lista que irá guardar os valores digitados pelo usuário

            moedas = []

            # lê o valor da quantidade de moedas que irá ser lida.

            m = int(input())

            # lendo as moedas e guardando na lista

            for v in range(m):
                moedas.append(int(input()))

            # no problema descrito vemos que os valores são lidos inversamente, então

            # invertemos os valores.

            moedas.reverse()

            # lendo o valor que irá receber a quantidade de saltos na lista
        n = int(input())

        # variável que irá guardar a soma dos valores que foram saltados.

        soma = sum(moedas[::n])

        # mostra na tela o resultado da chamada da função

        print(checa_primo(soma))

        # se houver o erro EOF, pare o laço while.

    except EOFError:
    break

