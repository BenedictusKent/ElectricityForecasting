if __name__ == '__main__':
    # Unmodifiable
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')

    parser.add_argument('--output',
                        default='submission.csv',
                        help='output file name')
    args = parser.parse_args()
    
    # Modifiable
    import warnings
    import pandas as pd
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    warnings.filterwarnings('ignore')

    df_training = pd.read_csv(args.training, index_col='日期', parse_dates=True)
    model = SARIMAX(df_training['備轉容量(MW)'], order=(0,1,5), seasonal_order=(1,0,1,7))
    model = model.fit()
    index_future_dates = pd.date_range(start='2022-03-23', end='2022-04-06')
    df_result = model.predict(start=len(df_training), end=len(df_training)+14, typ='levels')
    df_result.index = index_future_dates
    # print(type(df_result))
    df_result.to_csv(args.output, header=False)