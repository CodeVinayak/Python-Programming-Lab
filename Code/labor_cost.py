def calculate_labor_cost(rate_per_hour, hours_worked):
    return rate_per_hour * hours_worked

def calculate_total_charge(rate_per_hour, hours_worked, cost_of_materials):
    labor_cost = calculate_labor_cost(rate_per_hour, hours_worked)
    total_charge = labor_cost + cost_of_materials
    return total_charge

# Example usage:
rate_per_hour = 45
hours_worked = 10
cost_of_materials = 500

labor_cost = calculate_labor_cost(rate_per_hour, hours_worked)
total_charge = calculate_total_charge(rate_per_hour, hours_worked, cost_of_materials)

print(f"Labour Cost: Rs.{labor_cost}/-")
print(f"Total Charge: Rs.{total_charge}/-")
