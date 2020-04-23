def fixed_first_fit(block_size,blockno,process_size,processno):
    frag_list=[]
    process_list=[]
    frag_list=[0]*processno
    process_list=[-1]*processno
    occupied=[]
    allocated=[]
    occupied=[0]*blockno
    allocated=[-1]*blockno
    for i in range(processno):
        for j in range(blockno):
            if occupied[j]==0 and block_size[j]>=process_size[i]:#first fit condition
                process_list[i]=1
                allocated[j]=i
                occupied[j]=1
                frag_list[i]=block_size[j]-process_size[i]
                break
    
    intfrag=0
    for i in range(processno):
        intfrag+=frag_list[i]#calculating internal fragmentation
    print("Total Internal Fragmentation is",intfrag,"\n")

    #calculating external fragmentation
    leftspace=intfrag
    for i in range(blockno):
        if allocated[i]==0:
            leftspace+=block_size[i]
    external_frag=[]
    for i in range(processno):
        if process_list[i]==-1:
            external_frag.append(process_size[i])
    if len(external_frag)==0:
        print("External Fragmentation is 0")

    for i in range(len(external_frag)):
        high=i
        for j in range(i+1,len(external_frag)):
            if external_frag[j]>external_frag[high]:#arranging in descending order
                high=j
        temp=external_frag[i]
        external_frag[i]=external_frag[high]
        external_frag[high]=temp
    for i in range(len(external_frag)):
        if external_frag[i]<=leftspace:
            print("External fragmentation is",external_frag[i])

    
def fixed_best_fit(block_size,blockno,process_size,processno):
    frag_list=[]
    process_list=[]
    lowest=9999
    frag_list=[0]*processno
    process_list=[-1]*processno
    block_list=[]
    block_list=[0]*blockno
    
    
    for i in range(processno):
        for j in range(blockno):
            if block_list[j]!=1:
                temp=block_size[j]-process_size[i]
                if temp>=0:
                    if lowest>temp:#best fit condition
                        process_list[i]=j
                        lowest=temp
        if process_list[i]!=-1:
            frag_list[i]=lowest
            block_list[process_list[i]]=1
            lowest=10000
    intfrag=0
    for i in range(processno):
        intfrag+=frag_list[i]#calculating internal fragmentation
    print("Total Internal Fragmentation is",intfrag,"\n")

    leftspace=intfrag
    for i in range(blockno):
        if block_list[i]==0:
            leftspace+=block_size[i]
    external_frag=[]
    for i in range(processno):
        if process_list[i]==-1:
            external_frag.append(process_size[i])
    if len(external_frag)==0:
        print("External Fragmentation is 0")

    for i in range(len(external_frag)):
        high=i
        for j in range(i+1,len(external_frag)):
            if external_frag[j]>external_frag[high]:#arranging in descending order
                high=j
        temp=external_frag[i]
        external_frag[i]=external_frag[high]
        external_frag[high]=temp
    for i in range(len(external_frag)):
        if external_frag[i]<=leftspace:
            print("External fragmentation is",external_frag[i])

def fixed_worst_fit(block_size,blockno,process_size,processno):
    frag_list=[]
    process_list=[]
    highest=-9999
    frag_list=[0]*processno
    process_list=[-1]*processno
    block_list=[]
    block_list=[0]*blockno
    for i in range(processno):
        for j in range(blockno):
            if block_list[j]!=1:
                temp=block_size[j]-process_size[i]
                if temp>=0:
                    if highest<temp:#worst fit condition
                        process_list[i]=j
                        highest=temp
        
        if process_list[i]!=-1:
            frag_list[i]=highest
            block_list[process_list[i]]=1
            highest=-9999

    intfrag=0
    for i in range(processno):
        intfrag+=frag_list[i]
    print("Total Internal Fragmentation is",intfrag,"\n")

    leftspace=intfrag
    for i in range(blockno):
        if block_list[i]==0:
            leftspace+=block_size[i]
    
    #calculating external fragmentation
    external_frag=[]
    for i in range(processno):
        if process_list[i]==-1:
            external_frag.append(process_size[i])
    if len(external_frag)==0:
        print("External Fragmentation is 0")

    for i in range(len(external_frag)):
        high=i
        for j in range(i+1,len(external_frag)):
            if external_frag[j]>external_frag[high]:
                high=j
        temp=external_frag[i]
        external_frag[i]=external_frag[high]
        external_frag[high]=temp
    for i in range(len(external_frag)):
        if external_frag[i]<=leftspace:
            print("External fragmentation is",external_frag[i])

if __name__=="__main__":
    blockno=int(input("Enter the number of blocks"))
    processno=int(input("Enter the number of process"))
    block_size = []  
    process_size = []
    for i in range(blockno):
        num=int(input("Enter the blocks"))
        block_size.append(num)
    for i in range(processno):
        num=int(input("Enter the processes"))
        process_size.append(num) 
    print("\n 1)Fixed First Fit \n 2)Fixed Best Fit \n 3)Fixed Worst Fit")
    ch=int(input("Enter the choice"))
    try:
        if not(ch==1 or ch==2 or ch==3):
            raise Exception
    except Exception:
        print("Invalid Input")
    else:
        if ch==1:
           fixed_first_fit(block_size, blockno, process_size, processno)
        elif ch==2:
            fixed_best_fit(block_size, blockno, process_size, processno)
        else:
           fixed_worst_fit(block_size, blockno, process_size, processno)
    
    
        
        