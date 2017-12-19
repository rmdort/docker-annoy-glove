import annoy
import numpy as np
import json
from progressbar import ProgressBar

index = annoy.AnnoyIndex(300, 'angular')
with open('glove.840B.300d.txt', 'r') as f:
    n_vocab_total = 2196017
    n_vocab = 400000
    p = str(int(float(n_vocab) * 100 / n_vocab_total))
    vocab = {}
    pbar = ProgressBar(n_vocab)
    print('Reading...')
    print('Using only ' + p + ' % of vocab.')
    for i in range(n_vocab):
        l = f.readline().split(' ')
        x = l[0]
        v = list(map(float, l[1:]))
        index.add_item(i, v)
        pbar.update()
        vocab[x] = i
print(' ')
print('Building index...')
index.build(10)
print('Writing...')
index.save('embeddings.ann')
print('Saving vocab...')
with open('vocab.json', 'w') as f:
    json.dump(vocab, f)
print('Done.')