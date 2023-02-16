import warnings
from SMEFT19 import likelihood_fits
from SMEFT19.scenarios import rotBII
import SMEFT19
from copy import deepcopy
import sys
from pathlib import Path

my_path = Path(__file__).parent
d_ell = SMEFT19.ellipse.load(my_path.parent / "data" / "ellipses" / 'rotBII.yaml')
bf = d_ell['bf']

dim_min = [-0.1, -0.07, -0.04, -0.15, -0.7]
dim_max = [0.1, 0.07, 0.04, 0.07, 3.0]

coefs = ['C', 'al', 'bl', 'aq', 'bq']

if __name__ == '__main__':
    id_x = coefs.index(sys.argv[-2])
    id_y = coefs.index(sys.argv[-1])

    def lh(num: int) -> float:
        xmin = dim_min[id_x]
        xmax = dim_max[id_x]
        ymin = dim_min[id_x]
        ymax = dim_max[id_x]
        xmargin = 0.02*(xmax-xmin)
        ymargin = 0.02*(ymax-ymin)
        ix = num % 30
        iy = num // 30
        x = (xmin-xmargin) + ix/30 * ((xmax+xmargin) - (xmin-xmargin))
        y = (ymin-ymargin) + iy/30 * ((ymax+ymargin) - (ymin-ymargin))
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            lh_point = deepcopy(bf)
            lh_point[id_x] = x
            lh_point[id_y] = y
            lg = likelihood_fits(lh_point, rotBII)
            return {k: max(v, -100) for k, v in lg.items()}
    with open(my_path.parent / "data" / "likelihood" / f'likelihood_rotBII_{sys.argv[-2]}{sys.argv[-1]}.dat', 'rt') as f_global:
        t = f_global.read()
        calculated = t.count('\t') + t.count('\n')

    with open(my_path.parent / "data" / "likelihood" / f'likelihood_rotBII_{sys.argv[-2]}{sys.argv[-1]}.dat', 'at') as f_global, \
            open(my_path.parent / "data" / "likelihood" / f'likelihood_rotBII_{sys.argv[-2]}{sys.argv[-1]}_RK.dat', 'at') as f_RK, \
            open(my_path.parent / "data" / "likelihood" / f'likelihood_rotBII_{sys.argv[-2]}{sys.argv[-1]}_RD.dat', 'at') as f_RD, \
            open(my_path.parent / "data" / "likelihood" /  f'likelihood_rotBII_{sys.argv[-2]}{sys.argv[-1]}_LFV.dat', 'at') as f_LFV:
        for i in range(calculated, 30*30):
            lg = lh(i)
            if i % 30 == 29:
                sep = '\n'
                f_global.flush()
            else:
                sep = '\t'
            f_global.write(f'{lg["global"]}{sep}')
            f_RK.write(f'{lg["likelihood_lfu_fcnc.yaml"]}{sep}')
            f_RD.write(f'{lg["likelihood_rd_rds.yaml"]}{sep}')
            f_LFV.write(f'{lg["likelihood_lfv.yaml"]}{sep}')
            print(i)

