meraj="either hyderabad/kadapa/Bengaluru"

def travel():
    global meraj
    meraj="or any beautiful country"
    print(meraj)

print(meraj)
travel()

def meraj_nonlocal():
    meraj="Either Hyderabad/kadapa/Bengaluru"
    print(meraj)
    def change():
        nonlocal meraj
        meraj="or only remote"
        print(meraj)
    change()

meraj_nonlocal()
print("i deserve this for the pain and trauma i have been carrying so far")