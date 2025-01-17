#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    for cf in allcfs.crazyflies:
        print(cf.id)
        cf.setLEDColor(1,0,0)
        cf.takeoff(1.0, 2.5)
        cf.setLEDColor(0,0,1)
        print("press button to continue")
        swarm.input.waitUntilButtonPressed()
        cf.land(0.04, 2.5)


if __name__ == "__main__":
    main()
