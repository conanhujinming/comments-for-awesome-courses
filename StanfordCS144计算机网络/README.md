课号：[Stanford CS144 Fall 2020](https://cs144.github.io/)

教授：Keith Winstein& Nick McKeown

评论贡献者：[Jinming Hu](https://conanhujinming.github.io/)

- [ ] Videos：有mooc版本的，我觉得讲得不好，这里就不贴了

- [X] [Lab x 7](https://cs144.github.io/)
- [X] [AutoGrader](https://cs144.github.io/) 

- [X] [Slides & Reading](https://cs144.github.io/)

## 课程信息

计算机网络导论。前五个lab是从零开始写一个能用的TCP，后面的lab则是实现了计算机网络其他层的内容。

## 适合人群

适合学完数据结构+操作系统的同学，适合作为第一门计算机网络的课程。

## 课程评价

我不太适应MOOC的授课视频。所以这门课的精髓在lab上，前4个lab难度不大，主要是测试不够强，很多问题到lab4的时候才会暴露出来，所以lab4和lab7会需要花比较多的时间。个人觉得是非常好的lab，对TCP和计算机网络的知识的掌握帮助很大。美中不足的是这门课开得时间不长，所以lab的文档的问题比较多，经常需要“面向测试编程”。视个人基础，大概需要100到200小时左右的学习时间。

## 需要注意的坑点

1. 有一些设计的选择细节并没有在PDF里给出，我有的时候需要去看test case才会知道Lab希望怎样去设计。不过也许这些内容在上课的时候会提到。
2. Lab2和Lab3的test case不够多，导致错误或者是与Lab期望的设计不符的实现也能通过全部的test case。然后在Lab4里，这些问题会全部暴露出来......结果就是在做Lab4的时候完全不能信任自己在Lab2和Lab3里的相应实现，这样也大大增加了debug难度。
3. Lab4里有两个test case即fsm_ack_rst和fsm_ack_rst_relaxed期待的行为是完全相反的。实际上在官方的FAQ页面上给出的状态机是与fsm_ack_rst期待的行为一致，但Lab4默认启用的却是fsm_ack_rst_relaxed......类似的问题挺多的，所以有些情况下不得不去读test case才知道需要实现什么样的功能。
4. 官方提供的VirtualBox Image中的GDB是有bug的，在cmake_build_type=Debug生成的binary上不能正确地打断点。在Lab4之前我还能靠肉眼调试，但是Lab4实在是肉眼调不动了，不得不寻求解决方案。后来问了一位之前也做过这个Lab的清华大佬，他告诉我说他用的是LLDB。我就赶紧换了LLDB，这才能愉快的进行调试。

## 非官方资料推荐

- 暂无

## 后续课程推荐

- 暂无
