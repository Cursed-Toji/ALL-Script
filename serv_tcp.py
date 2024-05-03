#!/usr/bin/python3

#Usar o netcat como cliente nc 127.0.0.1 + porta
import socket

#cria um serve tcp
serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

file = open('test.txt', 'w')

try:
    # inicia o serv '0.0.0.0' (todos os IPs disponíveis na máquina) e à porta 123
    serve.bind(('0.0.0.0', 123))

    #numero maximo conexões simultâneas que o servidor pode usar em 5
    serve.listen(5)
    print('Socket is listening')

    # aguada o aceite da conexão
    client_socket, address = serve.accept()
    print('Socket is connected', address[0])

    # Loop infinito para receber dados do cliente

    # Recebe dados do cliente (máximo de 1024 bytes) e os decodifica em uma string
    data = client_socket.recv(1024).decode()

    file.write(data)

    # Fecha o socket do servidor
    serve.close()

except Exception as error:
    # Em caso de exceção, imprime o erro
    print(error)
    serve.close()

    # Comentários adicionais sobre o código que foi removido
    '''
    print(serve.accept())
    # serve.accept() retorna uma tupla contendo um objeto de socket do servidor e o endereço do cliente
    # A primeira parte do retorno é um objeto de socket do cliente
    # A segunda parte é uma tupla contendo o endereço do cliente e a porta de saída que utilizou para fazer a conexão
    # Exemplo: (<socket.socket fd=4, family=2, type=1, proto=0, laddr=('127.0.0.1', 123), 
    #            raddr=('127.0.0.1', 53600)>, ('127.0.0.1', 53600))
    # O primeiro elemento da segunda tupla é o endereço IP do cliente e a segunda é a porta de saída que o cliente utilizou
    '''
