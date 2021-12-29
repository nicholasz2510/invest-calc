# invest-calc

What is the safe withdrawal rate (SWR)? 

Assuming you have E equity invested in S&P 500 index fund and W withdrawal
rate when you start your retirement at year 0:  
To cover next year's expenses, you withdraw  
&emsp;E W  
The remaining equity at the end of year 0 is  
&emsp;e<sub>0</sub> = E - E W  

If annual return for year 1 is r<sub>1</sub>, then at the end of year 1,
the equity becomes  
&emsp;e<sub>0</sub> (1+r<sub>1</sub>)  
To adjust for year 1's inflation i<sub>1</sub>, now you withdraw  
&emsp;E W (1+i<sub>1</sub>)  
to cover next year's expenses. The remaining equity at the end of year 1 is  
&emsp;e<sub>1</sub> = e<sub>0</sub> (1+r<sub>1</sub>) - E W (1+i<sub>1</sub>)   

If annual return for year 2 is r<sub>2</sub>, then at the end of year 2,
the equity becomes  
&emsp;e<sub>1</sub> (1+r<sub>2</sub>)  
After withdrawal for next year's expenses, the remaining equity at the end of
year 2 is  
&emsp;e<sub>2</sub> = e<sub>1</sub> (1+r<sub>2</sub>) - E W (1+i<sub>1</sub>) (1+i<sub>2</sub>)  
And so on.

In general after withdrawal for next year's expenses, the remaining equity
at the end of year n is  
&emsp;e<sub>n</sub> = e<sub>n-1</sub> (1+r<sub>n</sub>) - E W (1+i<sub>1</sub>) ... (1+i<sub>n</sub>)  

References

[1] <https://en.wikipedia.org/wiki/Trinity_study> "Trinity study"
[2] <https://www.macrotrends.net/2526/sp-500-historical-annual-returns> "S&P 500 Annual Returns"
[3] <https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-> "Annual Consumer Price Index"
