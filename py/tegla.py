from teglalap import Téglalap

t1 = Téglalap()
print("A t1 kerület: {0}, területe:{1}".format(t1.GetKerület(),t1.GetTerület()))

t1.SetA(12)
t1.SetB(56)
print(f"A t1 kerület: {t1.GetKerület()},területe: {t1.GetTerület()}")

