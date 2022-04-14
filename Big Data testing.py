#!/usr/bin/env python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

datatype=[('index',np.float32), ('floati',np.float32), 
        ('floatq',np.float32)]
filename='10C_vectors_E01_Fad_200000.txt'

def main():
    plt.figure()
    data = np.genfromtxt("10C_vectors_E01_Fad_200000.txt")
    e = np.empty(len(data)//4)
    i=1
    j=0
    while i < len(data):
        e[j] = data[i]  # i am a fucking idiot
        i = i+4
        j +=1
      
    print(e)
    plt.hist(e, bins=100)
    #plt.ylim(top=800)
    plt.grid(True)
    plt.title("e+ of 10C")
    plt.xlabel("Energy")
    plt.ylabel("counts")
    plt.savefig('example1.png')

if __name__ == "__main__":
    main()  
