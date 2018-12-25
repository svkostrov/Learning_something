b = {"test" : 1, "test_2" : "Test22"}

print(b["test_2"])


dd = dict (short="1", long="2")
dd["short"]="22"
print(dd)


ddd = dict ([(23, 34), (56, 11)])
print(ddd)

d1= dict.fromkeys(["a", "b"], 1)
print(d1)


dw = {a: a ** 2 for a in range(7)}
print(dw)