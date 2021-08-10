"""
1. Lexical Analysis
   token     token
   keyword     1
   separator   2
   operator    3
   alpha       4
   digit       5
"""


# define the keywords
keyword = ['int', 'float', 'string', 'if', 'for', 'while', 'return']

# define the operators
operator = ['+', '-', '*', '/', '>', '<', '=']

# initialize the output
word_stream = []

# get the filename as the input
source_code = open('./source_code', 'r')
# initialize the token number value
token = 0

for line in source_code.readlines():
    chars = line[:-1].split(' ')
    for char in chars:
        if len(char) == 1:
            # if ";" then set token as 2
            if char == ';':
                token = 2
                word_stream.append((char, token))
            # if it is an operator, set token as 3
            elif char in operator:
                token = 3
                word_stream.append((char, token))
            # if it is a letter, set token as 4
            elif char.isalpha():
                token = 4
                word_stream.append((char, token))
            # if it is a number, set token as 5
            elif char.isdigit():
                token = 5
                word_stream.append((char, token))
        else:
            if char in keyword:
                word_stream.append((char, 1))
            else:
                try:
                    # if they are all digits
                    try:
                        char = int(char)
                    except:
                        char = float(char)
                    char = str(char)
                    word_stream.append((char, 5))
                except:
                    # if it is character string
                    if char.startswith("'") and char.endswith("'"):
                        word_stream.append((char, 5))
                    else:
                        word_stream.append((char, 4))


# close the file after finished reading
source_code.close()

# output in new file
output_file = open('./output', 'w')

# output
output_file.write(str(word_stream))

# close the file
output_file.close()
print('Saved!')


"""
2. Grammatical Analysis
two kinds of structure in statement: 
(1). keywords + digits, ex: return 0;
(2). keywords + variable + (operator + variable) * n; ex: int a = a * b + 2;
"""


# method to judge the correctness
def grammar(char, t_sentence):
    # syntax in non-terminal symbols
    for production in eval(char):
        # sequence as syntax
        for sequence in range(0, len(production)):
            # if non-terminal
            if type(production[sequence]) == str:
                # since not terminal
                # remaining statement
                t = t_sentence[sequence:]
                # delete statement
                t_sentence = t_sentence[:sequence]
                # detect syntax, then go back to the next level
                result = grammar(production[sequence], t)
                if not result:
                    # extend case
                    t_sentence.extend(t)
                    return False
                else:
                    # if return contained
                    t_sentence.append(result)
                    return t_sentence
            # syntax correct
            elif production[sequence] == t_sentence[sequence][1]:
                # correct case
                if sequence == len(t_sentence) - 1:
                    return t_sentence
            else:
                # end syntax but not correct case
                if production == eval(char)[-1]:
                    return False
                # not end, then go next syntax rule
                else:
                    break


# define the syntax
S = [[1, 5], [1, 4, 3, 5], [4, 'F']]
F = [[3, 4, 'F'], [3, 5, 'F']]


# current position
current_word = 0

# last semicolon position
last_semicolon = 0

# number of element
end_word = len(word_stream) - 1

# store the result in tree
tree = []

# output initialization
grammar_result = []


# while-loop
while True:
    # judge end or not
    if last_semicolon == len(word_stream):
        print('\nAnalysis done!')
        break

    # get new element from word_stream
    while True:
        # semicolon or not
        if word_stream[current_word][0] == ';':
            # delete the semicolone
            sentence = word_stream[last_semicolon:current_word]
            # go next element
            current_word += 1
            break
        # go next element
        current_word += 1

    # grammar analysis
    tree = grammar('S', sentence)
    if tree is False:
        result = 'Syntax incorrect!'
    else:
        result = 'Syntax correct!'
    # store the result
    grammar_result.append(result)
    # update the semicolon position
    last_semicolon = current_word

# print out the analysis results
print('First: ', grammar_result[0])
print('Second: ', grammar_result[1])
print('Third: ', grammar_result[2])
print('Fourth: ', grammar_result[3])
print('Fifth: ', grammar_result[4])
print('Sixth: ', grammar_result[5])
print('Seventh: ', grammar_result[6])


"""
3. Semantic Analysis
Variable assignment rules：
(1). cant assign string to int, float variables
(2). cant assign int, float to string variables
"""

# define the keywords for assignment
keyword = ['int', 'float', 'string']


# method to judge the correctness
def semantics(t_sentence):
    # if assignment statement
    if t_sentence[0][0] in keyword:
        if len(t_sentence) == 4:
            # assign string to int variable
            if t_sentence[0][0] == 'int':
                try:
                    item = t_sentence[3][0]
                    # try to convert to int
                    int(item)
                    return t_sentence
                except:
                    # incorrect assignment
                    return False
            # assign string to float variable
            elif t_sentence[0][0] == 'float':
                try:
                    item = t_sentence[3][0]
                    # try to convert to float
                    float(item)
                    return t_sentence
                except:
                    # incorrect assignment
                    return False
            # assign int, float to string variable
            elif t_sentence[0][0] == 'string':
                # string containing detection
                if t_sentence[3][0].startswith("'") and t_sentence[3][0].endswith("'"):
                    return t_sentence
                else:
                    # incorrect assignment
                    return False
        else:
            return t_sentence
    # not assignment statement
    else:
        return t_sentence


# current position
current_word = 0

# last semicolon location
last_semicolon = 0

# number of element
end_word = len(word_stream) - 1

# store the analysis result
tree = []

# output initialization
semantics_result = []

# while-loop
while True:

    # judge end or not
    if last_semicolon == len(word_stream):
        print('\nAnalysis done!')
        break

    # get new element from word_stream
    while True:
        # semicolon or not
        if word_stream[current_word][0] == ';':
            # delete the semicolon
            sentence = word_stream[last_semicolon:current_word]
            # go next element
            current_word += 1
            break
        # go next element
        current_word += 1

    # semantic analysis
    tree = semantics(sentence)
    if tree is False:
        result = 'Semantic incorrect!'
    else:
        result = 'Semantic correct!'
    # store the semantic analysis result
    semantics_result.append(result)
    # update the semicolon position
    last_semicolon = current_word

# print out the semantic analysis results
print('First: ', semantics_result[0])
print('Second: ', semantics_result[1])
print('Third: ', semantics_result[2])
print('Fourth: ', semantics_result[3])
print('Fifth: ', semantics_result[4])
print('Sixth: ', semantics_result[5])
print('Seventh: ', semantics_result[6])

