# Car EMI Calculator

# Input statements
loan_amount = float(input("Enter the loan amount : "))
annual_interest_rate = float(input("Enter the annual interest rate : "))
loan_tenure_years = int(input("Enter the loan tenure (in years): "))

# Calculations
monthly_interest_rate = annual_interest_rate / (12 * 100)  # Convert annual rate to monthly
loan_tenure_months = loan_tenure_years * 12  # Convert years to months

# EMI formula: EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_tenure_months) / \
      ((1 + monthly_interest_rate) ** loan_tenure_months - 1)

# Output the result
print(f"\nYour monthly EMI is: ₹{emi:.2f}")
