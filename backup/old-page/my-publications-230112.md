---
layout: page
permalink: /publications/index.html
title: Publications
pubs:
  - author: "Hanlin Cai, Zheng Li, Jiaqi Hu, Wei Hong Lim, Sew Sun Tiang, Mastaneh Mokayef, Chin Hong Wong"
    title: "Deep Residual Neural Network for Efficient Traffic Sign Detection"
    url: "https://caihanlin.com/mypaper/202302ICAROB.pdf"
    keywords: "RNN"
    month: "February"
    year: "2023"
    address: "Oita, Japan"
    booktitle: "28th International Conference on Artificial Life and Robotics ([ICAROB])"

  - author: "Hanlin Cai, Jiaqi Hu, Zheng Li, Wei Hong Lim, Mastaneh Mokayef, Chin Hong Wong"
    title: "An IoT Garbage Monitoring System for Effective Garbage Management"
    url: "https://caihanlin.com/mypaper/202208cenim.pdf"
    slides: "https://caihanlin.com/mypaper/slides/2022-CENIM-Pre-v2.pdf"
    Talk: "https://www.bilibili.com/video/BV1jv4y1S7VQ/"
    keywords: "IoT"
    month: "November"
    year: "2022"
    address: "Surabaya, Malaysia"
    booktitle: "4th International Conference on Computer Engineering, Network and Intelligent Multimedia ([CENIM])"

---







# Publications

{% for pub in page.pubs %}
{% unless pub.hidden %}

  - {% if pub.url %} [{{pub.title}}]({{pub.url}}).
    {% else %} {{pub.title}}.
    {% endif %}{% if pub.type %}({{pub.type}}){% endif %}<br>
    {{pub.author}}.<br>
    {% if pub.type == 'Technical Report' %}{{pub.number}}
    {% endif %}{{pub.booktitle}}{{pub.school}}{{pub.journal}}.<br>{% if pub.talk %}[Talk]({{pub.talk}}).{% endif %}{% if pub.slides %}[Slides]({{pub.slides}}).{% endif %}<br>{% if pub.address %}{{pub.address}}. {% endif %}{{pub.month}}, {{pub.year}}.
    {% if pub.key %}[Bibtex](http://groups.csail.mit.edu/commit/bibtex.cgi?key={{pub.key}}).{% endif %}{% if pub.bibtex %}[Bibtex]({{pub.bibtex}}).{% endif %}
    {% endunless %}
    {% endfor %}



## Working Paper

- RIGMS Testbed for IoT Cybersecurity Using Machine Learning Based Approach. *The latest manuscript [can be found here](https://caihanlin.com/mypaper/202210camb.pdf) (Update in 29th Dec 2022)*

- fsdkjal<br>



[CENIM]:http://cenim.its.ac.id/#pdfexpress
[ICAROB]:https://alife-robotics.org/



