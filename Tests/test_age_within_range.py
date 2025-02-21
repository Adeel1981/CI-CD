import pandas as pd

def test_age_within_range():
    try:
        # Load data
        data = pd.read_csv("data/bank.csv")

        # Check if 'age' column exists
        assert 'age' in data.columns, "'age' column is missing"

        # Check if age is within a valid range (for example, 18 to 100)
        assert data['age'].between(18, 100).all(), "Some ages are out of the valid range (18-100)"

        print("Test Passed: Age is within valid range.")
    except Exception as e:
        print(f"Test Failed: {e}")

# Run the test
test_age_within_range()
 
