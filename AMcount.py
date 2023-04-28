def AMcount():
   z = open("poem.txt", "w")
   x = z.write("function to count a aand m a in a strmMing including both the cases")
   z.close()
   p = open("poem.txt", "r")
   y = p.read()
   p.close()
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
