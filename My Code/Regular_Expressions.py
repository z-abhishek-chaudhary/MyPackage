import re


list_single = re.findall('\d',"PRA12Ga782d45601$3")
list_multiple = re.findall("[0-9]+","PRA12Ga782d45601$3")

list_digits_in_between = re.findall("[3-8]","PRA=-*12Ga7*82d4560@$1$3")

print(list_single)
print(list_multiple)
print(list_digits_in_between)



# ^ -> symbol matches the starting of the string.
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')



# $ -> symbol matches the starting of the string.
string = "Hello World!"
pattern = r"World!$"
 
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")



# re.compile -> It complies the pattern object to further searching and matching uses.
p = re.compile("[r-z]+")
string = "Abhissshek is going to Delhi"
print(p.findall(string))
