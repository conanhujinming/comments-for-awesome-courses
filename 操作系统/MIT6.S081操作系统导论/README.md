课号：[MIT 6.S081 Fall 2020](https://pdos.csail.mit.edu/6.S081/2020/)

教授：[Frans Kaashoek](https://pdos.csail.mit.edu/~kaashoek/) & [Robert Morris](https://pdos.csail.mit.edu/~rtm/)

评论贡献者：[Jinming Hu](https://conanhujinming.github.io/)

- [X] Videos，[Youtube](https://pdos.csail.mit.edu/6.S081/2020/schedule.html), [B站](https://search.bilibili.com/all?keyword=6.s081&from_source=webtop_search&spm_id_from=333.851)

- [X] [Lab x 11](https://pdos.csail.mit.edu/6.S081/2020/labs/guidance.html)
- [X] [AutoGrader](https://pdos.csail.mit.edu/6.S081/2020/labs/guidance.html) 

- [X] [Slides & Reading](https://pdos.csail.mit.edu/6.S081/2020/schedule.html)

## 课程信息

操作系统导论。是在两位教授开发的供教学用的迷你操作系统xv6做一些进一步的开发，来理解操作系统内核的工作原理。这门课程适合想要深度理解操作系统的同学，而操作系统可以说是计算机科学中极为基础和重要的领域，学扎实的话，无论是做工程还是做科研都受益无穷。

## 适合人群

个人认为适合作为第二门操作系统课程，第一门的话更推荐CMU 15-213。

## 课程评价

我有些不适应来自FK教授的授课视频。个人觉得这门课的精髓在那11个lab上，结合做lab与阅读xv6 book，则可以对xv6操作系统内核的工作原理有较为深刻的认识，而这些原理也是现代操作系统中最为核心的部分。lab使用c语言完成，难度较大，尤其是第三个lab page table，应该可以说是所有lab中最大的坎，但这些lab能很好地加深对操作系统的认识，也能较好地磨练自己的工程能力，非常值得一做。视个人基础，大概需要100到200小时左右的学习时间。

## 需要注意的坑点

这里主要给出前两个lab的坑点：

1. 在开始lab之前，先按照[tools](https://link.zhihu.com/?target=https%3A//pdos.csail.mit.edu/6.828/2020/tools.html) 配环境。如果是使用ubuntu的话，我个人推荐用ubuntu20，这样可以免去自己配toolchain的痛苦；而如果是更早的ubuntu系统的话，那么需要按照页面上的指点自己build toolchain。另外使用`apt-get`安装的QEMU的版本估计是不够新的，如果版本号低于5.1.0，那么也需要自己手动build QEMU. 最后验证安装的时候，如果不是自己手动build的toolchain的话，可能不是按照官方说的用`riscv64-unknown-elf-gcc`之类的，而是其他的一些命令，具体可以在`/usr/bin`或者`/usr/local/bin` 下查看 。对于验证安装，我个人建议先确定qemu版本，再尝试在xv6运行`make qemu`，如果能够正常进入，应该就没有问题了。

2. 之后阅读[guidance](https://link.zhihu.com/?target=https%3A//pdos.csail.mit.edu/6.828/2020/labs/guidance.html) 注意一个坑点是`make qemu-gdb`的部分，在另一个窗口跑`gdb`或者`riscv64-linux-gnu-gdb`可能都不一定有用，也许是`gdb-multiarch`或者是 `riscv64-unknown-elf-gdb` 具体同样可在`/usr/bin`或者`/usr/local/bin`下查看。可以自己试试哪个会work>_<

3. 如果你要用xv6的某些自带的函数，发现它们不像你想得那样工作，那么请大胆地去看源码，也许它们的实现的behavior和标准库的是不一样的>_< 并且，要敢于而且主动地去看xv6的源码，甚至可以说这些Lab的目的就是帮助你熟悉了解xv6的源码的。

4. 如果你的机器（像我一样）很烂，在某些case上可能会碰到timeout的问题（纯粹是因为机器太烂），那么可以把gradelib里默认的timeout调大一些......

5. 关于用gdb在user程序中打断点出现Cannot access memory at address错误的问题，

   xv6的主分支上已经修复了这个问题。但是2020版的前几个lab没merge这个patch，需要自己在.gdbinit.tmpl-riscv里加一行`set riscv use-compressed-breakpoints yes`

关于后面lab的注意事项，可以加入[6.S081学习交流群](https://zhuanlan.zhihu.com/p/251366985)了解。
## 关于在mac上的环境搭建
* 大部分参考https://zhayujie.com/mit6828-env.html
* qemu
   * 版本为5.1.0 手动make（可能需要多次make才会成功）
   * 下载地址 https://download.qemu.org/
* xv6 需要clone2020课程的仓库，但是链接感觉失效了，需要自己百度一下clone。
* RISC-V工具链：
   *  版本9.2.0 （不要用brew安装，因为会在gdb调试时出问题）
   *  下载地址：第一个链接里给出了，用博主给的下载链接自行make
   *  注意！在make前修改一下源码 在riscv-gdb/readline/rltty.c 和 riscv-gdb/readline/terminal.c 中添加头文件#include<sys/ioctl.h>
   *  如果编译中途退出，记得多编译几次，大概持续30min-60min。
## 非官方资料推荐

1. 强推[肖宏辉大神](https://www.zhihu.com/people/xiao-hong-hui-15)的[课程内容翻译](https://mit-public-courses-cn-translatio.gitbook.io/mit6-s081/)。
2. [6.S081学习交流群](https://zhuanlan.zhihu.com/p/251366985) 的群piazza里也有大量优质问答。

## 后续课程推荐

- [MIT 6.828](https://abelay.github.io/6828seminar/index.html) 系统论文阅读研讨会，适合对系统领域的科研感兴趣的同学。
- [System Paper Reading Seminar](https://learn-sys.github.io/cn/reading/)：很多同学自己组织的系统论文研讨会，中文资源，有视频。
- [MIT 6.824](https://pdos.csail.mit.edu/6.824/)：分布式系统。
