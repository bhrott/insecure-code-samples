#!/bin/python
def eval_injection(a, b):
  return eval("%s + %s" % (a, b))

def exec_injection(a, b):
  return exec("%s + %s" % (a, b))
