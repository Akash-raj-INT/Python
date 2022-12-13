a =list(map(int ,input('list: ').split(',')))
a.sort()
print(a[-1]**2, a[0]**2, abs(a[-1]**2-a[0]**2), sep='\n')