arch={}
try:
    with open("arch.text","r", encoding="utf-8") as file:
        for line in file:
            m,info=line.strip().split('|',1)
            d,y,g=info.strip().split('|')
            arch[m]=[d,y,g]
except FileNotFoundError:
    print("There is no archive")
print (arch)
s=input("\nMovie Archive Program\nEnter your choice\nto add movies, A\nto edit movies, E \nto delete movies, D\nto list movies, L\nto filter movies, F\nto sort movies, S\nto quit, Q:  ").upper()
if s=="A":
    while True:
        m=input("\nMovie name? ")
        d=input("Director? ")
        y=input("Year ")
        g=input("Genre ")
        arch[m]=[d,y,g]
        m=input("\nAdd more, enter 'M' or 'Q' ! ").upper()
        if m!='M': break
elif s=='L':
    for i in arch: 
        print(f"{i} : {arch[i]}")
elif s== 'E':
    mov=input("enter the name of the movie to edit : ") 
    s=int(input("what information of that movie to edit?\nEnter 0 for the movie name, 1 for Director Name, 2 for year, 3 for genre  : ")) 
    if s==1 : 
        d=input("Enter Director Name ") 
        (arch[mov])[0]=d   
    elif s==2: 
        r=input("Enter release Date ") 
        (arch[mov])[1]=r 
    elif s==3: 
        g=input("Enter genre ") 
        (arch[mov])[2]=g 
    elif s==0:
        NewMovi=input('enter movie name to update ')
        arch[NewMovi]=arch.pop(mov)
        print(arch)
elif s=='S':
    sel=input("to sort movies, movie/director/year/genre(0/1/2/3) ").upper()
    if sel=='0':
        for i in sorted(arch.keys() ):
            print(f"{i} : {arch[i]}")
    elif sel=='1':
        b={}
        for i in sorted( [ y[0] for x,y in arch.items() ]):
            for j in arch:
                if i==arch[j][0]:
                    b[j]=arch[j]
        print("\nSort by Director")
        for i in b:
            print(f"{i}:{b[i]}")    
    elif sel=='2':
        b={}
        for i in sorted( [ y[1] for x,y in arch.items() ]):
            for j in arch:
                if i==arch[j][1]:
                    b[j]=arch[j]
        print("\nSort by Year")
        for i in b:
            print(f"{i}:{b[i]}") 
    elif sel=='3':
        b={}
        for i in sorted( [ y[2] for x,y in arch.items() ]):
            for j in arch:
                if i==arch[j][2]:
                    b[j]=arch[j]
        print("\nSort by Genre")
        for i in b:
            print(f"{i}:{b[i]}") 
        
#     else: print("Please enter a valid input ") 
elif s=="F":
    sel=input("Enter Y, for YEAR; type G, for GENRE; to filter  ").upper()
    if sel=="G":
        s=input("enter genre?: ")
        for x,y in arch.items():
            if y[2]==s:
                print(f"{x}, {y}")
    elif sel=="Y":
        s=input("enter year?: ").upper()
        for x,y in arch.items():
            if y[1]==s:
                print(f"{x} | {y}")
elif s=='D': 
    mov=input("enter the name of the movie to delete : ") 
    del arch[mov] 

with open("arch.text","w", encoding="utf-8") as file:
    for movie,info in arch.items():
        file.write(f"{movie}|{info[0]}|{info[1]}|{info[2]}\n")