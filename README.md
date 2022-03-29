# Electricity Operating Reserve Forecasting

The goal of this project is to predict the electricity operating reserve (備轉容量) for the next 14 days (2022/03/30 ~ 2022/04/13).

## Data Preprocessing

Data is taken from [台灣電力公司](https://data.gov.tw/).  
Training data is the combination of 3 CSV's:  
1. [Data](https://data.gov.tw/dataset/19995) from 2020/01/01 ~ 2021/04/30
2. [Data](https://data.gov.tw/dataset/19995) from 2021/01/01 ~ 2022/02/28
3. [Data](https://data.gov.tw/dataset/25850) from 2022/01/01 ~ 2022/03/29

The datas needed for this project:
1. Dates
2. Operating reserve (unit in MW)  

![Table Sample](/img/table.png)

## Data Analysis

Below is the graph of operating reserve plotted against dates:  
![Data Graph](/img/chart.png)

Using `seasonal_decompose`, we can discover more from the graph whether it is a stationary or non-stationary data:
![Seasonal Graph](/img/decompose.png)
From the above chart, we can see that there is an apparent seasonality in the chart, hence it is a **non-stationary** graph

We can also use *Augmented Dickey-Fuller (ADF)* and *Kwiatkowski-Phillips-Schmidt-Shin (KPSS)* test to determine the nature of the graph.  
Click to learn more of [Dickey-Fuller](https://analyticsindiamag.com/complete-guide-to-dickey-fuller-test-in-time-series-analysis/) and [KPSS](https://www.machinelearningplus.com/time-series/kpss-test-for-stationarity/).  
**ADF test**:  
![ADF test](/img/adf.png)
> If the test statistic is less than the critical value, we can reject the null hypothesis (aka the series is stationary). When the test statistic is greater than the critical value, we fail to reject the null hypothesis (which means the series is not stationary).  

Since `Test Statistic > Critical Value`, we can infer that the chart is **Not Stationary**

**KPSS test**:  
![KPSS test](/img/kpss.png)
> If the test statistic is greater than the critical value, we reject the null hypothesis (series is not stationary). If the test statistic is less than the critical value, if fail to reject the null hypothesis (series is stationary).   

We can see that `Test Statistic < Critical Value`, hence the chart is **Stationary**

Since 2 different tests resulted in 2 different conclusions, we can determine the type of stationarity.
![Type of Stationarity](/img/stationarity.png)

[Related article](https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/)