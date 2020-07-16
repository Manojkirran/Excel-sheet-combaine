import tkinter as tk
from tkinter import filedialog
import pandas as pd
root = tk.Tk()
root.withdraw()
import os.path
file_path = filedialog.askopenfilenames()

data = {}
data2 = []
for filename in file_path:
    filenae = os.path.split(filename)
    tmp = filenae[-1].replace(".xlsx","")    
    xls = pd.ExcelFile(filename)
    name1 = xls.sheet_names
    for sheet in name1:
        df = pd.read_excel(filename,sheet_name=sheet)
        if sheet in data2:
           df = pd.read_excel(filename,sheet_name=sheet)
           sheet = sheet + "_" + tmp
           data[sheet] = df
        data2.append(str(sheet))
        data[sheet] = df
        
print (data)
print (data2)
input()
writer = pd.ExcelWriter(r'D:\Manoj\Excel out put\output.xlsx')
for sheet in data:
    df = data[sheet]
    x``
    
    df.to_excel(writer,sheet_name= sheet, index =False)
writer.save()
