def main():
    s0 = {"a0b0":"s0","a1b0":"s0","a1b1":"s0","a0b1":"s1"}
    s1 = {"a0b0":"s1","a1b0":"s2","a1b1":"s0","a0b1":"s1"}
    s2 = {"a0b0":"s1","a1b0":"s2","a1b1":"s2","a0b1":"s3"}
    s3 = {"a0b0":"s3","a1b0":"","a1b1":"s2","a0b1":"s3"}
    pr_tab = {"s0" : s0,"s1" : s1,"s2": s2,"s3": s3}

    stav = "s0"
    s = s0

    beh = True
    while beh: 
        kluc = input(str("zadaj vstup v tvare aXbX(napr. a0b0) >> "))
        s = pr_tab.get(stav)
        stav = s.get(kluc)
        print("Aktuálny stav:",stav)
        print("Semafór","zelená" if stav == "s3" else "červená")
        if (input("pokračovať ano/nie>> ") == "ano"):
            beh = True
        else:
            beh = False
     
main()
