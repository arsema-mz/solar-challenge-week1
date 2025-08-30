# Solar Data Discovery Challenge

## Project Overview
This project focuses on conducting exploratory data analysis (EDA) on solar farm data from Benin, Sierra Leone, and Togo. The objective is to analyze these datasets to identify key trends and insights that will support MoonLight Energy Solutions in enhancing operational efficiency through solar investments.

## Methodology
1. **Data Profiling and Cleaning:**
   - Profiling the datasets to identify missing values and outliers.
   - Implementing data cleaning techniques to ensure accuracy and consistency.

2. **Exploratory Data Analysis (EDA):**
   - Generating summary statistics and visualizations to understand the data better.
   - Analyzing relationships between key variables, including GHI, DNI, temperature, and humidity.
   - Creating time series plots and wind rose diagrams to visualize temporal and directional data patterns.

3. **Comparative Analysis:**
   - Combining datasets from all three countries to facilitate comparative analysis.
   - Evaluating strengths and weaknesses of solar investment opportunities in each country.

## Results
Key Insights: Benin shows the highest Global Horizontal Irradiance (GHI) and Direct Normal Irradiance (DNI), indicating the best potential for solar energy generation. Sierra Leone exhibits lower irradiance values with greater variability, suggesting a need for improved infrastructure. Togo presents moderate solar potential, making hybrid systems a viable option.
Visualizations: Correlation matrices revealed strong relationships between GHI, DNI, and environmental factors. Time series analyses highlighted seasonal trends in solar irradiance, while wind rose diagrams illustrated prevailing wind patterns that could affect solar panel efficiency.
Investment Recommendations: Based on the analysis, Benin is prioritized for solar investments, while Sierra Leone requires infrastructure enhancements. Togo's hybrid system implementation is suggested to ensure reliable energy supply.

## Installation
To set up the project environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/arsema-mz/solar-challenge-week1.git
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   python app.py
   ```

## Future Work
- Further refine analyses based on additional datasets or variables.
- Explore machine learning models to predict solar energy generation potential.
- Engage local communities to gather qualitative insights that could complement quantitative data.


