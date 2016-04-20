#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 25
Números de aluno: 44314, 43551, 44285
"""
# Zona para fazer imports

import sys
import signal
import lock_stub as ls


def handler(signum, frame):
    print ""
    print 'closing socket and program...'
    lstub.close()
    sys.exit()

# Control + z handler

signal.signal(signal.SIGTSTP, handler)

# Programa principal

client_commands = ["LOCK", "RELEASE", "TEST", "STATS", "EXIT"]
client_id_commands = ["LOCK", "RELEASE"]


if len(sys.argv) > 3:
    try:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        ID = int(sys.argv[3])
    except TypeError:
        print "Parametros Incorretos"
        sys.exit()

    lstub = ls.LockStub(HOST, PORT)

    try:
        while True:
            msg = raw_input("Comando: ")
            msg = msg.split(" ")
            
            try:
                for index, arg in enumerate(msg):
                    if msg[index] not in client_commands:
                        msg[index] = int(msg[index])
            except:
                print "String nos argumentos sem ser no comando!"
                continue

            # verificacao do comando

            if msg[0] == "EXIT":
                sys.exit()

            if len(msg) <= 1 or msg[0] not in client_commands:
                print "verificar comando"
                continue

            if msg[0] in client_id_commands and len(msg) == 2:
                msg.insert(1, ID)

            if msg[0] in client_commands and len(msg) > 1:
                if len(msg) <= 3:
                    resposta = ''

                    if msg[0] == 'LOCK':
                        resposta = lstub.lock(msg)

                    elif msg[0] == 'RELEASE':
                        resposta = lstub.release(msg)

                    elif msg[0] == 'TEST':
                        resposta = lstub.test(msg)

                    elif msg[0] == 'STATS':
                        resposta = lstub.stats(msg)

                    print 'Pedido Recebido: %s' % str(resposta)
                    print ""
                else:
                    print "O comando foi mal feito."
                    continue
            else:
                print "O comando foi mal feito."
                continue
    except KeyboardInterrupt:
        print ""
        print 'closing socket and program...'
        lstub.close()
        sys.exit()
else:
    print "Sem argumentos ou argumentos incompletos"
