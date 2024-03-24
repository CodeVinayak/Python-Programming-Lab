medicaldata=[(25,'Male','Malaria'),(30,'Male','Typhoid'),(54,'Male','Sugar'),(26,'Female','Asthma'),(41,'Female','Cancer'),(45,'Male','ColdFlu'),(35,'Male','Malaria'),(32,'Male','ColdFlu'),(29,'Female','Sugar'),(65,'Male','Asthma'),(20,'Female','ColdFlu')]

count = {}
c_total_age = {}

total_age = 0
total_patients = len(medicaldata)

for age,gender,condition in medicaldata:
   total_age =  total_age + age
   if condition in count:
       count[condition] =  count[condition] + 1
       c_total_age[condition] = c_total_age[condition] +age
   else:
       count[condition] = 1
       c_total_age[condition] = age

average_age = total_age / total_patients
print("Name : Vinayak Kumar Singh \nRegister No: 23MCA1030")
print("Total Number of patients are:",total_patients)
print(f"Average Age of patients are: {average_age:.2f}")

for condition, count in count.items():
   print(f"Number of patients with {condition}: {count}")
