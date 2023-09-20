import comments
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


#operators=[arithematic_operators+assignment_operators+comparison_operators+logical_operators+bitwise_operators]
chars=comments.wordSplitter("text.txt")
for ch in chars:
    if (re.findall(identifiers,ch)) and (ch not in default_Keywords):
        print(ch,'----->',"identifers")
    elif(ch in default_Keywords) and (re.findall(identifiers,ch)) :
        print(ch,"----->",'Keywords')
    elif ch in punctuators:
        print(ch, "----->", 'punctuators')
    elif ch in assignment_operators:
        print(ch+"----->","assignment operators")
    elif ch in comparison_operators:
        print(ch, "----->", 'comparision operators')
    elif ch in logical_operators:
        print(ch, "----->", 'logical operator')
    elif ch in bitwise_operators:
        print(ch, "----->", 'bitwise operator')
    elif ch.isdigit():
        print(ch, "----->", 'Integer')
    elif ch.replace(".","").isnumeric():
        print(ch, "----->", 'float')
    elif ch in increament_operator:
        print(ch, "----->", 'Increament Operator')
    elif ch in strings:
        print(ch,"---->","String")


    else:
        print(f"unknown value{ch}")

