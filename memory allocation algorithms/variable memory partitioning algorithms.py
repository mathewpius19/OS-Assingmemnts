#Variable First Fit
def firstfit(block_size,blockno,process_size,processno): 
    #no block is assigned to any process initially
    allocation = [-1] * processno #This stores id of each process that is entered by user 
    for i in range(processno): 
        for j in range(blockno): 
            if block_size[j] >= process_size[i]:#first fit condition is checked 
                  
                 
                allocation[i] = j  
  
                 
                block_size[j] -= process_size[i]#Reduces remaining memory of block.  
                break
  
    print(" Process No|Process Size|Block no.") 
    for process in range(processno): 
        print(" ", process + 1, "       |     ", process_size[process],  
                          end = "   |  ")  
        if allocation[process] != -1:  
            print(allocation[process] + 1)  
        else: 
            print("Not Allocated") 
    
    print("Internal Fragmentation=0\n")#no internal fragmentation
    leftspace=0
    for i in range(blockno):
        leftspace+=block_size[i]
    external_frag=[]
    for i in range(processno):
        if allocation[i]==-1:#checking all unallocated processes to calculate external fragmentation 
            external_frag.append(process_size[i])
    if len(external_frag)==0:#to check if its zero
        print("External fragmentation is 0")
    for i in range(len(external_frag)):
        high=i
        for j in range(i+1,len(external_frag)):
            if external_frag[j]>external_frag[high]:#arranges the processes in descending order
                high=j
        temp=external_frag[i]
        external_frag[i]=external_frag[high]
        external_frag[high]=temp
    for i in range(len(external_frag)):
        if external_frag[i]<=leftspace:
            print("External fragmentation is",external_frag[i])



def bestfit(block_size, blockno, process_size, processno):  
    #no block is assigned to any process initially
    allocation = [-1] * processno #This stores id of each process that is entered by user 
    for i in range(processno): 
          
        
        best_index = -1
        for j in range(blockno): 
            if block_size[j] >= process_size[i]: #best fit condition is checked
                if best_index == -1:  
                    best_index = j  
                elif block_size[best_index] > block_size[j]:  
                    best_index = j 
  
      
        if best_index != -1: #to check if we can find block for current process
              
             
            allocation[i] = best_index  
  
             
            block_size[best_index] -= process_size[i]#Reduces remaining memory of block. 
  
    print(" Process No|Process Size|Block no.") 
    for process in range(processno): 
        print(" ", process + 1, "       |     ", process_size[process],  
                          end = "   |  ")  
        if allocation[process] != -1:  
            print(allocation[process] + 1)  
        else: 
            print("Not Allocated") 

    print("Internal Fragmentation=0\n")#no internal fragmentation
    leftspace=0
    for i in range(blockno):
        leftspace+=block_size[i]
    external_frag=[]
    for i in range(processno):
        if allocation[i]==-1:#checking all unallocated processes to calculate external fragmentation 
            external_frag.append(process_size[i])
    if len(external_frag)==0:
        print("External fragmentation is 0")#checks if its zero
    for i in range(len(external_frag)):
        high=i
        for j in range(i+1,len(external_frag)):
            if external_frag[j]>external_frag[high]:#arranges the processes in descending order
                high=j
        temp=external_frag[i]
        external_frag[i]=external_frag[high]
        external_frag[high]=temp
    for i in range(len(external_frag)):
        if external_frag[i]<=leftspace:
            print("External fragmentation is",external_frag[i])
        
def worstfit(block_size, blockno, process_size, processno): 
      
    # Stores block id of the block  
    # allocated to a process  
      
    # Initially no block is assigned  
    # to any process  
    allocation = [-1] * processno
      
    # pick each process and find suitable blocks  
    # according to its size ad assign to it  
    for i in range(processno): 
          
        # Find the best fit block for  
        # current process  
        wstIdx = -1
        for j in range(blockno): 
            if block_size[j] >= process_size[i]: 
                if wstIdx == -1:  
                    wstIdx = j  
                elif block_size[wstIdx] < block_size[j]:  
                    wstIdx = j 
  
        # If we could find a block for  
        # current process  
        if wstIdx != -1: 
              
            # allocate block j to p[i] process  
            allocation[i] = wstIdx  
  
            # Reduce available memory in this block.  
            block_size[wstIdx] -= process_size[i] 
  
    print(" Process No|Process Size|Block no.") 
    for process in range(processno): 
        print(" ", process + 1, "       |     ", process_size[process],  
                          end = "   |  ")  
        if allocation[process] != -1:  
            print(allocation[process] + 1)  
        else: 
            print("Not Allocated")             
   

    print("Internal Fragmentation=0 \n")#no internal fragmentation
    leftspace=0
    for i in range(blockno):
        leftspace+=block_size[i]
    external_frag=[]
    for i in range(processno):
        if allocation[i]==-1:#checking all unallocated processes to calculate external fragmentation 
            external_frag.append(process_size[i])
    if len(external_frag)==0:
        print("External fragmentation is 0")#checks if its zero
    for i in range(len(external_frag)):
        high=i
        for j in range(i+1,len(external_frag)):
            if external_frag[j]>external_frag[high]:#arranges the processes in descending order
                high=j
        temp=external_frag[i]
        external_frag[i]=external_frag[high]
        external_frag[high]=temp
    for i in range(len(external_frag)):
        if external_frag[i]<=leftspace:
            print("External fragmentation is",external_frag[i])
        
        
   
if __name__ == '__main__':  
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
  
    print("\n 1)Variable First Fit \n 2)Variable Best Fit \n 3)Variable Worst Fit")
    ch=int(input("Enter the choice"))
    try:
        if not(ch==1 or ch==2 or ch==3):
            raise Exception
    except Exception:
        print("Invalid Input")
    else:
        if ch==1:
           firstfit(block_size, blockno, process_size, processno)
        elif ch==2:
            bestfit(block_size, blockno, process_size, processno)
        else:
           worstfit(block_size, blockno, process_size, processno)