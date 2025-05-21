import unittest
import pandas as pd
from scripts.data_processing import fetch_data

class TestDataProcessing(unittest.TestCase):
    
    def test_fetch_data(self):
        # Test with specific start and end dates
        start_date = pd.to_datetime("2023-01-01")
        end_date = pd.to_datetime("2023-01-10")
        
        data = fetch_data(start_date, end_date)
        
        # Check if the data is a DataFrame
        self.assertIsInstance(data, pd.DataFrame)
        
        # Check if the date range is correct
        self.assertEqual(len(data), (end_date - start_date).days + 1)
        self.assertTrue((data['Date'].min() >= start_date) and (data['Date'].max() <= end_date))

if __name__ == '__main__':
    unittest.main()