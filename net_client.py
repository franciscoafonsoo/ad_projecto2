# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - net_client.py
Grupo:
Números de aluno:
"""

# zona para fazer importação

import sock_utils as s
import pickle as p

# definição da classe server


class server:
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
        resposta recebida pela mesma socket.
        """
        self.client_sock.sendall(p.dumps(data))
        temp = s.receive_all(self.client_sock, 1024)
        return p.loads(temp)

    def close(self):
        """
        Termina a ligação ao servidor.
        """

        self.client_sock.close()
