aktualis_ido = int(input("Írd be a jelenlegi időt: "))
csengetes_ido = int(input("Írd be máhny óra múlva csörögkön az óra: "))

for i in range(0, csengetes_ido):
   if aktualis_ido == 23:
      aktualis_ido = 0
   else:
      aktualis_ido += 1

print("Az óra",aktualis_ido,"órakkor fog megszólalni!")