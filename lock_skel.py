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
            print "ERROR"
            msg = "cant do op"
        return p.dumps(msg, -1)

    def lock(self, cms):
        if self.lp.lock(cms[1], cms[2], t.time() + self.rs):
            msg = 'OK'
        else:
            msg = 'NOK'
        return msg

    def release(self, cms):
        if self.lp.release(cms[1], cms[2]):
            msg = 'OK'
        else:
            msg = 'NOK'
        return msg

    def test(self, cms):
        if self.lp.test(cms[1]):
            msg = 'LOCKED'
        else:
            msg = 'UNLOCKED'
        return msg

    def stats(self, cms):
        msg = self.lp.stat(cms[1])
        return msg
