"""
Variable assignment rules：
1. cant assign string to int, float variables
2. cant assign int, float to string variables
"""

#get tokens from lexical analysis
from lexical_analysis import word_stream

#define the keywords
keyword = ['int', 'float', 'string']

#method to judge the correctness 
def semantics(t_sentence):
    #if assignment statement
    if t_sentence[0][0] in keyword:  
        if len(t_sentence) == 4:
            #assign string to int variable
            if t_sentence[0][0] == 'int':  
                try:
                    item = t_sentence[3][0]
                    #try to convert to int
                    int(item)   
                    return t_sentence
                except:  
                    #incorrect assignment
                    return False
            #assign string to float variable
            elif t_sentence[0][0] == 'float':  
                try:
                    item = t_sentence[3][0]
                    #try to convert to float
                    float(item)  
                    return t_sentence
                except:  
                    #incorrect assignment
                    return False
            #assign int, float to string variable
            elif t_sentence[0][0] == 'string':  
                #string containing detection
                if t_sentence[3][0].startswith("'") and t_sentence[3][0].endswith("'"):  
                    return t_sentence
                else:   
                    #incorrect assignment
                    return False
        else:   
            return t_sentence
    #not assignment statement
    else:   
        return t_sentence


#current position
current_word = 0

#last semicolon location
last_semicolon = 0

#number of element
end_word = len(word_stream) - 1

#store the analysis result
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
            #delete the semicolon
            sentence = word_stream[last_semicolon:current_word]
            #go next element
            current_word += 1
            break
        #go next element
        current_word += 1

    #semantic analysis
    tree = semantics(sentence)
    if tree is False:
        tree = 'Semantic incorrect!'
    else:
        tree = 'Semantic correct!'
    #store the semantic analysis result
    grammar_forest.append(tree)
    #update the semicolon position
    last_semicolon = current_word

#print out the semantic analysis results 
print('First: ', grammar_forest[0])
print('Second: ', grammar_forest[1])
print('Third: ', grammar_forest[2])
print('Fourth: ', grammar_forest[3])
print('Fifth: ', grammar_forest[4])
print('Sixth: ', grammar_forest[5])
print('Seventh: ', grammar_forest[6])