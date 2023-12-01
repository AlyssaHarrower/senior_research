from difflib import SequenceMatcher #importing comparison library

#opens target 'malicious' file and reads it
f = open('test1.exe', 'b+r')
filedata = str(f.read())
f.close()

#opens target 'malicious' file and reads it
r = open('test2.exe', 'b+r')
filedata2 = str(r.read())
r.close()

#converts to binary
filebin = ''.join(format(ord(i), '08b') for i in filedata)
filebin2 = ''.join(format(ord(i), '08b') for i in filedata2)

#Find longest matching sequence between both files
match = SequenceMatcher(None,filebin,filebin2).find_longest_match()

#Prints matching sequence and length
print(match) 
print(filebin[match.a:match.a + match.size])  
print(filebin2[match.b:match.b + match.size])

#creates a file to store signature
s = open("BinSignature.txt", "w")
s.write(filebin[match.a:match.a + match.size])
s.close()