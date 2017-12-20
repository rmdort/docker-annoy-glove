import numpy as np
from mprpc import RPCClient

client = RPCClient('127.0.0.1', 9033)

with client_pool.connection() as client:
    vec =  client.call('embedding', ['hey', 'there', 'how', 'are', 'you'])
    print (np.shape(vec))