# import pickle
# import csv
# dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java', 'mini' : {'A':1,"B":2}}
# dict2 = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
# x = 1
#
# w
# f = open("file.pkl","wb")
# pickle.dump(dict,f)
# pickle.dump(dict2,f)
# pickle.dump(x,f)
# f.close()
#
# f = open('file.pkl','rb')
# data = pickle.load(f)
# f.close()

# print(data)

import re

text = 'Wow this string is that good that I them work well. This is string example....wow!!! This is really string'

word = 'this'
key = '(?i)\\b'+word+'\\b'
new_string = re.sub(key, 'python', text)

new_string
