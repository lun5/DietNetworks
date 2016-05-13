import os

from featsel_supervised import execute


def main(embedding_path):
    print "Starting main loop"
    embedding_methods = []

    for directory, _, embeddings in os.walk(embedding_path):
        embedding_methods.extend([emb for emb in embeddings
                                  if ".npz" in emb and "pls" in emb])

    print "Embedding methods: {}".format(embedding_methods)
    mod = 1
    lr_candidates = [5*1e-5, 1e-5, 1e-4, 1e-3, 1e-2]

    for lr_value in lr_candidates:
        for embedding in embedding_methods:
            print "Training model %s: model %d out of %d" % \
                    (embedding, mod, len(embedding_methods))
            execute(embedding, num_epochs=1000, split_valid=.2,
                    lr_value=lr_value,
                    save_path=embedding_path)
            mod += 1

if __name__ == '__main__':
    embedding_path = "/data/lisatmp4/sylvaint/data/feature_selection/"
    # embedding_path = "/data/lisatmp4/sylvaint/data/feature-selection-datasets/"
    main(embedding_path)
