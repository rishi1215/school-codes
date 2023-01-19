names=[]
salary=[]
emp_dict={'empname':names,'salary':salary}
choice=1
while choice!=0:
    print("1.Add Employee Detail")
    print("2. Show All Employee Detail")
    print("3. Search Employee")
    print("0. Quit")
    choice=int(input("enter your choice:"))
    if choice ==1:
        name=input("Enter name")
        sal=int(input("Enter salary"))
        names.append(name)
        salary.append(sal)
    elif choice ==2:
        print("***************EMPLOYEE DETAILS**************")
        print("%20s"%"name","%10s"%"salary")
        print("----------------------------------------------------------------------------------")
        n=emp_dict['empname']
        s=emp_dict['salary']
        for i in range(len(n)):
            print("%20s"%n[i],"%10s"%s[i])
        print("----------------------------------------------------------------------------------")
    elif choice==3:
        print("Enter name to search: ")
        name=input("Enter name")
        n=emp_dict['empname']
        s=emp_dict['salary']
        try:
            pos=n.index(name)
            print("## RECORD FOUND##")
            print("salary: ",s[pos])
        except:
            print("##NAME NOT IN THE RECORD##")
