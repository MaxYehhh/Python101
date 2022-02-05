var = input("Please enter number of cities , number of base stations , covering radius: ")
var = var.split()
n = int(var[0])
p = int(var[1])
d = int(var[2])
pos = []
population = []
dst_list = [[] for i in range(n)]
cover_p_list = []
total_cover_p = 0
num = []

# 建立座標與人口數List
for i in range(n):
    pos.append(input().split())
    population.append(pos[i][2])
    del pos[i][2]
    for j in range(2):
        pos[i][j] = int(pos[i][j])
for k in range(n):
    population[k] = int(population[k])

# 計算城鎮之間的距離 & 各城鎮cover人口數
for x in range(p):
    cover_p_list = []
    for i in range(n):
        cover_p = 0
        for j in range(n):
            dst = ((pos[i][0] - pos[j][0]) **2 + (pos[i][1] - pos[j][1]) **2) ** 0.5
            if x == 0:
                dst_list[i].append(dst)
            if dst <= d:
                cover_p += population[j]
            if j == n - 1:
                cover_p_list.append(cover_p)

    total_cover_p += max(cover_p_list)
    num.append(cover_p_list.index(max(cover_p_list)) + 1)

    # 將已覆蓋的城鎮人口數歸零
    for k in range(n):
        if dst_list[cover_p_list.index(max(cover_p_list))][k] <= d:
            population[k] = 0

# print(num)
# print(cover_p_list)
# print(dst_list)
# print(population)
# print(total_cover_p)

print(*num , total_cover_p)