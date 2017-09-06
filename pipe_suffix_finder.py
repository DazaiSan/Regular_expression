import re

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')

message = ["Batmobile lost wheel", "Batmotorcycle is sold in this shop" ,"Her favourite is Batman series"]


for i in range(3):
    temp_message = message[i]
    mo = bat_regex.search(temp_message)
    if (mo != None):
        print("Found ",mo.group())
        print("Suffix was ",mo.group(1))
    else :
        print("Not found")
