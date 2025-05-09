
#task1 (1-9 matrix):

i = 1
j = 1
k = 1

while (j<4):
    while (k<4):
        print(i , end=" ")
        i+=1
        k+=1
    print("\n")
    k=1
    j+=1



#task2 (patterns):

#1

"""
for(int i=0 ; i<4 ; i++){
    for(int j=0 ; j<2 ; j++){
        cout << "*";
    }
    cout << " ";
}
"""

for i in range(4):
    for j in range(2):
        print("*", end=" ")
    print(" " , end=" ")
print("\n\n")



#2.
"""
int x=2, flag=0;
for(int i=0 ; i<3 ; i++){
    if(flag==0){
        x=2; flag=1;
    }
    else{
        x=1; flag=0;
    }
   
    for(int j=0 ; j<x ; j++)
       cout << "*";
    cout << " ";
}
"""

x = 2
flag = 0
for i in range(3):
    if flag == 0:
        x = 2
        flag = 1
    else:
        x = 1
        flag = 0

    for j in range(x):
        print("*", end=" ")
    print(" ", end=" ")   
print("\n\n")



#3.
"""
int x=1;
for(int i=1 ; i<=4 ; i++){
    for(int j=0 ; j<x ; j++)
        cout << x << " ";
    x++;
}
"""

x = 1
for i in range(1, 5):
    for j in range(x):
        print(x, end=" ")
    x+=1
print("\n\n")



4.
"""
int x=1;
for(int i=1 ; i<=4 ; i++){
    for(int j=1 ; j<=x ; j++)
        cout << 2*j-1 << " ";
    cout << " ";
    x++;
}
"""

x=1
for i in range(1,5):
    for j in range(1,x+1):
        print(2*j-1, end=" ")
    print(" ", end=" ")
    x+=1