import argparse
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description="Wczytaj z url")
    parser.add_argument("--url", type=str, help="URL do wczytania", required=True)
    parser.add_argument("--columns", nargs="+", help="Kolumny do wczytania", default=None)
    parser.add_argument("--rows", type=int, help="Liczba wierszy do wczytania", default=10)

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    df = pd.read_csv(args.url, nrows=args.rows, usecols=args.columns)
    print(df.head(args.rows))