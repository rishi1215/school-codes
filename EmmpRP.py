import pickle
with open("emp.dat", "wb") as f:
    ans = "y"
    while ans.lower() == "y":
        eid = int(input("Enter Employee ID: "))
        name = input("Enter Name of Employee : ")
        desg = input("Enter the Designation : ")
        sal = int(input("Enter the Salray : "))
        city = input("Enter the City :")
        dic = {"ID": eid, "Name": name,"Designation": desg, "Salary": sal, "City": city}
        pickle.dump(dic, f)
        ans = input("Add more?y/n ")
    with open("emp.dat", "rb") as f:
        try:
            while True:
                r = pickle.load(f)
                if r["Name"][0].lower() == "r" and r["Name"][-1].lower() == "p":
                    print(r)
        except:
            print("NO SUCH DATA FOUND")
