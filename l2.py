a = [[1,2,3,4],
     [2,3,4,6],
     [3,4,5,8],
     [3,4,5,9]]
def triangle(a):
    if len(a) == len(a[0]):
        data = []
        e = len(a)
        x = -1
        for i in range(e - 1, -1, -1):
            for j in range(len(a[i]) - 1, x, -1):
                data.append(a[i][j])
            x += 1
        return (data)
    else:
        return ('не квадратная')
print(triangle(a))
