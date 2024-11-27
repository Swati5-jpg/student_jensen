nr1 = 5
nr2 = 7
sum = nr1 +nr2
print(sum)

def count_banana(fruits):
    count = 0
    for f in fruits:
        if f == "banana":
            count += 1
    return count
fruits =["banana","apple","appelsin","banana"]
count =count_banana(fruits)
print(count)  