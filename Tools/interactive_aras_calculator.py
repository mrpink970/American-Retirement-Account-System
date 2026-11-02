# ARAS Interactive Retirement Calculator
# This script asks the user for their inputs and calculates their ARAS retirement balance and monthly income.

def get_float_input(prompt, default):
    user_input = input(f"{prompt} (default: {default}): ")
    if user_input.strip() == "":
        return default
    try:
        return float(user_input)
    except ValueError:
        print("Invalid input. Using default.")
        return default

def calculate_aras_retirement():
    print("=========================================")
    print("   ARAS Retirement Calculator (v1.0)")
    print("=========================================")
    print("Press Enter to use the default values.\n")

    # 1. Gather Inputs
    starting_salary = get_float_input("Enter your starting annual salary ($)", 50000)
    annual_salary_growth = get_float_input("Enter expected annual salary growth (e.g., 0.03 for 3%)", 0.03)
    years_worked = get_float_input("Enter number of years you will work", 40)
    market_return = get_float_input("Enter expected stock market return (e.g., 0.07 for 7%)", 0.07)
    bond_return = get_float_input("Enter expected bond return (e.g., 0.03 for 3%)", 0.03)
    
    print("\n--- Cohort Selection ---")
    print("Which cohort are you in?")
    print("1. Age 20 or younger (100% private account)")
    print("2. Age 21-25 (90% private account)")
    print("3. Age 26-30 (80% private account)")
    print("4. Age 31-35 (60% private account)")
    print("5. Age 36-40 (40% private account)")
    print("6. Age 41-45 (20% private account)")
    print("7. Age 46-50 (10% private account)")
    
    cohort_choice = input("Enter choice (1-7, default: 1): ")
    cohort_map = {
        "1": 1.00, "2": 0.90, "3": 0.80, "4": 0.60,
        "5": 0.40, "6": 0.20, "7": 0.10
    }
    cohort_private_pct = cohort_map.get(cohort_choice, 1.00)

    # 2. Simulation
    print("\nCalculating...")
    
    balance = 0.0
    current_salary = starting_salary
    total_payroll_tax = 0.124
    
    for year in range(int(years_worked)):
        annual_contribution = current_salary * total_payroll_tax * cohort_private_pct
        balance = (balance + annual_contribution) * (1 + market_return)
        current_salary *= (1 + annual_salary_growth)
        
    # 3. Drawdown Phase
    blended_drawdown_return = (0.80 * bond_return) + (0.20 * market_return)
    months_in_retirement = (90 - 62) * 12
    monthly_rate = blended_drawdown_return / 12
    
    if monthly_rate == 0:
        monthly_withdrawal = balance / months_in_retirement
    else:
        monthly_withdrawal = balance * (monthly_rate / (1 - (1 + monthly_rate) ** -months_in_retirement))

    # 4. Output
    print("\n=========================================")
    print("              YOUR RESULTS               ")
    print("=========================================")
    print(f"Balance at Age 62:        ${balance:,.2f}")
    print(f"Estimated Monthly Check:  ${monthly_withdrawal:,.2f}")
    print(f"Estimated Annual Income:  ${monthly_withdrawal * 12:,.2f}")
    print("=========================================")
    print("\nNote: This is a simplified projection. It does not include inflation, taxes on the legacy check, or the Floor Reserve backstop.")

if __name__ == "__main__":
    calculate_aras_retirement()
