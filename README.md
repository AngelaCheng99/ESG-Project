# ESG-Project

## Table of Contents

Database/Draft Reports
- [BLK](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#blackrock)
- [SSB](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#state-street)
- [JPM](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#jp-morgan)
- [BNYM](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#bny-mellon)
- [Citi](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#citi)

[Wk1 May 27th Research](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#research)
- [Idea 1: Key Targets & Metrics](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#idea-1-look-for-key-targets--metrics)
- [Idea 2: ESG Wordlist](https://github.com/AngelaCheng99/ESG-Project/edit/main/README.md#idea-2-look-for-esg-wordlist-as-described-in-this-research)
- [BLK Reports]
- [SSB Reports]
- [JPM Reports]
- [BNYM Reports]

 
## Wk1 (May 27th) Research

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

#### **BLACKROCK**

[BLK 2020 TCFD Report](https://www.blackrock.com/corporate/literature/continuous-disclosure-and-important-information/blk2020tcfdreport.pdf)

[BLK 2021 TCFD Report](https://www.blackrock.com/corporate/literature/continuous-disclosure-and-important-information/tcfd-report-2021-blkinc.pdf)
- P34-38 Environment related stats and metrics (e.g. emission)

[BLK 2020 ESG Report](https://www.blackrock.com/corporate/literature/continuous-disclosure-and-important-information/blackrock-2020-sasb-disclosure.pdf)
- p39-40 BlackRock ESG criteria and how they are measured

[BLK 2021 ESG Report] Not yet available


#### **STATE STREET**

[SSB 2020 ESG Report](https://www.statestreet.com/content/dam/statestreet/documents/values/state-street-esg-report-04-2021.pdf)
- p19 Summary of all ESG metrics (2020 progress, 2021 goals)
- p153 TCFD (p170 onwards GHG emission table)

[SSB 2021 ESG Report](https://www.statestreet.com/content/dam/statestreet/documents/esg/SSC-ESG-2021-Final-Full.pdf)
- p17 Summary of all ESG metrics (2020 progress, 2021 goals)
- p51 Diversity goals
- p155 energy use/TCFD reporting tables

#### **BNY MELLON**

[BNYM 2020 ESG Report](https://www.bnymellon.com/content/dam/bnymellon/documents/pdf/2020-enterprise-esg-report.pdf.coredownload.pdf)
- High-level progress (p11). Specifics are covered in KPI Textboxes throughout the report
- Environmental sustainability/emission specifically (p73)

[BNYM 2021 ESG Report] Likely to be released in June

#### **JP MORGAN**

[JP Morgan 2020 ESG Report Appendices](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/documents/jpmc-esg-report-appendices-2020.pdf) This document gives indiciations on where to find metrics/targets in the main ESG Reprt (p14)

[JP Morgan 2020 ESG Main Report](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/documents/jpmc-esg-report-2020.pdf)
- Wholesale Credit Exposure to Select Industries (p. 17)
- Current Portfolio and 2030 Portfolio Targets (p. 50)
- Our 2020 Sustainable Development Activities (p. 52) 
- 2020 Carbon Footprint Environmental Data (p. 32)
- Current Portfolio and 2030 Portfolio Targets (p. 50)

[JP Morgan 2021 ESG Main Report](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/documents/jpmc-esg-report-2021.pdf)
- Detailed TCFD Reporting to be released later in the year (p13)

#### **CITI**

[Citi 2020 TCFD Report](https://www.citigroup.com/citi/sustainability/data/finance-for-a-climate-resilient-future-2.pdf?ieNocache=229) (P47-55)

[Citi 2020 ESG Main Report](https://www.citigroup.com/citi/about/esg/download/2020/Global-ESG-Report-2020.pdf?ieNocache=291) Relevant sections include:
- 2025 Citi ESG commitment (p. 23)
- Citi progress on Operational Goals/Environment sustainability (p. 55-58)
Citi 2021 TCFD Report is not available (only 2021 and 2018)

[Citi 2021 ESG Main Report](https://www.citigroup.com/citi/about/esg/download/2021/Global-ESG-Report-2021.pdf?ieNocache=291)
- Citi progress on Operational Goals/Environment sustainability (p. 48-64)

### Idea 2: Look for ESG Wordlist as described in this research

Literature inspiration: [Environmental, social and governance reporting in annual reports: A textual analysis](https://onlinelibrary.wiley.com/doi/full/10.1111/fmii.12132)

**PROs**: more suitable for python code (something which is definitely people cannot do - too tedious)
**CONs**: not really goal tracking. Companies who talk more about ESG may or may not necessarily complete/realize their goals.

**PROCESS**
1. Look at main vocab based on 4 ESG reports. Visualize wordcloud ("junk" words expected) 
2. Come up with a ESG wordlist/Cross reference my ESG wordlist with what's in the literature. 
3. Get a score for each bank after searching for the ESG wordlist 
4. Compared that score with MSCI ESG score for each companny (Test reliability of the index)

Another idea is to build the wordlist from 2020 reports and test in 2021 reports. But this might not be a good idea (key themes can change over time. What's relevant last year may not be the focus this year). 

Note: original ESG wordlist is from annual reports, not ESG reports 



