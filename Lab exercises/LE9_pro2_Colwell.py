# Written by Jayden Colwell
import pandas as pd
import  numpy as np

# Series of these 4 numbers.
series1 = pd.Series([7, 11, 13, 17])
print(f'Series 1: \n{series1}')
# Series of 100.0, 5 times.
series2 = pd.Series([100.0] * 5)
print(f'Series 2: \n{series2}')
# Series of 20 random numbers 1-100 and printing the description.
series3 = pd.Series(np.random.randint(0, 101, 20))
print(f'Series 3 description: \n{series3.describe()}')
# Series of temperatures with corresponding index names.
series4 = pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])
print(f'Series 4: \n{series4}')
# Turns series4 into a dictionary then back into series5.
dict_s4 = series4.to_dict()
series5 = pd.Series(dict_s4)
print(f'Series 4 as dict: \n{dict_s4}')
print(f'Series 5: \n{series5}')