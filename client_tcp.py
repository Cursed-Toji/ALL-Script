#!/usr/bin/python3

import socket

# Criando um cliente TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    # conectando-se ao servidor na máquina do KALI '0.tcp.sa.ngrok.io' na porta 11583
    client.connect(('0.tcp.sa.ngrok.io', 11583))

    # enviando uma mensagem para o KALI
    # o 'b' antes da string indica que está convertendo para bytes
    client.send(b"Oi, tudo bem?")
    client.sendall()

    # recebendo a resposta do Kali (até 1024 bytes)
    pacote_recebido = client.recv(1024).decode()

    # pegando o print da resposta do kali
    print(pacote_recebido)

except:
    # qualquer erro que der vai cair aqui
    print('Erro no pacote')
