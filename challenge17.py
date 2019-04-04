import re

text = "The ghost that says boo haunts the loo"
m = re.findall(".oo", text)
print(m)