课号：[Stanford CS110L SPRING 2020](https://reberhardt.com/cs110l/spring-2020/)

授课人：[Ryan Eberhardt](https://reberhardt.com/) & Armin Namavari

评论贡献者：[Qi Wang](https://github.com/wangqiim)

- [X] [Videos]((https://github.com/reberhardt7/cs110l-spr-2020-starter-code))：2020版本有video(Youtube)，但是后面几课缺失，之后的2021以及2022版都无视频

- [X] [lab x 6  + project x 2](https://github.com/reberhardt7/cs110l-spr-2020-starter-code)

- [ ] AutoGrader: 不对外开放

- [X] [Slides & Reading](https://reberhardt.com/cs110l/spring-2020/) 2020、2021、2022都提供

## 课程信息
系统编程中的安全。课程内容主要涉及系统编程中的安全问题以及讲解如何使用Rust。实验包含6个每周的lab和2个最终的project。

### 6个每周的Lab包括：
1. Rust的基本语法练习
2. Rust的ownship和type的练习
3. Rust的Error处理和I/O处理和trait练习
4. 无（project代替）
5. Rust线程与并发
6. Rust并发中，使用channel来通信
> 不同年份的实验有一些不一样，比如2021只提供了第一个实验，其中添加了：C编程中的安全问题练习（同时介绍静态代码检验、动态内存检验工具），每个lab花费时间1-6小时。

### 2个project
1. Deet: 实现一个tiny GDB （包含基本的run、breakpoint、continue、backtrace功能）
2. Balancebeam: 实现一个tiny 反向代理服务器（包含负载均衡、限流、主动/被动探活功能）
> 这两个项目如果从头写有很多“邪恶”的细节，因此该课程提供了基本的框架和很多工具函数。实现起来并不需要写太多代码。因此每个project花费时间1-3天足够。

## 适合人群
适合有C语言基础、GC语言基础、系统编程基础以后学习这门课。同时可以作为学习Rust的入门课。

## 课程评价
该课程的教师似乎是一个研究生，视频里他说他带的CS110课是Stanford学生评价最高的课。该课程应该在学过CS110之后学效果最好，但是网上似乎没有太多CS110的资料。总体来说是一门不错的课，在介绍Rust之余，浅浅的介绍了很多系统编程、安全方面的知识，学了就能有收获。同时，实验花费的时间应该是我做过的网课目前来说最少的一个。

## 需要注意的坑点
1. 课程里经常把Rust和其他语言对比，因此有其他语言（主要是C）的基础再学更好。有些地方也讲了系统编程中遇到的一些问题，建议看对应的地方之前提前做预习。
2. 课程视频很重要，如果看了视频很多Lab能很快搞定。
3. Project 2(Balancebeam)给的框架代码，由于依赖的库有一些改动，因此需要rename一些变量才能build，可以参考github上别人的repo。
4. 做实验时候主要的参考资料是Rust的官方文档。有什么问题谷歌直接搜"Rust xxx"就可以找到对应的文档。

## 非官方资料推荐

- 暂无

## 后续课程推荐

- 暂无
