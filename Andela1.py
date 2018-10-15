class latin:
    def __init__(self):
        print("Welcome to Simple Pig Latin Converter")

    def convert(self,letter):
        try:
            if len(letter) == 0:
                latin_name = 'empty word is not allowed'
                # change to lowercase
            elif len(letter) > 0:
                original = letter.lower()
                # the first character
                k=0
                first_char= original[k]
    # check the char
                converted_original = list(original)
                length = len(converted_original) - 1
                y = []
                if any(str.isdigit(c) for c in original):
                    latin_name = 'word is invalid  contains numeric value'
                elif first_char == 'a' or first_char == 'e' or first_char == 'i' or first_char == 'o' or first_char == 'u':
                    latin_name = (original + "way")
                else:
                    while k <= length:
                        if first_char == 'a' or first_char == 'e' or first_char == 'i' or first_char == 'o' or first_char == 'u':
                            break
                        else:
                            converted_original.remove(first_char)
                            y.append(first_char)
                            k = k + 1
                            first_char = original[k]
                    new_name = converted_original + y
                    latin_name = ''.join(new_name) + 'ay'
            return latin_name
        except:
            return "word contain only consonants"



