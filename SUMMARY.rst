Summary
=======

-  `Introduction <README.md>`__

Lab 0
-----

-  `Lab 0 <lab0.md>`__

   -  `实验目的 <lab0/lab0_1_goals.md>`__
   -  `准备知识 <lab0/lab0_2_prepare.md>`__

      -  `了解OS实验 <lab0/lab0_2_1_about_labs.md>`__
      -  `设置实验环境 <lab0/lab0_2_2_environment.md>`__

         -  `开发OS实验的简单步骤 <lab0/lab0_2_2_1_lab_steps.md>`__
         -  `通过虚拟机使用Linux实验环境（推荐：最容易的实验环境安装方法） <lab0/lab0_2_2_2_vm_experiment.md>`__
         -  `安装使用Linux实验环境（适合希望自己安装Linux系统的同学） <lab0/lab0_2_2_3_install.md>`__
         -  `实验中可能使用的软件 <lab0/lab0_2_2_3_1_softwares.md>`__

      -  `了解编程开发调试的基本工具 <lab0/lab0_2_3_tools.md>`__

         -  `gcc的基本用法 <lab0/lab0_2_3_1_gcc_usage.md>`__

            -  `编译简单的 C
               程序 <lab0/lab0_2_3_1_1_compile_c_prog.md>`__
            -  `AT&T汇编基本语法 <lab0/lab0_2_3_1_2_att_asm.md>`__
            -  `GCC基本内联汇编 <lab0/lab0_2_3_1_3_gcc_inline_asm.md>`__
            -  `GCC扩展内联汇编 <lab0/lab0_2_3_1_4_extend_gcc_asm.md>`__

         -  `make和Makefile <lab0/lab0_2_3_2_make_makefile.md>`__
         -  `gdb使用 <lab0/lab0_2_3_3_gdb.md>`__
         -  `进一步的相关内容 <lab0/lab0_2_3_4_further.md>`__

      -  `基于硬件模拟器实现源码级调试 <lab0/lab0_2_4_debug_with_emulator.md>`__

         -  `安装硬件模拟器QEMU <lab0/lab0_2_4_1_install_qemu.md>`__

            -  `Linux运行环境 <lab0/lab0_2_4_1_1_linux_runtime.md>`__
            -  `Linux环境下的源码级安装过程 <lab0/lab0_2_4_1_2_linux_source_install.md>`__

               -  `获得并应用修改 <lab0/lab0_2_4_1_2_1_patch_qemu.md>`__
               -  `配置、编译和安装 <lab0/lab0_2_4_1_2_2_configure_make_install_qemu.md>`__

         -  `使用硬件模拟器QEMU <lab0/lab0_2_4_2_qemu_usage.md>`__

            -  `运行参数 <lab0/lab0_2_4_2_1_qemu_runtime_arguments.md>`__
            -  `常用调试命令 <lab0/lab0_2_4_2_2_qemu_monitor_debug.md>`__

         -  [基于qemu内建模式调试ucore]
         -  `结合gdb和qemu源码级调试ucore <lab0/lab0_2_4_4_gdb_qemu_debug_ucore.md>`__

            -  `编译可调试的目标文件 <lab0/lab0_2_4_4_1_make_obj.md>`__
            -  `ucore 代码编译 <lab0/lab0_2_4_4_2_ucore_make.md>`__
            -  `使用远程调试 <lab0/lab0_2_4_4_3_remote_debug.md>`__
            -  `使用gdb配置文件 <lab0/lab0_2_4_4_4_gdb_config_file.md>`__
            -  `加载调试目标 <lab0/lab0_2_4_4_5_load_debug_target.md>`__
            -  `设定调试目标架构 <lab0/lab0_2_4_4_6_set_debug_arch.md>`__

      -  `了解处理器硬件 <lab0/lab0_2_5_cpu_hardware.md>`__

         -  `Intel
            80386运行模式 <lab0/lab0_2_5_1_intel_80386_modes.md>`__
         -  `Intel 80386内存架构 <lab0/lab0_2_5_2_intel_80386_mem.md>`__
         -  `Intel
            80386寄存器 <lab0/lab0_2_5_3_intel_80386_registers.md>`__

      -  `了解ucore编程方法和通用数据结构 <lab0/lab0_2_6_ucore_programming.md>`__

         -  `面向对象编程方法 <lab0/lab0_2_6_1_oop.md>`__
         -  `通用数据结构双向循环链表 <lab0/lab0_2_6_2_generic_data_structure.md>`__

            -  `双向循环链表 <lab0/lab0_2_6_2_1_linked_list.md>`__

   -  `附录A.ucore实验中的常用工具 <lab0/lab0_ref_ucore-tools.md>`__
   -  `附录B.ucore实验参考资料 <lab0/lab0_ref_ucore-resource.md>`__

