---

layout: page
permalink: /publications/index.html
title: Publications
pubs:
  - author: "Jason Ansel, Marek Olszewski"
    title: "BFTree - Scaling HotStuff to Millions of Validators"
    month: "June"
    year: "2019"
    booktitle: "Whitepaper"
    url: "https://medium.com/celohq/bftree-scaling-hotstuff-to-millions-of-validators-7d6930ee046a"

  - author: "Dongqi Su, Ying Yin Ting, Jason Ansel"
    title: "Tight Prediction Intervals Using Expanded Interval Minimization"
    month: "June"
    year: "2018"
    booktitle: "Technical Report"
    url: "https://arxiv.org/abs/1806.11222"

  - author: "Jason Ansel, Han Hong, Jessie Li"
    title: "OLS and 2SLS in Randomized and Conditionally Randomized Experiments"
    month: "March"
    year: "2018"
    booktitle: "Journal of Economics and Statistics"
    url: "https://doi.org/10.1515/jbnst-2018-0016"

  - author: "Daniel Haas, Jason Ansel, Lydia Gu, Adam Marcus"
    title: "Argonaut: Macrotask Crowdsourcing for Complex Data Processing"
    keywords: "Locu"
    month: "September"
    year: "2015"
    address: "Kohala Coast, Hawaii"
    booktitle: "International Conference on Very Large Data Bases"
    url: 2015vldb-argonaut.pdf
    bibtex: 2015vldb-argonaut.bib

  - key: "ding:pldi:2015"
    author: "Yufei Ding, Jason Ansel, Kalyan Veeramachaneni, Xipeng Shen, Una-May O’Reilly, Saman Amarasinghe"
    title: "Autotuning Algorithmic Choice for Input Sensitivity"
    url: "http://groups.csail.mit.edu/commit/papers/2015/yding-pldi15-pbinput.pdf"
    keywords: "OpenTuner"
    month: "June"
    year: "2015"
    address: "Portland, Oregon"
    booktitle: "ACM SIGPLAN Conference on Programming Language Design, Implementation"

  - key: "ansel:pact:2014"
    author: "Jason Ansel, Shoaib Kamil, Kalyan Veeramachaneni, Jonathan Ragan-Kelley, Jeffrey Bosboom, Una-May O'Reilly, Saman Amarasinghe"
    title: "OpenTuner: An Extensible Framework for Program Autotuning"
    url: "http://groups.csail.mit.edu/commit/papers/2014/ansel-pact14-opentuner.pdf"
    slides: "http://groups.csail.mit.edu/commit/papers/2014/ansel-pact14-opentuner-slides.pdf"
    keywords: "OpenTuner"
    month: "August"
    year: "2014"
    address: "Edmonton, Canada"
    booktitle: "International Conference on Parallel Architectures and Compilation Techniques"



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

# Patents

Null.
