# print("Hello world")

try:
    print("1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday\n7. Sunday ")
    user_select = int(input("Enter menu number: "))
#
    # v1
    if user_select == 1:
        print("Monday")
    elif user_select == 2:
        print("Tuesday")
    elif user_select == 3:
        print("Wednesday")
    elif user_select == 4:
        print("Thursday")
    elif user_select == 5:
        print("Friday")
    elif user_select == 6:
        print("Suturday")
    elif user_select == 7:
        print("Sunday")
    else:
        print("Incorrect menu item!")

    # match user_select:
    #         case == 1:
    #            print("Monday")
    #         case == 2:
    #            print("Tuesday")
    #         case == 3:
    #            print("Wednesday")
    #         case == 4:
    #            print("Thursday")
    #         case == 5:
    #            print("Friday")
    #         case == 6:
    #            print("Saturday")
    #         case == 7:
    #            print("Sunday")
    #         case_:
    #             print("incorrect menu item!")

except Exception as e:
    print(f"Error: {e}")

