import numpy as np
import pandas as pd


def main():
    s = pd.Series([i * 2 for i in range(1, 10)])
    dates = pd.date_range("20170301", periods=8)
    df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list('ABCDE'))
    print(df.head(2))
    print(df.sort_index(axis=1,ascending=False))


if __name__ == '__main__':
    main()
