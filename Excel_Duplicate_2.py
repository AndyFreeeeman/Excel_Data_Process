import pandas as pd 
import os
import numpy as np
from pandas import DataFrame

file_path = 'E:\\下載\\all_data.xlsx'
df = pd.read_excel(file_path)


print("done.")

all_data = np.array(df)



save_path = 'E:\\下載\\test.xlsx'

final_data_store = []

row_counter = 0
counter1 = 0

for person_counter in range (0,1746):
    
    person_year_count = 0
            
    # 算單人有幾年data pre_tx baseline  143 +25....
    for personal_year_counter in range (0,40):
        
        check = all_data[person_counter][142 + personal_year_counter * 25]
        if pd.isna(check):
            break
        else:
            person_year_count = person_year_count + 1
            
    # 每個.5年 (每行)
    for year_counter in range (0,person_year_count):
        
        row_data = [0] * 166
        #per_year_data = [0] * 25 # 每年資料 25格
        
        # 單人全部資料 pre_tx baseline 1 ~ 141
        for i in range (0,140):
            row_data[i] = all_data[person_counter][i]
        
        # 每個.5年的資料 142~166
        for i in range (0,25):
            row_data[141 + i] = all_data[person_counter][141 + 25 * year_counter + i]
            
        # 儲存這行
        final_data_store.append(row_data)
        
        
DataFrame(final_data_store).to_excel(save_path, sheet_name='test', index=False, header=True)
print('done.')
