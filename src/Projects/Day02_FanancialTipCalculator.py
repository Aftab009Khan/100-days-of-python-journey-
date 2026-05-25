# 1. Gather inputs from the user
print("Welcome to the Tip Calculator!")

bill_total = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? (e.g., 15, 18, 20): "))

number_of_people = int(input("How many people are splitting the bill? "))

# Convert the tip percentage
tip_multiplier = tip_percentage / 100
total_tip_amount = bill_total * tip_multiplier

# Add the tip to the original bill to find the grand total

grand_total = bill_total + total_tip_amount

amount_per_person = grand_total / number_of_people

# 3. Display the results
# The round() function limits our final answer to exactly 2 decimal places
final_amount = round(amount_per_person, 2)

print("\n--- Results ---")
print("Each person should pay: $" + str(final_amount))
