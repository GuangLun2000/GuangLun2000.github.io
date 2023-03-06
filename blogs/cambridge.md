---
layout: page
permalink: /blogs/cambridge/index.html
title: Cambridge
---

## Cambridge 线上暑研回忆录

> 本文第一版发表于[MIEC中文博客](https://mieclance.club/archives/4389)，下为修改版
>
> 之前那篇写得太那啥了......

### 写在最前面

10月21号正式提交论文后，就进入了大三学年以来最舒服的一个周末。而过去三个月来暑研的困难程度，和我6月份报名投递申请时所想象的完全不同。

整体上来看，CCISTC线上暑研（下称Camb暑研）大体分为四个部分：

1. Academic Practical （10学时，基本的科研学术技能，机器学习入门）
2. Workshop（12学时，可以理解为工具课：雅思英语、留学规划、学术网站，教你怎么宣传自己）
3. AI Lecture（6学时，所谓的大佬正课，但我其实没听懂多少，这个后面会讲到）
4. Research Project（暑研课题，大约花费了300-320小时？巨累）

而Camb暑研最后的考评/推荐信是基于以下三个部分：

1. 暑研课程出勤（10%，大家都差不多，甚至请假还可以豁免，这个不提）
2. Research Proposal（45%，单写作花了5天时间）
3. Final Report（45%，单写作花了14天时间）

最后放一下成绩单和推荐信，相当于"暑研收获"了

1. Certificate of Completion
2. Programme Transcript
3. Letter of Recommendation

<div class="third">
<img src="/blogs/cambridge.assets/cc.png" width = 32.5%>
<img src="/blogs/cambridge.assets/st.png" width = 32.5%>
<img src="/blogs/cambridge.assets/rl.png" width = 32.5%>
</div>





------



### 关于暑研

就针对暑研来说，线下的体验绝对是好过online的，但迫于疫情（担心新学期，学校不给进，隔离周期太长），还有就是菜（没错就是菜，大二无paper弱鸡根本申不到实地）所以选择了这次的Camb线上项目。



从今年6月确定收到offer开始，到正式出成绩单（预计11月中旬），完整的流程大概是持续了5个月。如果再算上这次的final report改成paper投递的话，可能就要再持续半年左右？



说回来暑研本身，导师 Pietro Lio' 是意大利人，在剑桥拿到了MA，然后回意大利攻了两个PhD学位——Systems Dynamics & Theoretical Genetics——而现在主要是做图神经网络和计算生物学，这看起来巨神奇的履历......确实是见识了一番大牛的时间管理水平。



但就像同AI项目的朋友在知乎上吐槽的，教授的英文口语确实是一言难尽——三节AI正课几乎是靠意志力撑着——虽然一方面确实是口音的问题；但更多的是ML（Machine Learning）经历的欠缺。连Python基础都是在今年6-8月补起来的我，居然在未来的三个月搞了一个ML-Based的大项目，中间的水份真是一言难尽呐......



但总之，这次暑研的最大收获——至少在DDL的push下，确实做了深入的review，最后提交的report也能让自己心满意足了，具体细节可以看[这里]。



还要提到，暑研的Supervisor是Lio'教授的二年级博士生，我们叫他Jerry学长——Jerry是BUPT的本科，然后在Sheffield读了一年MSc(with distinction)，然后PhD阶段来到了剑桥做Wireless+ML



Jerry给我们上Practical（讲学术技能和ML入门），以及Supervision（项目辅导，给我们的课题进展提供建议）两门课。豪不夸张地说，这次暑研的质量与体验感，很大程度上都是靠Jerry一个人撑起来的...



------



### 其他的故事

暑研的同期，把大二下学期搞的那篇IoT-System的文章给投了，最后稀里糊涂的中了个IEEE CENIM（某亚洲水会...但确实是没有想到会这么顺利）



因为后来reviewer修改意见下来之后，在10月中旬和导师又一起认真改了一轮，发现投上去的那个版本的语言真的是巨烂啊...当然那一版写得拧巴，确实因为不是我主笔的好吧......哈哈



总之这篇能一投即中，算是一个意料之外的收获吧，具体细节可以看[这里]。



而回过头来，这次Camb暑研的经历，也让我暂时是坚定了未来攻PhD的念头，感到自己确实对这个领域是有点激情和想法（or天赋？）的，与此同时，受暑研搭档（wyc, chx...）的启发，也让我开始更多地关注海外机会——也即后来的Canada Mitacs项目，这个之后会再详谈。



------



### 关于暑研做的东西

最后还是想简单总结一下这次暑研做的东西：**RIGMS Testbed for IoT Cybersecurity Using Machine Learning Based Approach**



整体思路很大程度上参考了这篇：*SCADA System Testbed for Cybersecurity Research Using Machine Learning Approach*，连标题都是模仿它的好吧......这个系列作者的工作很有意思，对于想入门IoT+Security方向的，他们的工作**必看**。



anyway，我们的工作是依照之前实现的IoT-System进行魔改，目的是把这个现成的System整合成一个Physical Testbed，然后对其实施随机安全攻击（Cyber-attacks，通过现成的工具实施攻击，抓包也是现成的工具）



进一步，在攻击过程中，捕捉Traffic Activities，提取Traffic Features，最后总结分析Data Analysis，并汇总成一个独立的RIGMS-Datasets，用于后续的训练工作；



再来，我们选用了5个不同类型的ML模型来进行训练、测试，大体上达到了合适的效果（并保留了改进空间，你懂的哈哈）最后，附上Abstract......逃



> This paper proposes a real-time intelligent garbage monitoring system (RIGMS) testbed for IoT cybersecurity research. The testbed is established by realistic devices in the physical world, which is a stage in the process of municipal waste disposal. Multiple-mix-attacks were conducted based on the testbed. During the attack scenarios, the network activities were analyzed, and the traffic features were extracted to design a representative RIGMS dataset for training and verifying the authenticity of the machine learning based models. In this paper, five advanced ML models were utilized to detect the cyber-attacks. Experiment results verified the feasibility of implementing learning based models to detect multiple-mix-attacks.



*然后上图：*

<div>
<img src="/blogs/cambridge.assets/attacks.png">
</div>



![img](/Users/lancecai/Documents/GitHub/GuangLun2000.github.io/blogs/cambridge.assets/F354CC71-43C8-4956-9E7D-CBF6B1FDD60E.45778736cee449129ca8dfda2a540ea8.png)

*图3—Testbed的主要框架*



![img](/Users/lancecai/Documents/GitHub/GuangLun2000.github.io/blogs/cambridge.assets/BE029E66-C7EB-498A-83A9-FEAF356090BC.c3b8de2981624a1bb20921b43173d382.png)

*图5—训练测试的flow-chart*



![img](/Users/lancecai/Documents/GitHub/GuangLun2000.github.io/blogs/cambridge.assets/D252CE28-83D5-4B43-86F3-02260164C872.46423ac0ea324dc2ab12abffe2c68638.png)

*表9—最终跑出来的效果（by lyc）*



![img](/Users/lancecai/Documents/GitHub/GuangLun2000.github.io/blogs/cambridge.assets/ED66FE31-3BD8-4E0F-853E-691D04D58900.b7f8bcaacf234315a738b4bf728d5ccc.png)

*图6—Matlab画的Acc对比图，DDL最后一天下午现学现画的......这里强推[图通道]*



> 以上是几张我觉得最舒服的图片（不过会有人关注这个嘛，哈哈...）



------



### 写在最后



Research of IoT已然是一片红海，和IR/VR、无人机，甚至是今年的元宇宙都很像。突然概念爆火，然后一堆人蜂拥而入。



在每年产出数万篇的论文里，可能不到3000篇值得看（要锤别人先锤自己，包括我们的上一篇，可以自定义为‘学术楽色’）。而在这3000篇值得review的文章里头，能进一步，值得深入分析，甚至复现的，可能就不到200篇了？且看且珍惜吧......



另外，这几天水知乎看到这么个题目：*# 如何看待广西自治区政府奖学金评审，广西大学推荐人选跨专业取得多项成果和发明专利，大学生真有这么厉害吗？*



均分不到70，却有40+个项目......各种专利、软著（经查大部分都是并未得到授权的，反正都稀里糊涂填上去）——然后，这样的履历真的漂亮吗？评选出这样履历的学校们，真的光彩吗？



> 分享我在这个话题下的回答：
>
> 
>
> “脚踏实地，脚踏实地啊，学弟学妹们”
>
> 
>
> 人生是要跨越**100级**台阶的，而这**第1、2、3级**台阶走得多快，对于人生的整体而言，无足轻重。要明白，走得快并不代表走得远。
>
> 
>
> 进一步，有一步的欢喜。



本科生进实验室，发paper，绝对是利大于弊的，即使是所谓的‘灌水’——*毕竟丘先生说过，“绝大部分的数学论文都是...”*——从这点出发，有Paper至少能证明你科研的能力、激情与基本素养...



但是，绝不要提倡**为了卷而卷的本科生科研**，不要涌入**一切为了刷简历的囹圄当中”**。



在FZU-MIEC的三年，我见过太多一心为了刷履历、卷综测，最后落得身败名裂，两头空的家伙——读者朋友们，请一定不要如此呀。



**“人生，是要跨越一百级台阶的。”**



------

### 之后的打算





