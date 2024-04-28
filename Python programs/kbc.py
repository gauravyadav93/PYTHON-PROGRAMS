question = [["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],
            ["what is our national animal ?", "tiger", "lion","python","cheetah", "none", 1],]
            
            # ["what is our national bird ?", "hen","peigon", "peacock", "crow", "none", 3],
            #  ["who is the prime minister of india ?", "modi", "nehru","azad","manmohan","atal", 1]]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
i = 0
for i in range(0, len(question)):
    questions = question[i]
    print(f"questions for Rs.{levels[i]}")
    print(questions[0])
    print(f"a.{questions[1]}          b. {questions[2]}")
    print(f"c.{questions[3]}          d. {questions[4]}")
    reply = int(input("enter your answer questions(1-4): or press 0 to quit"))
    if(reply==questions[-1]):
        print(f"correct answer you have won Rs.{levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i ==14):
            money = 10000000
    else:
        print("your answer is wrong")
        break
print(f"your take home money is {money}")

















