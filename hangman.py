
import random 
words =["book" , "tree" , "python" , "bag" , "umbrell" , "dog" , "clock", "engineer" , "toothpaste", "shirmoz"]
word = random.choice(words)
joon = 10
kalame = len(word) 
x = print("-" * kalame)
while joon > 0 :
    guess = input("kalame mored nazar khod ra hads bezanid: ").lower()
    for a in word:
        if a == guess:
         print(a, end="")

        else:
             print("-" , end= "")

    if guess in word:
        print('correct')
        kalame = kalame - 1 
        
        if kalame == 0 :
            print('you win')
            break
    else:
        joon = joon - 1 
        print("no")

print(word)