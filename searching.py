shopiing_list = ["milk", "chair", "beer", "pendrive"]
item = "beer"
found = None

for index in range(len(shopiing_list)):
    if shopiing_list[index] == item:
        found = index + 1
        break
print("the position it was {}". format(found))