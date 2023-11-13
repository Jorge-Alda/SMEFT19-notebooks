#!/usr/bin/env python3

import warnings
from SMEFT19 import likelihood_fits
from SMEFT19.scenarios import rotBIII
import SMEFT19
from copy import deepcopy
from pathlib import Path


my_path = Path(__file__).parent
d_ell = SMEFT19.ellipse.load(my_path.parent / "data" / "ellipses" / 'rotBIII.yaml')
bf = d_ell['bf']


dim_min = [-0.3, -0.3, 0]
dim_max = [0, 0.0, 3.0]
N = 50

coefs = ['C1', 'C3', 'bq']

for (fit_x, fit_y) in [('C1', 'C3'), ('C1', 'bq'), ('C3', 'bq')]:

    id_x = coefs.index(fit_x)
    id_y = coefs.index(fit_y)
    def lh(num: int) -> float:
        xmin = dim_min[id_x]
        xmax = dim_max[id_x]
        ymin = dim_min[id_y]
        ymax = dim_max[id_y]
        xmargin = 0.02*(xmax-xmin)
        ymargin = 0.02*(ymax-ymin)
        ix = num % N
        iy = num // N
        x = (xmin-xmargin) + ix/N * ((xmax+xmargin) - (xmin-xmargin))
        y = (ymin-ymargin) + iy/N * ((ymax+ymargin) - (ymin-ymargin))
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            lh_point = deepcopy(bf)
            lh_point[id_x] = x
            lh_point[id_y] = y
            lg = likelihood_fits(lh_point, rotBIII)
            # print(f"{x:.4f}\t{y:.4f}\t{lg['global']:.4f}")
            return {k: max(v, -100) for k, v in lg.items()}
    try:
        with open(my_path.parent / "data" / "likelihood" / f'likelihood_rotBIII_{fit_x}{fit_y}.dat', 'rt') as f_global:
            t = f_global.read()
            calculated = t.count('\t') + t.count('\n')
    except:
        calculated = 0
     
    with open(my_path.parent / "data" / "likelihood" / f'likelihood_rotBIII_{fit_x}{fit_y}.dat', 'at') as f_global, \
            open(my_path.parent / "data" / "likelihood" / f'likelihood_rotBIII_{fit_x}{fit_y}_RK.dat', 'at') as f_RK, \
            open(my_path.parent / "data" / "likelihood" / f'likelihood_rotBIII_{fit_x}{fit_y}_RD.dat', 'at') as f_RD, \
            open(my_path.parent / "data" / "likelihood" /  f'likelihood_rotBIII_{fit_x}{fit_y}_LFV.dat', 'at') as f_LFV, \
            open(my_path.parent / "data" / "likelihood" / f'likelihood_rotBIII_{fit_x}{fit_y}_bqnunu.dat', 'at') as f_bqnunu:
        for i in range(calculated, N**2):
            lg = lh(i)
            if i % N == N-1:
                sep = '\n'
                f_global.flush()
                f_RK.flush()
                f_RD.flush()
                f_LFV.flush()
                f_bqnunu.flush()
                print(f"Plot for {fit_x}-{fit_y}: {i}/{N**2} ({i/N**2*100:.2f}%)")
            else:
                sep = '\t'
            f_global.write(f'{lg["global"]}{sep}')
            f_RK.write(f'{lg["likelihood_lfu_fcnc.yaml"]}{sep}')
            f_RD.write(f'{lg["likelihood_rd_rds.yaml"]}{sep}')
            f_LFV.write(f'{lg["likelihood_lfv.yaml"]}{sep}')
            f_bqnunu.write(f'{lg["likelihood_bqnunu.yaml"]}{sep}')
