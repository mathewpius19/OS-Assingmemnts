There are two Memory Management Techniques: Contiguous, and Non-Contiguous. In Contiguous Technique, executing process must be loaded entirely in main-memory. Contiguous Technique can be divided into:
1)Fixed (or static) partitioning
2)Variable (or dynamic) partitioning

I)Fixed Partitioning:

This is the oldest and simplest technique used to put more than one processes in the main memory.
In this partitioning, number of partitions (non-overlapping) in RAM are fixed but size of each partition may or may not be same. 
As it is contiguous allocation, hence no spanning is allowed. 
Here partition are made before execution or during system configure.

Advantages of Fixed Partitioning –

1)Easy to implement:
Algorithms needed to implement Fixed Partitioning are easy to implement. It simply requires putting a process into certain partition without focussing on the emergence of Internal and External Fragmentation.

2)Little OS overhead:
Processing of Fixed Partitioning require lesser excess and indirect computational power.
Disadvantages of Fixed Partitioning –

3)Internal Fragmentation:
Main memory use is inefficient. Any program, no matter how small, occupies an entire partition. This can cause internal fragmentation.
External Fragmentation:
The total unused space (as stated above) of various partitions cannot be used to load the processes even though there is space available but not in the contiguous form (as spanning is not allowed).

4)Limit process size:
Process of size greater than size of partition in Main Memory cannot be accommodated. Partition size cannot be varied according to the size of incoming process’s size. 
Hence, process size of 32MB in above stated example is invalid.
Limitation on Degree of Multiprogramming:
Partition in Main Memory are made before execution or during system configure. 
Main Memory is divided into fixed number of partition. 
Suppose if there are n1 partitions in RAM and n2 are the number of processes, then n2 <= n1 condition must be fulfilled. 
Number of processes greater than number of partitions in RAM is invalid in Fixed Partitioning.

II)Variable Partitioning –
It is a part of Contiguous allocation technique. It is used to alleviate the problem faced by Fixed Partitioning. 
In contrast with fixed partitioning, partitions are not made before the execution or during system configure. 
Various features associated with variable Partitioning-

Advantages of Variable Partitioning –

1)No Internal Fragmentation:
In variable Partitioning, space in main memory is allocated strictly according to the need of process, hence there is no case of internal fragmentation. There will be no unused space left in the partition.

2)No restriction on Degree of Multiprogramming:
More number of processes can be accommodated due to absence of internal fragmentation. A process can be loaded until the memory is empty.

3)No Limitation on the size of the process:
In Fixed partitioning, the process with the size greater than the size of the largest partition could not be loaded and process can not be divided as it is invalid in contiguous allocation technique. Here, In variable partitioning, the process size can’t be restricted since the partition size is decided according to the process size.

Disadvantages of Variable Partitioning –

1)Difficult Implementation:
Implementing variable Partitioning is difficult as compared to Fixed Partitioning as it involves allocation of memory during run-time rather than during system configure.

2)External Fragmentation:
There will be external fragmentation inspite of absence of internal fragmentation.
For example, suppose in above example- process P1(2MB) and process P3(1MB) completed their execution. Hence two spaces are left i.e. 2MB and 1MB. 
Let’s suppose process P5 of size 3MB comes. The empty space in memory cannot be allocated as no spanning is allowed in contiguous allocation. 
The rule says that process must be contiguously present in main memory to get executed.
Hence it results in External Fragmentation.


User Input:1)Number of Blocks
	   2)Number of Processes
	   3)Size of Each Block
	   4)Size of each process
Ouput:1)Internal Fragmentation
      2)External Fragmentation