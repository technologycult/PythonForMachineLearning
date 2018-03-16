'''
Topic to be covered

How to read the following file types in Python

1. .csv
2. excel
3. text
4. json
5. zipped

6. XML
7. Html
8. docx
9. .mp3 & .mp4 
10 Images
11 Hierarchical Data Format
'''
import pandas as pd

# No1 - .csv files

df_csv = pd.read_csv('SalaryData_train.csv')

# No 2 - excel file

df_exel = pd.read_excel('sample1.xlsx')

# No3 - .txt file

df_txt = pd.read_csv('Salary.txt')

# No4 - .json files

df_json = pd.read_json('worldbank.json',lines=True)

# No5 - zipped File
import zipfile

zf = zipfile.ZipFile('SalaryData_Train.zip')
df_zip = pd.read_csv(zf.open('SalaryData_Train.csv'))







