import pickle

with open("dvd.dat", "wb") as f:
    ans = "y"
    while ans.lower() == "y":
        did = int(input("Enter DvD ID: "))
        name = input("Enter Name of DvD : ")
        qty = int(input("Enter the Quantity :"))
        price = int(input("Enter the Price : "))
        dic = {"ID": did, "Name": name, "Quantity": qty, "Price": price}
        pickle.dump(dic, f)
        ans = input("Add more?y/n ")
with open("dvd.dat", "rb") as f:
    try:
        while True:
            r = pickle.load(f)
            if r["Price"] > 25:
               print(r)
    except:
        pass
