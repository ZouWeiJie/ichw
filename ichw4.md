# 1.	解释作业、进程、线程的概念，进程和线程概念的提出分别解决了什么问题
## 作业：用户要求计算机完成的所有任务和工作的集合
## 进程：进程是指在系统中能独立运行并作为资源分配的基本单位，它由一组机器指令，数据和堆栈等组成，是一个能独立运行的活动实体。
## 线程：线程是进程中的一个实体，是被系统独立调度和分派的基本单位。
## 进程概念的提出解决的问题：使得系统资源的分配和调度可独立进行，任何进程都可与其它进程一起并发执行，效率提高
## 线程概念的提出解决的问题：线程自己不拥有系统资源，只拥有一点儿在运行中必不可少的资源，但它可与同属一个进程的其它线程共享进程所拥有的全部资源。采用多线程与创建多进程相比创建和撤销线程的开销较小，CPU在线程之间开关时的开销远比进程要少得多增加了通讯的有效性，无需内核参与，因为线程间的通讯是在同一进程的地址空间内的，共享主存和文件。
# 2. 虚拟存储器的概念，描述其工作原理和作用
## 虚拟存储器的概念：对于每一个进程，它所能接触到的地址都不是实际的物理地址，而是通过虚拟地址（虚拟存储器）进行映射而来的，即虚拟存储器提供了一段虚拟地址。
## 工作原理：在每一个进程开始创建的时候，都会分配一个虚拟存储器（就是一段虚拟地址）然后通过虚拟地址和物理地址的映射来获取真实数据，这样进程就不会直接接触到物理地址，甚至不知道自己调用的那块物理地址的数据。
## 虚拟存储器的作用：解决了三个问题
### 1.主存的容量有限。虽然我们现在的主存容量在不断上升，但是我们的进程是无限，如果计算机上的每一个进程都独占一块物理存储器(即物理地址空间)。那么，主存就会很快被用完。但是，实际上，每个进程在不同的时刻都是只会用同一块主存的数据，这就说明了其实只要在进程想要主存数据的时候我们把需要的主存加载上就好，换进换出。针对这样的需求，直接提供一整块主存的物理地址就明显不符合。
### 2.进程间通信的需求。如果每个进程都 独占一块物理地址，这样就只能通过socket这样的手段进行进程通信，但如果进程间能使用同一块物理地址就可以解决这个问题。
### 3主存的保护问题。对于主存来说，需要说明这段内存是可读的，可写的，还是可执行的。针对这点，光用物理地址也是很难做到的，如果利用虚拟存储器提供的虚拟地址就可以很好的解决这个问题。
