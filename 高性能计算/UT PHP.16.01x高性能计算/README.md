课程号：[UTAustinX UT.PHP.16.01x](https://learning.edx.org/course/course-v1:UTAustinX+UT.PHP.16.01x+2T2020/home)

课程地址: [edx.org](https://learning.edx.org/course/course-v1:UTAustinX+UT.PHP.16.01x+2T2020/home)

视频地址: [youtube](https://www.youtube.com/channel/UCH9ic-k054S8-YmRwQJS6kg)

Textbook: None

## 课程信息

---

**LAFF-On Programming for High Performance**是**The University of Texas as Austin**开设的一门高性能计算初步课程，从最简单的矩阵乘法入手，一步步深入讲解我们现在常用的**BLAS**库是如何实现高性能的矩阵乘法的，课程需要C语言基础来实现代码和Matlab Livescript进行性能测试与图表绘制。

- Week0 - Getting started： 课程内容讲解和环境配置
- Week1 - Loops and More Loops：调整一般矩阵乘法的三层`IJK`循环，比较速度，并给出不同视角解释矩阵乘法的更新过程
- Week2 - Start Your Engines：分块与使用AVX2
- Week3 - Pushing the Limits：如何充分利用三级Cache，预打包优化
- Week4 - Multithreaded  Parallelism：OpenMP并行

## 适合人群
---
与一般见到的CS课程不同，课程通常没有大型Lab，主要是通过一步步讲解与优化来提高`GEMM`的性能，先讲解优化思路，让学生尝试优化，然后老师给出参考方案

## 课程评价
---
 优秀的高性能计算入门课程，很多CS专业的学生，很少会接触高性能计算领域，这一课程使用了一些常用的优化手段和工具，是入门高性能计算的优秀课程

- 优点：
	讲解详细，有参考代码，每周最后有Enrichment的部分，供有兴趣的同学深入学习其他课程与经典的论文
- 缺点：
	性能测试使用了Matlab Livesript，对大部分同学不是很友善

## 需要注意的坑点
---
- 后期的代码逻辑结构比较复杂，多画画图进行理解
- 推荐使用`Git`，这门课程的代码特点是，基础实现加上反复迭代

## 非官方资料推荐
---
暂无

## 后续课程推荐
---
请看每周的Enrichment部分，有大量论文、教材与延伸课程