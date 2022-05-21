.Astro
#0654

.Astro — 04/29/2022
alr lmk when
Yeti — 04/29/2022
Ok I've just got home, let's call at 12?
.Astro — 04/29/2022
can we do it at 1
Yeti — 04/30/2022
hahhaah sure
ill take a look at the prompts till then
.Astro
 started a call that lasted an hour.
 — 04/30/2022
.Astro — 04/30/2022
https://www.dcode.fr/en
Yeti — 04/30/2022
https://github.com/SohamNagi/Hackathon-Deerhacks-Project.git
GitHub
GitHub - SohamNagi/Hackathon-Deerhacks-Project
Contribute to SohamNagi/Hackathon-Deerhacks-Project development by creating an account on GitHub.
GitHub - SohamNagi/Hackathon-Deerhacks-Project
.Astro — 04/30/2022
https://www.youtube.com/watch?v=A2ceblXTBBc
YouTube
Visual Studio Code
Remote collaboration in Visual Studio Code
Image
Yeti — 04/30/2022
https://prod.liveshare.vsengsaas.visualstudio.com/join?EAC5219FA92DBD2AB0DD5D0B57BD639254FC
Visual Studio Code for the Web
Build with Visual Studio Code, anywhere, anytime, entirely in your browser.
https://prod.liveshare.vsengsaas.visualstudio.com/join?B24E4F2D16210B1D5E2AC50546C09AA7822A
Visual Studio Code for the Web
Build with Visual Studio Code, anywhere, anytime, entirely in your browser.
Yeti — 04/30/2022
https://docs.google.com/spreadsheets/d/1m96o7bWC5qqLHLdyFSfHhfd98aPut_pusOeJIGMbSbI/edit?usp=sharing
Google Sheets - create and edit spreadsheets online, for free.
Create a new spreadsheet and edit with others at the same time -- from your computer, phone or tablet. Get stuff done with or without an internet connection. Use Sheets to edit Excel files. Free from Google.
.Astro — 04/30/2022
wanna start working on cs?
Yeti — 04/30/2022
just finishing up lunch
.Astro — 04/30/2022
bruh im leaving to get a phone rn
moms in the car and everythin
Yeti — 04/30/2022
We'll work later then
.Astro — 04/30/2022
these mans took way too long to transfer data
id be down to get on now but ill have to go eat at like 8
so u wanna call at 930 or now?
either way i delayed this bare so ill be staying up late to work on it
Yeti — 04/30/2022
Yeah let's do 9.30
.Astro — 04/30/2022
call?
Yeti — 04/30/2022
Now I'm eating dinner 🤣
.Astro — 04/30/2022
nw lmk when ur done
Yeti — 04/30/2022
aight should we work
.Astro
 started a call that lasted 4 hours.
 — 04/30/2022
Yeti — 04/30/2022
Attachment file type: acrobat
math135notes.pdf
956.35 KB
https://prod.liveshare.vsengsaas.visualstudio.com/join?B24E4F2D16210B1D5E2AC50546C09AA7822A
Visual Studio Code for the Web
Build with Visual Studio Code, anywhere, anytime, entirely in your browser.
.Astro — 04/30/2022
Image
Image
Yeti — 04/30/2022
Image
.Astro — 05/01/2022
https://www.youtube.com/watch?v=zoCBaxRweU4&t=49s
YouTube
Reenu Math
What Are Co-Prime  Numbers / Co-Prime Numbers
Image
Yeti — 05/01/2022
https://prod.liveshare.vsengsaas.visualstudio.com/join?7185934DD7724A0C9F19441EC9F30E5B79C7
Visual Studio Code for the Web
Build with Visual Studio Code, anywhere, anytime, entirely in your browser.
.Astro — 05/01/2022
https://deerhacks.devpost.com/
DeerHacks
DeerHacks
Join us for UTM's Largest Hackathon!
Image
Yeti — 05/01/2022
from math import floor
from math import gcd
import math

def next_row(row1, row2):
    q = floor(row1[2]/row2[2])
    a= row1[0]- (q * row2[0])
    b = row1[1]- (q * row2[1])
    r = row1[2]- (q * row2[2])
    new_row = [a,b,r,q]
    return new_row

def eea(x,y):
    headers = ["a","b","r","q"]
    block = ["---","---","---","---"]
    block2 = ["-----","-----","-----","-----"]
    row_1 = [1,0, x ,0]
    row_2 = [0,1, y ,0]
    data = [block, headers,block,row_1,row_2]
    a=3
    b=4    
    while(True):
        new_row =  next_row(data[a], data[b])
        data.append(new_row)
        a += 1
        b += 1
        if (new_row[2] == 0):
            data.append(block)
            break
        
    for row in data:
        print('| {:^5} | {:^5} | {:^5} | {:^5} |'.format(*row))
    return data[b-1]     

def LDE(a,b, c):
    if ((c % gcd(a,b)) != 0):
        print("A solution does not exist!")
    else:
        row = eea(a,b)
        cd = c/gcd(a,b)
        out_a = row[0]*cd
        out_b = row[1]*cd
        print(out_a,"a + ",out_b, "b = ", c)

