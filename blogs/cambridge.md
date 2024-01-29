---
layout: page
permalink: /blogs/cambridge/index.html
title: Cambridge
---

## Cambridge 线上暑研回忆录

> 本文第一版发表于 [mieclance博客](https://mieclance.club/archives/4389)，下为修改版
>
> 记录了2022年7月—12月发生的故事（暑研、大三上）
>
> 中英文混用预警，还请见谅

### 写在最前面

10月21号正式提交论文后，就进入了大三学年以来最舒服的一个周末。而过去三个月来暑研的困难程度，和我6月份报名投递申请时所想象的完全不同。

<br>整体上来看，CCISTC线上暑研（下称Camb暑研）大体分为四个部分：

- Academic Practical （10学时，基本的科研学术技能、机器学习入门）
- Workshop（12学时，可以理解为工具课；雅思英语、留学规划、学术网站，教你怎么宣传自己）
- AI Lecture（6学时，所谓的大佬正课，但我其实没听懂多少，这个后面会讲到）
- Research Project（暑研课题，大约花费了300-320小时？巨累）

<br>而Camb暑研最后的成果考评是基于以下三个部分：

- 暑研课程出勤（10%，大家都差不多，甚至请假还可以豁免，这个不提）
- Research Proposal（45%，单写作花了5天时间）
- Final Report（45%，单写作花了14天时间）

<br>最后放一下成绩单和推荐信，相当于"暑研收获"了

- Certificate of Completion 结课证明，没啥用
- Programme Transcript 成绩单(双A)，还算不错，CV上可以多两个字符？
- Letter of Recommendation 基本算“模版推”，没想到的是，之后在暑研申请派上用场了，这个会在另一篇文章细聊。

<center>
<img src="/blogs/cambridge.assets/rl.png">
</center>



------

### 关于暑研本身

就针对暑研来说，线下的体验绝对是更好、收获更多的。但**疫情影响**（担心新学期，学校不给进，隔离周期太长）；还有就是**实力太差**（没错就是菜，大二无paper无connection弱鸡，根本申不到实地暑研）

<br>所以最终选择走付费暑研这种野路子，虽然含金量不高，但胜在方便，不会打乱节奏。总之，从今年6月确定收到offer开始，到正式出成绩单（11月中旬），完整的流程大概是走了5个月。

<br>说回暑研本身，导师 Pietro Liò 是意大利人，在剑桥拿到了Msc学位，然后回意大利攻了**两个PhD** (Systems Dynamics & Theoretical Genetics)，而近几年他主要是做图神经网络和计算生物学。

<br>但就像同项目的朋友(wyc)在知乎上吐槽的，教授的英文口音确实是一言难尽，三节AI正课几乎听不懂——当然，一方面确实是口音的问题，但更多的是ML (机器学习) 经历的欠缺。不过，至少这次暑研在比较感兴趣的 **ML+IIoT** 领域，做了比较深入的文献综述，最后产出的 [Research Proposal](https://caihanlin.com/mypaper/IP/Proposal.pdf) 和 [Final Report](https://caihanlin.com/mypaper/202210camb.pdf) 在大三下的实习学期也给我带来了很大的便利。

<br>最后还要提到，暑研的 Supervisor 是 Liò 教授的二年级博士生，我们叫他Jerry学长——北邮本科，然后在 Sheffield 读了一年MSc，在PhD阶段来到了剑桥做Wireless和ML

<br>学长主要是负责给我们上 Practical（学术技能和ML入门）和 Supervision（项目辅导，给我们的课题进展提供建议）两门课，豪不夸张地说，这次暑研的质量与体验感，很大程度上都是靠Jerry学长撑起来的。

---

### 同期的故事

暑研的同期，把大二下学期搞的那篇 [IoT-System](https://caihanlin.com/mypaper/202208cenim.pdf) 的文章给投了，稀里糊涂中的某IEEE亚洲水会，虽然水的一批，但总算是完成了自己的第一段经历。

<br>同时，大三学年停掉了一切学生工作之后，终于可以静下心来学习、读论文、做自己真正喜欢的事情了。大三上，拿到了本科生涯第1次专业第一（GPA3.97），开始做[第二篇文章](https://caihanlin.com/mypaper/202302ICAROB.pdf)并投稿，达到了舒适的**Work-Life-Balance**，总而言之，我逐渐达到了自己所向往的生活。

<br>而回过头来，这次Camb暑研的经历，也让我暂时是坚定了未来攻读PhD的念头。与此同时，受暑研同学（wyc, chx, wjy）的启发，也让我开始更多地关注海外机会——即后来的“海外暑研申请”，这个后面会再写一篇文章细谈。



------

### 关于暑研做的东西

最后还是想简单总结一下这次暑研做的东西。

<br>整体思路很大程度上参考了这篇：SCADA System Testbed for Cybersecurity Research Using Machine Learning Approach（连标题都是模仿的，这个系列作者的工作可读性很强）

<br>总之，我们的工作是依照之前实现的 IoT-System 进行魔改，目的是把这个现成的System整合成一个Physical Testbed，然后对其实施定向多源安全攻击（Mutiple-Mixed-Attacks，通过现成的工具实施攻击，抓包也是现成的工具）

<br>进一步，在攻击过程中，捕捉Traffic Activities，提取Traffic Features，最后对数据进行挖掘分析、打标签并汇总，用于后续的训练测试。最后，我们选用了5个不同类型的ML模型来进行训练、测试验证。

<br>最后上几张图吧：

<left>
<img src="/blogs/cambridge.assets/system.png">
</left>
*图3—Testbed的主要框架*

<left>
<img src="/blogs/cambridge.assets/flowchart.png">
</left>
*图5—训练测试的flow-chart*

<left>
<img src="/blogs/cambridge.assets/table.png">
</left>

*表9—最终跑出来的效果*

<left>
<img src="/blogs/cambridge.assets/results.png">
</left>
*图6—Matlab画的Acc对比图*



------

### 写在最后

最后是闲聊时间。

<br>这几天在知乎看到这么个题目：*# 如何看待广西自治区政府奖学金评审，广西大学推荐人选跨专业取得多项成果和发明专利，大学生真有这么厉害吗？*

<br>均分不到70，却有40+个项目...各种专利、软著（经查大部分都是并未得到授权的，反正都稀里糊涂填上去），这样的履历真的漂亮吗？评选出这样履历的学校们，真的光彩吗？

> “脚踏实地，脚踏实地啊，学弟学妹们”，人生是要跨越**100级**台阶的，而这**第1、2、3级**台阶走得多快，对于人生的整体而言，无足轻重。要明白，走得快并不代表走得远。

本科生进实验室，做paper，绝对是利大于弊的，即使是所谓的“灌水”——毕竟Q先生说过——“90%的数学论文都是...”——从这点出发，有paper至少能证明你科研的能力、激情与基本素养。

<br>但是，绝不要提倡**为了卷而卷的本科生科研**，不要涌入**“一切为了刷简历”**的囹圄当中。在 FZU-MIEC 的三年，我们见过太多一心为了刷履历、卷综测，最后落得身败名裂，两头空的家伙——读者朋友们，请一定勿忘初心呀。

<br>**“人生，是要跨越一百级台阶的。”**

<br>

------

### 后来的故事

> 谢谢你看到这里，改天再更。
