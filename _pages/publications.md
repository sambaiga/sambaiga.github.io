---
layout: page
permalink: /publications/
title: Publications
description: 
years: [2021, 2020, 2017]
nav: true
---

<div class="publications">

{% for y in page.years %}
<div class="jumbotron">
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
  </div>
{% endfor %}

</div>
