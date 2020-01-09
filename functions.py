DICT = { 'A':'.-', 'B':'-...',
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
   '(':'-.--.', ')':'-.--.-'
}

def encrypt(msg):
  moar=""
  for let in msg:
    if(let not in DICT and let !=" " ):
      return("invalid input")

    if(let!=" "):
      moar+=DICT[let]+" "
    else:
      moar+=" "
  return moar

def decrypt(moar):
  msg=""
  moar+=" "
  temp=""
  for let in moar:
    if(let!=" "):
      i=0
      temp+=let
    else:
      i+=1
      if(i==2):
        msg+=" "
      else:
        lis=list(DICT.values())
        if( temp not in lis ):
          return("invalid input")
        else:
          msg += list(DICT.keys())[list(DICT.values()).index(temp)]
          temp = ''
  return msg