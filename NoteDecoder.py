# File: DarkfallDecoder.py
# To Do:
#    Make I's capital when own word
#    Make decrypted characters print one after the other as you type them
#    Make text appear in a scroll-designed box at bottom of terminal window

def main():

    codec = { 'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t',
              'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n', 'n':'m',
              'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'g', 'u':'f',
              'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a'
             }
    print()
    print('''                                   {~ Arther's Note Decoder ~}
          <(==========================================================================)>
          
          
                                Can you hear him whistle? ..
             Enter a text of cipher per line and you should be able to read it below
                                                          (tap Enter/Return to exit)                                                
          <(==========================================================================)>                                             
          '''
          )
    while True:
        userInput = input(" ~'00~   ")
        if userInput == '' or userInput == ' ':
            break
        cipherText = list(userInput)
        times = 1
        for character in cipherText:
            if character not in codec:
                print(character, end='')
            else:
                indentatortot(times)
                times = times + 1
                currentCharacter = codec[character]
                print(currentCharacter, end='')
        print()



def indentatortot(once):
    if once == 1:
        print("\t\t> ", end='')


main()
