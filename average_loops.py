chosen_countries = ["France","Italy","Spain"]

country_costs = {
    "France":1000, "Italy":800,"Spain": 900,"Japan":1200
}

total_trip_cost = 0
for country in chosen_countries:
    total_trip_cost += country_costs[country]

average_cost_per_country = total_trip_cost /len(chosen_countries)
# Calculating the average cost

# Display the total cost and the average cost per country
print(f"The total cost of the trip is: ${total_trip_cost}")
print(f"The average cost per country is: ${average_cost_per_country:.2f}")