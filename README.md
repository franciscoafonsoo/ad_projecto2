Projeto de Aplicações Distribuidas do grupo 025

Francisco Pires, nº44314
Alexandre Machado nº43551
Nuno Silva, nº44285

------------------ Primeira Entrega ------------------

Ficheiros pertencentes a entrega:
lock_pool.py
lock_skel.py
lock_server.py
net_client.py
lock_stub.py
lock_client.py
sock_utils.py
readme.md

Comandos disponiveis no cliente:
    LOCK,RELEASE,TEST,STATS,EXIT


Guia de utilização:
    1. Iniciar o servidor (lock_server.py),com ou sem parametros.
        1.a A sintaxe dos parametros é a seguinte:
            lock_server.py (PORTA) (N DE RECURSOS) (TEMPO DE VIDA)
    2. Iniciar o cliente (lock_client.py) com parametros.
        2.a A sintaxe dos parametros é a seguinte:
            lock_client.py (ENDEREÇO) (PORTA) (ID DO CLIENTE)
    3. Apos a ligação estar feita, utilizar os comandos referidos anteriormente a descrição.
        3.a A sintaxe dos comandos é a seguinte.
            - LOCK (N DO RECURSO)
            - RELEASE (N DO RECURSO)
            - TEST (N DO RECURSO)
            - STATS (N DO RECURSO)
