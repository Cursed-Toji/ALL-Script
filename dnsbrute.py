#!/usr/bin/python3
import sys
import dns.resolver

resolver = dns.resolver.Resolver()




if len(sys.argv) == 1 or sys.argv[1] == '-h':
    print("Use desta forma: ./seu_script.py || python3  <alvo> <wordlist>")
    sys.exit()


try:
	alvo = sys.argv[1]
	wordlist = sys.argv[2]

except:
	print("Use desta forma: ./seu_script.py ||python3  <alvo> <wordlist>")

	sys.exit()


try:
    with open(wordlist, "r") as arq:
        subdominios = arq.read().splitlines()

except FileNotFoundError:
    print('arquivo não encontrado')
    sys.exit()


for subdominio in subdominios:
    try:
        sub_alvo = "{}.{}".format(subdominio, alvo)
        resp = resolver.resolve(sub_alvo, "A")
        for resultado in resp:
            print("{} -> {}".format(sub_alvo, resultado))
    except:
        pass
