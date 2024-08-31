# Hypothesis

What happens when a gambler invests in the stock market? The idea is to invest a defined amount every day. If the stock price goes down, you invest double the amount.

# Dataset
The [dataset](https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks?resource=download&select=sp500_index.csv#) used, to test this gambler's approach to investing, was the daily closing price of the S&P500 index.
Here is the head of the dataset:

<table border="1" class="data frame">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>S&amp;P500</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014-07-31</td>
      <td>1930.67</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014-08-01</td>
      <td>1925.15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014-08-04</td>
      <td>1938.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014-08-05</td>
      <td>1920.21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014-08-06</td>
      <td>1920.24</td>
    </tr>
  </tbody>
</table>

# Strategies
## Gambler Strategy
Invest a defined amount every day. If the stock price goes down, you invest double the amount.

## Yearly Strategy
Invest the same amount that the [Gambler Strategy](#gambler-strategy) will invest in a year, but all upfront at the beginning of the year.
    
## Monthly Strategy
Invest the same amount that the [Gambler Strategy](#gambler-strategy) will invest in a month, but all upfront at the beginning of the month.

# Results

During __6.95 years__, assuming the defined amount by the [gambler](https://danielvcorreia.com/nsfw) is __$10__ if the S&P500 index goes up and __$20__ if it goes down or stays the same, the results obtained were:

| Strategy | Invested | Balance |
| ----------- | ----------- | ----------- |
| Gambler | $37140 | $71263 |
| Yearly | $37705 | $79076 |
| Monthly | $37200 | $71781 |

The results show that the [gambler](https://danielvcorreia.com/+18) was not in a good day.
