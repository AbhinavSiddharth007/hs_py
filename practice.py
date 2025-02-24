def test(y):
    y(0) = 10
    return 20

y = [1]
test(y)
print(y)

