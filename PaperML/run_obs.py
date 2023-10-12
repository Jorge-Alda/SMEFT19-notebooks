#!/usr/bin/env python3

from math import sqrt
import flavio
import yaml
from parscanning import MontecarloScan
from SMEFT19.SMEFTglob import likelihood_global, prediction
from SMEFT19.ellipse import load
from SMEFT19.scenarios import rotBI, rotBII

obslist = [
    ('<Rmue>(B+->Kll)', 0.045, 1.1),
    ('<Rmue>(B+->Kll)', 1.1, 6.0),
    ('<Rmue>(B0->K*ll)', 0.045, 1.1),
    ('<Rmue>(B0->K*ll)', 1.1, 6.0),
    'Rtaul(B->Dlnu)',
    'Rtaul(B->D*lnu)',
    'Rtaumu(B->D*lnu)',
    'Rtaumu(Bc->J/psilnu)',
]

def calculate(wfun, minx, maxx, fout, fin, name, num=1):
    values = dict()
    values['name'] = name
    uncert = []
    dellipse = load(fin)
    bf = dellipse['bf']
    w = wfun(bf)
    for obs in obslist:
        values[str(obs)] = dict()
        if isinstance(obs, str):
            values[obs]['SM'] = dict()
            values[obs]['exp'] = dict()
            values[obs]['NP'] = dict()
            values[obs]['NP']['central'] = float(flavio.np_prediction(obs, w))
            uncert.append(flavio.np_uncertainty(obs, w))
            values[obs]['SM']['central'] = float(flavio.sm_prediction(obs))
            values[obs]['SM']['uncert'] = float(flavio.sm_uncertainty(obs))
            dist = flavio.combine_measurements(obs)
            values[obs]['exp']['central'] = float(dist.central_value)
            values[obs]['exp']['uncert'] = float((dist.error_left + dist.error_right)/2)
        else:
            values[str(obs)]['SM'] = dict()
            values[str(obs)]['exp'] = dict()
            values[str(obs)]['NP'] = dict()
            values[str(obs)]['NP']['central'] = float(flavio.np_prediction(obs[0], w,
                                                                           obs[1], obs[2]))
            uncert.append(flavio.np_uncertainty(obs[0], w, obs[1], obs[2]))
            values[str(obs)]['SM']['central'] = float(flavio.sm_prediction(obs[0], obs[1], obs[2]))
            values[str(obs)]['SM']['uncert'] = float(flavio.np_uncertainty(obs[0], w,
                                                                           obs[1], obs[2]))
            dist = flavio.combine_measurements(obs)
            values[str(obs)]['exp']['central'] = float(dist.central_value)
            values[str(obs)]['exp']['uncert'] = float((dist.error_left + dist.error_right)/2)

    MS = MontecarloScan(likelihood_global, minx, maxx, num, bf, 0.1, wfun)
    return MS

MS = calculate(rotBII, [-0.25, -0.15, -0.03, -0.12, 0], [0.0, 0.15, 0.03, 0.07, 3.5], '../data/observables/obsBII.yaml',
                            '../data/ellipses/rotBII.yaml', name='Scenario I')

for _ in range(50):
    MS.run(rotBII)
    preds = []
    for obs in obslist:
        if isinstance(obs, str):
            preds.append(flavio.np_prediction(obs, rotBII(MS.points[-1])))
        else:
            preds.append(flavio.np_prediction(obs[0], rotBII(MS.points[-1]), *obs[1:]))
    with open("observables_rotBII.dat", "at") as f:
        f.write("\t".join([str(p) for p in preds])+'\n')
