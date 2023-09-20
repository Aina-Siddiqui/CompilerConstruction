import done
import re

identifiers="^[a-zA-Z_]+[a-zA-Z0-9_]*"
default_Keywords=["if","elseif","for","continue","break","int","float","double","boolean",
                  "string","protected","private","public","true","false","global","while","in",
                  "not","this","print","try","except","None"]
arithematic_operators=['+','-','*','/','%','**','++','__']
assignment_operators=['=','+=','-=','*=','/=','%=','//=','**=','&=','|=','^=','>>=','<<=']
comparison_operators=['==','!=','<','>','>=','<=']
logical_operators=['AND','OR','NOT','XOR','NOR','NAND','XNOR','&&','||']

bitwise_operators=['&','|','^','~','<<','>>']
punctuators = ['(', ')', ',',':']
increament_operator=['++','--']
strings=["'",'"']
for token in done.tokens:
    if (re.findall(identifiers,token[0])) and (token[0] not in default_Keywords):
        print(f'valuePart: {token[0]},line Number: {token[1]},identifier')
    elif(token[0] in default_Keywords) and (re.findall(identifiers,token[0])) :
        print(f'valuePart: {token[0]},line Number: {token[1]},Keyword')
    elif token[0] in punctuators:
        print(f'valuePart: {token[0]},line Number: {token[1]},punctuator')
    elif token[0] in assignment_operators:
        print(f'valuePart: {token[0]},line Number: {token[1]},assignment operator')
    elif token[0] in comparison_operators:
        print(f'valuePart: {token[0]},line Number: {token[1]},comparision operator')
    elif token[0] in logical_operators:
        print(f'valuePart: {token[0]},line Number: {token[1]},logical operator')
    elif token[0] in bitwise_operators:
        print(f'valuePart: {token[0]},line Number: {token[1]},bitwise operator')
    elif token[0].isdigit():
        print(f'valuePart: {token[0]},line Number: {token[1]},Integer')
    elif token[0].replace(".","").isnumeric():
        print(f'valuePart: {token[0]},line Number: {token[1]},float')
    elif token[0] in increament_operator:
        print(f'valuePart: {token[0]},line Number: {token[1]},IncreamentOperator')
    elif token[0] in strings:
        print(f'valuePart: {token[0]},line Number: {token[1]},String')
    elif token[0] in arithematic_operators:
        print(f'valuePart: {token[0]},line Number: {token[1]},Aritmetic operator')
    else:
        print(f"Invalid {token[0]},linen:{token[1]}")

