# A gambler's approach to investing

What happens when a gambler invests in the stock market? Let's see the results shall we?!

## Dataset
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

## Gambler Strategy
Invest a defined amount every day. If the stock price goes down, you invest double the amount.

For __6.95 years__ you invested a total of __$37140 dollars__ and you ended up with a total of __$71263 dollars__

## Yearly Strategy
Invest the same amount that the [Gambler Strategy](#gambler-strategy) will invest in a year, but all up front in the begining of the year
    
For __6.95 years__ you invested a total of __$37705__ and you ended up with a total of __$79076__
    
## Monthly Strategy
Invest the same amount that the [Gambler Strategy](#gambler-strategy) will invest in a month, but all up front in the begining of the month
    
For __6.95 years__ you invested a total of __$37200__ and you ended up with a total of __$71780__
