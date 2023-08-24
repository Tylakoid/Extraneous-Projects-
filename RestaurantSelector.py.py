#Restaurant Selector
print("Let me ask you some questions before I tell you your restaurant!")
done=False
while done!=True:
 vegetable = input("Anyone in your party a vegetarian? ")
 vegan = input("Anyone in your party a vegan? ")
 gluten_free = input("Anyone in your party gluten-free? ")
 if vegetable == "No" and vegan == "No" and gluten_free == "No":
    done= True
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza Company")
    print("Corner Café")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
 elif vegetable == "Yes" and vegan == "No" and gluten_free == "No":
    print("Main Street Pizza Company")
    print("Corner Café")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
    done= True
 elif vegetable == "No" and vegan == "Yes" and gluten_free == "No":
    print("Corner Café")
    print("The Chef's Kitchen")
    done= True
 elif vegetable == "No" and vegan == "No" and gluten_free == "Yes":
    print("Corner Café")
    print("The Chef's Kitchen")
    done= True
 elif vegetable == "Yes" and vegan == "Yes" and gluten_free == "No":
    print("Corner Café")
    print("The Chef's Kitchen")
    done= True
 elif vegetable == "No" and vegan == "Yes" and gluten_free == "Yes":
    print("Corner Café")
    print("The Chef's Kitchen")
    done= True
 elif vegetable == "Yes" and vegan == "No" and gluten_free == "Yes":
    print("Main Street Pizza Company")
    print("Corner Café")
    print("The Chef's Kitchen")
    done= True
 elif vegetable=="Yes" and vegan=="Yes" and gluten_free=="Yes":
    done = True
    print("Corner Café")
    print("The Chef's Kitchen")
 else:
    print("Please tell me again.")
    done=False
else:
    print("I hope you have a nice dinner!")
print("See you next time.")



    
