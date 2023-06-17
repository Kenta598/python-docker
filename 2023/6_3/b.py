N = int(input())

N_str = str(N)
N_step = len(N_str)
kirisute = N_step -3

N_ls = list(N_str)

if kirisute > 0:
    for i in range(1,kirisute+1):
        N_ls[-i] = '0'

print(int(''.join(N_ls)))