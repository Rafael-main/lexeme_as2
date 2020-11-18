import re

# input string	
text = str(input())

# searches if string has operations like +,-,/,* at the beginning and end of the string 
not_expression = re.search('^[+-/=*)]+|[+-/*=(]+$|\d+[.]\d+|^\d*$|^[a-zA-Z0-9]*$|^[0-9a-zA-Z]*$|^([()])*$', text)

# checks if not_expression exists else it splits the expression
if not_expression:
	print(text + ":" + "Invalid expression")
else:
    split_the_text = re.findall('([0-9a-zA-Z]+|\d+|[+-/*=()]|[a-zA-Z0-9]+)', text)

    #checks if parenthesis are out of palce or missing
    if '(' in split_the_text and ')' not in split_the_text:
    	print(text + ":" + "Invalid expression")
    elif '(' not in split_the_text and ')' in split_the_text:
    	print(text + ":" + "Invalid expression")

    else:
	    # prints the expression
	    print(split_the_text)