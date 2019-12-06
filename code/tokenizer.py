"""
Copyright 2018 Software Reliability Lab, ETH Zurich

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import re

BV_THEORY = [
    'bvadd', 'bvsub', 'bvneg', 'bvmul', 'bvurem', 'bvsrem', 'bvsmod',
    'bvshl', 'bvlshr', 'bvashr', 'bvor', 'bvand', 'bvnand', 'bvnor',
    'bvxnor', 'bvule', 'bvult', 'bvugt', 'bvuge', 'bvsle', 'bvslt',
    'bvsge', 'bvsgt', 'bvudiv', 'extract', 'bvudiv_i', 'bvnot',
]

ST_TOKENS = [
    '=', '<', '>', '==', '>=', '<=', '=>', '+', '-', '*', '/',
    'true', 'false', 'not', 'and', 'or', 'xor',
    'zero_extend', 'sign_extend', 'concat', 'let', '_', 'ite',
    'exists', 'forall', 'assert', 'declare-fun', "define-fun",
    'Int', 'Bool', 'BitVec',
]

ALL_TOKENS = ["UNK"] + ST_TOKENS + BV_THEORY

def bow(filename):
    token_idx = {}
    for i, token in enumerate(ALL_TOKENS):
        token_idx[token] = i

    with open(filename, 'r') as f:
        txt = f.read()
        txt = re.sub('[\(\)\n]', ' ', txt)
        txt = re.sub('[ ]+', ' ', txt)

        tokens = txt.split(' ')

        idx = []
        for token in tokens:
            if token not in token_idx:
                # print("UNK: " + token)
                idx.append(0)
            else:
                idx.append(token_idx[token])

    ret = [0 for _ in ALL_TOKENS]
    for x in idx:
        ret[x] += 1
    return ret
