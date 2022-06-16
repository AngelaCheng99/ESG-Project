from pdfminer.high_level import extract_text
import re
import collections
from collections import Counter
import pandas as pd

#Import ESG Wordlist
df = pd.read_csv(r'ESG-Wordlist_2020.csv')
df_v1=df.dropna()
G_words=df_v1.query('Topic=="Governance"')['Word'].tolist()
S_words=df_v1.query('Topic=="Social"')['Word'].tolist()
E_words=df_v1.query('Topic=="Environmental"')['Word'].tolist()

def readPDF(inputPath):
    raw_text = extract_text(inputPath)
    lc_text = raw_text.lower()
    reg_words = re.findall(r'\b[a-z]{3,15}\b', lc_text)
    return reg_words

BLK_words=readPDF('BLK 2020 ESG Report.pdf')

def esgTest(Keywords,Pool):
    Freq = {key : Pool.count(key) for key in Keywords}
    Freq_table = pd.DataFrame(Freq.items(), columns=["Words", "Frequency"])
    Rank_table = Freq_table.sort_values(by="Frequency", ascending=False)
    return Rank_table

#Environment
E_Freq = {key : BLK_words.count(key) for key in E_words}
E_Freq_table = pd.DataFrame(E_Freq.items(), columns=["Words", "Frequency"])
E_Rank_table = E_Freq_table.sort_values(by="Frequency", ascending=False)
print(Counter(BLK_words)['biodiversity'])  #verify frequency of selected words in original BLK words

Environment = esgTest(E_words,BLK_words)
Social = esgTest(S_words,BLK_words)
Governance = esgTest(G_words,BLK_words)

#Create a loop, systematically loop through ESG words for each report
#Only save output for one function? Or can function return multiple output?

#Cannot install wordcloud as currently only available for Python 3.8
#https://github.com/amueller/word_cloud




