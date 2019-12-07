# Solver-aided Language SMT2 Benchmark

You are recommended to use the open source git repo [here](https://github.com/izgzhen/fantastic-octo-disco)
to run the following steps
if you get this as a snapshot tarball.

## Set up python3

You are recommended to use virtualenv:

```
virtualenv -p python3 .venv
source .venv/bin/activate
```

## Download the data and run the experiments

- `git submodule update --init`
- The dataset source can be downloaded from http://bit.ly/solver-aided-benchmark.
  Unzip it inside `data/`.
- `df_durations.p` is a pickled dataframe containing the ground-truth -- i.e. the runtime of
  different solvers on the dataset queries
- `explore.ipynb` contains examples on how to use the above data as well as our baseline results

## Run the demo

This demo shows one case in which Boolector performs much better than Z3,
and our trained model can predict the right solver to use for an unknown
sample.

After getting dataset ready as above:

```
python3 demo/main.py
```

The output should be

```
data/serval_rosette_smt2/rosette15753980511575398051320_0.clean.smt2 data/serval/monitors/certikos/verif/riscv.rkt boolector
```

And you can try them out if you have boolector and z3 installed in your `PATH`:

```
time z3 -smt2 data/serval_rosette_smt2/rosette15753980511575398051320_0.clean.smt2
# versus
time boolector --input-format smt2 --model-gen data/serval_rosette_smt2/rosette15753980511575398051320_0.clean.smt2
```

## Acknowledgement

Thanks to contributions from [MarisaKirisame](https://github.com/MarisaKirisame/) and advice from Prof. Emina Torlak.
