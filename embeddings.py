import numpy as np
import annoy
import json
import os

DIMENSION = 300
EMPTY_ARRAY = [float(e) for e in np.zeros(DIMENSION)]

# Open vocab
with open(os.path.join(os.path.dirname(__file__), 'vocab.json')) as f:
  vocab = json.load(f)

# Index
index = annoy.AnnoyIndex(300, 'angular')
# Load the embeddings
index.load(os.path.join(os.path.dirname(__file__), 'embeddings.ann'))

# Get embedding of a word
# If it doesnt exist in the vocab, outputs zero vectors
def get_embedding(x):
  # Lowercase word
  x = x.lower()
  if x in vocab:
    idx = vocab[x]
    return [float(e) for e in index.get_item_vector(idx)]
  else:
    return EMPTY_ARRAY
