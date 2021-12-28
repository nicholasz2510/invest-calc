import csv
import matplotlib.pyplot as plt

annual_yield = []
annual_inflation = []
with open('annual_inflation.csv', 'r') as annual_inflation_file:
    reader = csv.reader(annual_inflation_file)
    for row in reader:
        annual_inflation = [float(num) for num in row]
with open('annual_yield.csv', 'r') as annual_yield_file:
    reader = csv.reader(annual_yield_file)
    for row in reader:
        annual_yield = [float(num) for num in row]

# print(annual_inflation)
# print(annual_yield)
# annual_inflation = annual_inflation[1990 - 1930:]
# annual_yield = annual_yield[1990 - 1930:]


def remaining_investment(investment, expense, years):
    curr_invest = investment
    curr_expense = expense
    for year in range(years):
        curr_invest -= curr_expense
        curr_invest *= 1 + annual_yield[year]
        curr_expense *= 1 + annual_inflation[year]
    return curr_invest


def show_results(investment, expense, years):
    remaining_invest = remaining_investment(investment, expense, years)
    print("\nRemaining investment: " + str(int(remaining_invest)))
    print("Initial withdrawal ratio: " + str(expense / investment))
    print("Remaining investment ratio: " + str(int(remaining_invest) / investment))
    print()


def get_withdrawal_amount(investment, years):
    try_expense = 0
    while remaining_investment(investment, try_expense, years) > 0:
        try_expense += 1
    return try_expense
    # show_results(300, expense, 5)


# initial_withdrawal_amount = get_withdrawal_amount(300, 30)
# print("Initial withdrawal amount: " + str(initial_withdrawal_amount))
# show_results(300, initial_withdrawal_amount, 30)

withdrawal_ratios = []

investment = 1000000
years = 30
print("Year | initial withdrawal ratio")
for year in range(1930, 1980):
    withdrawal_ratio = get_withdrawal_amount(investment, years) / investment
    print(str(year) + " | " + str(withdrawal_ratio))
    withdrawal_ratios.append(withdrawal_ratio)

    annual_inflation = annual_inflation[1:]
    annual_yield = annual_yield[1:]

print("\nAverage initial withdrawal ratio = " + str(sum(withdrawal_ratios) / len(withdrawal_ratios)))
fig, ax = plt.subplots()
ax.set_title('Boxplot of Withdrawal Ratios')
ax.boxplot(withdrawal_ratios, patch_artist=True, medianprops=dict(color='black'), boxprops=dict(facecolor='w'), vert=False)

plt.show()
