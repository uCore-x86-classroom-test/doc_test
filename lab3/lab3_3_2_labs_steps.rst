实验执行流程概述
================

本次实验主要完成ucore内核对虚拟内存的管理工作。其总体设计思路还是比较简单，即首先完成初始化虚拟内存管理机制，即需要设置好哪些页需要放在物理内存中，哪些页不需要放在物理内存中，而是可被换出到硬盘上，并涉及完善建立页表映射、页访问异常处理操作等函数实现。然后就执行一组访存测试，看看我们建立的页表项是否能够正确完成虚实地址映射，是否正确描述了虚拟内存页在物理内存中还是在硬盘上，是否能够正确把虚拟内存页在物理内存和硬盘之间进行传递，是否正确实现了页面替换算法等。lab3的总体执行流程如下。

首先是初始化过程。参考ucore总控函数init的代码，可以看到在调用完成虚拟内存初始化的vmm_init函数之前，需要首先调用pmm_init函数完成物理内存的管理，这也是我们lab2已经完成的内容。接着是执行中断和异常相关的初始化工作，即调用pic_init函数和idt_init函数等，这些工作与lab1的中断异常初始化工作的内容是相同的。

在调用完idt_init函数之后，将进一步调用三个lab3中才有的新函数vmm_init、ide_init和swap_init。这三个函数涉及了本次实验中的两个练习。第一个函数vmm_init是检查我们的练习1是否正确实现了。为了表述不在物理内存中的“合法”虚拟页，需要有数据结构来描述这样的页，为此ucore建立了mm_struct和vma_struct数据结构（接下来的小节中有进一步详细描述），假定我们已经描述好了这样的“合法”虚拟页，当ucore访问这些“合法”虚拟页时，会由于没有虚实地址映射而产生页访问异常。如果我们正确实现了练习1，则do_pgfault函数会申请一个空闲物理页，并建立好虚实映射关系，从而使得这样的“合法”虚拟页有实际的物理页帧对应。这样练习1就算完成了。

ide_init和swap_init是为练习2准备的。由于页面置换算法的实现存在对硬盘数据块的读写，所以ide_init就是完成对用于页换入换出的硬盘（简称swap硬盘）的初始化工作。完成ide_init函数后，ucore就可以对这个swap硬盘进行读写操作了。swap_init函数首先建立swap_manager，swap_manager是完成页面替换过程的主要功能模块，其中包含了页面置换算法的实现（具体内容可参考5小节）。然后会进一步调用执行check_swap函数在内核中分配一些页，模拟对这些页的访问，这会产生页访问异常。如果我们正确实现了练习2，就可通过do_pgfault来调用swap_map_swappable函数来查询这些页的访问情况并间接调用实现页面置换算法的相关函数，把“不常用”的页换出到磁盘上。

ucore在实现上述技术时，需要解决三个关键问题：

1. 当程序运行中访问内存产生page
   fault异常时，如何判定这个引起异常的虚拟地址内存访问是越界、写只读页的“非法地址”访问还是由于数据被临时换出到磁盘上或还没有分配内存的“合法地址”访问？
2. 何时进行请求调页/页换入换出处理？
3. 如何在现有ucore的基础上实现页替换算法？

接下来将进一步分析完成lab3主要注意的关键问题和涉及的关键数据结构。
