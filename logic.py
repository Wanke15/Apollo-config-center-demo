from pyapollo import ApolloClient

client = ApolloClient('Mengniu-Rec-test')


def recommend():
    client.start()
    v = client.get_value("source_id_weight")
    return v
