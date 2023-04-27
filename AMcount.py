def AMcount():
   z = open("poem.txt", "w")
   x = z.write("function to count a and m a in a strmMing including both the cases")
   z.close()
   op = open("poem.txt", "r")
   y = op.read()
   op.close()
   countA, countM = 0,0 
   for i in y:
       if i.isalpha():
           if i in "aA" :
               countA+=1
           elif i in "mM" :
               countM+=1
   print("A or a = ", countA)
   print("M or m = ", countM)
AMcount()
