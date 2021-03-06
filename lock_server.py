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
import sock_utils
import pickle as p
import select as sel
import lock_skel as skel


def handler(signum, frame):
    print ""
    print 'closing socket and program...'
    sock.close()
    sys.exit()


# Control + z handler
signal.signal(signal.SIGTSTP, handler)

if len(sys.argv) > 3:
    try:
        HOST = ''
        PORT = int(sys.argv[1])
        resource_number = int(sys.argv[2])
        resource_time = int(sys.argv[3])
    except:
        print "Input incorrecto, a usar os parametros padrão"
        HOST = ''
        PORT = 9999
        resource_number = 10
        resource_time = 10
else:
    HOST = ''
    PORT = 9999
    resource_number = 10
    resource_time = 10
    print "A utiizar os parametros padrão"

print "Porta: " + str(PORT)
print "Recursos: " + str(resource_number) + " Tempo: " + str(resource_time)


# iniciar o skel
lskel = skel.LockSkel(resource_number)

# iniciar sock e arrays extra
# msgcliente = []
# ret = []
sock = sock_utils.create_tcp_server_socket(HOST, PORT, 5)

# variaveis para select
SocketInput = [sock]
SocketOutput = []

while True:
    try:
        R, W, X = sel.select(SocketInput, SocketOutput, [])
        for soquete in R:
            try:
                if soquete is sock:
                    (conn_sock, addr) = sock.accept()
                    print "Cliente" + str(conn_sock.getpeername())
                    SocketInput.append(conn_sock)
                else:
                    resp = []
                    recvv = soquete.recv(50)
                    if recvv == '':
                        print 'Client Close' + str(soquete.getpeername())
                        soquete.close()
                        SocketInput.remove(soquete)
                    else:
                        tamanho = int(p.loads(recvv))
                        soquete.sendall(p.dumps("SIZEOK", -1))
                        comando = sock_utils.receive_all(soquete, tamanho)
                        if tamanho == sys.getsizeof(comando):
                            msg_unp = p.loads(comando)
                            print 'Pedido Recebido: ' + str(msg_unp)
                            print ""
                            msg_unp[1] = int(msg_unp[1])
                            if len(msg_unp) > 2:
                                msg_unp[2] = int(msg_unp[2])
                                msg_unp[1] = int(msg_unp[1])

                            resp = lskel.handle(msg_unp)
                            soquete.sendall(resp)
                        else:
                            print 'Erro: Mensagem recebida nao tem o mesmo tamanho da original'
                            soquete.close()
                            SocketInput.remove(soquete)
            except IOError:
                soquete.close()
                SocketInput.remove(soquete)
                print "Unexpected error:", sys.exc_info()[0]
    except KeyboardInterrupt:
        print 'closing socket and program...'
        sock.close()
        sys.exit()
sock.close()
