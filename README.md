# Hydroclimate-Pantanal

Welcome to the **Hydroclimate-Pantanal** repository, which hosts the code and data processing scripts used for the analyses in the article:

**"Decadal Hydroclimatic Changes in the Pantanal – the World's Largest Tropical Wetland."**

## Overview

This repository contains scripts for analyzing hydroclimatic changes in the Pantanal wetland, with a focus on data such as precipitation, runoff, temperature, potential evapotranspiration, vapor pressure deficit, and land use/cover. These analyses aim to deepen our understanding of climate and land use impacts on wetland dynamics in the Pantanal, contributing to future conservation efforts.

## Contents

- **Data**: Contains all `.csv` files used in the analyses. Data sources are documented in a text file within this folder.
- **Data Preparation**: Scripts for data cleaning and preprocessing.
- **Analysis**: Scripts for exploring relationships among hydroclimatic variables over time, generating figures (time series plots, regression analyses, spatial maps) used in the article.

## Requirements

The primary tools used in this repository include Python and the following packages:
- `numpy`, `pandas`, `geopandas`, `matplotlib`, `seaborn`, `scipy`, `scikit-learn`, `plotly`, `statsmodels`, and `ruptures`.

To install the required packages:
```bash
pip install -r requirements.txt```

   
## Repository Structure

- `data/`:  Processed data files in CSV format for analysis.
- `scripts/`:  Python scripts for data processing, change point detection, and trend analysis.
- `README.md`: Repository overview, setup instructions, and other relevant information..

## Citation

If you use this repository in your research, please cite the article as follows:

> Author(s), "Decadal Hydroclimatic Changes in the Pantanal – the World's Largest Tropical Wetland," Journal, Year.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code, provided that appropriate credit is given.

---

We hope this repository aids your understanding of the hydroclimatic dynamics in the Pantanal. If you have any questions or suggestions, please feel free to reach out (cb3910@msstate.edu)!