def prime(p):
    prime=False
    if (int(p)==2 or int(p)==1):
        prime=False
    for number in range(2, int(p)):
        val=int(p)/int(number)
        if val.is_integer():
            prime=True
            break
    if (prime==True):
        print(p,"num is not prime")
        return False
    else:
        print(p,"num is prime")
        return True
#prime(3)
#prime(100)
#prime(43)
def prime_factor(fpf):
    pflst=[]
    for number in range(2, math.ceil(math.sqrt(fpf))):
        val=int(fpf)/int(number)
        if val.is_integer() and prime(number)==True:
            pflst.append(number)
    print("The prime factors for", fpf,"are: ",pflst)
    return pflst

def print_factors(x):
   retval=[]
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           retval.append(i)
   print("The factors for", x,"are: ",retval)
   return retval
#print_factors(10)

def coprime(x,y):
    x_factors=print_factors(x)
    y_factors=print_factors(y)
    same=0
    for elem in x_factors:
        if elem in y_factors:
            same=same+1
    if same==1:
        print(x,"and", y, "are coprime")
        return True
        
    else:
        print(x,"and", y, "are not coprime")
        return False

#coprime(9,90)

def remainder(big,small):
    print("The remainder of", big, "and",small,"is",int(big)%int(small))
... (53 lines left)
Collapse
Calculator.py
6 KB
.Astro — 05/01/2022
Image
.Astro — 05/11/2022
yo i got 5
u think u could link 3a
Yeti — 05/11/2022
Image
.Astro — 05/11/2022
Image
also did u get the same shit for 1
Image
rlly dont wanna lose these free marks
Yeti — 05/11/2022
f is inc if approved
https://learn.uwaterloo.ca/d2l/le/content/804195/viewContent/4383412/View
c is 8 and 10 from this site
.Astro — 05/11/2022
i was using this one but i think urs is prolly better cuz its specific to crowdmark
Image
.Astro — 05/11/2022
for f would it even be possible for inc to be considered cuz of the crowdmark portion?
Image
Image
Yeti — 05/11/2022
ohhhh that's true
Yeti — 05/11/2022
I've solved 5  too, just got 4c left at this point
.Astro — 05/11/2022
same
for 2b did u get 480i?
Yeti — 05/11/2022
yes
.Astro — 05/15/2022
yo how r u studying for econ?
reading slides makes me wanna kms
Yeti — 05/15/2022
I haven't started studying yet 💀💀
.Astro — 05/15/2022
bruh
.Astro — 05/18/2022
yo have u started the math assignment?
Yeti — 05/18/2022
yeah doing it rn
stuck on q2
.Astro — 05/18/2022
a or b?
Yeti — 05/18/2022
a
I hate this course so much 🥲
.Astro — 05/18/2022
since l is orthogonal its the normal aswell
so u can use (-5,2,0) as the normal to find the sclar equation
orthogonal to the plan so its the normal
and for vector i used the 3 point strat
i can send u my work if u want
Yeti — 05/18/2022
x = (-5,1,0) + t(L)? basically?
.Astro — 05/18/2022
maybe
Yeti — 05/18/2022
yes id appreciate that, struggling to wrap my head aeound this
.Astro — 05/18/2022
i used a diff order so idk if the same algebraicilly
one sec
Image
lmk if i did smtg wrong
also obv use diff numbers for the points so we dont get caught
any random points work
j dont make them all parrallel
Yeti — 05/18/2022
Image
here's what online grapher says
scalar equation should be -5x+2y = 27 then
which is what you got i think
Yeti — 05/18/2022
i get the logic for this, just not sure how to EXACTLY do it in a way where they dont rape me in markihg
.Astro — 05/18/2022
wouldnt it be (3,0,7)
Yeti — 05/18/2022
yes although that didnt change the answer
.Astro — 05/18/2022
weird for me it did
Image
did i do it wrong?
Yeti — 05/18/2022
no?
n = (-5,2,0)
we want a plane perp to n which contains the given point
https://discord.com/channels/842207080626389012/887443926280204370/976656959392591873
Yeti — 05/18/2022
https://www.emathhelp.net/en/linear-algebra-calculator/ - Vector calc which works with complex numbers as well

https://www.geogebra.org/calculator ---- 3D desmos - check answers
Linear Algebra Calculator - eMathHelp
Calculator that answers your linear algebra problems for free and with steps shown
Calculator Suite - GeoGebra
.Astro — 05/18/2022
yo how much r u done so far?
im almost done
Yeti — 05/18/2022
im stuck on 2a, need to convert the scalar into vector form
prolly gonna need to stay up all night
.Astro — 05/18/2022
ah alr
﻿
from math import floor
from math import gcd
import math

def next_row(row1, row2):
    q = floor(row1[2]/row2[2])
    a= row1[0]- (q * row2[0])
    b = row1[1]- (q * row2[1])
    r = row1[2]- (q * row2[2])
    new_row = [a,b,r,q]
    return new_row

