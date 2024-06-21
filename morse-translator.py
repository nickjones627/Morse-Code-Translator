MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': '/'}

def eng_to_morse():
    user = input("\n#####################\nENGLISH TO MORSE CODE\n#####################\n\nType 'quit123' to return to the menu.\nPlease enter the sentence you would like to translate to Morse code\n>: ").upper()
    if user == 'quit123'.upper():
        intro()
    mrse = []
    for x in user:
        if x in MORSE_CODE_DICT:
            mrse.append(MORSE_CODE_DICT[x])
    print('Translation:')
    print(' '.join(mrse))
    eng_to_morse()

def morse_to_eng():
    REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
    
    user = input("\n#####################\nMORSE CODE TO ENGLISH\n#####################\n\nENTER A SPACE BETWEEN EACH CHARACTER AND A '/' FOR SPACING.\nType 'quit123' to return to the menu.\nPlease enter the sentence you would like to translate to English\n>: ").upper()
    if user == 'quit123'.upper():
        intro()
    morse_code_letters = user.split(' ')
    inds = []
    for x in morse_code_letters:
        if x in REVERSE_MORSE_CODE_DICT:
            inds.append(REVERSE_MORSE_CODE_DICT[x])
        else:
            inds.append('?')
    print('Translation:')  
    print(''.join(inds))
    morse_to_eng()

def intro():
    print("\n########################################\nWelcome to Nick's Morse Code Translator!\n########################################")
    mte = input('\nPlease select <1> or <2>\n1. MORSE TO ENGLISH \n2. ENGLISH TO MORSE \n\n>: ')
    while True:
        if mte == '1':
            morse_to_eng()
            break
        elif mte == '2':
            eng_to_morse()
            break
        else:
            intro()
            break
     
intro()