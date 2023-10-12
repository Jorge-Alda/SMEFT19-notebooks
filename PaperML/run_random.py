import SMEFT19
from parscanning import RandomScan

RS = RandomScan(SMEFT19.likelihood_global, [-0.3, -0.08, -0.025, -0.15, 0], [0, 0.08, 0.025, 0.15, 3.0], 1)

for _ in range(200):
    RS.run_mp(8, SMEFT19.scenarios.rotBII)
    RS.write("../data/samples/randompoints.dat", "at")
    RS.clear()
