t1 = (1, 2, 3)
t2 = 5, 6, 7
print(type(t1), type(t2))

print(t1[2])
print(t2[1:])
t3= t1 + t2
print(t3)

t4 = t1*4
print(t4)

print(len(t4))



#딕셔너리
d1 = {"사과": 1000, "바나나" : 500}
print(type(d1))

d1["망고"] = 400
print(d1)

del d1["바나나"]
print(d1)

v1 = d1["사과"]
print(v1)

print(d1)
print(d1.keys())
print(d1.values())

d1.items()
print(d1.items())



v2 = d1.get("바나나")
print(v2)

print("호랑이" in d1)




















