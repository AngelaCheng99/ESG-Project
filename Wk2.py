#----------------------------------------------------Import files---------------------------------------------#

from pathlib import Path
from pdfminer.high_level import extract_text

#Find filepath for all files from 2020
blkPath = Path("BLK 2020 ESG Report.pdf")
ssbPath = Path("SSB 2020 ESG Report.pdf")
jpmPath = Path("JPM 2020 ESG Report.pdf")
bnymPath = Path ("BNYM 2020 ESG Report.pdf")
citiPath = Path ("Citi 2020 ESG Report.pdf")

#Import all files as raw pdf text
raw_blk_text = extract_text(blkPath)
raw_ssb_text = extract_text(ssbPath)
raw_jpm_text = extract_text(jpmPath)
raw_bnym_text = extract_text(bnymPath)
raw_citi_text = extract_text(citiPath)

print (raw_blk_text) #example output

#-------------------------------------------------Error Message for SSB--------------------------------------–#
#raw_ssb_text = extract_text(ssbPath)
#The PDF <_io.BufferedReader name='SSB 2020 ESG Report.pdf'> contains a metadata field indicating that it should not allow text extraction. Ignoring this field and proceeding. Use the check_extractable if you want to raise an error in this case
#But print(raw_ssb_text) still works

#-------------------------------How to create table for frequency of words -----------------------------------#

#Sample test of frequency table method
import re
import collections
test="My name is Angela. Angela is learning how to coding."
lc_test=test.lower()
test_words=re.findall(r'\b[a-z]{3,15}\b',lc_test)
f=collections.Counter(test_words)
print(dict(f))  

#convert all text into lower cases
lc_blk_text=raw_blk_text.lower()
lc_ssb_text=raw_ssb_text.lower()
lc_jpm_text=raw_jpm_text.lower()
lc_bnym_text=raw_bnym_text.lower()
lc_citi_text=raw_citi_text.lower()

print(lc_blk_text) #example output

#Specify what count as a regular word
#This is taken from this website: https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965
import re
reg_blk_words=re.findall(r'\b[a-z]{3,15}\b',lc_blk_text)
reg_ssb_words=re.findall(r'\b[a-z]{3,15}\b',lc_ssb_text)
reg_jpm_words=re.findall(r'\b[a-z]{3,15}\b',lc_jpm_text)
reg_bnym_words=re.findall(r'\b[a-z]{3,15}\b',lc_bnym_text)
reg_citi_words=re.findall(r'\b[a-z]{3,15}\b',lc_citi_text)

print(reg_blk_words) #example output

#count the frequency
import collections
freq_blk=collections.Counter(reg_blk_words)
freq_ssb=collections.Counter(reg_ssb_words)
freq_jpm=collections.Counter(reg_jpm_words)
freq_bnym=collections.Counter(reg_bnym_words)
freq_citi=collections.Counter(reg_citi_words)

print(freq_blk) #example output

#Create a frequency table
import pandas as pd
freq_blk_table=pd.DataFrame(freq_blk.items(),columns=["BLK words","frequency"])
freq_ssb_table=pd.DataFrame(freq_ssb.items(),columns=["SSB words","frequency"])
freq_jpm_table=pd.DataFrame(freq_jpm.items(),columns=["JPM words","frequency"])
freq_bnym_table=pd.DataFrame(freq_bnym.items(),columns=["BNYM words","frequency"])
freq_citi_table=pd.DataFrame(freq_citi.items(),columns=["Citi words","frequency"])

print(freq_blk_table) #example output

#Rank the words by frequency
rank_blk_table=freq_blk_table.sort_values(by="frequency", ascending=False)
rank_ssb_table=freq_ssb_table.sort_values(by="frequency", ascending=False)
rank_jpm_table=freq_jpm_table.sort_values(by="frequency", ascending=False)
rank_bnym_table=freq_bnym_table.sort_values(by="frequency", ascending=False)
rank_citi_table=freq_citi_table.sort_values(by="frequency", ascending=False)

print(rank_citi_table) #example output

#Export dataset into csv
rank_blk_table.to_csv("BLK Word Freq.csv", index=False)
rank_ssb_table.to_csv("SSB Word Freq.csv", index=False)
rank_jpm_table.to_csv("JPM Word Freq.csv", index=False)
rank_bnym_table.to_csv("BNYM Word Freq.csv", index=False)
rank_citi_table.to_csv("Citi Word Freq.csv", index=False)

#-------------------------------Error Message for Exporting data to Excel table--------------------------------------–#
#Not sure why the code below doesn't work
with pd.ExcelWriter('Frequency Tables.xlsx',engine="openpyxl") as writer:
    rank_blk_table.to_excel(writer, sheet_name='BlackRock')
    rank_ssb_table.to_excel(writer, sheet_name='State Street')
    rank_jpm_table.to_excel(writer, sheet_name='JPM')
    rank_bnym_table.to_excel(writer, sheet_name='BNYM')
    rank_citi_table.to_excel(writer, sheet_name='Citi')

#Messages in Python Console
#Traceback (most recent call last):

  #File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/code.py", line 90, in runcode
    #exec(code, self.locals)
  #File "<input>", line 1, in <module>
  #File "/Users/xinyuecheng/PycharmProjects/ESG Project/venv/lib/python3.8/site-packages/pandas/core/generic.py", line 2345, in to_excel
    #formatter.write(
  #File "/Users/xinyuecheng/PycharmProjects/ESG Project/venv/lib/python3.8/site-packages/pandas/io/formats/excel.py", line 888, in write
    #writer = ExcelWriter(  # type: ignore[abstract]
  #File "/Users/xinyuecheng/PycharmProjects/ESG Project/venv/lib/python3.8/site-packages/pandas/io/excel/_openpyxl.py", line 49, in __init__
    #from openpyxl.workbook import Workbook
  #File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/_pydev_bundle/pydev_import_hook.py", line 21, in do_import
    #module = self._system_import(name, *args, **kwargs)
#ModuleNotFoundError: No module named 'openpyxl'
      
#Messages in Terminal
#(venv) (base) xinyuecheng@pc-68-53 ESG Project % pip install 'openpyxl'
#Requirement already satisfied: openpyxl in /Users/xinyuecheng/opt/anaconda3/lib/python3.8/site-packages (3.0.5)
#Requirement already satisfied: et-xmlfile in /Users/xinyuecheng/opt/anaconda3/lib/python3.8/site-packages (from openpyxl) (1.0.1)
#Requirement already satisfied: jdcal in /Users/xinyuecheng/opt/anaconda3/lib/python3.8/site-packages (from openpyxl) (1.4.1)
      
   
      
