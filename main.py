from gevent.server import StreamServer
from mprpc import RPCServer
from embeddings import get_embedding, get_nearest
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class EmbeddingServer(RPCServer):
  def embedding(self, word):
    if isinstance(word, (list, tuple)):
      return [ get_embedding(w) for w in word ]
    return get_embedding(word)

  def nearest(self, word, count = 10):
    return get_nearest(word, count)


def serve ():
  logging.info('Creating server')
  server = StreamServer(('0.0.0.0', 9033), EmbeddingServer())

  logging.info('Done. Serving forever')
  server.serve_forever()

if __name__ == "__main__":
  serve()