#Optimal Page Replacement
def optimal(pages,n,capacity):
    frames=[]
    miss=0
    hit=0
    occurance=[None]* capacity
    for page in range(len(pages)):
        if pages[page] in frames:#To check if page is there or not
            hit+=1
        else:#if page is not there then,it goes to next condition
            if len(frames)<capacity:#check if list is full or not
                frames.append(pages[page])#if space is there insert page 
				 
            else: #if there is not space in list
                for i in range(len(frames)):
                    if frames[i] not in pages[page+1:]:#checking if there are future refernces of the specific page
					  
                        frames[i] = pages[page] 
                        break
                    else:
                        occurance[i] = pages[page+1:].index(frames[i]) #if page occurs again then it will be added to occurance
                else:
                    frames[occurance.index(max(occurance))] = pages[page] 
            miss += 1#This increases miss by 1
    
    print("Number of faults are:",miss)
    print("Number of hits are:",hit)
    print("Total number of pages entered are:",n)
    print("Miss rate is:",(miss/n)*100,"%")#calculates the miss rate by dividing misses by number of pages

#First In First Out Page Replacement
def FIFO(pages,n,capacity):
    frames=[]
    fault=0
    top=0
    hit =0
    for page in pages:
        if page not in frames:#checks if the string referenced is there in frame or not
            if len(frames)<capacity:#if not,then checks if frame capacity is full or not
                frames.append(page)#if not then it adds the page
            else:
                frames[top] = page#replaces with the topmost page page.e.first page in the frame
                top = (top+1)%capacity#top updates to next page
            fault += 1#fault is incremented if not found    
        else:
            hit+=1#hit is incremented if found
    print("Total number of pages entered were:",n)
    print("Misses are :",fault)#Displays the misses
    print("Hits are:",hit)#Displays the hits
    print("Miss rate is:",((fault/n)*100),"%")#Calculates the miss rate

#Least Recently Used Page Replacement
def Least_Recent(pages,n,capacity):
    frames = set() #frames in which pages are stored
    indices = {} #in this we store indices of least recently used pages
    fault = 0
    hit=0
    for page in range(n):
        if pages[page] in frames:
            hit+=1
        if (len(frames) < capacity): #check if set can hold more pages
            if (pages[page] not in frames): #if not present in set,add the page indicating page fault
                frames.add(pages[page])
                fault += 1 #increment fault 
            indices[pages[page]] = page #index of Least_Recent page is stored
        else: #if the frame is full,then Least_Recent page is removed from frame
            if (pages[page] not in frames): #page is not present in the frame
                Least_Recent = float('inf') 
                for i in (frames): #with this we find least recently used pages
                    if indices[i] < Least_Recent :
                        Least_Recent = indices[i]
                        item = i
                frames.remove(item) #index of Least_Recent page is removed
                frames.add(pages[page]) #inserting current page into frame
                fault += 1
            indices[pages[page]] = page #update index of current page
        
    print("Number of requests are:",n)
    print("Number of misses are",fault)#displays number of misses
    print("Number of hits are:",hit)#displays number of hits
    print("Miss rate is:",(fault/n)*100,"%")#displays miss rate

if __name__=="__main__":
    n = int(input("How many pages can be entered?"))
    pages = []
    for page in range(n):
        page = int(input("Enter page number "))
        pages.append(page)
    capacity = int(input("Enter the capacity of the frame"))
    print("\n 1)Optimal Page Replacement \n 2)FIFO Page Replacement \n 3)Least_Recent Page Replacement")
    ch=int(input("Enter the choice"))
    try:
        if not(ch==1 or ch==2 or ch==3):
            raise Exception
    except Exception:
        print("Invalid Input")
    else:
        if ch==1:
            optimal(pages,n,capacity)
        elif ch==2:
            FIFO(pages,n,capacity)
        else:
            Least_Recent(pages,n,capacity)

        