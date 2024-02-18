'''The below code is a representation of a chatbot that is designed for university students. 
It offers selections from the menu and guides and/or informs students accordingly.'''


print("Hello! I am UniBuddy.")

name = input("What is your name?: ").capitalize()
print(f"Welcome to the campus {name}! I will do my best to help you settle in")

menu_choice = 0

while menu_choice != 4:
    print("Please make a numerical choice below.")
    print("1. Academic")
    print("2. Finance")
    print("3. Activities")
    print("4. Quit")
    menu_choice = int(input("Menu Choice (1-4): "))
    
    
    if menu_choice == 1:
          
          print('\n'"""Here some information for you:
    * Your first class starts at 2pm. The classroom is located in the mail hall next to the cafeteria.
    * Library is accessible from 8am to 11pm everyday.
    * There is discount offer on books and photocopies on Tuesdays!
    """)
          
        
    elif menu_choice == 2:
        print('\n'"""Good news!
    Your studies qualify for an installment plan. 
    To learn more, please contact the accounts team on 0201234567 or email: accounts@unibuddy.com""")
        print()

    
    elif menu_choice == 3:
        print()
        print("We can explore the activities by themes!")
    
        themes = 0
        while themes != 3:
            print()
            print("Please make a theme choice to continue.")
            print("1. Sports")
            print("2. Colour")
            print("3. Creative")
            themes = int(input("Menu Choice (1-3): "))
        
            if themes == 1:
                print("""
           I see you are interested in sports. We have great interst in keeping active too.
           I have some options for you!
           """)     
                print("""
1. HypeDev Gym Membership
2. HypeDev Swimming Pool
3. HypeDev Campus League football Club
4. Indoor and outdoor tennis courts
5. Indoor and outdoor basketball courts
    """)
                
    
            elif themes == 2:
                fav_colour = input("What is your favourite colour: ").capitalize()
                

                if fav_colour == "Red":
                    print("That's great! My favourite colour is blue but check out following red themed clubs in the campus!: ")
                    print("""
            1. Red Hot Chilli Rockers
            2. Red Cooking Club
          """)
                    

                elif fav_colour == "Blue":
                    print(f"Such a relief to hear your favourite colour is {fav_colour}, too! We have that in common! Here comes some suggestions.")
                    print("""
        Blue Sea Rowing Club 
        Blues Jazz Club""")
                    
     
                elif fav_colour == "Black":
                    print("I have just the right thing for you!")
                    print("""
        Black and White Chess Club
        Blackish Metal Hub
           """)
                
            
            elif themes == 3:
                print("""Let's get creative!
        Theatre and Drama on Campus at 8pm on Mondays
        Dance with us at 5pm on Wednesdays
        Art and Dine Club at 7pm on Fridays 
                       """)
            else:
                 print("Please make a valid choice.\nReturning the main menu.")
            break
    
    
    elif menu_choice == 4:
                print("Thank you for visiting. Bye now!")
                break
    continue
    