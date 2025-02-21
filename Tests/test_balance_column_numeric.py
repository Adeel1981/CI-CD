import pandas as pd

def test_balance_column_numeric():
    try:
        # Load data
        data = pd.read_csv("data/bank.csv")

        # Check if 'balance' column exists
        assert 'balance' in data.columns, "'balance' column is missing"

        # Check if 'balance' column is numeric
        assert pd.to_numeric(data['balance'], errors='coerce').notna().all(), "Some values in 'balance' column are not numeric"

        print("Test Passed: Balance column is numeric.")
    except Exception as e:
        print(f"Test Failed: {e}")

# Run the test
test_balance_column_numeric()
 
