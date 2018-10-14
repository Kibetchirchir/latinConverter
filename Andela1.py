class latin:
    def __init__(self):
        print("Welcome to Simple Pig Latin Converter")

    def converter(self,letter):
        # change to lowercase
        original = letter.lower()
        # the first character
        k=0
        first_char= original[k]
        # check the char
        converted_original = list(original)
        length = len(converted_original)
        y = []
        if first_char == 'a' or first_char == 'e' or first_char == 'i' or first_char == 'o' or first_char == 'u':
            print(original + "way")
        else:
            for i in converted_original:
                if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                    break
                else:
                    converted_original.remove(i)
                    y.append(i)
                    # print(y)
                    # print(converted_original)

            new_word = converted_original + y
            # new_word = ''.join(new_word) + 'ay'
            print(y)
                    


latin =  latin()
action = input("Hi what is your name?")
latin.converter(action)




