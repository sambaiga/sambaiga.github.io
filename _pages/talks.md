---
layout: page
title: Talks
permalink: /talks/
description: 
nav: true
---


{% if site.data.conference_talks %}

### Conference Presentation
<div class="jumbotron">
<ul>
{% for publi in site.data.conference_talks %}
<li> 
<strong>{{ publi.title }}</strong> <br/> 
 {{ publi.authors | replace_first: 'A. Faustine', '<b>A. Faustine</b>'}} <br/>
 <i>{{ publi.conf }}</i> ({{ publi.year }})  
 {% if publi.url %}
 <a href="{{ site.url }}{{ site.baseurl }}/talk/{{ publi.url }}.pdf" target="_blank"><i class="far fa-file" aria-hidden="true"></i>slides</a>{% endif %} 
 {% if publi.link %}
 <a href="{{ publi.link }}" target="_blank"><i class="fas fa-link" aria-hidden="true"></i>link</a>
 {% endif %}
 {% if publi.youtube %} 
   <a data-toggle="collapse" href="#{{publi.youtube}}" aria-expanded="false" aria-controls="{{publi.youtube}}"><i class="fa fa-film"  aria-hidden="true"></i>video</a>
   {% endif %}
{% if publi.youtube %} 
<div class="collapse" id="{{publi.youtube}}"><div class="well-collapse">
<div class="row justify-content-sm-center"> 
<div class="embed-responsive embed-responsive-16by9">
<center>
    <iframe  src="https://www.youtube.com/embed/{{publi.youtube}}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

</div>
</div>
 </div></div>
   {% endif %}
 </li>
 {% endfor %}
 </ul>
</div>


{% endif %}


{% if site.data.invited_talks %}

### Invited Talks and Workshop
<div class="jumbotron">
<ul>
{% for publi in site.data.invited_talks %}
<li> 
<strong>{{ publi.title }}</strong> <br/> 
 {{ publi.authors | replace_first: 'A. Faustine', '<b>A. Faustine</b>'}} <br/>
 <i>{{ publi.conf }}</i> ({{ publi.year }})  
 {% if publi.url %}
 <a href="{{ site.url }}{{ site.baseurl }}/talk/{{ publi.url }}.pdf" target="_blank"><i class="far fa-file" aria-hidden="true"></i>slides</a>{% endif %} 
 {% if publi.link %}
 <a href="{{ publi.link }}" target="_blank"><i class="fas fa-link" aria-hidden="true"></i>link</a>
 {% endif %}
 {% if publi.youtube %} 
   <a data-toggle="collapse" href="#{{publi.youtube}}" aria-expanded="false" aria-controls="{{publi.youtube}}"><i class="fa fa-film"  aria-hidden="true"></i>video</a>
   {% endif %}
{% if publi.youtube %} 
<div class="collapse" id="{{publi.youtube}}"><div class="well-collapse">
<div class="row justify-content-sm-center"> 
<div class="embed-responsive embed-responsive-16by9">
<center>
    <iframe  src="https://www.youtube.com/embed/{{publi.youtube}}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

</div>
</div>
 </div></div>
   {% endif %}
 </li>
 {% endfor %}
 </ul>
</div>
{% endif %}