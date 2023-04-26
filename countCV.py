def count_c_v():
    z = open("data.txt", "w")
    z.write("""the quick brown fox jumps over the lazy dog
     the lazy dog is sleeping""")
    z.close()
    x = open("data.txt", "r")
    str1 = x.read()
    x.close()
    countv = 0
    countc = 0
    v = "aeiouAeIOU"
    c="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in str1:
        if i in v:
            countv += 1
        elif i in c:
            countc += 1
    print("NO. of vowels = ", countv)
    print("NO. of consonants = ", countc )
count_c_v()