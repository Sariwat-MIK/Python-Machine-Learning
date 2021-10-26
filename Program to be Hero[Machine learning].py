from sklearn import tree
print("**************************************")
print("*************WELCOME HERO*************")
print("**************************************")
play=int(input("if you want to play press(1), if youwant to end game press(0): "))
while play!=0:
    n=input("What's your name?: ")
    o=int(input('How old are you?: '))
    s=input("Sex?(Male/Female): ")
    h=int(input("Height?: "))
    w=int(input("Weight?: "))
    if (s=='Male') :
        A=[[53,78,172.72],[42,84,188],[37,86,184],[37,79,187.5],[35,105,190],[42,78,183],[39,101,188],[51,72,173],[47,82,178]] #ข้อมูล [อายุ,น้ำหนัก,ส่วนสูง]
        B=['Robert Downey Jr/Ironman','Ryan Reynolds/Deadpool','Chris Evans/Captain America','Tom Hiddleston/Loki','Chris Hemsworth/Thor','Benedict Cumberbatch/Doctor Strange','Chris Pratt/Star Lord','Mark Ruffalo/Bruce Banner','Jeremy Renner/Hawkeye'] #ข้อมูล ฮีโร่มาเวล
        classifier= tree.DecisionTreeClassifier()
        classifier=classifier.fit(A,B)
        print(n,"you can be",classifier.predict([[o,w,h]]))
    elif (s=='Female') :
        C=[[34,56,163],[28,55,167],[32,56,163]]
        D=['Scarlett Johansson/Black Widow','Brie Larson/Captain Marvel','Elizabeth Chase Olsen/Wanda']
        classifier= tree.DecisionTreeClassifier()
        classifier=classifier.fit(C,D)
        print(n,"you can be",classifier.predict([[o,w,h]]))
    play=int(input("if you want to play press(1), if youwant to end game press(0): "))
print('end game !')
    

