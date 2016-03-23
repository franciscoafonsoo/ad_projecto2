#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo:
Números de aluno:
"""

# Zona para fazer importação
import time as t
import pickle
import sock_utils
import sys
import lock_pool as l


if len(sys.argv) > 3:
    HOST = ''
    PORT = int(sys.argv[1])
    resource_number = int(sys.argv[2])
    resource_time = int(sys.argv[3])

else:
    HOST = ''
    PORT = 9999
    resource_number = 10
    resource_time = 10
    print "A utiizar os parametros padrão"

print "Porta: " + str(PORT)
print "Recursos: " + str(resource_number) + " Tempo: " + str(resource_time)

lp = l.lock_pool(resource_number)
msgcliente = []
ret = []
sock = sock_utils.create_tcp_server_socket(HOST, PORT, 1)

while True:
    (conn_sock, addr) = sock.accept()
    print 'ligado a %s', addr
    try:
        msg = sock_utils.receive_all(conn_sock, 1024)
        msg_unp = pickle.loads(msg)
        print 'recebi %s' % msg_unp
        msg_unp[1] = int(msg_unp[1])
        if len(msg_unp) > 2:
            msg_unp[2] = int(msg_unp[2])
            msg_unp[1] = int(msg_unp[1])

        if msg_unp[1] > len(lp.lock_pool_array):
            msg_pronta_enviar = 'UNKNOWN RESOURCE'
        else:
            lp.clear_expired_locks()
            if msg_unp[0] == 'LOCK':
                if lp.lock(msg_unp[1], msg_unp[2], t.time() + resource_time):
                    msg_pronta_enviar = 'OK'
                else:
                    msg_pronta_enviar = 'NOK'

            elif msg_unp[0] == 'RELEASE':
                if lp.release(msg_unp[1], msg_unp[2]):
                    msg_pronta_enviar = 'OK'
                else:
                    msg_pronta_enviar = 'NOK'

            elif msg_unp[0] == 'TEST':
                if lp.test(msg_unp[1]):
                    msg_pronta_enviar = 'LOCKED'
                else:
                    msg_pronta_enviar = 'UNLOCKED'

            elif msg_unp[0] == 'STATS':
                msg_pronta_enviar = lp.stat(msg_unp[1])

            else:
                print "ERROR ERROR ERROR ABORT ABORT ABORT :D"
                msg_pronta_enviar = "cant do op"

        msg_pronta_enviar = pickle.dumps(msg_pronta_enviar, -1)
        conn_sock.sendall(msg_pronta_enviar)
        conn_sock.close()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        conn_sock.close()
sock.close()
