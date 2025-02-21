import pandas as pd

def test_data_loading():
    try:
        # Load data
        data_file = "data/bank.csv"
        data = pd.read_csv(data_file)  # Read the CSV using the relative path

        # Check if the data is loaded properly
        assert not data.empty, "Data is empty!"
        print("Test Passed: Data loaded successfully.")
    except Exception as e:
        print(f"Test Failed due to: {e}")

# Run the test
test_data_loading()
