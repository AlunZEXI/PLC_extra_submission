"""
two kinds of structure in statement: 
1. keywords + digits, ex: return 0;
2. keywords + variable + (operator + variable) * n; ex: int a = a * b + 2;

"""


#get the tokens from lexical analysis
from lexical_analysis import word_stream

#method to judge the correctness 
def grammar(char, t_sentence):
    #syntax in non-terminal symbols
    for production in eval(char):
        #sequence as syntax
        for sequence in range(0, len(production)):
            #if non-terminal
            if type(production[sequence]) == str:
                #since not terminal
                #remaining statement
                t = t_sentence[sequence:]
                #delete statement
                t_sentence = t_sentence[:sequence]
                #detect syntax, then go back to the next level
                result = grammar(production[sequence], t)
                if not result:
                    #extend case
                    t_sentence.extend(t)
                    return False
                else:
                    #if return contained
                    t_sentence.append(result)
                    return t_sentence
            #syntax correct
            elif production[sequence] == t_sentence[sequence][1]:
                #correct case
                if sequence == len(t_sentence) - 1:
                    return t_sentence
            else:
                #end syntax but not correct case
                if production == eval(char)[-1]:
                    return False
                #not end, then go next syntax rule
                else:   
                    break


#define the syntax
S = [[1, 5], [1, 4, 3, 5], [4, 'F']]
F = [[3, 4, 'F'], [3, 5, 'F']]


#current position
current_word = 0

#last semicolon position
last_semicolon = 0

#number of element
end_word = len(word_stream) - 1

#store the result in tree
tree = []

#output initialization
grammar_forest = []


#while-loop
while True:
    #judge end or not
    if last_semicolon == len(word_stream):
        print('Analysis done!')
        break

    #get new element from word_stream
    while True:
        #semicolon or not
        if word_stream[current_word][0] == ';':
            #delete the semicolone
            sentence = word_stream[last_semicolon:current_word]
            #go next element
            current_word += 1
            break
        #go next element
        current_word += 1

    #grammar analysis
    tree = grammar('S', sentence)
    if tree is False:
        tree = 'Syntax incorrect!'
    else:
        tree = 'Syntax correct!'
    #store the result
    grammar_forest.append(tree)
    #update the semicolon position
    last_semicolon = current_word

#print out the analysis results
print('First: ', grammar_forest[0])
print('Second: ', grammar_forest[1])
print('Third: ', grammar_forest[2])
print('Fourth: ', grammar_forest[3])
print('Fifth: ', grammar_forest[4])
print('Sixth: ', grammar_forest[5])
print('Seventh: ', grammar_forest[6])
