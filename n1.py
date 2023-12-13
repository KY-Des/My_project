def TimeToHMS(T):
    H = T // 3600
    T -= H*3600
    M = T // 60
    T -= M*60
    S = T
    return H,M,S
print(TimeToHMS(int(input("T1 = "))))
print(TimeToHMS(int(input("T2 = "))))
print(TimeToHMS(int(input("T3 = "))))
print(TimeToHMS(int(input("T4 = "))))
print(TimeToHMS(int(input("T5 = "))))
print("Конец")

