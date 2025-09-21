# 트로미노

blocks_2 = [
    [[1,0],
    [1,1]],

    [[1,1],
    [0,1]],

    [[0,1],
    [1,1]],

    [[1,1],
    [1,0]]
    ]

blocks_3 = [
    [[1,1,1],
    [0,0,0],
    [0,0,0]],
    
    [[0,0,0],
    [1,1,1],
    [0,0,0]],

    [[0,0,0],
    [0,0,0],
    [1,1,1]],

    [[1,0,0],
    [1,0,0],
    [1,0,0]],
    
    [[0,1,0],
    [0,1,0],
    [0,1,0]],
    
    [[0,0,1],
    [0,0,1],
    [0,0,1]]
    ]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for y in range(n-1):
    for x in range(m-1):

        for i in range(len(blocks_2)):
            shape = blocks_2[i]

            ab_sum = 0
            for a in range(2):
                for b in range(2):
                    ab_sum += shape[a][b] * grid[y+a][x+b]

            # ab_sum 블럭이 위치한 곳의 값의 합
            ans = max(ans,ab_sum)

for y in range(n-2):
    for x in range(m-2):
        
        for i in range(len(blocks_3)):
            shape = blocks_3[i]

            ab_sum = 0
            for a in range(3):
                for b in range(3):
                    ab_sum += shape[a][b] * grid[y+a][x+b]
            
            ans = max(ans,ab_sum)

print(ans)