# Flight Price Prediction: EDA and Feature Engineering

## Overview
This project performs Exploratory Data Analysis (EDA) and Feature Engineering to predict flight prices. The dataset provides comprehensive details about flights, including airline, source and destination cities, class, duration, and ticket prices. The goal is to extract insights, identify trends, and prepare the dataset for predictive modeling.

## Dataset
- **Source**: [Kaggle Dataset: Flight Price Prediction](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)
- **Features**: 11 columns with categorical and numerical data.  
  - **Airline**: Name of the airline.  
  - **Flight**: Flight code.  
  - **Source City**: City of departure.  
  - **Destination City**: City of arrival.  
  - **Departure/Arrival Time**: Grouped into time bins.  
  - **Stops**: Number of stops during the journey.  
  - **Class**: Economy or Business.  
  - **Duration**: Travel time in hours.  
  - **Days Left**: Days between booking and travel date.  
  - **Price**: Ticket price (target variable).  

## Key Steps

### 1. Data Inspection
- Dataset loaded into a Pandas DataFrame and inspected using:
  - `.head()` and `.tail()` for a preview of rows.
  - `.info()` for an overview of data types and missing values.
  - `.describe()` for statistical summaries.

```python
# Load data
df = pd.read_excel('flight_price.xlsx')
df.head()
```

### 2. Exploratory Data Analysis (EDA)
- **Univariate Analysis**: Examined distributions of key features.
- **Bivariate Analysis**: Analyzed relationships between features such as class, stops, and price.
- **Visualizations**: Created using Matplotlib and Seaborn for trends and correlations.

### 3. Feature Engineering
- Derived new features to enhance the dataset:
  - **Days Left**: Calculated as the difference between booking and travel dates.
  - **Time Periods**: Grouped departure and arrival times into bins for analysis.

### 4. Insights
- Business class flights are priced significantly higher than economy.
- Price increases as the number of stops and travel duration increase.
- Last-minute bookings tend to have higher ticket prices.

### 5. Visualizations
- **Bar Charts**: Compar prices across airlines and cities.
- **Heatmaps**: Highlight correlations among numerical features.
- **Boxplots**: Show variations in price across different categories.

## How to Use
1. Clone the repository and ensure the dataset (`flight_price.xlsx`) is in the working directory.
2. Install the required Python libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`.
3. Run the Jupyter notebook to replicate the analysis and visualizations.

## Future Work
- Build and evaluate machine learning models to predict flight prices.
- Address potential data imbalances in categorical features.
- Optimize features for enhanced prediction accuracy.

## Dependencies
- Python Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`

## Acknowledgments
Special thanks to the creators of the dataset on Kaggle for providing valuable data for analysis.
```
