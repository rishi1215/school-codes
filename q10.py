def add_record():
    import pickle
    with open("stud.dat","wb") as f:
      ans = "y"
      while ans.lower() == "y":
          roll = int(input("Enter the roll number : "))
          name = input("Enter the Name : ")
          marks = int(input("Enter the marks : "))
          t = (roll,name,marks)
          pickle.dump(t,f)
          print("Data Saved!!")
          ans = input("Add more?y/n")
def search_record(rollno):
    import pickle
    with open("stud.dat","rb") as f:
        try:
            while True:
                    r = pickle.load(f)
                    if r[0] == rollno:
                        print(r)
        except:
            pass
add_record()
search_record()
