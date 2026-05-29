# 🏠 House Price Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Web%20Scraping-2EAD33.svg)](https://playwright.dev/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-red.svg)](https://scikit-learn.org/)
[![CatBoost](https://img.shields.io/badge/CatBoost-0.7869%20R²-green.svg)](https://catboost.ai/)

An end-to-end machine learning pipeline that predicts house prices in Islamabad's Bani Gala area. This project covers the entire data lifecycle: from **automated dynamic web scraping using Playwright**, to advanced feature engineering, and finally, robust predictive modeling.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Dataset & Scraping Architecture](#dataset--scraping-architecture)
- [Models Implemented](#models-implemented)
- [Results & Evaluation](#results--evaluation)
- [Installation](#installation)
- [Usage](#usage)
- [Challenges & Solutions](#challenges--solutions)
- [Future Improvements](#future-improvements)
- [Author & Acknowledgments](#-author--acknowledgments)

---

## 🎯 Overview

This system leverages real estate listings from Zameen.com to deliver accurate property price predictions. Because modern real estate platforms rely heavily on JavaScript and dynamic content, traditional scraping tools often fail. This project utilizes **Playwright** to simulate real browser interactions, creating a high-quality custom dataset from scratch. 

Multiple regression models were trained and evaluated on this dataset, with **CatBoost** emerging as the best performer, achieving an **R² score of 0.7869** (explaining 78.7% of the variance in property prices).

---

## ✨ Key Features

- 🕷️ **Advanced Web Scraping** - Utilizes **Playwright** to handle dynamic JavaScript rendering, infinite scrolling, and anti-bot measures, ensuring reliable data extraction from Zameen.com.
- 🧹 **Robust Data Preprocessing** - Automated pipelines to handle missing values, drop duplicates, and standardize inconsistent currency/area formats.
- 🔧 **Feature Engineering** - Derives 16+ new predictive features (e.g., `luxury_score`, `property_age`, `area_per_bedroom`) to boost model accuracy.
- 🤖 **Comprehensive ML Training** - Evaluates 6 distinct regression models ranging from baseline Linear Regression to advanced gradient-boosted trees.
- 💻 **Interactive Notebook** - A unified Jupyter Notebook environment for both model training and real-time predictions.

---

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── scraper/
│   └── zameen_scraper.py                  # Playwright automation scripts
│
├── data/
│   ├── zameen_data.csv                    # Raw data extracted by Playwright
│   └── bani_gala_model_ready.csv          # Cleaned, engineered dataset
│
├── notebooks/
│   ├── data_preprocessing.ipynb           # EDA, cleaning, and feature engineering
│   ├── Model_and_predication_System.ipynb # Combined training & prediction system
│   └── hyperparameter_tuning.ipynb        # CatBoost optimization
│
├── models/
│   └── final_catboost_model.pkl           # Serialized production model
│
├── src/
│   └── preprocess.py                      # Reusable data cleaning modules
│
├── requirements.txt                       # Project dependencies
├── README.md                              # Documentation
└── Final_Report.pdf                       # Comprehensive academic report
