# TODO: Define a list named chosen_countries with countries selected for the road trip
chosen_countries = ["Spain","Italy","Portugal","UK"]
# TODO: Define a dictionary named country_fuel_costs with fuel costs for countries
country_fuel_costs = {
    "Spain": 500,"Italy":300,"Portugal":150,"UK":200}
# TODO: Initialize a variable total_fuel_cost to 0
total_fuel_costs = 0
# TODO: Use a for loop to add up the fuel cost for each chosen country
for country in chosen_countries:
    total_fuel_costs += country_fuel_costs[country]
    
    
    # TODO: Calculate the average fuel cost per country
average_fuel_costs = total_fuel_costs/len(chosen_countries)
# TODO: Print the total fuel cost for the road trip
print(f"The total fuel cost for the road trip is: {total_fuel_costs}")
# TODO: Print the average fuel cost per country
print(f"The average fuel cost per country is: {average_fuel_costs}")