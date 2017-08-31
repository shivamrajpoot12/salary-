
gen = input("enter the gender")
salary = int(input("Enter the salary"))
if(salary>=2000):
     if(gen=='male'):
        bonus = int(5*salary/100)
        salary =salary+bonus
        print("new salary with bonus",salary)
     if(gen=='female'):
        bonus = int(10*salary/100)
        salary =salary+bonus
        print("new salary with bonus",salary)
elif(salary<2000):        
    if(gen=='male'):
        bonus = int(7*salary/100)
        salary =salary+bonus
        print("new salary with bonus",salary)
    if(gen=='female'):
        bonus = int(12*salary/100)
        salary =salary+bonus
       