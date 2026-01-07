# file = open("Enigme1.txt","r")
# list_words = []
# result = []
# for line in file:
#     for word in line.split():
#         list_words.append(word)
# file.close()
# for i in range(0,len(list_words)):
#     result += chr(int(list_words[i]))
# result = "".join(result)
# list_words = " ".join(list_words)
# print(result)
# print(list_words)
for S in range (1, 10):
    for E in range (10):
        if E != S:
            for N in range (10):
                if N != E and N != S:
                    for D in range (10):
                        if D != E and D != S and D != N:
                            for M in range (1, 10):
                                if M != E and M != S and M != N and M != D:
                                    for O in range (10):
                                        if O != E and O != S and O != N and O != D and O != M:
                                            for R in range (10):
                                                if R != O and R != S and R != N and R != D and R != M and R != E:
                                                    for Y in range (10):
                                                        if Y != R and Y != O and Y != S and Y != N and Y != D and Y != M and Y != E:
                                                            if ((1000*S+100*E+10*N+D) + (1000*M+100*O+10*R+E) == (10000*M+1000*O+100*N+10*E+Y)):
                                                                print ("SEND=  ",1000*S+100*E+10*N+D)
                                                                print("MORE=  ", 1000*M+100*O+10*R+E)
                                                                print ("MONEY=",10000*M+1000*O+100*N+10*E+Y)