# RPC Docker/Kubernetes container for glove embeddings using Annoy

This is an RPC container for glove 840 billion word embeddings `glove.840B.300d.txt`. Has around 250MB memory footprint on k8.

More info about annoy - https://github.com/spotify/annoy

Annoy (Approximate Nearest Neighbors Oh Yeah) is a C++ library with Python bindings to search for points in space that are close to a given query point. It also creates large read-only file-based data structures that are mmapped into memory so that many processes may share the same data.

## Docker image

````
docker run -p 127.0.0.1:9033:9033 olasearch/annoy_server:latest
````

## Deploy in kuberentes

````
kubectl apply -f k8-annoy-deployment.yml
````

A new service `annoy-service-en` will be created on port `80`

From a different container, you can access this service using RPC

You need `mprpc` client to access the RPC server
````
pip install mprpc
````

From your k8 container, you can access word embedding using
````
import numpy as np
from mprpc import RPCClient

client = RPCClient('annoy-service-en', 80)

with client_pool.connection() as client:
    word_vectors =  client.call('embedding', ['hey', 'there', 'how', 'are', 'you'])
    print (np.shape(word_vectors))
````

