import matplotlib.pyplot as plt

# This is pretty much only for me since I don't pay rent at home. 
# Use case. Don't use it :)
# I'm using it to calculate how much it will cost me for x years AND
# How much I lose on rent on the loan. (since I can pay less if I save)

AMOUNT_SAVED = 500000 # How much you have year 0.
STARTING_DEBT = 1500000 # How much you would have to lend at the start
LIVING_COSTS_IN_APARTMENT = 7000 # Per month
LOAN_INTEREST_RATE = 0.04 # Per year
INCOME_PER_YEAR = 210000 # what you save
MARKET_RETURN_RATE = 1.07 # Stock market
YEARS_TO_COMPARE = 10


starting_debt_year_0 = STARTING_DEBT - AMOUNT_SAVED
starting_debt_year_1 = STARTING_DEBT - (AMOUNT_SAVED * MARKET_RETURN_RATE + INCOME_PER_YEAR)
starting_debt_year_2 = STARTING_DEBT - (AMOUNT_SAVED * (MARKET_RETURN_RATE**2) + INCOME_PER_YEAR * MARKET_RETURN_RATE + INCOME_PER_YEAR)

list_of_years = [starting_debt_year_0, starting_debt_year_1, starting_debt_year_2]
final_list = []

for current_debt in list_of_years:
    total_cost_list = []
    current_calculated = 0
    for year in range(YEARS_TO_COMPARE):
        current_calculated += current_debt * LOAN_INTEREST_RATE
        current_calculated += LIVING_COSTS_IN_APARTMENT * 12
        current_debt -= INCOME_PER_YEAR - (LIVING_COSTS_IN_APARTMENT * 12)
        if current_debt < 0:
            current_debt = 0
        total_cost_list.append(current_calculated)
    final_list.append(total_cost_list)


# Plot each scenario as a line on the same graph
for index, cost_list in enumerate(final_list):
    plt.plot(range(1, YEARS_TO_COMPARE + 1), cost_list, label=f"Buy Year {index}")

plt.xlabel('Year')
plt.ylabel('Total Cost')
plt.title('Total Cost Over Time for Different Scenarios')
plt.ticklabel_format(style='plain', axis='y')
plt.legend()
plt.grid(True)
plt.show()

money_saved_on_rent_list = [[],[]]
for index in range(YEARS_TO_COMPARE):
    money_saved_on_rent_list[0].append(final_list[0][index] - final_list[1][index])
    money_saved_on_rent_list[1].append(final_list[0][index] - final_list[2][index])
print(money_saved_on_rent_list)

for index, saved_list in enumerate(money_saved_on_rent_list):
    plt.plot(range(1, YEARS_TO_COMPARE + 1), saved_list, label=f"Buy Year {index + 1}")

plt.xlabel('Year')
plt.ylabel('Total saved on rent')
plt.title('Total saved Over Time for Different Scenarios')
plt.ticklabel_format(style='plain', axis='y')
plt.legend()
plt.grid(True)
plt.show()