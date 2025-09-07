def so_chan_hoan_hao(n):
    if n <= 0:
        return False
    tong_uoc_so_chan = 0
    for i in range(1, n):
        if n % i == 0 and i % 2 == 0:
            tong_uoc_so_chan += i
    return tong_uoc_so_chan == n

def kiem_tra_so(so):
    if so_chan_hoan_hao(so):  
        print(f"{so} là số chẵn hoàn hảo.")
    else:
        print(f"{so} không phải là số chẵn hoàn hảo.")

kiem_tra_so(28)
kiem_tra_so(6)
kiem_tra_so(12)