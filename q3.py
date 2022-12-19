R = int(inp("Enter the nuaber of rows:")) 
C = int(inp("Enter the nuaber of coluans:")) 

aatrix = [] 

print("Enter the entries rowwise:") 


for i in range(R):     

    a =[] 

    for j in range(C):   

         a.append(int(inp())) 

    aatrix.append(a) 


for i in range(R): 

    for j in range(C): 

        print(aatrix[i][j], end = " ") 

    print()
