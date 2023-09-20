# Read the file and store its contents as a list of lines
with open('text.txt', 'r') as file:
    operators = ['+', '-', '*', '=', '/', '<', '>','&']
    lines = file.readlines()
    tokens=[]
    currentString=''

# Initialize a flag to keep track of whether we're inside a comment block or not
inside_comment = False

# Iterate through each line
for line in lines:
    # Iterate through each character in the line
    index = 0
    while index < len(line):


        # Check if the current character is '*'
        if line[index] == '*':
            # Check if the next character is '/'
            if index < len(line) - 1 and line[index + 1] == '/':
                # Found '*/' indicating the end of the comment block
                inside_comment = False
                # Skip the '*/' characters

                index += 2

                continue


        # Check if the current character is '/'
        if line[index] == '/':
            # Check if the next character is '*'
            if index < len(line) - 1 and line[index + 1] == '*':
                # Found '/*' indicating the start of a comment block
                inside_comment = True
                # Skip the '/*' characters
                index += 2
                continue





        # Process the token if it's not inside a comment block
        if not inside_comment:



            # Process the token, e.g., add it to a list, print it, etc.
            if line[index].isalnum() or line[index]=='_':

                currentString+=line[index]
            else:
                if currentString:
                    linenumber = lines.index(line) + 1
                    tokens.append([currentString,linenumber])
                    currentString=''
                #single line comment
                elif line[index]=='/'  and line[index+1]=='/':
                    index=index+2
                    while line[index]!='\n':
                        index=index+1
                    index=index+1





                elif line[index] in operators :
                    if line[index+1] in operators:
                        linenumber = lines.index(line) + 1
                        tokens.append([line[index]+line[index+1],linenumber])
                        index+=1
                    elif line[index+1]==line[index]:
                        linenumber = lines.index(line)+ 1
                        tokens.append([line[index] + line[index + 1], linenumber])
                        index += 1
                    else:
                        linenumber = lines.index(line) + 1
                        tokens.append([line[index], linenumber])






                else:

                    linenumber = lines.index(line) + 1


                    tokens.append([line[index],linenumber])

        index =index+1

combined = []
is_quoted = False
quote_type = ''
temp = ''

for item in tokens:
    if item in ('"', "'"):
        if not is_quoted:
            is_quoted = True
            quote_type = item
            temp += item
        elif is_quoted and item == quote_type:
            is_quoted = False
            temp += item
            combined.append(temp)
            temp = ''
        else:
            temp += item
    elif is_quoted:
        temp += item
    else:
        combined.append(item)

res = combined
print(res)

