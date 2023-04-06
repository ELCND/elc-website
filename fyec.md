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

<div class="grid grid-md-4">
  {% for i in (0..7) %}
    <div class="person-hover" onclick="openDialog('ex', {{ i }})"><img class="image-circle" src="img/{{ site.data.FYEC[i].netid }}.jpg" hspace="0" vspace="20" id="myImage" loading="lazy">
      <h4> {{ site.data.FYEC[i].Name }} </h4>
      <i> {{ site.data.FYEC[i].Position }} </i>
      <dialog class="dialog-person" id="exdialog-{{i}}">
        <link rel="horizontal-xs" href="./stylesheets/site.css">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height = "1200" width="1200" src="img/{{ site.data.FYEC[i].netid }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ site.data.FYEC[i].Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ site.data.FYEC[i].Position }}</em>
            </p>
            <p class="dialog-content">
              {{ site.data.FYEC[i].Email }}
              <br>
              {{ site.data.FYEC[i].Bio }}
            </p>
          </div>
        </div>
      </dialog>
    </div>
   {% endfor %}
</div>

<script>
function openDialog(level, index) { 
  document.getElementById(level + "dialog-" + index.toString()).showModal(); 
} 
</script>