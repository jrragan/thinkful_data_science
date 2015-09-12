__author__ = 'rragan'

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

g = lambda x : int(str(x).split('-')[0])
h = lambda x : float(str(x).strip().rstrip('%'))/100
j = lambda x : int(str(x).split()[0].strip())

loansData['FICO.Score'] = map(g, loansData['FICO.Range'])
loansData['Interest.Rate'] = map(h, loansData['Interest.Rate'])
loansData['Loan.Length'] = map(j, loansData['Loan.Length'])

print(loansData['FICO.Score'])
print(loansData)

plt.figure()
p = loansData['FICO.Score'].hist()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
b = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(x)
print(y)
print(f.summary())

