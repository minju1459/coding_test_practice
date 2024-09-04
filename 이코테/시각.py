h = int(input())
count = 0

# 시간
for i in range(h+1):
    # 분
    for j in range(60):
        #초
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1


print(count)