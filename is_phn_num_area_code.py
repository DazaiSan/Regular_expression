import re

message = "My number is 415-555-4242.My office number is 866-207-5001."
phn_num_regex = re.compile(r'(\d\d\d)-((\d\d\d)-\d\d\d\d)')

mo = phn_num_regex.search(message)
print("Phone num :", mo.group())
print("Area code :",mo.group(1))
print("Main num  :",mo.group(2))

'''area_code,main_num = mo.groups()
print("Area code :",area_code)
print("Main num  :",main_num)'''
mo_list = phn_num_regex.findall(message)
print(mo_list)
