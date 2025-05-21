import pandas as pd

def fetch_data(start_date, end_date):
    # Simulate fetching data (replace with actual data fetching logic)
    date_range = pd.date_range(start=start_date, end=end_date)
    data = pd.DataFrame({
        'Date': date_range,
        'GHI': [100 + i for i in range(len(date_range))],  # Example data
        'DNI': [50 + i for i in range(len(date_range))],   # Example data
    })
    return data