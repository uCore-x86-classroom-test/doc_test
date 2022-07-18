实验环境配置
============


classroom配置
-------------------------------
基于github classroom，可方便建立开发用的git repository，并可基于github的 codespace（在线版ubuntu +vscode）在线开发使用。整个开发环境仅仅需要一个网络浏览器。classroom配置步骤如下：

   1.在网络浏览器中用自己的github id登录github.com

   2.接收实验练习uCore-x86-32的github classroom在线邀请(https://classroom.github.com/a/qvtO5fFM)，根据提示接受该实验练习。

   3.完成上一步后，你的实验练习uCore-x86-32的github repository会被自动建立好，刷新页面即可看到github repository的链接，点击此github repository的链接，就可看到你要完成的实验了。

   4.在你的实验练习的网页的中上部可以看到一个醒目的code绿色按钮，点击后，可以进一步看到 codespace 标签和醒目的create codesapce on main绿色按钮。请点击这个绿色按钮，就可以进入到在线的ubuntu + vscode环境中。

   5.进入到实验分支 git checkout labx

   6.获取自动测试脚本以及环境配置脚本sh setup.sh

   6.配置实验运行环境ubuntu环境下执行make setupenv 
   
   7. **重要** 

   在github codespace环境中请手动把下面内容添加到 /etc/apt/sources.list

   deb http://dk.archive.ubuntu.com/ubuntu/ xenial main 

	deb http://dk.archive.ubuntu.com/ubuntu/ xenial universe

   然后执行 

   sudo apt update
   
   sudo apt install -y gcc-4.8


   7.然后就可以基于在线vscode进行开发、运行、提交等完整的实验过程了。

   8.完成提交后会触发classroom提供的自动测试功能，你可以点击仓库名下边的“Actions”标签查看自动测试的结果，第一次提交触发自动测试可能需要执行5-7分钟，随后的提交所触发的自动测试则不需要这么长的时间。

上述的3，4，5步不是必须的，你也可以直接克隆Github Classroom生成git repository到本地，按照下面的环境安装提示配置好本地的开发环境，然后在本地进行实验开发与提交。

