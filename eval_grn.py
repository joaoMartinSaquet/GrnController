import jpype
import jpype.imports
from jpype.types import *
# launch the JVM
jpype.startJVM(classpath=['GRNEAT/target/GRNEAT-0.0.1.jar'])


import sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(parent.joinpath('pyGRN').as_posix())

import math
import pygrn
import numpy as np
from PongEnv.pong_env import pong_env
# to do ennd this shit
from pygrn.grns.classic import ClassicGRN


import matplotlib.pyplot as plt
import os


grn_path = "CoverageControl/run_24692440971211/grn_668_-2.393888979239919.grn"
if __name__ == "__main__":

    # env = pong_env(seed=34554, normalize=True)
    GRNModel_class = jpype.JClass('grn.GRNModel') 
    grn = GRNModel_class().loadFromFile(grn_path)
    # grn = grn.loadFromFile(grn_path)
    grn.reset()
    grn.evolve(25)

    nstep = 100
    y_pred = np.zeros(nstep)
    y_true = np.zeros(nstep)
    t = np.arange(nstep)

    error = 0
    for i in range(100):

        input_ = i/100.0
        
        grn.proteins.get(0).concentration = input_
        grn.evolve(1)
        y_pred[i] = (grn.proteins.get(1).concentration*2.0)-1.0
        y_true[i] = math.sin(0.05*i) # 0.05*math.sin(i)
        error += abs(y_true[i]-y_pred[i])
    plt.plot(t, y_true - y_pred, "b-", label="error")
    plt.plot(t, y_true, "r--", label="True")
    plt.plot(t, y_pred, "g-", label="Predicted")
    print(f"Error : {error}")
    plt.legend(loc="upper left")
    plt.show()    
    jpype.shutdownJVM()

