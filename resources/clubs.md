---
layout: sidebar
title: Engineering Societies
subpage1: First Year
subpage1url: first_year
subpage2: Engineering Societies
subpage2url: clubs
subpage3: FYEC Newsletter
subpage3url: fyec_newsletter
nav: Resources
---
<p class="lede"> Below you will find a table populated
with  contact information for a variety of different engineering societies here
on campus. Reach out to the contact of the society you are interested in. </p>
<table>
  <thead>
    <tr>
      <th>Engineering Society</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    {% for i in (0..12) %}
      <tr>
        <td>{{ site.data.clubs[i].Club}}</td>
        <td>{{ site.data.clubs[i].Email}}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>
