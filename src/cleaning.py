import pandas as pd

def categoric (dataset):
    dataset.replace({'cut':{'Ideal':4,'Premium':5,'Very Good':3,'Good':2,'Fair':1}}, inplace=True)
    dataset.replace({'color':{'D':7,'E':6,'F':5,'G':4,'H':3,'I':2,'J':1}}, inplace=True)
    dataset.replace({'clarity':{'IF':8, 'VVS1':7, 'VVS2':6,'VS1':5,'VS2':4,'SI1':3,'SI2':2,'I1':1}}, inplace=True)
    pass

def outliers_IQR (dataset):
    Q1 = dataset.quantile(0.25)
    Q3 = dataset.quantile(0.75)
    IQR = Q3 - Q1
    dataset = dataset[~((dataset < (Q1 - 1.5 * IQR)) |(dataset > (Q3 + 1.5 * IQR))).any(axis=1)]
    return dataset
