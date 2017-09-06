import re

bat_regex = re.compile(r'Bat(wo)?man')#zero or one
message = ["Batman is not fatman" , "Batwoman is not fatwoman" , "Batwowoman is not fatwowoman"]

for temp in message:
    mo = bat_regex.search(temp)
    if (mo != None):
        print(" Found :",mo.group())
        print(" Woman or man ? ",mo.group(1),"man")
    else :
        print("Not Found")

bat_regex2 = re.compile(r'Bat(wo)*man')#zero or more
for temp in message:
    mo = bat_regex2.search(temp)
    if ( mo != None):
        print("Found :",mo.group())
        print(" Woman or man ?", mo.group(1),"man")
    else:
        print("Not found")

bat_regex3 = re.compile(r'Bat(wo)+man')#one or more
for temp in message:
    mo = bat_regex3.search(temp)
    if ( mo != None):
        print("Found :",mo.group())
        print(" Woman or man ?", mo.group(1),"man")
    else:
        print("Not found")


phn_num_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
message = [" My number is 415-555-1234. Call me tomorrow",
        "My office number is 556-1245."]
for temp in message:
    mo = phn_num_regex.search(temp)
    if ( mo != None):
        print("Found no : ", mo.group())
    else :
        print("Not found")
phn_num_regex2 = re.compile(r'((\d){3}-)?(\d){3}-(\d){4}')
message = [" My number is 415-555-1234. Call me tomorrow",
        "My office number is 556-1245."]
for temp in message:
    mo = phn_num_regex2.search(temp)
    if ( mo != None):
        print("Found no : ", mo.group())
    else :
        print("Not found")


