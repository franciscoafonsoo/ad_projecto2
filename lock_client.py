#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo:
Números de aluno:
"""
# Zona para fazer imports

import sys
import lock_stub as ls

# Programa principal

client_commands = ["LOCK", "RELEASE", "TEST", "STATS", "EXIT"]
client_id_commands = ["LOCK", "RELEASE"]


if len(sys.argv) > 3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ID = int(sys.argv[3])

    lstub = ls.LockStub(HOST, PORT)

    while True:
        msg = raw_input("Comando: ")
        msg = msg.split(" ")

        # verificacao do comando

        if msg[0] == "EXIT":
            sys.exit()

        if msg[0] in client_id_commands and len(msg) == 2:
            msg.insert(1, ID)
            print msg

        if msg[0] in client_commands and len(msg) > 1:

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
            "Comando estranho"
else:
    print "Sem argumentos ou argumentos incompletos"
