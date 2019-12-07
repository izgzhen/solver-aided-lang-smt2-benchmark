import pickle
import sys
import os
import pandas as pd
import random
import numpy as np
sys.path.append("./code")
from util import tokenize_doc, run_task
from tokenizer import bow

clf = pickle.load(open("best_clf.p", "rb"))
print(clf)
y_test = pickle.load(open("df_durations.p", "rb"))
doc2vec = pickle.load(open("doc2vec.p", "rb"))

def run(smt2, rkt):
    smt_vec = bow(smt2)
    rkt_vec = doc2vec.infer_vector(tokenize_doc(rkt))

    df_smt = pd.DataFrame([smt_vec])
    df_rkt = pd.DataFrame([rkt_vec])
    df_rkt = df_rkt.rename(columns={ c : ("rkt_%s" % c) for c in df_rkt.columns })

    X_test = pd.concat(([df_smt, df_rkt]), axis=1, sort=False)

    pred = clf.predict(X_test)[0]
    print(smt2, rkt, pred)

if __name__ == "__main__":
    smt2 = "data/serval_rosette_smt2/rosette15753980511575398051320_0.clean.smt2"
    rkt = "data/serval/monitors/certikos/verif/riscv.rkt"
    run(smt2, rkt)
