
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
import csv

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

#Edited Version
def wordsearch_v1(company_name,Keywords):
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

wordsearch_v1('BLK',E_words)
#make a function for line 48 to 54
#load the page only once. Use lc_text for 3 different lists of keywords

#Text Finding
def findWords(Keyword_list,extracted_text):
    Freq_per_page = {}
    for word in Keyword_list:
        if extracted_text.find(word) == -1:
            continue
        else:
            Freq_per_page[word] = extracted_text.count(word)
    return Freq_per_page

#New Function
def wordsearchPDF(company_name,E_Wordlist,S_Wordlist,G_Wordlist):
    pdfPath = Path(f'{company_name} 2020 ESG Report.pdf')
    E_results ={}
    S_results={}
    G_results={}
    File = PyPDF2.PdfFileReader(pdfPath)
    End_Page = File.getNumPages()
    for page in range(End_Page):
        lc_text = extract_text(pdfPath, page_numbers=[page]).lower()
        E_results[page+1]=findWords(E_Wordlist,lc_text) # page + 1 as
        S_results[page+1]=findWords(S_Wordlist,lc_text)
        G_results[page+1]=findWords(G_Wordlist,lc_text)
    return E_results,S_results,G_results

BLK_E_results, BLK_S_results, BLK_G_results = wordsearchPDF('BLK',E_words,S_words,G_words)

#Key Takeaways
# Operation slow in reading text: try to minimize the number of times we read/reload the text
# to learn more, google profiling (how long each line of the code takes to run/how much memory they take) There is a trade-off between the two


def output_names(company_names):
    for name in company_names:
        print(f'{name} e_words')
        print(f'{name} s_words')
        print(f'{name} g_words')

output_names(company)
BLK_E_Words = wordsearchPDF('BLK',E_words,0,46)
company= ['BLK']

BLK_Words=wordsearchPDF('BLK',E_words)

print(BLK_E_Words)
print(BLK_Words)

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