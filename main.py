def enchendo_galao():

    galao = float(input('Insira o volume do galão: '))
    qtd_garrafas = int(input('Insira a quantidade de garrafas: '))
    garrafas = list()
    i = 1

    while qtd_garrafas:

        garrafas.append(float(input(f'Garrafa {i}: ')))
        i += 1

        if i == qtd_garrafas + 1:
            break
        else:
            continue

    garrafas_ordenadas = sorted(garrafas)
    garrafas_usadas = list()
    volume_galao = galao
    sobra = 0

    for _ in garrafas:
        proximo = 0

        for garrafa in garrafas:
            if (garrafa <= volume_galao) & (garrafa > proximo):
                proximo = garrafa

        garrafas_usadas.append(proximo)
        volume_galao -= proximo

        if volume_galao == 0:
            break

    if sum(garrafas_usadas) < galao:
        for garrafa in garrafas_ordenadas:
            if garrafa >= volume_galao:
                garrafas_usadas.append(garrafa)
                sobra = abs(sum(garrafas_usadas) - galao)
                break

    garrafas_usadas = [filtro_garrafas for filtro_garrafas in garrafas_usadas if filtro_garrafas != 0]

    print(f'\nResposta: {garrafas_usadas}, sobra {sobra}L')


if __name__ == '__main__':
    enchendo_galao()
