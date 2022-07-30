import warnings
from SMEFT19 import likelihood_global
from SMEFT19.scenarios import rotBII
import SMEFT19
import numpy as np

d_ell = SMEFT19.ellipse.load('../data/ellipses/rotBII.yaml')
bf1 = d_ell['bf']


def lh(num: int) -> float:
    xmin = -0.02
    xmax = 0.02
    ymin = 0.0
    ymax = 2.0
    xmargin = 0.02*(xmax-xmin)
    ymargin = 0.02*(ymax-ymin)
    ix = num % 50
    iy = num // 50
    x = (xmin-xmargin) + ix/50 * ((xmax+xmargin) - (xmin-xmargin))
    y = (ymin-ymargin) + iy/50 * ((ymax+ymargin) - (ymin-ymargin))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        lg = likelihood_global([bf1[0], bf1[1], x, bf1[3], y], rotBII)
        return max(lg, -100)


start = 0

with open('../data/likelihood/likelihood_rotBII_blbq.dat', 'at') as f:
    for i in range(start, 50*50):
        lg = lh(i)
        if i%50 == 49:
            sep = '\n'
        else:
            sep = '\t'
        f.write(f'{lg}{sep}')
        f.flush()
        print(i)
