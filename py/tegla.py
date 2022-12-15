from teglalap import teglalap

t1 = teglalap()
print("A t1 kerület: {0}","területe:{1}".format(t1.getkerulet(),t1.getterulet()))

t1.setA(12)
t1.setB(56)
print(f"A t1 kerület: {t1.getkerulet()},területe: {t1.getterulet()}")