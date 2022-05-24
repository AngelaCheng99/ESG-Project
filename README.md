# ESG-Project

## Table of Contents

## [Database/Draft Reports](https://github.com/AngelaCheng99/ESG-Project/blob/main/Database.md)
- [BLK](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#blackrock)
- [SSB](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#state-street)
- [JPM](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#jp-morgan)
- [BNYM](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#bny-mellon)
- [Citi](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#citi)

## [Wk1 May 27th Research](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#research)
- [Idea 1: Key Targets & Metrics](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#idea-1-look-for-key-targets--metrics)
- [Idea 2: ESG Wordlist](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#idea-2-look-for-esg-wordlist-as-described-in-this-research)



### Idea 1: Look for Key Targets & Metrics

**Recurring themes:** 
- GRI ([Global Reporting Index](https://www.globalreporting.org/how-to-use-the-gri-standards/gri-standards-english-language/))
- TCFD ([Task Force on Climate-related Financial Disclosures](https://www.fsb-tcfd.org/)) Metrics and Targets
- Link to SDG ([Sustainable Development Goals](https://sdgs.un.org/))
- SASB ([Sustainability Accounting Standards Board](https://www.sasb.org/))

**PROs**
- Align with goal-tracknig purpose/principle in work

**CONs**
- Hard to standardize across providers (fragemented pieces). Might as well read the pdf.
- The only thing which is more standardized is reporting on E (Environment). TCFD Metrics and Targets are the closest with some stats available for comparison between providers. But if looking for this specifically, then might as well search in the pdf (no need for python) 
- Example standardized stats: fund exposure, carbon/emission footprint

Would be interesting to identify what are the common stats available across providers.
- Extract all the goals from each provider
- Compare the goals with each other to see if they are similar
- Challenging: some providers give ad hoc stats and do not publish progress on the goals using numbers (more using text) and can change stats reported from year to year (lack of consistency)

### Idea 2: Look for ESG Wordlist as described in this research

Literature inspiration: [Environmental, social and governance reporting in annual reports: A textual analysis](https://onlinelibrary.wiley.com/doi/full/10.1111/fmii.12132)

**PROs**: more suitable for python code (something which is definitely people cannot do - too tedious)\
**CONs**: not really goal tracking. Companies who talk more about ESG may or may not necessarily complete/realize their goals.

**PROCESS**
1. Look at main vocab based on 4 ESG reports. Visualize wordcloud ("junk" words expected) 
2. Come up with a ESG wordlist/Cross reference my ESG wordlist with what's in the literature. 
3. Get a score for each bank after searching for the ESG wordlist 
4. Compared that score with MSCI ESG score for each companny (Test reliability of the index)

Another idea is to build the wordlist from 2020 reports and test in 2021 reports. But this might not be a good idea (key themes can change over time. What's relevant last year may not be the focus this year). 

Note: original ESG wordlist is from annual reports, not ESG reports 



