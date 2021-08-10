"""
   token     token
   keyword     1
   separator   2
   operator    3
   alpha       4
   digit       5
"""


#define the keywords
keyword = ['int', 'float', 'string', 'if', 'for', 'while', 'return']

#define the operators 
operator = ['+', '-', '*', '/', '>', '<', '=']

#initialize the output
word_stream = []

#get the filename as the input
source_code = open('./source_code', 'r')
#initialize the token number value
token = 0

for line in source_code.readlines():
    chars = line[:-1].split(' ')
    for char in chars:
        if len(char) == 1:
            #if ";" then set token as 2
            if char == ';':   
                token = 2
                word_stream.append((char, token))
            #if it is an operator, set token as 3
            elif char in operator:  
                token = 3
                word_stream.append((char, token))
            #if it is a letter, set token as 4
            elif char.isalpha():    
                token = 4
                word_stream.append((char, token))
            #if it is a number, set token as 5
            elif char.isdigit():    
                token = 5
                word_stream.append((char, token))
        else:
            if char in keyword:
                word_stream.append((char, 1))
            else:
                try:    
                    #if they are all digits
                    try:
                        char = int(char)
                    except:
                        char = float(char)
                    char = str(char)
                    word_stream.append((char, 5))
                except:  
                    #if it is character string
                    if char.startswith("'") and char.endswith("'"):  
                        word_stream.append((char, 5))
                    else:   
                        word_stream.append((char, 4))


#close the file after finished reading
source_code.close()

#output in new file 
output_file = open('./output', 'w')

#output
output_file.write(str(word_stream))

#close the file
output_file.close()
