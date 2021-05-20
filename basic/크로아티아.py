alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

string = input()

for i in alpha:
    if i in string:
        string = string.replace(i,' ')
print(len(string))