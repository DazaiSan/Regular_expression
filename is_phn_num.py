import re

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

phn_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phn_num_regex.search(message)
print(mo.group())

all_mo = phn_num_regex.findall(message)
print(all_mo)
