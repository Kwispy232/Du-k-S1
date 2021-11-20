def main():
    stav = ["s0","s1","s2","s3"]
    vyst = ["zelená","červená"]
    stavID = 0
    vystID = 0
    beh = True
    while beh: 
        if (int(input("zadaj a 1/0 >> ")) == 1):
            a = True
        else:
            a = False
        if (int(input("zadaj b 1/0 >> ")) == 1):
            b = True
        else:
            b = False
        match stav[stavID]:
            case "s0":
                if(a == 0 and b == 0):
                    stavID = 0
                    vystID = 0
                elif(a == 1 and b == 0):
                    stavID = 0
                    vystID = 0
                elif(a == 1 and b == 1):
                    stavID = 0
                    vystID = 0
                elif(a == 0 and b == 1):
                    stavID = 1
                    vystID = 0
            case "s1":
                if(a == 0 and b == 0):
                    stavID = 1
                    vystID = 0
                elif(a == 1 and b == 0):
                    stavID = 2
                    vystID = 1
                elif(a == 0 and b == 1):
                    stavID = 1
                    vystID = 0
                elif(a == 1 and b == 1):
                    stavID = 0
                    vystID = 0
            case "s2":
                if(a == 0 and b == 0):
                    stavID = 1
                    vystID = 0
                elif(a == 1 and b == 0):
                    stavID = 2
                    vystID = 1
                elif(a == 0 and b == 1):
                    stavID = 3
                    vystID = 1
                elif(a == 1 and b == 1):
                    stavID = 2
                    vystID = 1
            case "s3":
                if(a == 0 and b == 0):
                    stavID = 3
                    vystID = 1
                elif(a == 0 and b == 1):
                    stavID = 3
                    vystID = 1
                elif(a == 1 and b == 1):
                    stavID = 2
                    vystID = 1
        print("Aktuálny stav:",stav[stavID])
        print("Semafór",vyst[vystID])
        if (input("pokračovať ano/nie>> ") == "ano"):
            beh = True
        else:
            beh = False
        
main()