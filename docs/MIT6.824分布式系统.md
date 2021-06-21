课号：[MIT 6.824](https://pdos.csail.mit.edu/6.824/index.html) 

教授：Robert Morris

评论贡献者：[williamgrt](https://github.com/williamgrt)

- [x] [Lab x 4](https://pdos.csail.mit.edu/6.824/labs/lab-mr.html)
- [x] 本地有完善的测试用例
- [x] Videos [bilibili-2020版](https://www.bilibili.com/video/BV1R7411t71W)、[bilibili-2021版](https://www.bilibili.com/video/BV16f4y1z7kn)
- [x] [Complete Notes & Slides](https://pdos.csail.mit.edu/6.824/schedule.html)

## 课程信息

这门课程主要介绍构建分布式系统需要用到的相关技术，包括容错机制、复制、共识算法等。每节课一般会阅读一篇论文，上课的内容是对论文的内容进行讲解。论文选取的都是工业界广泛使用的技术，例如 MapReduce、GFS、Raft、Spanner、Spark 等。

课程一共有四个 lab，是这门课的精髓部分。每个 lab 的内容如下：

lab1: 根据 MapReduce 论文实现一个基本的 MapReduce 编程框架。

lab2: 根据 Raft 的论文，实现 Raft 共识算法。

lab3: 在 lab2 的基础上，构建一个可靠的键值数据库服务。

lab4: 在 lab3 的基础上，实现数据库的分片功能并且可以动态迁移。

## 适合人群

这门课有一定难度，需要一定的论文阅读能力和编程能力。个人觉得最好学过操作系统，了解多线程编程后再来学习这门课程。

## 课程评价

这门课提供的论文都值得一读，读完论文后可以观看课程对应的视频加深理解。由于时间的原因，我没有把所有的论文读完，时间够的话推荐把课程的论文都读一遍。

课程的实验难度挺大，写起来比较痛苦。课程最大的难点在于并发程序的调试，基本上只能通过打日志的方式找到问题，需要耗费比较多的时间，因此实现的过程中尽量多输出日志。lab2 需要对 Raft 论文理解完全到位，否则会踩坑。lab4 需要自己设计迁移数据的方法。lab2、lab3、lab4 之间存在关联，后一个 lab 依赖于前一个 lab 的正确性，这三个 lab 合起来是一个完整的分布式键值存储系统。

每个 lab 都有完善的测试用例，助教还提供了多次测试的脚本。

项目需要使用 Go 语言编写，同时涉及到了多线程编程和 RPC 相关的知识。没有接触过问题不大，课程都会提供学习材料学习。

## 非官方资料推荐

1. Designing Data-Intensive Applications ，中文名《数据密集型应用系统设计》。
2. 知乎问答：[如何的才能更好地学习 MIT6.824 分布式系统课程？](https://www.zhihu.com/question/29597104)
3. 交流群：1160513631

## 后续课程推荐

- [PingCAP tinykv](https://university.pingcap.com/talent-plan/implement-a-mini-distributed-relational-database)：PingCAP Talent Plan 项目，实现更加偏工业一些。



## 文件列表

- MIT6.824分布式系统
