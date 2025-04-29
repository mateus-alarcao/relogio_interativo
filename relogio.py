import time
from datetime import datetime
import requests
import pytz
import difflib
import random


def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    jogador = input("Escolha: pedra, papel ou tesoura: ").lower()
    if jogador not in opcoes:
        print("Escolha inválida!")
        return
    computador = random.choice(opcoes)
    print(f"Computador escolheu: {computador}")
    if jogador == computador:
        print("Empate!")
    elif (
            (jogador == 'pedra' and computador == 'tesoura') or
            (jogador == 'papel' and computador == 'pedra') or
            (jogador == 'tesoura' and computador == 'papel')
    ):
        print("Você venceu!")
    else:
        print("Você perdeu!")


def get_country():
    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    print("País:", data.get("country"))


def encontrar_timezone(lugar_usuario):
    todos_fusos = pytz.all_timezones
    resultado = difflib.get_close_matches(lugar_usuario.lower(), [tz.lower() for tz in todos_fusos], n=1)
    if resultado:
        indice = [tz.lower() for tz in todos_fusos].index(resultado[0])
        return todos_fusos[indice]
    else:
        return None


def mostrar_hora(lugar):
    timezone_name = encontrar_timezone(lugar)
    if timezone_name:
        timezone = pytz.timezone(timezone_name)
        hora = datetime.now(timezone)
        print(f"Hora em {timezone_name}: {hora.strftime('%H:%M:%S - %d/%m/%Y')}")
    else:
        print("Localização não reconhecida.")

print("BEM VINDO")
time.sleep(0.5)
print("carregando", end='')
for x in range(1, 5):
    print(f".", end='')
    time.sleep(0.5)
print()
print('=-' * 10)
print("RELÓGIO")
print('=-' * 10)
time.sleep(0.5)
hora_atual = datetime.now().strftime("%H:%M:%S")
print(f'HORA ATUAL: {hora_atual}')
print('=-' * 10)
time.sleep(0.5)
print("LOCALIZAÇÃO")
get_country()
time.sleep(0.5)
while True:
    print('=-' * 10)
    print("OPÇÕES: ")
    print("1: TEMPORIZADOR")
    print("2: CRONOMETRO")
    print("3: HORA EM OUTRO LUGAR DO MUNDO")
    print("4: SAIR")
    print("5: EXTRA")

    resposta = int(input("O que quer fazer? "))

    if resposta == 1:
        print('=-' * 10)
        tempo = int(input("QUANTOS SEGUNDOS? "))
        while tempo != 0:
            print(tempo)
            tempo -= 1
            time.sleep(1)

    elif resposta == 2:
        print('=-' * 10)
        tempocro = int(input("QUANTOS SEGUNDOS? "))
        for x in range(1, tempocro + 1):
            print(x)
            time.sleep(1)

    elif resposta == 3:
        print('=-' * 10)
        lugar = str(input("QUAL LUGAR? "))
        mostrar_hora(lugar)

    elif resposta == 4:
        print("VOLTE SEMPRE")
        print("desligando", end='')
        for x in range(1, 5):
            print(f".", end='')
            time.sleep(0.5)
        break

    elif resposta == 5:
        jogar()
