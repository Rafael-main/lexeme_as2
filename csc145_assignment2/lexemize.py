import re

# input string	
text = str(input())

# searches if string has operations like +,-,/,* at the beginning and end of the string 
not_expression = re.search('^[+-/*]+|[+-/*]+$|\d+[.]\d+', text)

# checks if not_expression exists else it splits the expression
if not_expression:
    print(text + "+" + "Invalid expression")
else:
    split_the_text = re.findall('[0-9a-zA-Z]+|\d+|[+-/*()]|[a-zA-Z0-9]+', text)
    # splits the expression
    print(text + "+" + split_the_text)