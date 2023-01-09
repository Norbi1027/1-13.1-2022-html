from teglalap import téglalap_hasab

t1 = téglalap_hasab()

t1.seta(10)
t1.setb(12)
t1.setm(30)

print(f"A téglalap hasáb felülete {t1.getfelület()}, a térfogata{t1.gettérfogat()} ")