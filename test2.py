with open("../omfun/aa.png","rb") as f1:
    with open("../omfun/bb.ts","wb") as f2:
        f1.seek(70)
        f2.write(f1.read())
