def phaser( lightcurve, period, epoch ):

    phased = list()
    for obs in lightcurve:
        phase = (obs[0] - epoch) / period
        new = [phase % 1, obs[1], obs[2]]
        phased.append(new)

    output = list()
    for i in phased:
        output.append(i)
        tp = [i[0] + 1, i[1], i[2]]
        output.append(tp)
    
    return output

import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("indata")
parser.add_argument("period")  
parser.add_argument("epoch",nargs='?',default=-1)
args = parser.parse_args()
indata = args.indata
period = float(args.period)
epoch = float(args.epoch)

use = (np.loadtxt(indata)).tolist()   

if epoch == -1:
    epoch = use[0][0]

for i in phaser(use,period,epoch):

    print(i[0],i[1],i[2])

