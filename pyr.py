

def top_view(n) :
    def corner(num) :
        if(num == 0) :
            return 
        for i in range(num) :
            print("* ",end = "  ")   

    stars = []
    for i in range(n+1) :
        stars.append(4*i + 1) 
    corners = 0 
    track = -1
    # middle = 1 
    # print(stars) 
    for i in range(2*(n+1)-1) :
        if(i%2 == 0) :
            corner(corners) 
            
            for j in range(stars[track])  :
                print("* ",end="")
            track -= 1
            print(" ",end=" ")
            corner(corners)
            corners += 1
            print()
        else :
            corner(corners) 
            
            for k in range(stars[-1]-2*i -1 ) :
                print("  ",end ="") 

            corner(corners)

            print() 
    corners = n    
    starting = 3 
    track = 1 
    for i in range(2*n) :
        if(i%2 == 0) :
            
            corner(corners)          
            for k in range(starting-1 ) :  ## ulta chala doya 
                print("  ",end ="") 

            corner(corners)
            corners -= 1
            starting += 4
            print()
        else :
            corner(corners) 
            
            for j in range(stars[track])  :
                print("* ",end="")
            track += 1
            print(" ",end=" ")
            corner(corners)
            # corners += 1
            print()
        

def side_view(n) :
    spaces = n*2
    k = 0
    for rows in range(n+1) :
        for i in range(spaces) :
            print(" ",end=" ") 
        for j in range(4*k + 1) :
            print("*",end=" ") 
        for i in range(spaces) :
            print(" ",end=" ") 
        spaces -= 2 
        k += 1
        print() 


def main() :
    n = int(input("enter the sweet value for n : ")) 

    flag  = 1 ## 1--> top view , 0 --> sode voew 

    top_view(n) 
    while True : 
        print("MENU FOR THE TERMINAL APPLICATION ") 
        print("A. switch view ")
        print("B. exit         ") 
        a = input("enter your response : ") 
        if(a.lower() == "a") :
            if(flag == 1) :
                flag = 0 
                side_view(n) 
            else :
                flag = 1 
                top_view(n) 

        else : 
            print("THANK YOU FOR CHOOSING US FOR VISUALISING") 
            break 


if(__name__ == "__main__") :
    main() 





    

    
    