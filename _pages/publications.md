---
layout: page
permalink: /publications/
title: Publications
description: 
years: [2022, 2021, 2020, 2017, 2014]
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
