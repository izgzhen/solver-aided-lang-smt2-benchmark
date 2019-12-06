
# Copyright (C) 2019-2020 Zhen Zhang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import subprocess
import time

solvers = {
    "z3": ("z3 -st -smt2", ":total-time"),
    "cvc4": ("cvc4 --stats --produce-models --lang smt", "driver::totalTime,"),
    # "yices": ("yices-smt2 -s", ":total-run-time"),
    "boolector": ("boolector --input-format smt2 --model-gen", None)
}

def run_task(task, timeout=60):
    (f, tool) = task
    cmd, stat_prefix = solvers[tool]
    full_cmd = ["timeout", str(timeout)] + cmd.split() + [f]
    if stat_prefix is None:
        before = time.time()
    p = subprocess.run(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if stat_prefix is None:
        duration = time.time() - before
    if p.returncode == 124:
        return (f, tool, None, {"cmd": " ".join(full_cmd), "reason": "timeout"})
    ret = str(p.stdout, "utf-8") + str(p.stderr, "utf-8")
    if "error" in ret or "invalid" in ret or "not supported yet" in ret:
        return (f, tool, None, {"cmd": " ".join(full_cmd), "reason": "error\n%s" % ret})
    if stat_prefix is not None:
        stat_lines = [ l for l in ret.split("\n") if stat_prefix in l ]
        if len(stat_lines) != 1:
            return (f, tool, None, {"cmd": " ".join(full_cmd), "reason": "not stat\n%s" % ret})
        stat_line = stat_lines[0]
        duration = float(stat_line.strip().split()[1].strip(")"))
    return (f, tool, duration, {"cmd": " ".join(full_cmd), "output": ret})

def tokenize_doc(f):
    with open(f, "r") as fh:
        code = fh.read()
        code = code.replace("(", " ").replace(")", " ").replace("\n", " ") # FIXME: this is too brutal?
        return code.split()