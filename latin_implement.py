from latin import latin

my_program = latin()
ans = 'n'
while ans != 'q':
    action = input('please enter the word you want to transform\n')
    word = my_program.convert(action)
    if word == 'empty word not allowed' or word == 'letter not allowed' or word == 'word is invalid  contains numeric value' or word == action + " word cannot be changed":
        print("Warning " + word)
    else:
        print('This is the converted word ' + word)
    reply = input('Do you want to quit press q to quit or any letter to continue converting')
    ans = reply.lower()
print('thank you for using my program')

