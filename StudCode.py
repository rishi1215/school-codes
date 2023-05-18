import pickle
with open("stud.dat", "wb") as f:
    ans = "y"
    while ans.lower() == "y":
        sid = int(input("Enter Student ID: "))
        name = input("Enter Name of Student : ")
        perc = int(input("Enter the Percentage :"))
        marks = int(input("Enter the Total Marks : "))
        dic = {"ID": sid, "Name": name, "Percentage": perc, "Total": marks}
        pickle.dump(dic, f)
        ans = input("Add more?y/n ")
with open("stud.dat", "rb") as f:
    try:
        while True:
            r = pickle.load(f)
            if r["Percentage"] > 50:
                print(r)
    except:
        print("NO STUDENT SCORED ABOVE 50%)")
