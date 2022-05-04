import pandas as pd 
import os
import numpy as np
from pandas import DataFrame
from IPython.display import clear_output

file_path = 'E:\\下載\\data2.xlsx'
df = pd.read_excel(file_path)


print("done.")

all_data = np.array(df)

save_path = 'E:\\下載\\test2.xlsx'

final_data_store = []

final_row_counter = 0
counter1 = 0

# 到 16332行
for row_counter in range (3,16333):
    print(str(int(row_counter/16331*100)))
    
    if all_data[row_counter][2] == 1:
        row_data = [0] * 167
        
        for i in range (0,167):
            row_data[i] = all_data[row_counter - 1][i]
            
        final_data_store.append(row_data)
        
    clear_output(wait=True)
        
        
DataFrame(final_data_store).to_excel(save_path, sheet_name='test', index=False, header=True)
print('done.')
