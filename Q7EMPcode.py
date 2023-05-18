RUN NHI HO RHA ,KUCH GALTI HAI
def Newemp():
    import pickle
    with open("emp.dat", "ab") as f:
         ans = "y"
         while ans.lower() == "y":
            empno = int(input("Enter Employee Number :"))
            name = input("Enter the Name : ")
            post = input("Enter the Post : ")
            sal = int(input("Enter the Salary : "))
            lst = [empno, name, post, sal]
            pickle.dump(lst, f)
            print("Data saved!!")
            ans = input("Add more?y/n")
    with open("emp.dat","rb") as f:
        try:
            while True:
                r = pickle.load(f)
                print(r)
        except:
            pass
def sumsalary(post):
    import pickle
    count = 0
    with open("emp.dat","rb") as f:
        try:
            while True:
                r = pickle.load(f)
                if r[2] == post:
                    count += r[3]
                    print(r[3])

        except:
            pass
    print("sum of salaries of employees of the post is ",count)
Newemp()
sumsalary("l")
