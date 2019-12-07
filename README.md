# Solver-aided Language SMT2 Benchmark

You are recommended to use the open source git repo [here](https://github.com/izgzhen/fantastic-octo-disco)
to run the following steps
if you get this as a snapshot tarball.

## Download the data and run the experiments

- `git submodule update --init`
- The dataset source can be downloaded from http://bit.ly/solver-aided-benchmark.
  Unzip it inside `data/`.
- `df_durations.p` is a pickled dataframe containing the ground-truth -- i.e. the runtime of
  different solvers on the dataset queries
- `explore.ipynb` contains examples on how to use the above data as well as our baseline results

## Run the demo

After getting dataset ready as above:

```
python3 code/main.py
```

## Acknowledgement

Thanks to contributions from [MarisaKirisame](https://github.com/MarisaKirisame/) and advice from Prof. Emina Torlak.
