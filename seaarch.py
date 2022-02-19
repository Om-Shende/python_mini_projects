shopiing_list = ["milk", "chair", "beer", "pendrive"]
item = "pendrive"
found = None
if item in shopiing_list:
    found = shopiing_list.index(item)
    found += 1
if found is not None:
    print("item found at {}".format(found))
else:
    print("value not found")
