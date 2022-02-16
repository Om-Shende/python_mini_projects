
choice = "-"
emplist = []

while choice != '0':
    if choice in "123456":
        print('adding {}'.format(choice))
        if choice == "1":
            emplist.append("Computer")
        elif choice == "2":
            emplist.append("Monitor")
        elif choice == "3":
            emplist.append("Keyboard")
        elif choice == "4":
            emplist.append("Mouse")
        elif choice == "5":
            emplist.append("Mouse mat")
        elif choice == "6":
            emplist.append("HDMI cable")

    else:
        print("please add options from below")

        print("1: Computer \n2: Monitor \n3: keyboard \n4: Mouse \n"
              "5: Mouse mat \n6 :HDMI cable \n0: Exit ")


    choice = input()

print(emplist)
