---
layout: sidebar
title: First Year Engineering Council (FYEC)
subpage1: About
subpage1url: about.html
subpage2: Members
subpage2url: bios.html
subpage3: FYEC
subpage3url: fyec.html
nav: Council
---
<p class="lede">The First Year Engineering Council is the
  First-Year division of the Engineering Leadership Council. In this role, we work
  to establish a meaningful relationship between the students and faculty of the
  Notre Dame College of Engineering. Through our events, we provide engaging opportunities
  for students to learn, interact, and serve. We enable First-Year students to explore
   the various fields within engineering and volunteer in the South Bend community. </p>
<p><strong> Be on the lookout in your inbox for instructions on how to apply to be a part of FYEC!</strong></p>

<h2>Leadershi[</h2>
<div class="grid grid-md-2">
  {% for i in (0..3) %}
      <h4> {{ site.data.FYEC[i].Name }} </h4>
      <i> {{ site.data.FYEC[i].Position }} </i>
      <p>{{ site.data.FYEC[i].netid }}@nd.edu</p>
      <div><p>{{ site.data.FYEC[i].Bio }}</p></div>
    </div>
   {% endfor %}
<!--</div>
<h4>FYEC Members Not Pictured</h4>
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    {% for i in (0..19) %}
      <tr>
        <td>{{ site.data.FYEC2[i].Name}}</td>
        <td>{{ site.data.FYEC2[i].Email}}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>
-->