Lab 1
-----

-  `Lab 1 <lab1.md>`__

   -  `实验目的 <lab1/lab1_1_goals.md>`__
   -  `实验内容 <lab1/lab1_2_labs.md>`__

      -  `练习 <lab1/lab1_2_1_exercise.md>`__

         -  `练习1 <lab1/lab1_2_1_1_ex1.md>`__
         -  `练习2 <lab1/lab1_2_1_2_ex2.md>`__
         -  `练习3 <lab1/lab1_2_1_3_ex3.md>`__
         -  `练习4 <lab1/lab1_2_1_4_ex4.md>`__
         -  `练习5 <lab1/lab1_2_1_5_ex5.md>`__
         -  `练习6 <lab1/lab1_2_1_6_ex6.md>`__
         -  `扩展练习 <lab1/lab1_2_1_7_ex7.md>`__

      -  `项目组成 <lab1/lab1_2_2_files.md>`__

   -  `从机器启动到操作系统运行的过程 <lab1/lab1_3_booting.md>`__

      -  `BIOS启动过程 <lab1/lab1_3_1_bios_booting.md>`__
      -  `bootloader启动过程 <lab1/lab1_3_2_bootloader.md>`__

         -  `保护模式和分段机制 <lab1/lab1_3_2_1_protection_mode.md>`__
         -  `地址空间 <lab1/lab1_3_2_2_address_space.md>`__
         -  `硬盘访问概述 <lab1/lab1_3_2_3_dist_accessing.md>`__
         -  `ELF文件格式概述 <lab1/lab1_3_2_4_elf.md>`__

      -  `操作系统启动过程 <lab1/lab1_3_3_booting_os.md>`__

         -  `函数堆栈 <lab1/lab1_3_3_1_function_stack.md>`__
         -  `中断与异常 <lab1/lab1_3_3_2_interrupt_exception.md>`__
         -  `lab1中对中断的处理实现 <lab1/lab1_3_3_3_lab1_interrupt.md>`__

   -  `实验报告要求 <lab1/lab1_4_lab_requirement.md>`__
   -  `附录A“关于A20 Gate” <lab1/lab1_appendix_a20.md>`__
   -  `附录B“第一条执行指令” <lab1/lab1_5_appendix.md>`__

Lab 2
-----

-  `Lab 2 物理内存管理 <lab2.md>`__

   -  `实验目的 <lab2/lab2_3_1_phymemlab_goal.md>`__
   -  `实验内容 <lab2/lab2_3_2_phymemlab_contents.md>`__

      -  `练习 <lab2/lab2_3_2_1_phymemlab_exercise.md>`__
      -  `项目组成 <lab2/lab2_3_2_2_phymemlab_files.md>`__

   -  `物理内存管理 <lab2/lab2_3_3_phymem_manage.md>`__

      -  `实验执行流程概述 <lab2/lab2_3_3_1_phymemlab_overview.md>`__
      -  `探测系统物理内存布局 <lab2/lab2_3_3_2_search_phymem_layout.md>`__
      -  `以页为单位管理物理内存 <lab2/lab2_3_3_3_phymem_pagelevel.md>`__
      -  `物理内存页分配算法实现 <lab2/lab2_3_3_4_phymem_allocation.md>`__
      -  `实现分页机制 <lab2/lab2_3_3_5_paging.md>`__

         -  `段页式管理基本概念 <lab2/lab2_3_3_5_1_segment_and_paging.md>`__
         -  `建立段页式管理中需要考虑的关键问题 <lab2/lab2_3_3_5_2_key_problems_in_seg_page.md>`__
         -  `系统执行中地址映射的四个阶段 <lab2/lab2_3_3_5_4_maping_relations.md>`__
         -  `建立虚拟页和物理页帧的地址映射关系 <lab2/lab2_3_3_5_3_setup_paging_map.md>`__

   -  `实验报告要求 <lab2/lab2_3_4_phymemlab_require.md>`__
   -  `附录A.
      探测物理内存分布和大小的方法 <lab2/lab2_3_5_probe_phymem_methods.md>`__
   -  `附录B.
      实现物理内存探测 <lab2/lab2_3_6_implement_probe_phymem.md>`__
   -  `附录C.
      链接地址/虚地址/物理地址/加载地址以及edata/end/text的含义 <lab2/lab2_3_7_phymemlab_concepts.md>`__
   -  `附录D. 自映射机制 <lab2/lab2_3_3_6_self_mapping.md>`__

