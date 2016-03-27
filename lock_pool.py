#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 25
Números de aluno: 44314, 43551, 44285
"""
# Zona para fazer imports

import time as t


class ResourceLock:

    def __init__(self):
        """
        Define e inicializa as características de um LOCK num recurso.
        """
        self.lock_state = False
        self.lock_counter = 0
        self.resource_owner = 0
        self.time_expire = 0

    def lock(self, client_id, time_limit):
        """
        Bloqueia o recurso se este não estiver bloqueado ou mantém o bloqueio
        se o recurso estiver bloqueado pelo cliente client_id. Neste caso renova
        o bloqueio do recurso até time_limit.
        Retorna True se bloqueou o recurso ou False caso contrário.
        """
        if not self.lock_state or client_id == self.resource_owner:
            self.lock_counter += 1
            self.lock_state = True
            self.resource_owner = client_id
            self.time_expire = time_limit
            return True
        return False

    def urelease(self):
        """
        Liberta o recurso incondicionalmente, alterando os valores associados
        ao bloqueio.
        """
        self.lock_state = False
        self.resource_owner = 0
        self.time_expire = 0

    def release(self, client_id):
        if self.resource_owner == client_id:
            self.lock_state = False
            self.resource_owner = 0
            self.time_expire = 0
            return True
        return False

    def test(self):
        """
        Retorna o estado de bloqueio do recurso.
        """
        return self.lock_state

    def stat(self):
        """
        Retorna o número de vezes que este recurso já foi bloqueado.
        """
        return self.lock_counter

    def time(self):
        """
        Devolve o tempo limite do recurso
        """
        return self.time_expire


class LockPool:

    def __init__(self, n):
        """
        Define um array com um conjunto de locks para N recursos. Os locks podem
        ser manipulados pelos métodos desta classe.
        """
        self.lock_pool_array = []
        for i in range(n):
            self.lock_pool_array.append(ResourceLock())

    def clear_expired_locks(self):
        """
        Verifica se os recursos que estão bloqueados ainda estão dentro do tempo
        de concessão do bloqueio. Liberta os recursos caso o seu tempo de
        concessão tenha expirado.
        """
        for lock in self.lock_pool_array:
            if lock.time() < t.time():
                lock.urelease()

    def lock(self, resource_id, client_id, time_limit):
        """
        Tenta bloquear o recurso resource_id pelo cliente client_id, até ao
        instante time_limit. Retorna True em caso de sucesso e False caso
        contrário.
        """
        return self.lock_pool_array[resource_id].lock(client_id, time_limit)

    def release(self, resource_id, client_id):
        """
        Tenta libertar o recurso resource_id pelo cliente client_id. Retorna
        True em caso de sucesso e False caso contrário.
        """
        return self.lock_pool_array[resource_id].release(client_id)

    def test(self, resource_id):
        """
        Retorna True se o recurso resource_id estiver bloqueado e False caso
        contrário.
        """
        return self.lock_pool_array[resource_id].test()

    def stat(self, resource_id):
        """
        Retorna o número de vezes que o recurso resource_id já foi bloqueado.
        """
        return self.lock_pool_array[resource_id].stat()

    def __repr__(self):
        """
        Representação da classe para a saída standard. A string devolvida por
        esta função é usada, por exemplo, se uma instância da classe for
        passada à função print.
        """
        output = ""
        counter = 0
        for lock in self.lock_pool_array:
            output += "recurso " + \
                str(counter) + " bloqueado pelo cliente " + \
                str(lock.resource_owner) + "\n"
            counter += 1
        #
        # Acrecentar a output uma linha por cada recurso bloqueado, da forma:
        # recurso <número do recurso> bloqueado pelo cliente <id do cliente> até
        # <instante limite da concessão do bloqueio>
        #
        # Caso o recurso não esteja bloqueado a linha é simplesmente da forma:
        # recurso <número do recurso> desbloqueado
        #
        return output
