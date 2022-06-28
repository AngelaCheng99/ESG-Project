
#Import ESG Wordlist
import pandas as pd
df = pd.read_csv(r'ESG-Wordlist_2020.csv')
df_v1=df.dropna()
G_words=df_v1.query('Topic=="Governance"')['Word'].tolist()
S_words=df_v1.query('Topic=="Social"')['Word'].tolist()
E_words=df_v1.query('Topic=="Environmental"')['Word'].tolist()

from pathlib import Path
from pdfminer.high_level import extract_text
import PyPDF2
import re

def wordsearch(company_name,Keywords,start_page,end_page):
    pdfPath = Path(f'{company_name} 2020 ESG Report.pdf')
    results={}
    #File = PyPDF2.PdfFileReader(pdfPath)
    #Page_Count = File.getNumPages()
    for word in Keywords:
        results[word]=[]
        for page in range(start_page,end_page):
            lc_text = extract_text(pdfPath, page_numbers=[page]).lower()
            if lc_text.find(word) == -1:
                continue
            else:
                Freq_per_page = {}
                Freq_per_page[page + 1] = lc_text.count(word)
                results[word].append(Freq_per_page)
        if len(results[word]) == 0:
            del results[word]
    return results

wordsearch('BLK',['angela','blackrock'],0,3)


print(BLK_E_Words)

def wordsearchPDF(company_name,Keywords):
    pdfPath = Path(f'{company_name} 2020 ESG Report.pdf')
    results={}
    for word in Keywords:
        results[word]=[]
    File = PyPDF2.PdfFileReader(pdfPath)
    End_Page = File.getNumPages()
    for page in range(End_Page):
        lc_text = extract_text(pdfPath, page_numbers=[page]).lower()
        for word in Keywords:
            if lc_text.find(word) == -1:
                continue
            else:
                Freq_per_page = {}
                Freq_per_page[page + 1] = lc_text.count(word) #counting function will give 0 if does not appear
                results[word].append(Freq_per_page)
    for word in Keywords:
        if len(results[word]) == 0:
            del results[word]
    return results

def output_names(company_names):
    for name in company_names:
        print(f'{name} e_words')
        print(f'{name} s_words')
        print(f'{name} g_words')

output_names(company)
BLK_E_Words = wordsearchPDF('BLK',E_words,0,46)
company= ['BLK']

BLK_E_Words=wordsearchPDF('BLK',E_words)
print(BLK_e_Words)
BLK_G_Words=wordsearchPDF('BLK',G_words)

results = {} #dict
for names in pdfNames:
    pdfPath = Path(f'{names} 2020 ESG Report.pdf')
    print(pdfPath)
    Output = readPDF(pdfPath)
    #print(Output)
    Output.to_csv(f'{names} Output Freq.csv', index=False)
    results[names]=Output