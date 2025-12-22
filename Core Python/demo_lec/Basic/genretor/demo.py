def intGenreator(n):
    for i in range(1, n + 1):
        yield i

res = intGenreator(10)

print(next(res))
print(next(res))
print(next(res))
