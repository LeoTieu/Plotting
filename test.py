import matplotlib.pyplot as plt

# This script is to show ME how much I would save if I wait x years from buying an apartment
# So this only works for people that are in my shoes :), aka living home without paying rent 

AMOUNT_SAVED = 500000 # How much you have year 0.
STARTING_DEBT = 1500000 # How much you would have to lend at the start
APARTMENT_FEES = 3000
INCOME_PER_YEAR = 210000 # what you save
MARKET_RETURN_RATE = 1.07 # Stock market, bank

starting_debt_year_0 = STARTING_DEBT - AMOUNT_SAVED
starting_debt_year_1 = STARTING_DEBT - (AMOUNT_SAVED * MARKET_RETURN_RATE + INCOME_PER_YEAR)
starting_debt_year_2 = STARTING_DEBT - (AMOUNT_SAVED * (MARKET_RETURN_RATE**2) + INCOME_PER_YEAR * MARKET_RETURN_RATE + INCOME_PER_YEAR)

list_of_years = [starting_debt_year_0, starting_debt_year_1, starting_debt_year_2]

years = [0, 1, 2]

plt.plot(years, list_of_years, marker='o')
plt.xlabel('Years Waiting Before Buying')
plt.ylabel('Starting Debt')
plt.title('Starting Debt vs Years Waiting')
plt.grid(True)
plt.show()



YEARS_TO_COMPARE = 10

def calculate_savings(years, initial, yearly, rate):
    total = initial
    for i in range(years):
        total = total * rate + yearly
    return total

years = list(range(YEARS_TO_COMPARE + 1))
starting_debts = []

for y in years:
    savings = calculate_savings(y, AMOUNT_SAVED, INCOME_PER_YEAR, MARKET_RETURN_RATE)
    debt = STARTING_DEBT - savings
    starting_debts.append(debt)

plt.plot(years, starting_debts, marker='o')
plt.xlabel('Years Waiting Before Buying')
plt.ylabel('Starting Debt')
plt.title('Starting Debt vs Years Waiting')
plt.grid(True)
plt.show()