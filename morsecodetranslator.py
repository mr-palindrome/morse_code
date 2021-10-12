morse_code_dict = {
    '.-':'A', '-...':'B',
   '-.-.':'C', '-..':'D', '.':'E',
   '..-.':'F', '--.':'G', '....':'H',
   '..':'I', '.---':'J', '-.-':'K',
   '.-..':'L', '--':'M', '-.':'N',
   '---':'O', '.--.':'P', '--.-':'Q',
   '.-.':'R', '...':'S', '-':'T',
   '..-':'U', '...-':'V', '.--':'W',
   '-..-':'X', '-.--':'Y', '--..':'Z',
   '.----':'1', '..---':'2', '...--':'3',
   '....-':'4', '.....':'5', '-....':'6',
   '--...':'7', '---..':'8', '----.':'9',
   '-----':'0', '--..--':',', '.-.-.-':'.',
   '..--..':'?', '-..-.':'/', '-....-':'-',
   '-.--.':'(', '-.--.-':')'
}

def translate_morse(message):
    message += " "
    decoded = ""
    morse_text = ''
    for text in message:
        if text != "/" and  text != " ":
            morse_text+= text
            # print(morse_text)
            i = 0
        else:
            i += 1
            if i == 2 :
                decoded += ' '

            else:
                decoded += morse_code_dict[morse_text]
                morse_text = ''
 
    return decoded
            


if __name__ == "__main__":
    message = input("Enter the morse code: ")
    message = message.replace('/','')

    print(translate_morse(message))
    