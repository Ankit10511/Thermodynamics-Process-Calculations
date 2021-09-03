x = eval(input("Enter Type of System ( 1 - Isolated System and 2 - Closed System ) : "))
if x == 1:
    Q = eval(input("Enter Value of Heat (Q) : "))
    print("Work Done :", Q)
else:
    Q = eval(input("Enter Value of Heat (Q) : "))
    U = eval(input("Enter Value of Internal Energy (U) : "))
    print("Work Done : ", U-Q)
