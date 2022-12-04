import re
def validation_check(input_string):
     regex = re.compile('my-random-[a-z]{3}-string_[0-9a-z]{32}\Z', re.I)
     match = regex.match(str(input_string))
     return bool(match)

def validation_hcl(input_string):
     regex = re.compile('#[0-9a-f]{6}\Z', re.I)
     match = regex.match(str(input_string))
     return bool(match)


data = ['#123abc', '#123abz', '123abc']   

for s in data:
    print(validation_hcl(s))
