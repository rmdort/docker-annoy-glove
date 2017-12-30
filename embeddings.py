import numpy as np
import annoy
import json
import os

DIMENSION = 300
EMPTY_ARRAY = [float(e) for e in np.zeros(DIMENSION)]

# Open vocab
with open(os.path.join(os.path.dirname(__file__), 'vocab.json')) as f:
  vocab = json.load(f)
  ind2word = {v: k for k, v in vocab.items()}

# Index
index = annoy.AnnoyIndex(300, 'angular')

# Load the embeddings
index.load(os.path.join(os.path.dirname(__file__), 'embeddings.ann'))

print ('Number of items in the index ', index.get_n_items())


def get_embedding(x):
  """
  Get embedding of a word
  If it doesnt exist in the vocab, outputs zero vectors
  """
  # Lowercase word
  x = x.lower()
  if x in vocab:
    idx = vocab[x]
    return [float(e) for e in index.get_item_vector(idx)]
  else:
    return EMPTY_ARRAY

def get_nearest (x, count):
  """
  get_nearest('physics')
  For phrases split the word and add the vectors
  # a = index.get_item_vector(vocab['san'])
  # b = index.get_item_vector(vocab['fransisco'])
  # c = np.add(a, b)
  # vec = index.get_item_vector(c)
  """
  # Lowercase word
  x = x.lower()
  if x in vocab:
    idx = vocab[x]
    pos, dist =  index.get_nns_by_item(idx, count, include_distances=True)    
    return [
      (ind2word[idx], 1 - dist[i]) for i, idx in enumerate(pos)
    ]
  else:
    return []