课号：[CMU 15445 Fall 2020](https://15445.courses.cs.cmu.edu/fall2020/) 

教授：Andy Pavlo 

评论贡献者：[WangAShao](https://github.com/WangAShao)

- [X] [Project x 4 & HomeWork x 5](https://15445.courses.cs.cmu.edu/fall2020/assignments.html)
- [X] [AutoGrader](https://www.gradescope.com/courses/195440) 
- [X] Videos [bilibili](https://www.bilibili.com/video/BV1q741127SQ), [youtube](https://www.youtube.com/watch?v=oeYBdghaIjc), [simviso中文翻译-付费](https://www.simtoco.com/#/albums?id=1000013)
- [X] [Complete Notes & Slides](https://15445.courses.cs.cmu.edu/fall2020/schedule.html#)

## 课程信息

数据库系统设计：CMU的神课，是讲数据库底层原理的课程，是在CMU开发的一个供教学的数据库系统bustub上面添加更多功能的支持。如果你想深入数据库的底层，那么这门课非常适合你。即便你以后做的是后台开发，了解数据库底层原理也对你大有裨益。Andy Pavlo也是数据库领域非常有名的教授，课堂效果很好。

这么课程的精髓在实验，下面简单介绍一下project主要做什么内容：

Project1：实现一个BufferPoolManager，难度：简单。主要考察数据结构以及对数据库的理解。具体来说是实现LRU替换算法和内存池管理器来管理内存，另外要求支持并发。预计用时：2~3天。

project2：实现B+树，难度：困难。首先实现B+树的数据结构，然后在此数据结构之上支持插入，查询，删除，迭代器，并发控制等。这一部分测试用例非常强劲。预计用时：7~10天。

peoject3：实现Query Exeution的支持，难度：中等。实现系统目录来跟踪有关数据库的元数据，然后实现像`SEQUENTIAL SCAN`，`INDEX SCANS`等一系列的执行子，使用的是火山模型。预计用时：3~5天

project4：支持并发的查询执行，难度：中等偏难。主要包括三个任务：锁管理器，死锁检测以及并发查询执行。预计用时4~6天。

## 适合人群

这门课程有一定的难度，需要有一定的代码能力，如果要量化一下的话个人认为难度比MIT6.s081高一些。

## 课程评价

视频我看过，讲的挺不错的，如果有时间的话推荐看一下，每一个lec对应的notes就是对上课内容的总结，没时间看视频直接看notes也行。

这门课的作业是小事，难度不大，可以用来复习一下上课讲到的算法，而且作业提供了标准答案。重点在于project上面，难度很大，非常的painful...尤其是第project2 B+树，本来难度就大，测试用例还非常强劲。

这门课虽然提供了自动测试，但是gradescope是限时开放的，gradscope的邀请码可以在课程主页中的FAQ里面找到。

项目采用C++语言，但是并没有用到很复杂的语法，之前没学过C++也不用太过担心，可以边做边学。另外project之间存在依赖，后面的project依赖于前面project的正确性。

最后的碎碎念：想要真的搞懂这门课，最重要的是一定要做Project，在达到了正确性之后，还可以去刷排行榜，尽可能提升自己程序的性能，用到上课讲到的优化策略。

## 非官方资料推荐

1. [CMU15445交流群](https://zhuanlan.zhihu.com/p/366484273)的piazza里面有大量优质问答

2. 一份整理的很不错的[CMU15445笔记](https://zhenghe.gitbook.io/open-courses/cmu-15-445-645-database-systems/relational-data-model)

3. 我自己也记录了一点[笔记](https://www.zhihu.com/column/c_1389608400238546945)，里面除了LRU之外基本没怎么贴代码，所以可以放心观看。LRU这一Part之所以贴了代码是因为毕竟是第一个task，如果读者跟着做最后看到了这个任务点的测试通过一定会感到大受鼓舞，那么后面会做的更加有动力。

   主要记录的是我印象比较深刻的坑点以及一些小技巧还有一些我认为比较难想清楚的地方。目前这篇笔记写得还比较捞，考完试之后我会花时间润色一下。

## 后续课程推荐

- [CMU15-721](https://15721.courses.cs.cmu.edu/spring2020/)：同样是Andy教授教学，是445的进阶课程
- [PingCAP tinysql](https://university.pingcap.com/talent-plan/implement-a-mini-distributed-relational-database)：PingCAP著名开源项目，适合对分布式，数据库等感兴趣的同学。