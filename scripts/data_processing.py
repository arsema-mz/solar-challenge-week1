import pandas as pd

def fetch_data(start_date, end_date):
    
    benin = pd.read_csv('../cleaned_data/cleaned_benin_data.csv')
    sierra_leone = pd.read_csv('../cleaned_data/cleaned_sierraleone_data.csv')
    togo = pd.read_csv('../cleaned_data/cleaned_togo_data.csv')

    benin['Country'] = 'Benin'
    sierra_leone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    data= pd.concat([benin, sierra_leone, togo], ignore_index=True)

    return data