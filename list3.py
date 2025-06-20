


n=int(input("enter the no. of employee:"))
salary=[]

for i in range(n):
    employee_salary=int(input("enter the salary:"))
    salary.append(employee_salary)
print("original salaries:",salary)
def analyze_salaries(salary):
    highest=max(salary)
    lowest=min(salary)
    print("highest",highest)
    print("lowest",lowest)
    average=sum(salary)/len(salary)
    print("average:",round(average,2))
    count=0
    for employee_salary in salary: 
      if employee_salary>average:
         count+=1
    print("above average:",count)
    increased_salries=[]
    for s in salary:
       increasedSalary=0.10 *s
       new_salary=s+increasedSalary
       increased_salries.append(increasedSalary)
    print("incraesed salaries are:",new_salary)    
analyze_salaries(salary)