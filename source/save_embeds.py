from __future__ import print_function

import sys
import codecs
import numpy as np

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--infile", help="input filename")



def main():
    args = parser.parse_args()

    embedding_file = args.infile
    print('Loading embeddings file from {}'.format(embedding_file))
    wv, words = load_embeddings(embedding_file)

    out_emb_file = embedding_file + '.wv'
    out_vocab_file = embedding_file + '.vocab'
    print('Saving binary file to {}'.format(out_emb_file))
    np.save(out_emb_file, wv)

    print('Saving vocabulary file to {}'.format(out_vocab_file))
    with codecs.open(out_vocab_file, 'w', 'utf-8') as f_out:
        for word in words:
            f_out.write(word + '\n')


def load_embeddings(file_name):
    """
    Load the pre-trained embeddings from a file
    :param file_name: the embeddings file
    :return: the vocabulary and the word vectors
    """
    with codecs.open(file_name, 'r', 'utf-8') as f_in:
        lines = [line.strip() for line in f_in]

    if len(lines[0].split()) < 10:
        lines = lines[1:]

    embedding_dim = len(lines[0].split()) - 1

    for i,line in enumerate(lines):
        if not len(line.split()) == embedding_dim + 1:
            print('ignoring:', line[:10])

    words, vectors = zip(*[line.strip().split(None, 1) for line in lines if len(line.split()) == embedding_dim + 1])

    wv = np.loadtxt(vectors)

    print(len(words))
    print(len(wv))
    return wv, words


if __name__ == '__main__':
    main()