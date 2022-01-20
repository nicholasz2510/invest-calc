import csv

with open('annual_return.csv', 'r') as annual_return_file:
    reader = csv.reader(annual_return_file)
    annual_return = list(reader)
annual_return[0][0] = int(annual_return[0][0])
annual_return[1] = [float(num) for num in annual_return[1]]

with open('annual_inflation.csv', 'r') as annual_inflation_file:
    reader = csv.reader(annual_inflation_file)
    annual_inflation = list(reader)
annual_inflation[0][0] = int(annual_inflation[0][0])
annual_inflation[1] = [float(num) for num in annual_inflation[1]]

def annual_return_inflation(year_1, year_n):
    if (year_1 > year_n):
        return
    if year_1 < annual_return[0][0]:
        return
    if year_1 < annual_inflation[0][0]:
        return
    if year_n >= annual_return[0][0] + len(annual_return[1]):
        return
    if year_n >= annual_inflation[0][0] + len(annual_inflation[1]):
        return
    return annual_return[1][year_1-annual_return[0][0]:year_n-annual_return[0][0]+1],\
           annual_inflation[1][year_1-annual_inflation[0][0]:year_n-annual_inflation[0][0]+1]

def prod(r_i):
    n = len(r_i[0])
    p = [1] * (n+1)
    for m in range(0, n+1):
        for k in range(0, m):
            p[m] *= 1+r_i[1][k]
        for k in range(m, n):
            p[m] *= 1+r_i[0][k]
    return p

def compound(r_i):
    n = len(r_i[0])
    c = [1] * (2)
    for m in range(0, n):
        c[0] *= 1+r_i[0][m]
        c[1] *= 1+r_i[1][m]
    return c

def swr(year_1, year_n):
    p = prod(annual_return_inflation(year_1, year_n))
    w = 0
    for m in range(0, len(p)):
        w += p[m]
    return p[0] / w

def remaining_equity(initial_equitiy, inital_withdrawal_rate, year_1, year_n):
    p = prod(annual_return_inflation(year_1, year_n))
    e = 0;
    for m in range(0, len(p)):
        e += p[m]
    return initial_equity * (p[0] - initial_withdrawal_rate * e)

def remaining_equity_n(initial_equitiy, inital_withdrawal_rate, year_1, year_n):
    r_i = annual_return_inflation(year_1, year_n)
    e = initial_equity - initial_equity * initial_withdrawal_rate
    for m in range(0, year_n-year_1+1):
        p = 1
        for k in range(0, m+1):
            p *= 1+r_i[1][k]
        e = e * (1+r_i[0][m]) \
            - initial_equity * initial_withdrawal_rate * p
        print(str(year_1+m) + "    %11.2f" % e)
    return e

def print_swr(years):
    n = years - 1

    print("Year    Return    Inflation    SWR")
    for year in range(1928, 2021-n+1):
        c = compound(annual_return_inflation(year, year+10-1))
        print(str(year) + "    %6.2f    %6.2f    %6.2f    %6.2f    %6.2f    %6.2f" \
                % ((annual_return[1][year-annual_return[0][0]]*100), \
                   (annual_inflation[1][year-annual_inflation[0][0]]*100), \
                   c[0], c[1], c[0]/c[1], \
                   (swr(year, year+n-1)*100)))
    for year in range(2021-n+1, 2021+1):
        print(str(year) + "    %6.2f    %6.2f" \
                % ((annual_return[1][year-annual_return[0][0]]*100),\
                   (annual_inflation[1][year-annual_inflation[0][0]]*100)))

def print_cirr(years):
    print("Year      CIRR")
    for year in range(1928, 2021-years):
        c = compound(annual_return_inflation(year, year+years-1))
        print(str(year) + "    %6.2f" % (c[1]/c[0]))

initial_equity = 1000000
initial_withdrawal_rate = 0.04
year_1 = 1970
year_n = 1999
#print("Remaining equity")
#for m in range(year_1, year_n+1):
#    print(str(m) + "    %11.2f" % remaining_equity(initial_equity, initial_withdrawal_rate, year_1, m))
#remaining_equity_n(initial_equity, initial_withdrawal_rate, year_1, year_n)

#print_swr(30)
print_cirr(10)
