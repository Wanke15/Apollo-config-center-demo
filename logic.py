import time

import threading

from pyapollo import ApolloClient

client = ApolloClient('Mengniu-Rec-test')


def client_loop(loop_interval=3):
    while True:
        client.start()
        time.sleep(loop_interval)


threading.Thread(target=client_loop, args=(3, )).start()


def recommend():
    v = client.get_value("source_id_weight")
    return v
