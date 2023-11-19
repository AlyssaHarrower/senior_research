#signature variable
sig = '010011101'

#opens target 'malicious' file and reads it
f = open('module1.exe', 'b+r')
filebin = f.read()

#checks for binary signature in file binary
if sig in filebin:
    print("detected")
else:
    print("not detected")
