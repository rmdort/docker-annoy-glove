import gsocketpool.pool
import numpy as np
from mprpc import RPCPoolClient

client_pool = gsocketpool.pool.Pool(RPCPoolClient, dict(host='127.0.0.1', port=9033))

with client_pool.connection() as client:
    vec =  client.call('embedding', ['from'])
    print (vec)