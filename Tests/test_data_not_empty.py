import pandas as pd

def test_data_not_empty():
    try:
        # Load data
        data = pd.read_csv("data/bank.csv")

        # Check if data is not empty
        assert not data.empty, "Data is empty!"

        print("Test Passed: Data is not empty.")
    except Exception as e:
        print(f"Test Failed: {e}")

# Run the test
test_data_not_empty()
 
