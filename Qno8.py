def SCOUNT():
    import pickle
    with open("NAMES.DAT","wb") as f:
      ans = "y"
      while ans.lower() == "y":
         name = input("Enter the Name : ")
         pickle.dump(name,f)
         ans = input("Add more?y/n")
    with open("NAMES.DAT","rb") as f:
        count = 0
        try:
            while True:
                r = pickle.load(f)
                if r[0].lower() == "s":
                    count +=1
        except:
            pass
    print("Total Names Begging from S are : ",count)
                    
SCOUNT()
