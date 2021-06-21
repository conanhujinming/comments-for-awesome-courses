课号：[Talent Plan TinyKV](https://university.pingcap.com/talent-plan/implement-a-mini-distributed-key-value-database/) 

教授：无

评论贡献者：[WangAShao](https://github.com/WangAShao)

- [x] [Project x 4](https://github.com/tidb-incubator/tinykv)
- [x] AutoGrader
- [ ] Videos
- [ ] Complete Notes & Slides
- [x] 代码查重

## 课程信息

由PingCAP推出的一门课程，我认为这门课程的意义在于帮助更多的人搞懂TiKV的架构，参与到TiKV的贡献当中来。

课程一共由4个Project，下面简单介绍一下：

- project1是构建一个单机kv server
- project2是基于raft算法实现分布式键值数据库服务端
- project3是在project2的基础上支持多个raft集群
- project4是在project3的基础上支持分布式事务

这些实验的难度都非常大，预计用时一个月。

另外做完之后提交PingCAP打分时是会有严格的查重的，所以建议做这个实验不要抄袭！

## 适合人群

本实验不适合分布式系统新手，因为哪怕通关了MIT6.824的选手，也难以能在2B，2C，3B当中轻易的存活下来。

本实验适合通关了MIT6.824来挑战或者有着很好的相关基础想要继续深入学习的人或者想要参与到TiKV的开发却苦恼于对TiKV的架构不太了解的人。

## 课程评价

因为我做的时候Talent Plan2.0才刚出来，所以存在很多问题

- 框架代码存在bug
- 指导书很简陋，导致不知道自己要做什么

但这些问题可能等你看到我的推荐的时候已经不存在了，因为有很多开源热爱者都在不断的对这个项目进行完善。

其他方面这门课程都很优秀，做到了学术与工业的完美接轨，让你感受读论文，然后实现论文的快感。

从另一个方面来评价：做这门课的人并不多，分享笔记的人也不多，这就意味着你很难找到人来交流实验过程中遇到的困难，遇到了bug网上也没有文章教你怎么解决，只能自己慢慢调试，所以难度挺大的。

## 非官方资料推荐

1. 自己当初在学校内部分享时写的一份简陋的[笔记](https://zhuanlan.zhihu.com/p/382432820)，没有涉及任何具体实现代码，所以可以放心观看，主要讨论解题思路，调试方法，工具选择，心态调整这些方面。

## 后续课程推荐

认真做完这个实验之后，你会对TiKV有着很深的理解，可以考虑学习一下rust然后参与到TiKV的开发当中。

## 文件列表

- Talent Plan tinykv分布式键值存储系统
