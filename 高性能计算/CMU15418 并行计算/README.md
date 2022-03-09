课程号: CMU15-418/618

教授: Kayvon

课程地址: [spring-2016](http://15418.courses.cs.cmu.edu/spring2016/lectures)

视频地址: [bilibili](https://www.bilibili.com/video/BV16k4y1z7z9?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click), [panopto](https://scs.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx#folderID=%22f62c2297-de88-4e63-aff2-06641fa25e98%22)

评论贡献者: [sheep](https://github.com/ysj1173886760)

## 课程信息

CMU开展的并行计算课程，有一门有一定关系的前置课是并行数据结构15-210。没有上过也没关系。教授会从最初始的概念——为什么需要并行开始讲起，途中会带我们了解现代处理器在多核并行方面都应用到了那些技术（比如超线程），GPU的架构以及一些CUDA programming，并行方面常谈的scheduling，还会带我们深入硬件的一些实现算法，比如cache coherence，很容易让人迷惑的memory model，并且会根据上面的知识教我们多核架构下我们怎么利用这些来实现锁。最后还会涉及到一些（当时）前沿的技术，比如异构架构下的并行，事务内存，Spark，Deep Network的evaluation和training，以及3D渲染管线。可以说是一门走向并行领域的必修课了。

课程有4个assignment

在官网就可以找到，这个教授由于后来去了stanford，所以后续的更新就在stanford了，课号是CS149

值得一提的是教授也在清华大学开过一次这个课程，在b站还可以找到录像

project我是做的CS149的，但是其实都比较类似，大家可以调自己感兴趣的做

project1是用ISPC写程序以及在多核CPU上analyse一些程序，主要目的就是让我们去识别这些并行程序，找到bottleneck

project2是写一个调度器，基本的策略在课上都有讲，可以说是一个C++多线程的练习

project3是用CUDA写一个Renderer

project4是用OpenMP来编写大规模图计算的程序，最后是根据程序的效率给分，还是非常有挑战性的

## 适合人群

这门课代码难度并不高，但是内容有的地方还是有一定难度的，有的时候一节课就需要用一天的时间去仔细思考。

## 课程评价

我个人的感觉就是上完了非常过瘾，对并行计算这方面有了一个整体的认识。课程没有教材，但是有很多推荐的reading。我个人认为如果想看书的话，根据上面的的内容也大概可以猜到，一定是《计算机体系结构：量化研究方法》了

对我这种想要学习并行计算但是无从下手的同学是一个非常好的课。并且学的过程中可以尝试与计算机体系结构等来融会贯通的去理解。如果也学习过一些系统方面的课程的话，学完后可以对计算机有一个比较整体的了解，再进阶就可以去读一读高性能计算方面的论文了。

我自己也记录了一些课程的笔记以及每次lecture的思考，但是因为有的内容并不是很全面就不放出来了，如果有想要相互交流的同学欢迎联系我。