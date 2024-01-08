word = list (input())
glasn = 0
soglasn = 0
a = 0
e = 0
i = 0
o = 0
u = 0
for i in range (len (word)):
    if (word[i] == 'a') or (word[i] == 'e') or (word[i] == 'i') or (word[i] == 'o') or (word[i] == 'u'):
        glasn += 1
        if word[i] == 'a':
            a += 1
        elif word[i] == 'e':
            e += 1
        elif word[i] == 'i':
            i += 1
        elif word[i] == 'o':
            o += 1
        else:
            u +=1
    else:
        soglasn +=1
print ("Количество гласных букв:", glasn)
print ("Из них букв а: ", a)
print ("Из них букв e:", e)
print ('Из них букв i:', i)
print ('Из них букв o:', o)
print ('Из них букв u:', u)
print ('Количество согласных букв:', soglasn)