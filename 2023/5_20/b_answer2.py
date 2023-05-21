import copy
H, W = map(int, input().split())
M = [input() for _ in range(H)]
 
dists = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
 
SNUKE = "snuke"
def check_snuke(cur):
    if 0 <= cur[0]+d_y <= H-1 and 0 <= cur[1]+d_x <= W-1:
        if M[cur[0]+d_y][cur[1]+d_x] == SNUKE[len(ans)]:
            cur[0] += d_y
            cur[1] += d_x
            ans.append(copy.copy(cur))
            if len(ans) < len(SNUKE):
                check_snuke(cur)
 
 
def call_ans(ans):
    for y, x in ans:
        print(y+1, x+1)
 
for h in range(H):
    for w in range(W):
        if M[h][w] == SNUKE[0]:
            ans = []
            ans.append([h, w])
            for d_y, d_x in dists:
                check_snuke([h, w])
                if len(ans) < len(SNUKE):
                    ans = ans[:1]
                    continue
                else:
                    call_ans(ans)
                    exit()