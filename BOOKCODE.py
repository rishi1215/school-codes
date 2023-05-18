def createfile():
    import pickle
    with open("Book.dat","wb") as f:
        ans = "y"
        while ans.lower() == "y":
            bookn = int(input("Enter the Book Number : "))
            name = input("Enter the Book Name : ")
            Auth = input("Who is the Author? ")
            prc = int(input("Enter the Price : "))
            dic = {"Book No.": bookn, "Book Name": name, "Author": Auth, "Price": prc}
            pickle.dump(dic, f)
            ans = input("Add more?y/n ")
def countrec(Author):
    import pickle
    count = 0
    with open("Book.dat", "rb") as f:
        try:
            while True:
                r = pickle.load(f)
                if r["Author"] == Author:
                    count += 1
        except :
            pass
    print("Number of Books Given by", Author, "are", count)
