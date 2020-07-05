import numpy as np
import pandas as pd
arr = np.load('arr_pandas.npy', allow_pickle = True) # Не заработале без разрешения десериализации. Странно, и вероятно приведет к проблемам в дальнейшем
# print(arr)
dat = pd.DataFrame(arr)

dat['year'] = int(2000)
