# Python program for quiz

import random

d={"Who invented ball-point pen?":"László Bíró",
   "Who invented radio?":"Guglielmo Marconi",
   "Who is known as the 'Father of Chemistry'?":"Antoine  Lavoisier",
   "Who discovered electricity?": "Benjamin Franklin",
   "Who invented air conditioner?":"Willis Carrier",
   "Who invented the number '0'?": "Aryabhatta",
   "Who is known as the 'Father of Artificial Intelligence'?":"John McCarthy",
   "Who discovered gravity?": "Sir Isaac Newton",
   "Who invented computer?":"Charles Babbage",
   "Who invented telephone?":"Alexander Graham Bell",
   "Who is known as the 'Father of Genetics'?":"Gregor Mendel",
   "Who invented the USB?":"Ajay Bhatt",
   "Who is known as the 'Father of Plastic Surgery'?":"Sushruta",
   "Who discovered penicillin?": "Alexander Fleming",
   "Who invented the gramophone?":"Thomas Alva Edison",
   "Who invented the 'Spinning Jenny'?":"James Hargreave"}

ques= list(d.keys())
opt= list(d.values())
score= 0
#print(ques),print(opt)
n=0

def quiz(x):
    global d
    i= random.randint(0,len(x)-1)
    print(x[i])
    ans= d[x[i]]
    return ans

def options(x):

    global opt
    dict_options= {}
    l= opt
    for a in l:
        if a==x:
            l.remove(a)
        else:
            pass
    l=random.sample(l,3)
    i= random.randint(0,len(l)-1)
    l.insert(i,x)
    random.shuffle(l)
    for j in range(len(l)):
        print(j+1,".", l[j])
        dict_options[j+1]= l[j]
    l.clear()
    return dict_options

while(n<5):
    print("\n\n===================================================\n\n")
    q= quiz(ques)
    print("\n")
    o= options(q)
    print("\n\n===================================================\n\n")
    try:
        a= int(input("Enter your answer(1-4): "))
        if o[a]==q:
            print("\nCorrect answer!!")
            score+=10
            print("\nScore: ", score)
            print("\n")
        else:
            print("\nSorry! Wrong answer.\n\nThe correct answer is: ", q)
            score-=5
            print("\nScore: ", score)
            print("\n")
    except (ValueError, IndexError, KeyError):
        print("Sorry! Invalid input")
        score-=1
        print("\nScore: ", score)
        print("\n")
    n= n+1

print("\n\n==============================================\n\n")

print("\n\nThe quiz ends.\n")
print("Your final score is: ",score)

print("\n\n==============================================\n\n")




"""
        Developed By:        Jivesh Singh
        College:             SRM University, Delhi-NCR
        Registration No.:    10316210048
        E-mail      :        jiveshs98@hotmail.com

"""
