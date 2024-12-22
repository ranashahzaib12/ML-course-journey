# Google Play Store Analysis: EDA and Feature Engineering

## Overview
This project conducts Exploratory Data Analysis (EDA) and Feature Engineering on a dataset of Google Play Store applications. The goal is to analyze app performance, ratings, and categories while identifying trends and insights to improve app strategies and user engagement.

## Dataset
- **Source**: [Google Play Store Dataset](https://www.kaggle.com/lava18/google-play-store-apps)
- **Features**:
  - App Name, Category, Rating, Reviews, Size, Installs, Type (Free/Paid)
  - Price, Content Rating, Genres, Last Updated, Current Version, and Android Version

## Key Steps

### 1. Data Inspection
- Dataset loaded and inspected for missing values, data types, and anomalies.

### 2. Exploratory Data Analysis (EDA)
- **Univariate Analysis**: Focused on individual features such as app categories, ratings, and install counts.
- **Bivariate Analysis**: Explored relationships between features like app category and rating, or app size and installs.
- **Visualizations**: Utilized Matplotlib and Seaborn for in-depth analysis.

### 3. Data Cleaning
- Handled missing and inconsistent data:
  - Imputation for missing ratings or reviews.
  - Standardized size and install values for uniformity.

### 4. Feature Engineering
- Created new features such as:
  - **Size Categories**: Grouped apps into size bins.
  - **Price Buckets**: Segmented apps into price ranges for analysis.

### 5. Insights
- Free apps generally have more installs but slightly lower ratings compared to paid apps.
- Certain categories like "Game" and "Education" dominate the Play Store in terms of number and popularity.

### 6. Visualizations
- **Bar Charts**: Showed app count distribution across categories.
- **Boxplots**: Highlighted price and rating variations across genres.
- **Correlation Heatmaps**: Identified relationships among numerical features.

## How to Use
1. Clone the repository and ensure the dataset is available in the working directory.
2. Install required libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`.
3. Run the notebook to replicate analysis and generate visualizations.

## Future Work
- Build predictive models for app success metrics such as ratings and installs.
- Perform sentiment analysis on user reviews for deeper insights.

## Dependencies
- Python Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`

## Acknowledgments
Special thanks to the dataset creators for making this project possible.