Lab 3
-----

-  `Lab 3 <lab3.md>`__

   -  `实验目的 <lab3/lab3_1_goals.md>`__
   -  `实验内容 <lab3/lab3_2_lab2.md>`__

      -  `练习 <lab3/lab3_2_1_exercises.md>`__
      -  `项目组成 <lab3/lab3_2_2_files.md>`__

   -  `虚拟内存管理 <lab3/lab3_3_vmm.md>`__

      -  `基本原理概述 <lab3/lab3_3_1_vmm_principles.md>`__
      -  `实验执行流程概述 <lab3/lab3_3_2_labs_steps.md>`__
      -  `关键数据结构和相关函数分析 <lab3/lab3_3_3_data_structures.md>`__

   -  `Page Fault异常处理 <lab3/lab3_4_page_fault_handler.md>`__
   -  `页面置换机制的实现 <lab3/lab3_5_swapping.md>`__

      -  `页替换算法 <lab3/lab3_5_1_page_swapping.md>`__
      -  `页面置换机制 <lab3/lab3_5_2_page_swapping_principles.md>`__

   -  `实验报告要求 <lab3/lab3_6_labs_requirement.md>`__

Lab 4
-----

-  `Lab 4 <lab4.md>`__

   -  `实验目的 <lab4/lab4_1_goals.md>`__
   -  `实验内容 <lab4/lab4_2_labs.md>`__

      -  `练习 <lab4/lab4_2_1_exercises.md>`__
      -  `项目组成 <lab4/lab4_2_2_files.md>`__

   -  `内核线程管理 <lab4/lab4_3_kernel_thread_management.md>`__

      -  `实验执行流程概述 <lab4/lab4_3_1_lab_steps.md>`__
      -  `设计关键数据结构 – 进程控制块 <lab4/lab4_3_2_pcb.md>`__
      -  `创建并执行内核线程 <lab4/lab4_3_3_create_exec_kernel_thread.md>`__

         -  `创建第0个内核线程idleproc <lab4/lab4_3_3_1_create_kthread_idleproc.md>`__
         -  `创建第1个内核线程initproc <lab4/lab4_3_3_2_create_kthread_initproc.md>`__
         -  `调度并执行内核线程initproc <lab4/lab4_3_3_3_sched_run_kthread.md>`__

   -  `实验报告要求 <lab4/lab4_4_labs_requirement.md>`__
   -  `附录A：实验四的参考输出 <lab4/lab4_5_appendix_a.md>`__
   -  `附录B：【原理】进程的属性与特征解析 <lab4/lab4_6_appendix_b.md>`__

Lab 5
-----

-  `Lab 5 <lab5.md>`__

   -  `实验目的 <lab5/lab5_1_goals.md>`__
   -  `实验内容 <lab5/lab5_2_lab2.md>`__

      -  `练习 <lab5/lab5_2_1_exercises.md>`__
      -  `项目组成 <lab5/lab5_2_2_files.md>`__

   -  `用户进程管理 <lab5/lab5_3_user_process.md>`__

      -  `实验执行流程概述 <lab5/lab5_3_1_lab_steps.md>`__
      -  `创建用户进程 <lab5/lab5_3_2_create_user_process.md>`__
      -  `进程退出和等待进程 <lab5/lab5_3_3_process_exit_wait.md>`__
      -  `系统调用实现 <lab5/lab5_3_4_syscall.md>`__

   -  `实验报告要求 <lab5/lab5_4_lab_requirement.md>`__
   -  `附录 A：【原理】用户进程的特征 <lab5/lab5_5_appendix.md>`__

Lab 6
-----

