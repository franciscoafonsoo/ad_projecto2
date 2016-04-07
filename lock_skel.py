#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 25
Números de aluno: 44314, 43551, 44285
"""
# Zona para fazer imports

import lock_pool as l
import pickle as p
import time as t


class LockSkel:

    def __init__(self, rs):
        self.rs = rs    
        self.lp = l.LockPool(rs)

    def handle(self, cms):

        self.lp.clear_expired_locks()

        if cms[0] == '10':
            msg = self.lock(cms)
        elif cms[0] == '20':
            msg = self.release(cms)
        elif cms[0] == '30':
            msg = self.test(cms)
        elif cms[0] == '40':
            msg = self.stats(cms)
        else:
            print "Comando Errado"
            msg = "cant do op"

        return p.dumps(msg, -1)

    def lock(self, cms):

        msg = list()
        msg.append('11')

        try:
            if cms[2] > self.rs:
                msg.append('None')
            elif self.lp.lock(cms[2], cms[1], t.time() + self.rs):
                msg.append('True')
            else:
                msg.append('False')

        except IndexError:
            msg.append('NOK')
            print 'skel - IndexError'
        except UnboundLocalError:
            msg.append('NOK')
            print 'skel - UnboundLocalError'
        return msg

    def release(self, cms):

        msg = list()
        msg.append('21')

        try:
            if cms[2] > self.rs:
                msg.append('None')
            elif self.lp.release(cms[2], cms[1]):
                msg.append('True')
            else:
                msg.append('False')

        except IndexError:
            msg.append('NOK')
            print 'skel - IndexError'
        except UnboundLocalError:
            msg.append('NOK')
            print 'skel - UnboundLocalError'
        return msg

    def test(self, cms):

        msg = list()
        msg.append('31')

        try:
            if cms[1] > self.rs:
                msg.append('None')

            elif self.lp.test(cms[1]):
                msg.append('True')
            else:
                msg.append('False')

        except IndexError:
            msg.append('NOK')
            print 'skel - IndexError'
        except UnboundLocalError:
            msg.append('NOK')
            print 'skel - UnboundLocalError'

        return msg

    def stats(self, cms):

        msg = list()
        msg.append('41')

        try:
            if cms[1] > self.rs:
                msg.append('None')
            else:
                msg.append(self.lp.stat(cms[1]))

        except IndexError:
            msg.append('NOK')
            print 'skel - IndexError'
        except UnboundLocalError:
            msg.append('NOK')
            print 'skel - UnboundLocalError'

        return msg
