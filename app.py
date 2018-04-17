from tabulate import tabulate
import pandas
import numpy as np
import keras

filepath = './processed/temp.tsv'

table = pandas.read_csv(filepath, sep="\t")

print(table.describe())

