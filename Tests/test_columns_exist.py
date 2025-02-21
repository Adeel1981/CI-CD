import pandas as pd

def test_columns_exist():
    try:
        # Load data
        data = pd.read_csv("data/bank.csv")

        # List of required columns
        required_columns = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'deposit']

        # Check if all required columns are present
        missing_columns = [col for col in required_columns if col not in data.columns]
        assert not missing_columns, f"Missing columns: {', '.join(missing_columns)}"

        print("Test Passed: All required columns are present.")
    except Exception as e:
        print(f"Test Failed: {e}")

# Run the test
test_columns_exist()
 
