#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 25
Números de aluno: 44314, 43551, 44285
"""
# Zona para fazer imports

import net_client
import pickle as p


class LockStub:

    def __init__(self, address, port):
        self.nt = net_client.NetClient(address, port)
        self.nt.connect()

    def lock(self, cms):
        cms[0] = '10'

        msg = p.dumps(cms, -1)
        return self.nt.send_receive(msg)

    def release(self, cms):
        cms[0] = '20'

        msg = p.dumps(cms, -1)
        return self.nt.send_receive(msg)

    def test(self, cms):
        cms[0] = '30'

        msg = p.dumps(cms, -1)
        return self.nt.send_receive(msg)

    def stats(self, cms):
        cms[0] = '40'

        msg = p.dumps(cms, -1)
        return self.nt.send_receive(msg)

    def close(self):
        self.nt.close()
