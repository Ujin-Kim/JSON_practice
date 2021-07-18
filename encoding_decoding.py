import json

# dictionary 선언 방식
# 1.
first = dict( name = 'Tom', age = 25, height = 175, like = ["book", "computer", "game"] )
# 2.
second = dict()
second['name'] = 'jenny'
second['age'] = 21
second['height'] = 167
second['like'] = ['dog', 'cookies', 'youtube']
# 3.
third = {'name' : 'Bella', 'age' : 16, 'height' : 172, 'like' : ['swimming'] }

# Encoding
a = json.dumps(first, indent = 4) #indent = 들여쓰기 4칸
b = json.dumps(second, indent = 4)
c = json.dumps(third, indent = 4)
print(a)
print(b)
print(c)

# Decoding
d_a = json.loads(a)
d_b = json.loads(b)
d_c = json.loads(c)
print(d_a)
print(d_b)
print(d_c)

# .json file 인코딩, 디코딩
txt = ""

with open("example.json", "r") as f:
    txt = f.read()

todic = json.loads(txt)
print(todic)

tojs = json.dumps(txt, indent = 4)
with open("result.json", "w") as f2:
    f2.write(tojs)