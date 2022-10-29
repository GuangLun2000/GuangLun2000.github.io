---

layout: page
permalink: /publications/index.html
title: Publications
pubs:

  - author: "Hanlin Cai, Jiaqi Hu, Zheng Li, Wei Hong Lim, Mastaneh Mokayef, Chin Hong Wong"
    title: "An IoT Garbage Monitoring System for Effective Garbage Management"
    keywords: "IoT"
    month: "November"
    year: "2022"
    address: "Surabaya, Malaysia"
    booktitle: "International Conference on Computer Engineering, Network and Intelligent Multimedia ([CENIM])"
    url: "https://caihanlin.com/mypaper/202208cenim.pdf"




---

# Publications

{% for pub in page.pubs %}
{% unless pub.hidden %}

  - {% if pub.url %} [{{pub.title}}]({{pub.url}}).
    {% else %} {{pub.title}}.
    {% endif %}{% if pub.type %}({{pub.type}})
    {% endif %}<br>
    {{pub.author}}.<br>
    {% if pub.type == 'Technical Report' %}{{pub.number}}
    {% endif %}{{pub.booktitle}}{{pub.school}}{{pub.journal}}.<br>
    {% if pub.address %}{{pub.address}}.
    {% endif %} {{pub.month}}, {{pub.year}}. {% if pub.slides %}[Slides]({{pub.slides}}).
    {% endif %}{% if pub.key %}[Bibtex](http://groups.csail.mit.edu/commit/bibtex.cgi?key={{pub.key}}).
    {% endif %}{% if pub.bibtex %}[Bibtex]({{pub.bibtex}}).
    {% endif %}
    {% endunless %}
    {% endfor %}



[CENIM]: http://cenim.its.ac.id/#pdfexpress



# Working Paper

- *Real-time Intelligent Garbage Monitering System Testbed for IoT Cybersecurity*.  

  Under the guidance of [Prof. Pietro Lio'](https://www.cl.cam.ac.uk/~pl219/ ) and [Chin-Hong Wong](https://www.researchgate.net/profile/Chin-Hong-Wong )  

  Support by the Cyber Range Lab at Fuzhou University  

  Expect to submit to Rivest, Shamir and Adleman (RSA) conference 2023  

  The latest manuscript can be found [Here](https://caihanlin.com/mypaper/202210camb.pdf) (Update in 29th Oct 2022)  





