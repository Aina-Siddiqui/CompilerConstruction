
    #if (s.isalnum()) and (not s.isalpha()) and(not s.isdigit()):

import re
def wordSplitter(filename):
    seperators=['(',')',','':']
    operators=['+','-','=','%','*','<','>','==',"&",'|']
    keywords=('while','for','if','elif','else')
    single_start="\\"


    chars=[]
    with open(filename,'r') as file:
        data=file.read()

        MultiLine = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "" ,data)
        singleLine=re.sub('//.*', "",MultiLine)
        tokens=re.findall(r'\w+|[^\w\s]', singleLine)

        i=0
        while i<len(tokens):
            token=tokens[i]
            #checking whitespace
            if token.isspace():
                continue
                i=i+1
            #checking separators
            elif token in seperators:
                chars.append(token)
                i=i+1
            #checking operators

            elif token in operators:
                #checking if token and next token are same
                if tokens[i+1]==token:
                    chars.append(token+tokens[i+1])
                    del tokens[i+1]
                    i=i+1
                #checking if next token are in operators
                elif tokens[i+1] in operators:
                    chars.append(token+tokens[i+1])
                    del tokens[i+1]
                    i=i+1
                else:
                    chars.append(token)
                    i=i+1






            elif token.isnumeric():
            #
                 if (tokens[i+1]==".") and (tokens[i+2].isalnum()) and (not tokens[i+2].isalpha()) and(not tokens[i+2].isdigit()):
                     digits = []
                     strings = []
                     operator = []
            #
                     current_digit = ""
                     current_string = ""
            #
                     for char in tokens[i+2]:
                         if char.isdigit():
                             if current_string:
                                 strings.append(current_string)
                                 current_string = ""
                             current_digit += char
                         elif char.isalpha():
                             if current_digit:
                                digits.append(current_digit)
                                current_digit = ""
                             current_string += char
                         else:
                             if current_digit:
                                 digits.append(current_digit)
                                 current_digit = ""
                             if current_string:
                                 strings.append(current_string)
                                 current_string = ""
                             operator.append(char)
            #
            #         # Append any remaining digit or string
                     if current_digit:
                         digits.append(current_digit)
                     if current_string:
                         strings.append(current_string)
            #
            #
            #
                     chars.append(token+tokens[i+1]+digits[0])
                     chars.append(strings[0])
                     chars.append(digits[1])
                     del tokens[i+1]
                     del tokens[i+1]
                     i=i+1
                     print(digits)
                     print(strings)
            #
            #
            #
                 elif (tokens[i + 1] == "."):
                     chars.append(token+tokens[i+1]+tokens[i+2])
                     del tokens[i+1]
                     del tokens[i+1]
                     i=i+1
            #
            #
                 else:
                     chars.append(token)
                     i=i+1
            #




            else:
                chars.append(token)
                i=i+1




        return chars







filename="text.txt"
res=wordSplitter(filename)
print(res)