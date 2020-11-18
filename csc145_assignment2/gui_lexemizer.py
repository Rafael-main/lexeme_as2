from tkinter import *
import re


# initailize gui with tkinter
top = Tk()


part_text = StringVar()
part_header_title = Label(top, text='A Simple Lexemizer', font=('fixedsys', 32), pady=20)
part_header_title.pack()
part_label = Label(top, text='Place your arithmetic expression', font=('fixedsys', 16))
part_label.pack()
part_input = Entry(top, textvariable=part_text, width=40, font=('fixedsys', 16), justify='center')
part_input.pack()


def lexemize():
	# input string	
	text = part_input.get()
	# searches if string has operations like +,-,/,* at the beginning and end of the string 
	not_expression = re.search('^[+-/=*)]+|[+-/*=(]+$|\d+[.]\d+|^\d*$|^[a-zA-Z0-9]*$|^[0-9a-zA-Z]*$|^([()])*$', text)
	output = ''

	# checks if not_expression exists else it splits the expression
	if not_expression:
		output = text + ":" + "Expression invalid"
		text_label = Label(top, text=output, font=('fixedsys', 14))


	else:
		split_the_text = re.findall('([0-9a-zA-Z]+|\d+|[+-/*=()]|[a-zA-Z0-9]+)', text)

		if '(' in split_the_text and ')' not in split_the_text:
			print(text + ":" + "Invalid expression")
			output = text + ":" + "Expression invalid"
		elif '(' not in split_the_text and ')' in split_the_text:
			print(text + ":" + "Invalid expression")
			output = text + ":" + "Expression invalid"
		else:

			# prints the expression
			print(split_the_text)
			output = text + ':' + str(split_the_text)

		# splits the expression
		text_label = Label(top, text=output, font=('fixedsys', 14))
		
	text_label.pack()
	part_input.delete(0,END)


part_submit = Button(top, text='Submit',font=('fixedsys', 16),command=lexemize)	
part_submit.pack()



# title
top.title('Lexemizer!')
#width and height of window
top.geometry('900x450')

# Start program
top.mainloop()