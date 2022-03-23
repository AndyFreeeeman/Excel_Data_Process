import pandas as pd 
import os
import numpy as np
from pandas import DataFrame



file_path = 'C:\\Users\\andy4\\Downloads\\'
base_path = os.path.join(file_path, 'long_form.xlsx')
file_path = 'C:\\Users\\andy4\\Downloads\\test.xlsx'
df = pd.read_excel(base_path)
all_data = np.array(df)



PA_follow_count = [0] * 1389
store_list = []

counter = 0
counter1 = 0

data_store = [["1" for _ in range(64)] for _ in range(1389)]

final_data_store = [["1" for _ in range(64)] for _ in range(15904)]

for i in range (0,15903):
    PA_follow_count[(int(all_data[i][0]) - 1)] = PA_follow_count[(int(all_data[i][0]) - 1)] + 1
    

for i in range (0,15903):
    if all_data[i][2] == 0 or all_data[i][2] == 1 :
        
        for j in range (2,64):
            data_store[counter][j] = all_data[i][j]
            
        counter = counter + 1

        
for i in range (0,1389):
    for j in range (0,PA_follow_count[i]):
        for k in range (0,64):
            final_data_store[counter1][k] = data_store[i][k]
            
        counter1 = counter1 + 1
        
        
DataFrame(final_data_store).to_excel(file_path, sheet_name='test', index=False, header=True)
print('done.')
