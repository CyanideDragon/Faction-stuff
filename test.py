import random
import secrets
import csv
fac_stf = True

allied = "Allied"
peace = "Peace"
war = "War"

data = []
with open("politics.csv") as G:
    for i in G:
        j=i.strip().split(",")
        data.append(j)

def conti():
    go_tf = int(input('''What would you like to do?
    1: View faction relations
    2: manually change faction relations.
    3: Advance faction relation change.'''))
    return go_tf

def man_fac_cng():
    it_works = True
    dis_fac_rel()
    while it_works == True:
        it_works = False
        man_fac1 = int(input('''What is the first faction? (type 11 to quit)
        1: Sand
        2: Mud
        3: Sky
        4: Sea
        5: Ice
        6: Rain
        7: Night
        8: Hyd
        9: Hood
        10: Storm'''))
        if man_fac1 != 11:
            man_fac2 = int(input('''What is the second faction?
            1: Sand
            2: Mud
            3: Sky
            4: Sea
            5: Ice
            6: Rain
            7: Night
            8: Hyd
            9: Hood
            10: Storm'''))
            if man_fac1 != man_fac2:
                fac_to_cng = data[man_fac1][man_fac2]
                var_flip = 0
                if len(fac_to_cng) <1:
                    fac_to_cng = data[man_fac2][man_fac1]
                    var_flip = 1
                print(f"You chose {data[0][man_fac1]} and {data[0][man_fac2]} with a relation of{fac_to_cng}")
                t_or_f = input("Is this correct?")
                if t_or_f.lower() == "yes":
                    new_rel = input("What is the new relation?")
                    if var_flip == 0:
                        data[man_fac1][man_fac2] = new_rel
                    elif var_flip == 1:
                        data[man_fac2][man_fac1] = new_rel
                    dis_fac_rel()
                else:
                    it_works = True
            else:
                print("You cannot choose the same faction twice!")
                it_works = True

def aut_fac_cng():
    for i, s in enumerate(data): #eneumerate assigns an index number to the first vale, and the actual data value to the second value
        for a, t in enumerate(s):
            if len(t) > 0 and len(t)<= 4 and t != "N/A":
                n = int(t)
                rng_pn = random.randint(1,2)
                rng = random.randint(1,10)
                if rng_pn == 1:
                    n = n + (-2 * rng)
                else:
                    n += rng
                if n >200:
                    n = 200
                elif n <-200:
                    n = -200
                data[i][a] = t.replace(t, str(n)) #This type of replace requires that the second value be a string, and state what is being replaced with what.
                print(n)
    dis_fac_rel()

def dis_fac_rel():
    for s in data:
        for t in s:
            print(f"{t:14}", end = " ")
        print('',sep='\n')


while fac_stf == True:
    go_tfc = conti()
    if go_tfc == 1:
        dis_fac_rel()
    if go_tfc == 2:
        dis_fac_rel()
        man_fac_cng()
    if go_tfc == 3:
        aut_fac_cng()


    #print(f"{data[4][9]}") This prints out a specific y, x coordinate. First number is the index, the second number is the index of the list item inside the