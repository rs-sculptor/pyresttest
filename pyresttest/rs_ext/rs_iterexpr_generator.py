from itertools import *
import pyresttest.validators as validators

"""
product、literexp: using itertools to yield variable

  - config:
    - testset: ""
    - generators:
        - a,b,c:
            type: product
            args: [['0001'], ['042015', '042016', '042017', '042018', '042019'], ['01', '02', '03', '04', '05']]
        - d,e:
            type: iterexpr
            expr: |
              product(['0001'], map(lambda x: '{:0>4}'.format(x), range(1,91)))
        - f:
            type: iterexpr
            expr: |
              chain.from_iterable(map(lambda d: repeat(d, 10), ["1","2"]))
  - test:
      - test_runs: 25
      - generator_binds:
          a,b,c: a,b,c
          d,e: d,e
          f: f
      - url:
          template: "/$a/$b/$c/$d/$e/$f"
"""

def iterexpr(config):
    expr = config.get('expr')
    v = eval(expr)
    yield from v

GENERATORS = {'iterexpr': iterexpr}