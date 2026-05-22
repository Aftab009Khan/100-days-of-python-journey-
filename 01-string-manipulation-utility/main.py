print("=========================================")
print("  WELCOME TO THE UTILITY NAME GENERATOR  ")
print("=========================================\n")

# Prompt user for data points with trailing whitespace sanitation
city_input = input("Enter the city you grew up in:\n").strip()
pet_input = input("Enter the name of a memorable pet:\n").strip()

# Input Validation Layer: Ensures application does not process blank inputs
if city_input == "" or pet_input == "":
    print("\n❌ Error: Inputs cannot be empty. Please restart the script.")
else:
    # Title-case transformation for standardized output aesthetics
    generated_brand_name = f"{city_input.title()} {pet_input.title()}"
    
    print("\n=========================================")
    print(f"🚀 Your Generated Brand Identity: {generated_brand_name}")
    print("=========================================")
  
