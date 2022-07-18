gdb使用
=======

gdb 是功能强大的调试程序，可完成如下的调试任务： - 设置断点 -
监视程序变量的值 - 程序的单步(step in/step over)执行 - 显示/修改变量的值
- 显示/修改寄存器 - 查看程序的堆栈情况 - 远程调试 - 调试线程

在可以使用 gdb 调试程序之前，必须使用 -g 或
–ggdb编译选项编译源文件。运行 gdb 调试程序时通常使用如下的命令：

::

   gdb progname

在 gdb 提示符处键入help，将列出命令的分类，主要的分类有：

-  aliases：命令别名
-  breakpoints：断点定义；
-  data：数据查看；
-  files：指定并查看文件；
-  internals：维护命令；
-  running：程序执行；
-  stack：调用栈查看；
-  status：状态查看；
-  tracepoints：跟踪程序执行。

键入 help
后跟命令的分类名，可获得该类命令的详细清单。gdb的常用命令如下表所示。

表 gdb 的常用命令

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <td>

break FILENAME:NUM

.. raw:: html

   </td>

.. raw:: html

   <td>

在特定源文件特定行上设置断点

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

clear FILENAME:NUM

.. raw:: html

   </td>

.. raw:: html

   <td>

删除设置在特定源文件特定行上的断点

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

run

.. raw:: html

   </td>

.. raw:: html

   <td>

运行调试程序

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

step

.. raw:: html

   </td>

.. raw:: html

   <td>

单步执行调试程序，不会直接执行函数

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

next

.. raw:: html

   </td>

.. raw:: html

   <td>

单步执行调试程序，会直接执行函数

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

backtrace

.. raw:: html

   </td>

.. raw:: html

   <td>

显示所有的调用栈帧。该命令可用来显示函数的调用顺序

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

where continue

.. raw:: html

   </td>

.. raw:: html

   <td>

继续执行正在调试的程序

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

display EXPR

.. raw:: html

   </td>

.. raw:: html

   <td>

每次程序停止后显示表达式的值,表达式由程序定义的变量组成

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

file FILENAME

.. raw:: html

   </td>

.. raw:: html

   <td>

装载指定的可执行文件进行调试

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

help CMDNAME

.. raw:: html

   </td>

.. raw:: html

   <td>

显示指定调试命令的帮助信息

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

info break

.. raw:: html

   </td>

.. raw:: html

   <td>

显示当前断点列表，包括到达断点处的次数等

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

info files

.. raw:: html

   </td>

.. raw:: html

   <td>

显示被调试文件的详细信息

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

info func

.. raw:: html

   </td>

.. raw:: html

   <td>

显示被调试程序的所有函数名称

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

info prog

.. raw:: html

   </td>

.. raw:: html

   <td>

显示被调试程序的执行状态

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

info local

.. raw:: html

   </td>

.. raw:: html

   <td>

显示被调试程序当前函数中的局部变量信息

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

info var

.. raw:: html

   </td>

.. raw:: html

   <td>

显示被调试程序的所有全局和静态变量名称

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

kill

.. raw:: html

   </td>

.. raw:: html

   <td>

终止正在被调试的程序

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

list

.. raw:: html

   </td>

.. raw:: html

   <td>

显示被调试程序的源代码

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

quit

.. raw:: html

   </td>

.. raw:: html

   <td>

退出 gdb

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

gdb调试实例
===========

下面以一个有错误的例子程序来介绍gdb的使用：

::

   /*bugging.c*/
   #include <stdio.h>
   #include <stdlib.h>

   static char buff [256];
   static char* string;
   int main ()
   {
       printf ("Please input a string: ");
       gets (string);
       printf ("\nYour string is: %s\n", string);
   }

这个程序是接受用户的输入，然后将用户的输入打印出来。该程序使用了一个未经过初始化的字符串地址
string，因此，编译并运行之后，将出现 “Segment Fault”错误：

::

   $ gcc -o bugging -g  bugging.c
   $ ./bugging
   Please input a string: asdf
   Segmentation fault (core dumped)

为了查找该程序中出现的问题，我们利用 gdb，并按如下的步骤进行：

[1] 运行 “gdb bugging” ，加载 bugging 可执行文件；

::

   $gdb bugging 

[2] 执行装入的 bugging 命令；

::

   (gdb) run

[3] 使用 where 命令查看程序出错的地方；

::

   (gdb) where

[4] 利用 list 命令查看调用 gets 函数附近的代码；

::

   (gdb) list

[5] 在 gdb 中，我们在第 11 行处设置断点，看看是否是在第11行出错；

::

   (gdb) break 11

[6] 程序重新运行到第 11 行处停止，这时程序正常，然后执行单步命令next；

::

   (gdb) next

[7] 程序确实出错，能够导致 gets 函数出错的因素就是变量
string。重新执行测试程，用 print 命令查看 string 的值；

::

   (gdb) run
   (gdb) print string
   (gdb) $1=0x0

[8]
问题在于string指向的是一个无效指针，修改程序，在10行和11行之间增加一条语句
“string=buff;”，重新编译程序，然后继续运行，将看到正确的程序运行结果。

用gdb查看源代码可以用list命令，但是这个不够灵活。可以使用“layout
src”命令，或者按Ctrl-X再按A，就会出现一个窗口可以查看源代码。也可以用使用-tui参数，这样进入gdb里面后就能直接打开代码查看窗口。其他代码窗口相关命令：

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <td>

info win

.. raw:: html

   </td>

.. raw:: html

   <td>

显示窗口的大小

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

layout next

.. raw:: html

   </td>

.. raw:: html

   <td>

切换到下一个布局模式

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

layout prev

.. raw:: html

   </td>

.. raw:: html

   <td>

切换到上一个布局模式

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

layout src

.. raw:: html

   </td>

.. raw:: html

   <td>

只显示源代码

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

layout asm

.. raw:: html

   </td>

.. raw:: html

   <td>

只显示汇编代码

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

layout split

.. raw:: html

   </td>

.. raw:: html

   <td>

显示源代码和汇编代码

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

layout regs

.. raw:: html

   </td>

.. raw:: html

   <td>

增加寄存器内容显示

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

focus cmd/src/asm/regs/next/prev

.. raw:: html

   </td>

.. raw:: html

   <td>

切换当前窗口

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

refresh

.. raw:: html

   </td>

.. raw:: html

   <td>

刷新所有窗口

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

tui reg next

.. raw:: html

   </td>

.. raw:: html

   <td>

显示下一组寄存器

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

tui reg system

.. raw:: html

   </td>

.. raw:: html

   <td>

显示系统寄存器

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

update

.. raw:: html

   </td>

.. raw:: html

   <td>

更新源代码窗口和当前执行点

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

winheight name +/- line

.. raw:: html

   </td>

.. raw:: html

   <td>

调整name窗口的高度

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

tabset nchar

.. raw:: html

   </td>

.. raw:: html

   <td>

设置tab为nchar个字符

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>
