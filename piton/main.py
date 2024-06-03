try:
    from parcel_calculator import calculate_price
    from parcel_saver import save_parcel_details
except ImportError as e:
    print(f"Error importing module: {e}")
    exit(1)

# Get user input for parcel dimensions and weight
try:
    length = float(input("Enter parcel length in centimeters: "))
    width = float(input("Enter parcel width in centimeters: "))
    height = float(input("Enter parcel height in centimeters: "))
    weight = float(input("Enter parcel weight in kilograms: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit(1)

# Save parcel details to file
try:
    save_parcel_details(length, width, height, weight)
except Exception as e:
    print(f"Error saving parcel details: {e}")
    exit(1)

# Calculate parcel price using imported function
try:
    price = calculate_price(length, width, height, weight)
except Exception as e:
    print(f"Error calculating price: {e}")
    exit(1)

# Print parcel price to user
print("The price of your parcel is: $", price)