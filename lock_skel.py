#!/usr/bin/python
# -*- coding: utf-8 -*-

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

        if cms[2] > self.rs:
            msg.append('None')
        elif self.lp.lock(cms[1], cms[2], t.time() + self.rs):
            msg.append('True')
        else:
            msg.append('False')
        return msg

    def release(self, cms):

        msg = list()
        msg.append('21')

        if cms[2] > self.rs:
            msg.append('None')
        elif self.lp.release(cms[1], cms[2]):
            msg.append('True')
        else:
            msg.append('False')
        return msg

    def test(self, cms):

        msg = list()
        msg.append('31')

        if cms[1] > self.rs:
            msg.append('None')
        elif self.lp.test(cms[1]):
            msg.append('True')
        else:
            msg.append('False')
        return msg

    def stats(self, cms):

        msg = list()
        msg.append('41')

        if cms[1] > self.rs:
            msg.append('None')
        else:
            msg.append(self.lp.stat(cms[1]))
        return msg
