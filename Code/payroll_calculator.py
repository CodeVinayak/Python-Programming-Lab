class Employee:
    def __init__(self, emp_id, name, basic_pay):
        self.emp_id = emp_id
        self.name = name
        self.basic_pay = basic_pay

    def calculate_salary(self):
        # Constants for allowances and deductions percentages
        da_percentage = 0.8  # 80% of Basic Pay
        hra_percentage = 0.3  # 30% of Basic Pay
        pf_percentage = 0.12  # 12% of Basic Pay

        # Calculate DA, HRA, and PF
        da = self.basic_pay * da_percentage
        hra = self.basic_pay * hra_percentage
        pf = self.basic_pay * pf_percentage

        # Calculate total salary
        total_salary = self.basic_pay + da + hra - pf

        return total_salary

# Example usage:
employee1 = Employee(emp_id=1, name="John", basic_pay=50000)
salary1 = employee1.calculate_salary()

employee2 = Employee(emp_id=2, name="Jane", basic_pay=60000)
salary2 = employee2.calculate_salary()

print(f"Employee {employee1.name}'s Total Salary: {salary1} Rupees")
print(f"Employee {employee2.name}'s Total Salary: {salary2} Rupees")
