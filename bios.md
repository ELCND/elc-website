---
layout: sidebar
title: Members
subpage1: About
subpage1url: about.html
subpage2: Members
subpage2url: bios.html
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

<h2>Executives</h2>
<div class="grid grid-md-4">
  {% for m in site.data.Executive %}{% if m.Name %}
    <div class="person-hover" onclick="openDialog('ex', {{ forloop.index0 }})"><img class="image-circle" src="img/{{ m.netid | strip }}.jpg" hspace="0" vspace="20" id="myImage" loading="lazy">
      <h4> {{ m.Name }} </h4>
      <i> {{ m.Position }} </i>
      <dialog class="dialog-person" id="exdialog-{{forloop.index0}}">
        <link rel="horizontal-xs" href="./stylesheets/site.css">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height = "1200" width="1200" src="img/{{ m.netid | strip }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ m.Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ m.Position }}</em>
            </p>
            <p class="dialog-content">
              {{ m.Email }}
              <br>
              {{ m.Bio }}
            </p>
          </div>
        </div>
      </dialog>
    </div>
   {% endif %}{% endfor %}
</div>

<h2>Committee Heads</h2>
<div class="grid grid-md-4">
  {% for m in site.data.srDirector %}{% if m.Name %}
    <div class="person-hover" onclick="openDialog('sr', {{ forloop.index0 }})"><img class="image-circle" src="img/{{ m.netid | strip }}.jpg" hspace="0" vspace="30" id="myImage" loading="lazy" height="1200" width="1200">
      <h4> {{ m.Name }} </h4>
      <i> {{ m.Position }} </i>
      <dialog class="dialog-person" id="srdialog-{{forloop.index0}}">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height = "1200" width="1200" src="img/{{ m.netid | strip }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ m.Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ m.Position }}</em>
            </p>
            <p class="dialog-content">
              {{ m.Email }}
              <br>
              {{ m.Bio }}
            </p>
          </div>
        </div>
      </dialog>
    </div>
   {% endif %}{% endfor %}
</div>

<h2>Directors</h2>
<div class="grid grid-md-4">
  {% for m in site.data.Director %}{% if m.Name %}
    <div class="person-hover" onclick="openDialog('sd', {{ forloop.index0 }})"><img class="image-circle" src="img/{{ m.netid | strip }}.jpg" hspace="0" vspace="30" id="myImage" loading="lazy" height="1200" width="1200">
      <h4> {{ m.Name }} </h4>
      <i> {{ m.Position }} </i>
      <dialog class="dialog-person" id="sddialog-{{forloop.index0}}">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height = "1200" width="1200" src="img/{{ m.netid | strip }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ m.Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ m.Position }}</em>
            </p>
            <p class="dialog-content">
              {{ m.Email }}
              <br>
              {{ m.Bio }}
            </p>
          </div>
        </div>
      </dialog>
    </div>
   {% endif %}{% endfor %}
</div>

<h2>Chairs</h2>
<div class="grid grid-md-4">
  {% for m in site.data.Chair %}{% if m.Name %}
    <div class="person-hover" onclick="openDialog('ch', {{ forloop.index0 }})"><img class="image-circle" src="img/{{ m.netid | strip }}.jpg" hspace="0" vspace="30" id="myImage" loading="lazy" height="1200" width="1200">
      <h4> {{ m.Name }} </h4>
      <i> {{ m.Position }} </i>
      <dialog class="dialog-person" id="chdialog-{{forloop.index0}}">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height="1200" width="1200" src="img/{{ m.netid | strip }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ m.Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ m.Position }}</em>
            </p>
            <p class="dialog-content">
              {{ m.Email }}
              <br>
              {{ m.Bio }}
            </p>
          </div>
        </div>
      </dialog>
    </div>
   {% endif %}{% endfor %}
</div>

<h2>Committee Members</h2>
<div class="grid grid-md-4">
  {% for m in site.data.Member %}{% if m.Name %}
    <div class="person-hover" onclick="openDialog('mb', {{ forloop.index0 }})"><img class="image-circle" src="img/{{ m.netid | strip }}.jpg" hspace="0" vspace="30" id="myImage" loading="lazy" height="1200" width="1200">
      <h4> {{ m.Name }} </h4>
      <i> {{ m.Position }} </i>
      <dialog class="dialog-person" id="mbdialog-{{forloop.index0}}">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height="1200" width="1200" src="img/{{ m.netid | strip }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ m.Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ m.Position }}</em>
            </p>
            <p class="dialog-content">
              {{ m.Email }}
              <br>
              {{ m.Bio }}
            </p>
          </div>
        </div>
      </dialog>
    </div>
   {% endif %}{% endfor %}
</div>

<h2>First Year Engineering Council</h2>
{% assign fyec_shown = 0 %}
<div class="grid grid-md-4">
  {% for m in site.data.FYEC %}{% if m.Name %}
    {% assign fyec_shown = fyec_shown | plus: 1 %}
    <div class="person-hover" onclick="openDialog('fy', {{ forloop.index0 }})">
      <img class="image-circle" src="img/{{ m.netid | strip }}.jpg"
           hspace="0" vspace="30" id="myImage" loading="lazy"
           height="1200" width="1200">
      <h4> {{ m.Name }} </h4>
      <i> {{ m.Position }} </i>
      <dialog class="dialog-person" id="fydialog-{{forloop.index0}}">
        <form method="dialog" class="dialog-close">
          <button title="Close">
            x
          </button>
        </form>
        <div class="dialog-frame">
          <div class="dialog-image">
            <img height="1200" width="1200"
                 src="img/{{ m.netid | strip }}.jpg" alt>
          </div>
          <div class="dialog-body">
            <h4 class="dialog-title">
              {{ m.Name }}
            </h4>
            <p class="dialog-desc">
              <em>{{ m.Position }}</em>
            </p>
            <p class="dialog-content">
              {{ m.Email }}
              <br>
              {{ m.Bio }}
            </p>
          </div>
        </div>
      </dialog>
    </div>
   {% endif %}{% endfor %}
</div>
{% if fyec_shown == 0 %}
  <p class="pending-note">This year's First Year Engineering Council is still being formed — check back soon for member bios!</p>
{% endif %}

<script>
function openDialog(level, index) { 
  document.getElementById(level + "dialog-" + index.toString()).showModal(); 
} 
</script>
