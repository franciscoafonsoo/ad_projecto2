#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo:
Números de aluno:
"""

# Zona para fazer importação
import sys
import sock_utils
import pickle as p
import lock_skel as skel


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


# iniciar o skel
lskel = skel.lock_stub(resource_number)

msgcliente = []
ret = []
sock = sock_utils.create_tcp_server_socket(HOST, PORT, 1)

while True:
    (conn_sock, addr) = sock.accept()
    print 'ligado a %s', addr
    try:
        msg = sock_utils.receive_all(conn_sock, 1024)
        msg_unp = p.loads(msg)
        print 'recebi %s' % msg_unp
        msg_unp[1] = int(msg_unp[1])
        if len(msg_unp) > 2:
            msg_unp[2] = int(msg_unp[2])
            msg_unp[1] = int(msg_unp[1])

        msg_pronta_enviar = lskel.handle(msg_unp)
        msg_pronta_enviar = p.dumps(msg_pronta_enviar, -1)
        conn_sock.sendall(msg_pronta_enviar)
        conn_sock.close()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        conn_sock.close()
sock.close()
