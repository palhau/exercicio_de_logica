# Desafio de programação inicial

# 1- O galão deve ser completamente preenchido com o volume das garrafas;
# 2- Procure esvaziar totalmente as garrafas escolhidas;
# 3- Quando não for possível esvaziar todas garrafas escolhidas, deixe a menor sobra possível;
# 4- utilize o menor número de garrafas possível;

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
    valor_galao = galao

    for map_garrafa in garrafas:
        proximo = 0
        sobra = 0

        for garrafa in garrafas:
            if (garrafa <= valor_galao) & (garrafa > proximo):
                proximo = garrafa

        garrafas_usadas.append(proximo)
        valor_galao -= proximo

        if valor_galao == 0:
            break

    if sum(garrafas_usadas) < galao:
        for garrafa in garrafas_ordenadas:
            if garrafa >= valor_galao:
                garrafas_usadas.append(garrafa)
                sobra = abs(sum(garrafas_usadas) - galao)
                break

    garrafas_usadas = [filtro_garrafas for filtro_garrafas in garrafas_usadas if filtro_garrafas != 0]

    print(garrafas_usadas)
    print(f'Resposta: {garrafas_usadas}, sobra {sobra}L')


if __name__ == '__main__':
    enchendo_galao()
