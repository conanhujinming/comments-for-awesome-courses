课号：[CMU 15721 Spring 2020](https://15721.courses.cs.cmu.edu/spring2020/) 

教授：Andy Pavlo 

评论贡献者：[Acat](https://github.com/XieJiann)

- [x] Project
- [ ] AutoGrader
- [x] Videos [bilibili](https://www.bilibili.com/video/BV1mJ41147KK?from=search&seid=13671603297959294879), [youtube](https://www.youtube.com/watch?v=SdW5RKUboKc&list=PLSE8ODhjZXjasmrEd2_Yi1deeE360zv5O&index=2)
- [x] [Complete Notes & Slides](https://15721.courses.cs.cmu.edu/spring2020/schedule.html)

## 课程信息

高级数据系统：这是15445的进阶课。15445介绍了数据的几个模块：

* 数据存储
* 索引
* 优化器
* 执行器
* 事务中的并发控制和容错处理

然而上面这些只是针对面向磁盘数据库，且对很对多模块的介绍很粗糙。在15721中，会介绍一些更前沿的知识，以及面向内存的数据库的一些优化。

与15445相似，这门课也有一个对应的开源数据库[noisepage](https://github.com/cmu-db/noisepage)。

不过这门课的project比较一般，project1是教你怎么用perf找Contention Hotspot；project2是实现一个B+树，和445很像（怪不得445的project2这么难.....）

## 适合人群

这门课程算是一门读论文的课，你需要在上课前完整的读完一篇论文，然后再去听课（不然很多听不懂）。

所以你需要基本的数据库知识，以及阅读英语论文的能力。而且由于这门课没有设计那么好的实验以及讲的内容比较零散，所以需要很强的自学能力，推荐445看完再来看721。

## 课程评价

这门课算是一个提高课吧，andy针对上面的一些数据库模块，列举了很多经典的论文，并且在课上也做了比较好的讲解。

如果说15445是通过实验和课程让你对数据建立一个整体的理解，那么15721就是深入各个模块，让你深入的了解各个领域中一些核心的问题以及学术界前沿的方法。

## 非官方资料推荐

暂无，不过很推荐阅读下[noisepage](https://github.com/cmu-db/noisepage)的源代码。

## 后续课程推荐

无，这应该是数据库领域最难的一门课了吧。后续的应该就是看数据库的顶会论文。