import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import csv


def opend(file):
    rawinput = csv.reader(open(file, "rb"), delimiter=",")
    x = list(rawinput)
    result = np.array(x)
    return result


def main():
    text = opend("../dresources/data_2009_updated2.csv")
    print(text)
    return


if __name__ == '__main__':
    main()

