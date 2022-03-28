# Electricity Operating Reserve Forecasting

The goal of this project is to predict the electricity operating reserve (備轉容量) for the next 14 days (2022/03/30 ~ 2022/04/13).

### Data Preprocessing & Analysis

Data is taken from [台灣電力公司](https://data.gov.tw/).  
Training data is the combination of 3 CSV's:  
1. [Data](https://data.gov.tw/dataset/19995) from 2020/01/01 ~ 2021/04/30
2. [Data](https://data.gov.tw/dataset/19995) from 2021/01/01 ~ 2022/02/28
3. [Data](https://data.gov.tw/dataset/25850) from 2022/01/01 ~ 2022/03/29

The datas needed for this project:
1. Dates
2. Operating reserve (unit in MW)  

![Table Sample](/img/table.png)