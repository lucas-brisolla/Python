

palavra = "pYtHoN"
numero  = str(1000000)
 

print(palavra.lower(), palavra.upper(), palavra.title(),  sep=" ")
print("&".join(palavra))


palavra = "       pYtHoN   "


print(palavra.strip())
print(palavra.rstrip())
print(palavra.lstrip())

print(palavra.center(12, (".")))
print(".".join(numero))
