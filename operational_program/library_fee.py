library_fee = int(input("Enter the library fee: "))

delayed_days = int(input("Enter the number of delayed days: "))

fine_per_day = 50

total_fine = delayed_days * fine_per_day

total_amount = library_fee + total_fine

print("The total amount to be paid is:", total_amount)