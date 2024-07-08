#Chandu assignment


Entrees = ["Veg Biryani","Chicken Biryani","Dahl"]
Drinks = ["Tea","Coffee","Orange Juice", "Water"]
Dessert = ["Vanilla Cake", "Chocolate cake", "Vanilla ice cream"]

Food = [Entrees,Drinks,Dessert]

Fcook = {"Good","Bad","Ugly"}

while True:
    num = input("What would you like to order?: ")
    print(num)

    if (num == "Food"):
        print(Entrees,Drinks,Dessert,"This is our menu!")
        num = input("So what do you want to get started off with?: ")
    if(num == "Dessert first"):
        print("That cannot be ordered first")
        break
    while num == Entrees:    
        #Entrees choice
        if(num == "Entrees"):
            print("Okay! No drinks then! Not EVEN WATER!","Here are our Entrees: "+str(Entrees))
            num = input("What Entree will you order?: ")
        
        if(num == "Veg Biryani"):
            print("You have 1 Veg Biryani!")
            num = input("Would you like dessert?: ")
        if(num == "Chicken Biryani"):
            print("You have 1 Chicken Biryani!")
            num = input("Would you like dessert?: ")
        if(num == "Dahl"):
            print("You have 1 Dahl curry!")
            num = input("Would you like dessert?: ")
        
        if(num == "Yes" or num == "yes"):
             print("Alright! Here are our Desserts:"+str(Desserts))
             num = input("What dessert will you order?: ")
     
        elif(num == "No", num == "no"):
             print("Ok! But it is mandatory to take a fortune cookie. It can Either be Good, Bad, or Ugly. It is randomized for you The first fortune cookie to appear will be yours!")
             print(Fcook)
        else:
             print("That's not an option")
    
        if(num == "Vanilla Cake"):
             print("You have 1 vanilla cake!")
             num = input("Good! You need to take a fortune cookie. It can Either be Good, Bad, or Ugly. It is randomized for you. The first fortune cookie to appear will be yours!")
             print(Fcook)
        if(num == "Chocolate Cake"):
             print("You have 1 choclate cake!")
             num = input("Good! You need to take a fortune cookie. It can Either be Good, Bad, or Ugly. It is randomized for you. The first fortune cookie to appear will be yours!")
             print(Fcook)
        if(num == "Vanilla ice cream"):
             print("You have 1 vanilla ice cream!")
             num = input("Good! You need to take a fortune cookie. It can Either be Good, Bad, or Ugly. It is randomized for you. The first fortune cookie to appear will be yours!")
             print(Fcook)

        #Drinks Choice
    if(num == "Drinks"):
        print(Drinks," are the only drinks we offer here")
        num = input("which drink will you order?: ")
        
    if(num == "Tea"):
        print("You have 1 Tea")
        num = input("Now we will move on to Entrees. "+str(Entrees)+ "What Entree would you like to order?: ")
    if(num == "water"):
        print("You have 1 water")
        num = input("Now we will move on to Entrees. "+str(Entrees)+ "What Entree would you like to order?: ")
        
    if(num == "Coffee"):
        print("You have 1 Coffee")
        num = input("Now we will move on to Entrees. "+str(Entrees)+ "What Entree would you like to order?: ")
        
    if(num == "Orange Juice"):
        print("You have 1 Orange Juice")
        num = input("Now we will move on to Entrees. "+str(Entrees)+ "What Entree would you like to order?: ")
       
    if(num == "Entrees"):
        print("Okay! No drinks then! Not EVEN WATER!","Here are our Entrees: "+str(Entrees))
        num = input("What Entree will you order?: ")
        
        
    if(num == "Veg Biryani"):
        print("You have 1 Veg Biryani!")
        num = input("Would you like dessert?: ")
       
    if(num == "Chicken Biryani"):
        print("You have 1 Chicken Biryani!")
        num = input("Would you like dessert?: ")
       
    if(num == "Dahl"):
        print("You have 1 Dahl curry!")
        num = input("Would you like dessert?: ")
        
        
    if(num == "Yes" or num == "yes"):
         print("Alright! Here are our Desserts:"+str(Dessert))
         num = input("What dessert will you order?: ")
         
    elif(num == "No", num == "no"):
         print("Ok! But it is mandatory to take a fortune cookie. It can Either be Good, Bad, or Ugly. It is randomized for you. The first fortune cookie to appear will be yours!")
         
         print(Fcook)
    else:
         print("That's not an option")
    
    if(num == "Vanilla Cake"):
         print("You have 1 vanilla cake!")
         num = input("Good! You need to take a fortune cookie. It can Either be Good, Bad, or Ugly. It is randomized for you. The first fortune cookie to appear will be yours!")
         print(Fcook)
    if(num == "Chocolate Cake"):
         print("You have 1 choclate cake!")
         num = input("Good! You need to take a fortune cookie. It can Either be Good, Bad, or Ugly. It is randomized for you. The first fortune cookie to appear will be yours!")
         print(Fcook)
    if(num == "Vanilla ice cream"):
         print("You have 1 vanilla ice cream!")
         num = input("Good! You need to take a fortune cookie. It can Either be Good, Bad, or Ugly. It is randomized for you. The first fortune cookie to appear will be yours!")
         print(Fcook)
