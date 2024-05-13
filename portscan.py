import socket
import sys


def scan(host, ports, timeout=0.5):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(timeout)
            code = client.connect_ex((host, int(port)))

            if code == 0:
                print('[+] {} is open'.format(port))

    except:
        print('error')

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            ports = sys.argv[2].split(',')
            if len(sys.argv) >= 4:
                timeout =  sys.argv[4]
        else:
            ports = range(100)
        scan(host, ports, timeout)
    else:
        print('[-] Uso: python portscan.py [host] + porta')