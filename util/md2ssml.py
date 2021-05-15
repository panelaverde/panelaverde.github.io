import sys

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

# **?
ini = text.find ('**')
while (ini != -1):
    text = text.replace ('**', '<emphasis>', 1)
    text = text.replace ('**', '</emphasis>', 1)
    ini = text.find('**')

# ![ ?
ini = text.find ("![")
while (ini != -1):
    fim = text[ini:len(text)].find (')')
    text = text[0:ini] + text[ini+fim+1:len(text)]
    ini = text.find ("![")

# <iframe ?
ini = text.find ("<iframe ")
while (ini != -1):
    fim = text[ini:len(text)].find ('</iframe>')
    text = text[0:ini] + text[ini+fim+9:len(text)]
    ini = text.find ("<iframe ")

# <iframe ?
ini = text.find ("<i ")
while (ini != -1):
    fim = text[ini:len(text)].find ('</i>')
    text = text[0:ini] + text[ini+fim+4:len(text)]
    ini = text.find ("<iframe ")

# output filename
fn = fn.replace (".md", ".ssml")
f = open (fn, 'w')
f.write (text)
f.close ()

print ('Output file: %s' % fn)
print('done.')
    