-  `Lab 6 <lab6.md>`__

   -  `实验目的 <lab6/lab6_1_goals.md>`__
   -  `实验内容 <lab6/lab6_2_labs.md>`__

      -  `练习 <lab6/lab6_2_1_exercises.md>`__
      -  `项目组成 <lab6/lab6_2_2_files.md>`__

   -  `调度框架和调度算法设计与实现 <lab6/lab6_3_scheduler_design.md>`__

      -  `实验执行流程概述 <lab6/lab6_3_1_exercises.md>`__
      -  `进程状态 <lab6/lab6_3_3_process_state.md>`__
      -  `进程调度实现 <lab6/lab6_3_4_process_implement.md>`__

         -  `内核抢占点 <lab6/lab6_3_4_1_kernel_preempt_point.md>`__
         -  `进程切换过程 <lab6/lab6_3_4_2_process_switch.md>`__

      -  `调度框架和调度算法 <lab6/lab6_3_5_scheduler_framework.md>`__

         -  `设计思路 <lab6/lab6_3_5_1_designed.md>`__
         -  `数据结构 <lab6/lab6_3_5_2_data_structure.md>`__
         -  `调度点的相关关键函数 <lab6/lab6_3_5_3_scheduler_point_functions.md>`__
         -  `RR 调度算法实现 <lab6/lab6_3_5_4_RR.md>`__

      -  `Stride Scheduling <lab6/lab6_3_6_stride_scheduling.md>`__

         -  `基本思路 <lab6/lab6_3_6_1_basic_method.md>`__
         -  `使用优先队列实现 Stride
            Scheduling <lab6/lab6_3_6_2_priority_queue.md>`__

   -  `实验报告要求 <lab6/lab6_4_labs_requirement.md>`__

Lab 7
-----

-  `Lab 7 <lab7.md>`__

   -  `实验目的 <lab7/lab7_1_goals.md>`__
   -  `实验内容 <lab7/lab7_2_labs.md>`__

      -  `练习 <lab7/lab7_2_1_exercises.md>`__
      -  `项目组成 <lab7/lab7_2_2_files.md>`__

   -  `同步互斥机制的设计与实现 <lab7/lab7_3_synchronization_implement.md>`__

      -  `实验执行流程概述 <lab7/lab7_3_1_experiment.md>`__
      -  `同步互斥机制的底层支撑 <lab7/lab7_3_2_synchronization_basic_support.md>`__

         -  `计时器 <lab7/lab7_3_2_1_timer.md>`__
         -  `屏蔽与使能中断 <lab7/lab7_3_2_2_interrupt.md>`__
         -  `等待队列 <lab7/lab7_3_2_3_waitqueue.md>`__

      -  `信号量 <lab7/lab7_3_3_semaphore.md>`__
      -  `管程和条件变量 <lab7/lab7_3_4_monitors.md>`__

   -  `实验报告要求 <lab7/lab7_4_lab_requirement.md>`__
   -  `附录 <lab7/lab7_5_appendix.md>`__

Lab 8
-----

-  `Lab 8 <lab8.md>`__

   -  `实验目的 <lab8/lab8_1_goals.md>`__
   -  `实验内容 <lab8/lab8_2_labs.md>`__

      -  `练习 <lab8/lab8_2_1_exercises.md>`__
      -  `项目组成 <lab8/lab8_2_2_files.md>`__

   -  `文件系统设计与实现 <lab8/lab8_3_fs_design_implement.md>`__

      -  `ucore
         文件系统总体介绍 <lab8/lab8_3_1_ucore_fs_introduction.md>`__
      -  `通用文件系统访问接口 <lab8/lab8_3_2_fs_interface.md>`__
      -  `文件系统抽象层 - VFS <lab8/lab8_3_4_fs_abstract.md>`__

         -  `file & dir接口 <lab8/lab8_3_4_1_file_dir_interface.md>`__
         -  `inode 接口 <lab8/lab8_3_4_2_inode_interface.md>`__

      -  `Simple FS 文件系统 <lab8/lab8_3_3_sfs.md>`__

         -  `文件系统的布局 <lab8/lab8_3_3_1_fs_layout.md>`__
         -  `索引节点 <lab8/lab8_3_3_2_inode.md>`__

   -  `设备层文件 IO 层 <lab8/lab8_3_5_dev_file_io_layer.md>`__

      -  `关键数据结构 <lab8/lab8_3_5_1_data_structure.md>`__
      -  `stdout设备文件 <lab8/lab8_3_5_2_stdout_dev_file.md>`__
      -  `stdin 设备文件 <lab8/lab8_3_5_3_stdin_dev_file.md>`__

   -  `实验执行流程概述 <lab8/lab8_3_6_labs_steps.md>`__
   -  `文件操作实现 <lab8/lab8_3_7_file_op_implement.md>`__

      -  `打开文件 <lab8/lab8_3_7_1_file_open.md>`__
      -  `读文件 <lab8/lab8_3_7_2_file_read.md>`__

   -  `实验报告要求 <lab8/lab8_4_lab_requirement.md>`__
