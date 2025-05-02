import pandas as pd

def load_club_data(filepath):
    try:
        df = pd.read_excel(filepath)
        print(df.head())
        print(df.columns)
        if 'Link' not in df.columns:
            raise ValueError("The 'Link' column is not found in the DataFrame.")
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
    except Exception as e:
        print(f"❌ Error loading file: {e}")
    return None
