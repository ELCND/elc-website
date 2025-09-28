---
layout: sidebar
title: Members
subpage1: About
subpage1url: about.html
subpage2: Members
subpage2url: bios.html
subpage3: FYEC
subpage3url: fyec.html
nav: Council
---
  <!-- Page Content -->
  
<style>
.image-circle {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 50%;
}
</style>


<div class="grid grid-md-4">
  {% for i in (0..3) %}
    <div class="person-hover" onclick="openDialog('ex', {{ i }})"><img class="image-circle" src="img/{{ site.data.Executive[i].netid }}.jpg" hspace="0" vspace="20" id="myImage" loading="lazy">
      <h4> {{ site.data.Executive[i].Name }} </h4>
      <i> {{ site.data.Executive[i].Position }} </i>
      <dialog class="dialog-person" id="exdialog-{{i}}">
        <link rel="horizontal-xs" href="./stylesheets/site.css">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height = "1200" width="1200" src="img/{{ site.data.Executive[i].netid }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ site.data.Executive[i].Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ site.data.Executive[i].Position }}</em>
            </p>
            <p class="dialog-content">
              {{ site.data.Executive[i].Email }}
              <br>
              {{ site.data.Executive[i].Bio }}
            </p>
          </div>
        </div>
      </dialog>
    </div>
   {% endfor %}
</div>

<h2>Senior Directors</h2>
<div class="grid grid-md-4">
  {% for i in (0..4) %}
    <div class="person-hover" onclick="openDialog('sd', {{ i }})"><img class="image-circle" src="img/{{ site.data.Director[i].netid }}.jpg" hspace="0" vspace="30" id="myImage" loading="lazy" height="1200" width="1200">
      <h4> {{ site.data.Director[i].Name }} </h4>
      <i> {{ site.data.Director[i].Position }} </i>
      <dialog class="dialog-person" id="sddialog-{{i}}">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height = "1200" width="1200" src="img/{{ site.data.Director[i].netid }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ site.data.Director[i].Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ site.data.Director[i].Position }}</em>
            </p>
            <p class="dialog-content">
              {{ site.data.Director[i].Email }}
              <br>
              {{ site.data.Director[i].Bio }}
            </p>
          </div>
        </div>
      </dialog>
    </div>
   {% endfor %}
</div>

<h2>Junior Directors</h2>
<div class="grid grid-md-4">
  {% for i in (0..3) %}
    <div class="person-hover" onclick="openDialog('jd', {{ i }})"><img class="image-circle" src="img/{{ site.data.jrDirector[i].netid }}.jpg" hspace="0" vspace="30" id="myImage" loading="lazy" height="1200" width="1200">
      <h4> {{ site.data.jrDirector[i].Name }} </h4>
      <i> {{ site.data.jrDirector[i].Position }} </i>
      <dialog class="dialog-person" id="jddialog-{{i}}">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height = "1200" width="1200" src="img/{{ site.data.jrDirector[i].netid }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ site.data.jrDirector[i].Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ site.data.jrDirector[i].Position }}</em>
            </p>
            <p class="dialog-content">
              {{ site.data.jrDirector[i].Email }}
              <br>
              {{ site.data.jrDirector[i].Bio }}
            </p>
          </div>
        </div>
      </dialog>
   {% endfor %}
</div>

<h2>Chairs</h2>
<div class="grid grid-md-4">
  {% for i in (0..4) %}
    <div class="person-hover" onclick="openDialog('ch', {{ i }})"><img class="image-circle" src="img/{{ site.data.Chair[i].netid }}.jpg" hspace="0" vspace="30" id="myImage" loading="lazy" height="1200" width="1200">
      <h4> {{ site.data.Chair[i].Name }} </h4>
      <i> {{ site.data.Chair[i].Position }} </i>
      <dialog class="dialog-person" id="chdialog-{{i}}">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height="1200" width="1200" src="img/{{ site.data.Chair[i].netid }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ site.data.Chair[i].Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ site.data.Chair[i].Position }}</em>
            </p>
            <p class="dialog-content">
              {{ site.data.Chair[i].Email }}
              <br>
              {{ site.data.Chair[i].Bio }}
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
