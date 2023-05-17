import pickle
with open("stud.dat", "wb") as f:
    ans = "y"
    while ans.lower() == "y":
        eid = int(input("Enter Student ID: "))
        name = input("Enter Name of Student : ")
        city = int(input("Enter the City :"))
        dic = {"ID": eid, "Name": name, "City": city}
        pickle.dump(dic, f)
        ans = input("Add more?y/n ")
with open("stud.dat", "rb") as f:
    try:
        while True:
            r = pickle.load(f)
            if r["Name"][0].lower() == "r" and r["Name"][-1].lower() == "p":
                print(r)
    except:
        pass
