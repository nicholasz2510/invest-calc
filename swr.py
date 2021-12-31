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

def swr(year_1, year_n):
    p = prod(annual_return_inflation(year_1, year_n))
    w = 0
    for m in range(0, len(p)):
        w += p[m]
    return p[0] / w

print("Year    Return    Inflation    SWR")
years = 30-1
for year in range(1928, 2021-years+1):
    print(str(year) + "    %6.2f    %6.2f    %6.2f" \
            % ((annual_return[1][year-annual_return[0][0]]*100), \
               (annual_inflation[1][year-annual_inflation[0][0]]*100), \
               (swr(year, year+years-1)*100)))
for year in range(2021-years+1, 2021+1):
    print(str(year) + "    %6.2f    %6.2f" \
            % ((annual_return[1][year-annual_return[0][0]]*100),\
               (annual_inflation[1][year-annual_inflation[0][0]]*100)))
