#!/usr/bin/env python
import numpy as np

def generate_random():
    data = np.random.randn(100).reshape(50,2)
    data[:,1]=data[:,1]**2
    data = np.cumsum(data,axis=0)
    return data

def write_data(filename,data):
    np.savetxt(filename, data, fmt="%.6g",delimiter=",",header="x,y")

if __name__ == "__main__":
    for i in range(100):
        write_data("data.{:03d}.csv".format(i),generate_random())



