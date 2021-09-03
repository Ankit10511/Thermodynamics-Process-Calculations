import math

p1 = eval(input("Enter P1 : "))
v1 = eval(input("Enter V1 : "))
t1 = eval(input("Enter T1 : "))
p2 = eval(input("Enter P2 : "))
v2 = eval(input("Enter V2 : "))
t2 = eval(input("Enter T2 : "))
Cv = eval(input("Enter Cv : "))
Cp = eval(input("Enter Cp : "))

if p1 == p2:
    process = 'isobaric'
elif t1 == t2:
    process = 'isothermal'
elif v1 == v2:
    process = 'isochoric'
else:
    process = 'adiabatic'

r = 8.314
if process == 'isobaric':
    u = Cv * (t2-t1)
    h = Cp * (t2-t1)
    q = h
    w = -r * (t2-t1)
    print("Type of Process : ", process, "\nChange in Internal Energy : ", u, "\nHeat : ", q, "\nChange in Enthalpy : ", h, "\nWork : ", w)
elif process == 'isothermal':
    u = h = 0
    q = r * t1 * math.log(v2/v1)
    w = -q
    print("Type of Process : ", process, "\nChange in Internal Energy : ", u, "\nHeat : ", q, "\nChange in Enthalpy : ", h, "\nWork : ", w)
elif process == 'isochoric':
    u = Cv * (t2 - t1)
    h = Cp * (t2 - t1)
    q = u
    w = -p1 * (v2 - v1)
    print("Type of Process : ", process, "\nChange in Internal Energy : ", u, "\nHeat : ", q, "\nChange in Enthalpy : ", h, "\nWork : ", w)
elif process == 'adiabatic':
    gamma = Cp/Cv
    u = w = Cv * (t2 - t1)
    q = 0
    h = Cp * (t2 - t1)
    print("Type of Process : ", process, "\nChange in Internal Energy : ", u, "\nHeat : ", q, "\nChange in Enthalpy : ", h, "\nWork : ", w, "\nGamma : ", gamma)






