# invest-calc

What is the safe withdrawal rate (SWR)? 

Assuming you have E equity invested in the S&P 500 index fund and a withdrawal
rate of W when you start your retirement at year 0:  
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

In general, after withdrawal for next year's expenses, the remaining equity
at the end of year n is  
&emsp;e<sub>n</sub> = e<sub>n-1</sub> (1+r<sub>n</sub>) - E W (1+i<sub>1</sub>) ... (1+i<sub>n</sub>)  
&emsp;&emsp;= e<sub>0</sub> (1+r<sub>1</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;- E W (1+i<sub>1</sub>) (1+r<sub>2</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;- ...  
&emsp;&emsp;&emsp;- E W (1+i<sub>1</sub>) ... (1+i<sub>m</sub>) (1+r<sub>m+1</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;- ...  
&emsp;&emsp;&emsp;- E W (1+i<sub>1</sub>) ... (1+i<sub>n</sub>)  
&emsp;&emsp;= E [&emsp;&emsp;(1+r<sub>1</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;&emsp;- W (1+r<sub>1</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;&emsp;- W (1+i<sub>1</sub>) (1+r<sub>2</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;&emsp;- ...  
&emsp;&emsp;&emsp;&emsp;- W (1+i<sub>1</sub>) ... (1+i<sub>m</sub>) (1+r<sub>m+1</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;&emsp;- ...  
&emsp;&emsp;&emsp;&emsp;- W (1+i<sub>1</sub>) ... (1+i<sub>n</sub>)&emsp;]  

Safe withdrawal rate is the initial withdrawal rate to use such that at the
end of year n, the remaining equity runs out (i.e. e<sub>n</sub> = 0). Since
the next year's expenses are already covered at this time, the initial equity
E actually lasted n+1 years. (note: the safe withdrawal rate does not really
depend on the initial equity amount E.)

&emsp;SWR = (1+r<sub>1</sub>) ... (1+r<sub>n</sub>) /  
&emsp;&emsp;&emsp;&emsp;[&emsp;&emsp;(1+r<sub>1</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;&emsp;&emsp;+ (1+i<sub>1</sub>) (1+r<sub>2</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;&emsp;&emsp;+ ...  
&emsp;&emsp;&emsp;&emsp;&emsp;+ (1+i<sub>1</sub>) ... (1+i<sub>m</sub>) (1+r<sub>m+1</sub>) ... (1+r<sub>n</sub>)  
&emsp;&emsp;&emsp;&emsp;&emsp;+ ...  
&emsp;&emsp;&emsp;&emsp;&emsp;+ (1+i<sub>1</sub>) ... (1+i<sub>n</sub>)&emsp;]  

SWR depends on how many years (i.e. n+1) the equity needs to last. It also
depends on the market performance (i.e. r<sub>m</sub>) and inflation (i.e.
i<sub>m</sub>) in those years after the retirement, hence, which year the
retirement starts. Typically, the equity expected to last 30 years after
retirement. Using historical data, the following figure shows the SWR for
each starting year.

![SWR over the years](swr.png)

The inverse of SWR, let's call it safe equity withdrawal ratio (SEWR),
can be written like  
&emsp;SEWR = 1 / SWR  
&emsp;&emsp;&emsp;&emsp;= 1  
&emsp;&emsp;&emsp;&emsp;&emsp;+ (1+i<sub>1</sub>) / (1+r<sub>1</sub>)   
&emsp;&emsp;&emsp;&emsp;&emsp;+ ...  
&emsp;&emsp;&emsp;&emsp;&emsp;+ [(1+i<sub>1</sub>) ... (1+i<sub>m</sub>)]  / [(1+r<sub>1</sub>) ... (1+r<sub>m</sub>)]  
&emsp;&emsp;&emsp;&emsp;&emsp;+ ...  
&emsp;&emsp;&emsp;&emsp;&emsp;+ [(1+i<sub>1</sub>) ... (1+i<sub>n</sub>)]  / [(1+r<sub>1</sub>) ... (1+r<sub>n</sub>)]  
&emsp;&emsp;&emsp;&emsp;= 1  
&emsp;&emsp;&emsp;&emsp;&emsp;+ ci<sub>1</sub> / cr<sub>1</sub>  
&emsp;&emsp;&emsp;&emsp;&emsp;+ ...  
&emsp;&emsp;&emsp;&emsp;&emsp;+ ci<sub>m</sub> / cr<sub>m</sub>  
&emsp;&emsp;&emsp;&emsp;&emsp;+ ...  
&emsp;&emsp;&emsp;&emsp;&emsp;+ ci<sub>n</sub> / cr<sub>n</sub>  

Above, ci<sub>m</sub> is the compound inflation from year 1 to year m.
Similarly, cr<sub>m</sub> is the compound return from year 1 to year m.

Specifically, if there is no change in inflation and return, or if the
inflation is identical to return every year, the safe equity withdrawal
ratio is  
&emsp;SEWR<sub>static</sub> = 1 + n  
For 30-year withdrawal, SEWR<sub>static</sub> is 30. This can serve as a
better indicator than the 4% rule (Initial equity should be 25 times the
initial withdrawal).

Only if you are optimistic and believe the compound inflations are always
lower than compound returns, the safe equity withdrawal ratio can be slightly
lower than SEWR<sub>static</sub>. If you are pessimistic, the safe
equity withdrawal ratio needs to be higher than SEWR<sub>static</sub>.


References

1. [Trinity study](https://en.wikipedia.org/wiki/Trinity_study)
2. [S&P 500 Annual Returns](https://www.macrotrends.net/2526/sp-500-historical-annual-returns)
3. [Annual Consumer Price Index](https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-)
