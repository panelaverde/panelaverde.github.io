import sys
import os

print ('Convert MD to SSML')

# filename from console
fn = sys.argv[1]
print ('Input: %s' % fn)

# open input
f = open (fn, 'r')
text = f.read ()
f.close ()

text = text.replace ('#', '<break time="250ms"/>' )
text = text.replace ('*', '<break time="250ms"/>' )

# remove layout
ini = text.index ('---')
fim = text[ini+2:len (text)].index ('---')
text = text[0:ini] + text[ini+2+fim+3:len (text)]

# <speak>
text = '<speak>' + text

# imagens
ini = text.find ('![')
while (ini != -1):
    fim = text[ini:len (text)].index ('](')
    text = text[0:ini] + \
    '<break time="100ms"/>' + \
    text[ini+2:ini+fim] + text[ini+fim:len (text)]    
    ini = text.index ('](')
    fim = text[ini:len (text)].index(')')
    text = text[0:ini] + \
    '<break time="100ms"/>' + \
    text[ini+fim+1:len (text)]
    ini = text.find ("![")

# links
ini = text.find ('[')
while (ini != -1):
    fim = text[ini:len (text)].index (']')
    text = text[0:ini] + \
    '<break time="100ms"/>' + \
    text[ini+1:ini+fim] + text[ini+fim:len (text)]
    ini = text.index ('](')
    fim = text[ini:len (text)].index(')')
    text = text[0:ini] + \
    '<break time="100ms"/>' + \
    ' link para ' + text[ini+2:ini+fim] + \
    '<break time="100ms"/>' + \
    text[ini+1+fim:len (text)]
    ini = text.find ("[")


# strong -> emphasis
ini = text.find ('**')
while (ini != -1):
    text = text.replace ('**', '<emphasis>', 1)
    text = text.replace ('**', '</emphasis>', 1)
    ini = text.find('**')

# <iframe ?
ini = text.find ("<iframe ")
while (ini != -1):
    fim = text[ini:len(text)].index ('</iframe>')
    text = text[0:ini] + text[ini+fim+9:len(text)]
    ini = text.find ("<iframe ")

# <i ?
ini = text.find ("<i ")
while (ini != -1):
    fim = text[ini:len(text)].index ('</i>')
    text = text[0:ini] + text[ini+fim+4:len(text)]
    ini = text.find ("<i ")

# </speak>
text = text + '</speak>'

# output filename
fn = fn.replace (".md", ".ssml")
fn = os.environ['HOME'] + '/' + fn
f = open (fn, 'w')
f.write (text)
f.close ()

print ('Output file: %s' % fn)
print('done.')
    
