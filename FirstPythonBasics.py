def initial():
    answer= input('''What would you like to do
            1.Getting you know you and me
            2.quit
            ''')
    if answer == "1" :
        print("You will now find out things about me and i will ask you some quesrtions")
        knowinglife()
    elif answer == "2":
        print("I believe you are making a terrible mistake by deciding to quit. But see you later.BYE")
    else:
        print("Please enter a relevant answer ")

def knowinglife():
	print("I want to eat Ben and Jerry'icecream")
	school = "I got to Joseph Rowntree  school"
	print(school)
	city = "I live in York"
	print (city)
	#variables 2
	askName = input("What is your name?")
	askAge = input("How old are you?")
	print ("Hello your name is",askName,"and you are",askAge )
initial()
