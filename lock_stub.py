#!/usr/bin/python
# -*- coding: utf-8 -*-

# refazer


class lock_stub:

    def __init__(self):
        self.commands = ["LOCK", "RELEASE", "TEST", "STATS", "EXIT"]
        self.id_commands = ["LOCK", "RELEASE"]

    def handle(self, cms):
        cms = 0

    def send(self, cms):
        cms = 0

    def receive(self, cms):
        cms = 0