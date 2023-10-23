jina="python expt"

for j in jina:
    if(j!=1):
        print(j)

x=["Python","exceptions","try and except"]


try:
    for i in range(5):
        print(f"The index and elements from list is {i,x[i]}")
except:
    print("The index is out of range")