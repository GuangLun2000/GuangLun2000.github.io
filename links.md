---
layout: page
permalink: /links/index.html
title: Links
comments: true

---

## Blogs

Here is my Blogs written by Chinese.

[《MIEC笔记》](https://mieclance.club/bao/lance-note)

[《Lance的回忆录》](https://mieclance.club/bao/lance-memoirs)

## Contact

***Jan 2023:*** I have set up some [online-coffee-time](https://calendly.com/lancecai/meet-with-lance) (Inspired by **[Shangzhe Wu](https://elliottwu.com/)**).

<!-- Calendly inline widget begin -->

<div class="calendly-inline-widget" data-url="https://calendly.com/lancecai/meet-with-lance" style="min-width:320px;height:630px;"></div>
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>

<!-- Calendly inline widget end -->

## Comment

{% if page.comments %}
<div id="disqus_thread"></div>
<script>
var disqus_config = function () {
this.page.url ="https://caihanlin.com/{{page.url}}" // <--- 修改成你的博客地址
this.page.identifier ="https://caihanlin.com/{{page.url}}";
};
(function() { // DON'T EDIT BELOW THISLINE
var d = document, s = d.createElemen('script');
s.src ='https://www-caihanlin-com.disqus.com/embed.js';// <--- 修改成你的 disqus 站点缩写名
s.setAttribute('data-timestamp', +newDate());
(d.head || d.body).appendChild(s);
})();
</script>


<noscript>Please enable JavaScript toview the <a href="https://disqus.com/ref_noscript" rel="nofollow">commentspowered by Disqus.</a></noscript>

{% endif %}
