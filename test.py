f = open("[month_data] Oseltamivir 2020-02-01~2020-03-01.txt", 'r')
data = f.readlines()

k = 0
for i in data:
    if "\"created_at\":" in i:
        k = k + 1
        print(i)
        print(k)
