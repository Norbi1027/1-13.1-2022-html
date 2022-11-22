xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

def jegy():
    for x in xs:
        if x<60:
            print("Ez sajnos egyes :(")

        if x>=60 and x<70:
            print("Ez egy kettecske lett")

        if x>=70 and x<80:
            print("Ez egy hármas lett")

        if x>=80 and x<90:
            print("Ez egy négyes lett")

        if x>=90:
            print("Ötööös")

jegy()