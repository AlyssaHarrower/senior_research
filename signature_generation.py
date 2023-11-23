from difflib import SequenceMatcher #importing comparison library

#opens target 'malicious' file and reads it
f = open('test1.exe', 'b+r')
filedata = str(f.read())
f.close()

#opens target 'malicious' file and reads it
r = open('test2.exe', 'b+r')
filedata2 = str(r.read())
r.close()

filebin = ''.join(format(ord(i), '08b') for i in filedata)
filebin2 = ''.join(format(ord(i), '08b') for i in filedata2)

#stand-in to test program
#test1 = '01111011110101'
#test2 = '0111100000101010'

#match = SequenceMatcher(None,filebin,filebin2).find_longest_match()

#print(match)  # -> Match(a=0, b=15, size=9)
#print(filebin[match.a:match.a + match.size])  # -> 011110
#print(filebin2[match.b:match.b + match.size])  # -> 011110