def eea(x,y):
    headers = ["a","b","r","q"]
    block = ["---","---","---","---"]
    block2 = ["-----","-----","-----","-----"]
    row_1 = [1,0, x ,0]
    row_2 = [0,1, y ,0]
    data = [block, headers,block,row_1,row_2]
    a=3
    b=4    
    while(True):
        new_row =  next_row(data[a], data[b])
        data.append(new_row)
        a += 1
        b += 1
        if (new_row[2] == 0):
            data.append(block)
            break
        
    for row in data:
        print('| {:^5} | {:^5} | {:^5} | {:^5} |'.format(*row))
    return data[b-1]     

def LDE(a,b, c):
    if ((c % gcd(a,b)) != 0):
        print("A solution does not exist!")
    else:
        row = eea(a,b)
        cd = c/gcd(a,b)
        out_a = row[0]*cd
        out_b = row[1]*cd
        print(out_a,"a + ",out_b, "b = ", c)

def prime(p):
    prime=False
    if (int(p)==2 or int(p)==1):
        prime=False
    for number in range(2, int(p)):
        val=int(p)/int(number)
        if val.is_integer():
            prime=True
            break
    if (prime==True):
        print(p,"num is not prime")
        return False
    else:
        print(p,"num is prime")
        return True
#prime(3)
#prime(100)
#prime(43)
def prime_factor(fpf):
    pflst=[]
    for number in range(2, math.ceil(math.sqrt(fpf))):
        val=int(fpf)/int(number)
        if val.is_integer() and prime(number)==True:
            pflst.append(number)
    print("The prime factors for", fpf,"are: ",pflst)
    return pflst

def print_factors(x):
   retval=[]
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           retval.append(i)
   print("The factors for", x,"are: ",retval)
   return retval
#print_factors(10)

def coprime(x,y):
    x_factors=print_factors(x)
    y_factors=print_factors(y)
    same=0
    for elem in x_factors:
        if elem in y_factors:
            same=same+1
    if same==1:
        print(x,"and", y, "are coprime")
        return True
        
    else:
        print(x,"and", y, "are not coprime")
        return False

#coprime(9,90)

def remainder(big,small):
    print("The remainder of", big, "and",small,"is",int(big)%int(small))
    return int(big)%int(small)
#remainder(15,4)
import time

print('''
  _      _                                  _            _                 __    _____      _            _       _             
 | |    (_)                           /\   | |          | |               /_ |  / ____|    | |          | |     | |            
 | |     _ _ __   ___  __ _ _ __     /  \  | | __ _  ___| |__  _ __ __ _   | | | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    | | '_ \ / _ \/ _` | '__|   / /\ \ | |/ _` |/ _ \ '_ \| '__/ _` |  | | | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |____| | | | |  __/ (_| | |     / ____ \| | (_| |  __/ |_) | | | (_| |  | | | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |______|_|_| |_|\___|\__,_|_|    /_/    \_\_|\__, |\___|_.__/|_|  \__,_|  |_|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                               __/ |                                                                           
                                              |___/                                                                            
    ''')
while (True):
    time.sleep(3)
    val=int(input('''Input 1 for gcd\nInput 2 for Extended Euclidean Table\nInput 3 for Prime Number Checker\nInput 4 for Linear Diophantine Equation Solver\nInput 5 for Prime Factor List\nInput 6 for Factor List\nInput 7 for Remainder Calculator\nInput 8 for Coprime Checker\nInput 9 for Modulus Calculator\nInput 10 to Quit\nInput:'''))
    if(val == 1):
        num1 = int(input("What's your first number: "))
        num2 = int(input("What's your second number: "))
        print("The gcd for your numbers is:", gcd(num1,num2))
    elif (val == 2):
        num1 = int(input("What's your first number: "))
        num2 = int(input("What's your second number: "))
        eea(num1,num2)
    elif (val == 3):
        num1 = int(input("What's your number: "))
        prime(num1)
    elif (val == 4):
        num1 = int(input("What's your a value: "))
        num2 = int(input("What's your b value: "))
        num3 = int(input("What's your c value: "))
        LDE(num1,num2,num3)
    elif (val == 5):
        p=int(input("Integer:"))
        prime_factor(p)
    elif (val == 6):
         num1 = int(input("What's your number: "))
         print_factors(num1)
    elif (val == 7):
       num1 = int(input("What's your bigger number: "))
       num2 = int(input("What's your smaller number: "))
       print("The remainder for your numbers is:", remainder(num1,num2)) 
    elif (val == 8):
        num1 = int(input("What's your first number: "))
        num2 = int(input("What's your second number: "))
        coprime(num1,num2)
    elif (val == 9):
        num1 = int(input("x=a(mod y)\na: "))
        num2 = int(input("y: "))
        print("x:", remainder(num1,num2)) 
    elif val == 10:
        break
Calculator.py
6 KB
