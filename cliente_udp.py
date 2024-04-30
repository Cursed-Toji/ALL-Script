#usr/bin/python3
import socket

#Criação do socket Socke para conexões UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#junção do conect com o send
try:
    while True:
        msg = input('mensagem do invasor: ') + '\n'
        client.sendto(msg.encode(), ('127.0.0.1', 123))
        # nc lvup (u para escutar como udp)
        client.sendto(b'MTbobo: Digite sua mensagem\n', ('127.0.0.1', 123))
        #para receber os dados
        # 1 elementro da tupla vai pro data, segundo elemento vai pra sender
        #como é uma tupla vai dividir
        data, sender = client.recvfrom(1024)
        #como o data está vindo como bytes tem que dar o decode pra vim como st>
        print(sender[0] + ':', data.decode())
        if data.decode() == 'sair\n' or msg == 'sair\n':
            break
    client.close()
except Exception as error:
    print(error)

