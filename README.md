#  Analysis of H-2 Visa Certifications and Experience Requirements

This repository contains data, methodologies, and analysis associated with the [BuzzFeed News article, "All You Americans Are Fired,"](http://www.buzzfeed.com/jessicagarrison/all-you-americans-are-fired) published December 1, 2015.

## Data

The analyses in this repository depend chiefly on visa-certification data published by the Department of Labor's Office of Foreign Labor Certification (OFLC). The OFLC publishes spreadsheets detailing its decisions about whether to approve ("certify") employers to bring H-2 guest workers to the United States. H-2 visas come in two types: H-2A for agricultural workers and H-2B for non-agricultural unskilled workers. The Department of Labor's data covers __H-2A decisions since FY2006__ and __H-2B decisions since FY2000__. The most recent data, for both visa types, includes data  __through FY2015__, which concluded on Sept. 30, 2015.

The raw data were collected from two sites — [doleta.gov](http://www.foreignlaborcert.doleta.gov/performancedata.cfm) and [fldatacenter.com](http://www.flcdatacenter.com/) — and were then processed into a standardized format. You can find that raw data, the processing scripts, and additional details [here](https://github.com/buzzfeednews/H-2-certification-data).


## Analyses

- __Passage__: "Last year, thousands of American companies won permission to bring a total of more than 150,000 people into the country as guest workers for unskilled jobs, under a federal program that grants them temporary work permits known as H-2 visas."
- __Analysis__: Because the OFLC does not publish unique identifiers for certified employers, it is virtually impossible to tally an exact count of these companies. However, a relatively conservative estimate — trying to account for some variations in how companies write their names — suggests that approximately 9,000 employers were certified in FY 2014, and approximately 10,000 in FY 2015. In FY 2014, the Department of State granted 157,376 H-2 visas, [per their annual report](http://travel.state.gov/content/dam/visas/Statistics/AnnualReports/FY2014AnnualReport/FY14AnnualReport-TableXVIB.pdf), though the Department of Labor "certified" employers for substantially larger number of positions. [Details here.](notebooks/certification-histories.ipynb)

---

- __Passage__: "During a three-year period reviewed by the Labor Department, [Linda White's] clients were approved for more than 8,000 visas, federal data show."
- __Analysis__: The three year period is 2010, 2011, and 2012. During that time, White was listed as the agent on applications approving 8,073 visas. (That number may represent an undercount if, for example, some applications misspelled or omitted White's name.) [Details here.](notebooks/certification-histories.ipynb)

---

- __Passage__: "[...] Fresh Harvest, a farm labor contractor based in California that accounted for roughly one-fifth of all agricultural H-2 visas approved in the state last year."
- __Analysis__: In 2014, the Office of Foreign Labor Certification certified Fresh Harvest to bring 1,253 workers to California, according to the OFLC's records. During the same year, the OFLC certified visas for a total of 6,001 California-based positions. 1,253 / 6,001 = 0.21. [Details here.](notebooks/certification-histories.ipynb)

---

- __Passage__: "In recent years a full three-quarters of companies approved to bring in agricultural guest workers have listed such requirements, according to a BuzzFeed News analysis of federal data. In some states — as geographically diverse as New York, North Carolina, Montana, and Washington — virtually all agricultural employers demand prior experience."
- __Analysis__: This data comes from the [OFLC's certification-decision data](http://www.foreignlaborcert.doleta.gov/performancedata.cfm) for the H-2A program for FY 2015, which includes a `EMP_EXPERIENCE_REQD` field. Additional data were drawn from the OFLC's [Labor Certification Registry](https://icert.doleta.gov/index.cfm?event=ehLCJRExternal.dspAdvCertSearch), which contains comparable information for prior years. [Details here.](notebooks/experience-requirements.ipynb)

---

## Reproducing These Analyses

This repository contains all the data and code necessary to reproduce the analyses above. In theory, it should be possible to perform the analysis in any computer language or statistical program. We performed our analysis in Python. To re-run it you'll need Python 3 and the libraries listed in [`requirements.txt`](requirements.txt).

## Questions / Feedback?

Email Jeremy Singer-Vine at jeremy.singer-vine@buzzfeed.com
