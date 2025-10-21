import pandas as pd

def main():
    df = pd.read_csv('data/sample_dataset.csv')
   
    df = df.drop_duplicates()
    
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
    
    df['amount_in_thousands'] = df['amount'] / 1000.0
    df.to_csv('data/cleaned_dataset.csv', index=False)
    print("Cleaned data saved to data/cleaned_dataset.csv")

if __name__ == "__main__":
    main()
