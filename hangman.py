import random 

words =["book" , "tree" , "python" , "bag" , "umbrell" , "dog" , "clock", "engineer" , "toothpaste", "shirmoz"]

word = random.choice(words)
joon = 10
kalame = len(word) 
while joon > 0 :
    print("-" * kalame)
    guess = input("kalame mored nazar khod ra hads bezanid: ").lower()
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