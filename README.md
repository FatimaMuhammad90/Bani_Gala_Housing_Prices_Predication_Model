# 🏠 House Price Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Web%20Scraping-2EAD33.svg)](https://playwright.dev/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-red.svg)](https://scikit-learn.org/)
[![CatBoost](https://img.shields.io/badge/CatBoost-0.7869%20R²-green.svg)](https://catboost.ai/)

An end-to-end machine learning pipeline that predicts house prices in Islamabad's Bani Gala area. This project covers the entire data lifecycle: from **automated dynamic web scraping using Playwright**, to advanced feature engineering, and finally, robust predictive modeling.

---

##  Overview

This system leverages real estate listings from Zameen.com to deliver accurate property price predictions. Because modern real estate platforms rely heavily on JavaScript and dynamic content, traditional scraping tools often fail. This project utilizes **Playwright** to simulate real browser interactions, creating a high-quality custom dataset from scratch. 

Multiple regression models were trained and evaluated on this dataset, with **CatBoost** emerging as the best performer, achieving an **R² score of 0.7869** (explaining 78.7% of the variance in property prices).

---

##  Key Features

- 🕷️ **Advanced Web Scraping** - Utilizes **Playwright** to handle dynamic JavaScript rendering, infinite scrolling, and anti-bot measures, ensuring reliable data extraction from Zameen.com.
- 🧹 **Robust Data Preprocessing** - Automated pipelines to handle missing values, drop duplicates, and standardize inconsistent currency/area formats.
- 🔧 **Feature Engineering** - Derives 16+ new predictive features (e.g., `luxury_score`, `property_age`, `area_per_bedroom`) to boost model accuracy.
- 🤖 **Comprehensive ML Training** - Evaluates 6 distinct regression models ranging from baseline Linear Regression to advanced gradient-boosted trees.
- 💻 **Interactive Notebook** - A unified Jupyter Notebook environment for both model training and real-time predictions.

---

##  Project Structure

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
│   ├── Model_and_predication_System.ipynb # Combined training & prediction system
│   
│
├── models/
│   └── catboost_info         # Serialized production model
│
├── src/
│   └── data_cleaning.py                      # Reusable data cleaning modules
│
├── requirements.txt                       # Project dependencies
├── README.md                              # Documentation
└── Final_Report.pdf                       # Comprehensive academic report
```

## Dataset & Scraping Architecture

### The Playwright Advantage
> Standard scraping libraries like BeautifulSoup cannot execute JavaScript, making them ineffective against modern, dynamic platforms like Zameen.com. **Playwright** spins up headless Chromium instances, waits for network payloads to fully resolve, interacts smoothly with pagination buttons, and cleanly extracts the DOM just as a human browser would.

### Data Overview

- **Source:** Zameen.com (Focusing on Bani Gala, Islamabad)
- **Volume:** 296 unique, verified property listings
- **Features:** 10 base attributes + 16 engineered features

### Base Features Collected

| Feature | Description | Type |
| :--- | :--- | :--- |
| **Price** | Target variable (represented in PKR) | Numeric |
| **Area** | Property size (standardized and converted to sq ft) | Numeric |
| **Beds** | Total number of bedrooms | Numeric |
| **Baths** | Total number of bathrooms | Numeric |
| **Built Year** | Year of construction completion | Numeric |
| **Property Type** | Structural type (e.g., House, Flat, Farm House) | Categorical |
| **Furnished** | Furnishing status flag (Yes / No) | Categorical |
| **Parking Spaces** | Number of dedicated vehicle parking spots | Numeric |
| **Servant Quarters** | Number of attached servant rooms | Numeric |
| **Floors** | Total story count of the property | Numeric |

### Key Engineered Features

| Feature | Formula / Logical Implementation | Target Benefit |
| :--- | :--- | :--- |
| `total_rooms` | `Beds + Baths` | Captures complete structural footprint |
| `property_age` | `2026 - Built Year` | Tracks structural depreciation over time |
| `area_per_bedroom` | `Area / Beds` | Identifies layout spaciousness vs layout density |
| `luxury_score` | `(Furnished × 2) + (Servant × 2) + (Parking × 1)` | Aggregates high-value premium amenities |
| `is_new` | `Built Year ≥ 2020` | Categorizes modern build classifications |

---

## Models Implemented

1. **Linear Regression** - Served as the initial baseline performance benchmark.
2. **Decision Tree** - Mapped non-linear data structures using hierarchical rules.
3. **Random Forest** - Used bagging ensembles to reduce variance and control overfitting.
4. **Gradient Boosting** - Combined sequential weak learners through gradient descent.
5. **XGBoost** - Implemented extreme gradient boosting with parallelized system optimization.
6. **CatBoost** - Leveraged native categorical feature processing to optimize overall accuracy.

---

## 📈 Results & Evaluation

### Performance Matrix

| Rank | Model | R² Score | MAE (PKR) | RMSE (PKR) |
| :---: | :--- | :---: | :---: | :---: |
| 1 | **Tuned CatBoost** | **0.7869** | 5,100,000 | 7,200,000 |
| 2 | Random Forest | 0.7435 | 5,507,263 | 7,817,750 |
| 3 | XGBoost | 0.6641 | 5,998,624 | 8,647,719 |
| 4 | Decision Tree | 0.6384 | 5,970,833 | 8,972,121 |
| 5 | Linear Regression | 0.4290 | 6,932,500 | 11,274,553 |
| 6 | Gradient Boosting | 0.1482 | 9,120,000 | 13,771,069 |

### The Value of Feature Engineering

| Model Architecture | Original R² Score | Engineered R² Score | Net Performance Jump |
| :--- | :---: | :---: | :---: |
| **CatBoost** | 0.6966 | 0.7442 | **+4.76%** |
| **Random Forest** | 0.7255 | 0.7435 | **+1.80%** |

### Hyperparameter Tuning (CatBoost)

| Optimization Run | R² Score Performance |
| :--- | :---: |
| Default Parameters | 0.7442 |
| **Conservative Optimization Tuning** | **0.7869** (+4.27%) |

**Final Hyperparameter Configuration:**
- `iterations` = 150
- `learning_rate` = 0.05
- `depth` = 6
- `l2_leaf_reg` = 5

---

##  Installation

### Prerequisites
- Python 3.8 or higher
- `pip` package manager
- Jupyter Notebook environment (`pip install notebook`)

### 1. Clone & Install
```bash
git clone [https://github.com/yourusername/house-price-prediction.git](https://github.com/yourusername/house-price-prediction.git)
cd house-price-prediction
pip install -r requirements.txt
```

# ⭐ Star this repository if you found it helpful!
