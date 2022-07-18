使用远程调试
============

为了与qemu配合进行源代码级别的调试，需要先让qemu进入等待gdb调试器的接入并且还不能让qemu中的CPU执行，因此启动qemu的时候，我们需要使用参数-S
–s这两个参数来做到这一点。在使用了前面提到的参数启动qemu之后，qemu中的CPU并不会马上开始执行，这时我们启动gdb，然后在gdb命令行界面下，使用下面的命令连接到qemu：

::

   (gdb)  target remote 127.0.0.1:1234

然后输入c（也就是continue）命令之后，qemu会继续执行下去，但是gdb由于不知道任何符号信息，并且也没有下断点，是不能进行源码级的调试的。为了让gdb获知符号信息，需要指定调试目标文件，gdb中使用file命令：

::

   (gdb)  file ./bin/kernel

之后gdb就会载入这个文件中的符号信息了。

通过gdb可以对ucore代码进行调试，以lab1中调试memset函数为例：

(1) 运行 ``qemu -S -s -hda ./bin/ucore.img -monitor stdio``

(2) 运行 gdb并与qemu进行连接

(3) 设置断点并执行

(4) qemu 单步调试。

运行过程以及结果如下：

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <td>

窗口一

.. raw:: html

   </td>

.. raw:: html

   <td>

窗口二

.. raw:: html

   </td>

.. raw:: html

   <tr>

.. raw:: html

   <td>

chy@laptop: ~/lab1$ qemu -S -s -hda ./bin/ucore.img

.. raw:: html

   </td>

.. raw:: html

   <td>

chy@laptop: ~/lab1$ gdb ./bin/kernel (gdb) target remote:1234 Remote
debugging using :1234 0x0000fff0 in ?? () (gdb) break memset Breakpoint
1, memset (s=0xc029b000, c=0x0, n=0x1000) at libs/string.c:271 (gdb)
continue Continuing. Breakpoint 1, memset (s=0xc029b000, c=0x0,
n=0x1000) at libs/string.c:271 271 memset(void \*s, char c, size_t n) {
(gdb)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>
