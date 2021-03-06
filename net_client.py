# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 25
Números de aluno: 44314, 43551, 44285
"""
# Zona para fazer imports

import sock_utils as s
import pickle as p
import sys

# definição da classe server


class NetClient:
    """
    Classe para abstrair uma ligação a um servidor TCP. Implementa métodos
    para estabelecer a ligação, para envio de um comando e receção da resposta,
    e para terminar a ligação
    """

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.client_sock = s.create_tcp_client_socket()

    def connect(self):
        """
        Estabelece a ligação ao servidor especificado na inicialização do
        objeto.
        """
        self.client_sock.connect((self.address, self.port))

    def send_receive(self, data):
        """
        Envia os dados contidos em data para a socket da ligação, e retorna a
        resposta recebida pela mesma socket. aplied to client
        """
        test = sys.getsizeof(data)
        test = str(test)
        tamanho = p.dumps(test, -1)
        self.client_sock.send(tamanho)

        if p.loads(self.client_sock.recv(2048)) == 'SIZEOK':

            self.client_sock.send(data)
            resposta = self.client_sock.recv(2048)
            msg = p.loads(resposta)

            return msg

    def close(self):
        """
        Termina a ligação ao servidor.
        """

        self.client_sock.close()
