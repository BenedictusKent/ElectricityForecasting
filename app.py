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
    from pmdarima import auto_arima
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    warnings.filterwarnings('ignore')

    df_training = pd.read_csv(args.training, index_col='日期', parse_dates=True)
    # Takes time to finish execution, no need to uncomment unless needed
    # stepwise_fit = auto_arima(df_training['備轉容量(MW)'], m=7, trace=True, suppress_warnings=True)
    # stepwise_fit.summary()
    # Best model: SARIMAX(2, 1, 3)x(1, 0, [1], 7)
    model = SARIMAX(df_training['備轉容量(MW)'], order=(2,1,3), seasonal_order=(1,0,1,7))
    model = model.fit()
    index_future_dates = pd.date_range(start='2022-03-23', end='2022-04-06')
    df_result = model.predict(start=len(df_training), end=len(df_training)+14, typ='levels')
    df_result.index = index_future_dates
    df_result.to_csv(args.output, header=False)