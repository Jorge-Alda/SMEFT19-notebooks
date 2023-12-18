def rotBIII(x):
    r'''
Scenario BIII\: NP affects only the third generation in the interaction basis
and then is rotated to the mass basis. Only the quark sector gets rotated. C1 and C3 can be different.

:Arguments:

    - x\: Coordinates in the parameter space of the fit. x = [C1, C3, beta_q].

:Returns:

    - A dictionary containing the SMEFT Wilson Coefficients of the fit.
    '''
    return massrotation([x[0], x[1], 0, 0, 0, x[2]])
