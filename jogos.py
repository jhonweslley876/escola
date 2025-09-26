import os
import random

fichas_totais = 1000
print(f'Suas fichas iniciais: {fichas_totais}')

while fichas_totais > 0:
    
    fichas = int(input('Quantas fichas você quer apostar?: '))
    if fichas > fichas_totais:
        print('Você não tem fichas suficientes para isso!')
        continue

    if fichas > 0:
        print('__________________________________________________')
        fichas_totais -= fichas
        print(f'Suas fichas totais são: {fichas_totais} após apostar {fichas}')

    baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4
    random.shuffle(baralho)

    def formatar_carta(carta):
        if carta == 1:
            return 'A'
        if carta == 10:
            return random.choice(['K', 'Q', 'J'])
        return str(carta)

    cartas = [baralho.pop(), baralho.pop()]
    total = sum(cartas)

    print('__________________________________________________')
    print(f'Suas cartas são: {", ".join(formatar_carta(c) for c in cartas)}')
    print(f'Seu total é: {total}')

    while True:
        print('__________________________________________________')
        compras = input('Comprar ou Finalizar?: ').strip().lower()

        if compras == 'comprar':
            print('__________________________________________________')
            nova_carta = baralho.pop()
            total += nova_carta
            cartas.append(nova_carta)

            print(f'Carta comprada: {formatar_carta(nova_carta)}.')
            print(f'Suas cartas: {", ".join(formatar_carta(c) for c in cartas)}.')
            print(f'Seu total é: {total}.')

            if total > 21:
                print('__________________________________________________')
                print(f'Você perdeu. Seu total de pontos é {total}, maior que 21!')
                print(f'Suas fichas: {fichas_totais}')
                break
        elif compras == 'finalizar':
            print('__________________________________________________')
            if total == 21:
                print('Parabéns, você ganhou!')
                fichas_totais += fichas * 2
                print(f'Suas fichas: {fichas_totais}')
            else:
                print('Veja se o seu valor é o maior da mesa para ganhar.')
                print('__________________________________________________')

                cartas_bot = [baralho.pop(), baralho.pop()]
                bot_total = sum(cartas_bot)

                print(f'Bot 1: {", ".join(formatar_carta(c) for c in cartas_bot)}')
                print(f'Bot 1: {bot_total}')

                while bot_total < 16:
                    nova_carta = baralho.pop()
                    cartas_bot.append(nova_carta)
                    bot_total += nova_carta
                    print(f'Bot 1 comprou: {formatar_carta(nova_carta)}')
                    print(f'Cartas Bot 1: {", ".join(formatar_carta(c) for c in cartas_bot)}')
                    print(f'Total: {bot_total}')
                    print('__________________________________________________')

                if bot_total > 21:
                    print('Bot 1 estourou o valor.')
                    print('Você venceu o jogo!')
                    fichas_totais += fichas * 2
                    print(f'Suas fichas: {fichas_totais}')

                elif total > bot_total:
                        print('Você ganhou!')
                        fichas_totais += fichas * 2
                        print(f'Suas fichas: {fichas_totais}')
                elif bot_total > total:
                    print('bot 1 ganhou!')
                    print(f'Suas fichas: {fichas_totais}')

                else:
                    print(f'Empate! as fichas serão devolvidas.')
                    fichas_totais += fichas
                    print(f'Suas fichas: {fichas_totais}')
                    print('__________________________________________________')

            break

        else:
            print('Digite apenas "comprar" ou "finalizar"!')

    if fichas_totais <= 0:
        print('Você perdeu todas as suas fichas! Boa sorte na próxima.')
        break

    continuar = input('Deseja continuar jogando? (s/n): ').strip().lower()
    print('__________________________________________________')
    if continuar != 's':
        print(f'Você terminou com {fichas_totais} fichas.')

        break