from difflib import SequenceMatcher #importing comparison library

#opens target 'malicious' file and reads it
#f = open('module1.exe', 'b+r')
#filebin = f.read()
#f.close()

#opens target 'malicious' file and reads it
#r = open('module2.exe', 'b+r')
#filebin2 = r.read()
#r.close()

#stand-in to test program
test1 = '01111011110101'
test2 = '0111100000101010'

match = SequenceMatcher(None,test1 ,test2).find_longest_match()

print(match)  # -> Match(a=0, b=15, size=9)
print(test1[match.a:match.a + match.size])  # -> 011110
print(test2[match.b:match.b + match.size])  # -> 011110
