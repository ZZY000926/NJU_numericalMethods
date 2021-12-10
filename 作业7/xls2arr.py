import pandas as pd
import numpy as np
import re

x = np.linspace(-2, 2, 17)
y = np.linspace(-2, 2, 17)
grid = np.meshgrid(x, y)

dfU = pd.read_excel('u.xls', usecols=range(1, 18))
dfV = pd.read_excel('v.xls', usecols=range(1, 18))

U = dfU.values.transpose()
V = dfV.values.transpose()
U = np.insert(U, 0, values=np.zeros(17), axis=0)
U = np.insert(U, 18, values=np.zeros(17), axis=0)
U = np.insert(U, 0, values=np.zeros(19), axis=1)
U = np.insert(U, 18, values=np.zeros(19), axis=1)

np.set_printoptions(linewidth=np.inf)
print(U)
with open('u.txt', 'w') as f:
    f.write(' ')
    f.write(re.sub('[\[\]]', '', np.array_str(U)))
    f.close()

with open('v.txt', 'w') as f:
    f.write(' ')
    f.write(re.sub('[\[\]]', '', np.array_str(V)))
    f.close()

with open('gird.txt', 'w') as f:
    f.write(' ')
    f.write(re.sub('[\[\]]', '', np.array_str(grid[0].transpose())))
    f.write('\n\n ')
    f.write(re.sub('[\[\]]', '', np.array_str(grid[1].transpose())))
    f.close()
