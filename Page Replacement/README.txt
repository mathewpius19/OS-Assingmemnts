In an operating system that uses paging for memory management, a page replacement algorithm is needed to decide which page 
needs to be replaced when new page comes in.

Page Fault – A page fault happens when a running program accesses a memory page that is mapped into the virtual address space,
but not loaded in physical memory.

This is a menu-driven python program simulating various page replacement alogrithms as given below:
1) Optimal Page Replacement algorithm → this algorithms replaces the page which will not be referred for so long in future. 
Although it can not be practically implementable but it can be used as a benchmark. Other algorithms are compared to this in terms 
of optimality.

2) Least recent used (LRU) page replacement algorithm → this algorithm replaces the page which has not been referred for a long time. 
This algorithm is just opposite to the optimal page replacement algorithm. In this, we look at the past instead of staring at future.

3) FIFO → in this algorithm, a queue is maintained. The page which is assigned the frame first will be replaced first. In other words,
 the page which resides at the rare end of the queue will be replaced on the every page fault.


User input:1)No of pages
	   2)Each page to be entered
	   3)Frame size
Output:1)No of misses.
       2)No of hits.
       3)Miss rate. 