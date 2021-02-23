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
<h2>Executives</h2>
<!-- <div class="flex-container">
  <div class="flex-child">
    <img src="ray.jpg" align="left" hspace="20" vspace="30" id="myImage">
    <h4>Ray Kman</h4>
    <i>President</i>
    <p>Devon is a senior studying Chemical Engineering with a minor in Engineering Corporate Practice from Charlotte, North Carolina. He resides in Baumer Hall, where he serves as a RA. Entering his third year with ELC, he is excited to help oversee the group's web presence and has helped relaunch the ELC website. Outside of ELC, Devon sings with the Glee Club and can often be spotted at Duncan Student Center or zooming across campus on his scooter. </p>
  </div>
  <div class="flex-child">
    <img src="ray.jpg" align="left" hspace="20" vspace="30" id="myImage">
    <h4>Ray Kman</h4>
    <i>President</i>
    <p>Devon is a senior studying Chemical Engineering with a minor in Engineering Corporate Practice from Charlotte, North Carolina. He resides in Baumer Hall, where he serves as a RA. Entering his third year with ELC, he is excited to help oversee the group's web presence and has helped relaunch the ELC website. Outside of ELC, Devon sings with the Glee Club and can often be spotted at Duncan Student Center or zooming across campus on his scooter. </p>
  </div>
</div>

-->
<div class="grid grid-md-2">
  {% for i in (0..3) %}
    <div><img src="img/{{ site.data.Executive[i].netid }}.jpg" align="left" hspace="20" vspace="30" id="myImage" loading="lazy">
      <h4> {{ site.data.Executive[i].Name }} </h4>
      <i> {{ site.data.Executive[i].Position }} </i>
      <p> {{ site.data.Executive[i].Email }} </p>
      <div><p>{{ site.data.Executive[i].Bio }}</p></div>
  <!--    <div>
        <span onclick="openNav()"><a class="btn btn-md">View Bio</a></span>
        <div class="popup" id="popup1">
          <!-- The overlay -->
  <!--      <div id="myNav" class="overlay">

         <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
         <!-- Overlay content
         <div class="overlay-content">
           <p>{{ site.data.Executive[i].Bio }}</p>
         </div>
        </div>
        </div>
      </div> -->
    </div>
   {% endfor %}
</div>

<h2>Senior Directors</h2>
<div class="grid grid-md-2">
  {% for i in (0..15) %}
    <div><img src="img/{{ site.data.Director[i].netid }}.jpg" align="left" hspace="20" vspace="30" id="myImage" loading="lazy">
      <h4> {{ site.data.Director[i].Name }} </h4>
      <i> {{ site.data.Director[i].Position }} </i>
      <p> {{ site.data.Director[i].Email }} </p>
      <div> {{ site.data.Director[i].Bio }} </div>
  <!--    <div>
        <span onclick="openNav()"><a class="btn btn-md">View Bio</a></span>
        <div class="popup" id="popup1">
          <!-- The overlay ->
        <div id="myNav" class="overlay">
         <!-- Button to close the overlay navigation ->
         <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
         <!-- Overlay content ->
         <div class="overlay-content">
           <p>{{ site.data.Director[i].Bio }}</p>
         </div>
        </div>
        </div>
      </div> -->
    </div>
   {% endfor %}
</div>

<h2>Junior Directors</h2>
<div class="grid grid-md-2">
  {% for i in (0..9) %}
    <div><img src="img/{{ site.data.jrDirector[i].netid }}.jpg" align="left" hspace="20" vspace="30" id="myImage" loading="lazy">
      <h4> {{ site.data.jrDirector[i].Name }} </h4>
      <i> {{ site.data.jrDirector[i].Position }} </i>
      <p> {{ site.data.jrDirector[i].Email }} </p>
      <div> {{ site.data.jrDirector[i].Bio }} </div>
  <!--    <div>
        <span onclick="openNav()"><a class="btn btn-md">View Bio</a></span>
        <div class="popup" id="popup1">
          <!-- The overlay ->
        <div id="myNav" class="overlay">
         <!-- Button to close the overlay navigation ->
         <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
         <!-- Overlay content ->
         <div class="overlay-content">
           <p>{{ site.data.Director[i].Bio }}</p>
         </div>
        </div>
        </div>
      </div> -->

    </div>
   {% endfor %}
</div>

<h2>Chairs</h2>
<div class="grid grid-md-2">
  {% for i in (0..10) %}
    <div><img src="img/{{ site.data.Chair[i].netid }}.jpg" align="left" hspace="20" vspace="30" id="myImage" loading="lazy">
      <h4> {{ site.data.Chair[i].Name }} </h4>
      <i> {{ site.data.Chair[i].Position }} </i>
      <p> {{ site.data.Chair[i].Email }} </p>
      <div> {{ site.data.Chair[i].Bio }} </div>
  <!--    <div>
        <span onclick="openNav()"><a class="btn btn-md">View Bio</a></span>
        <div class="popup" id="popup1">
          <!-- The overlay ->
        <div id="myNav" class="overlay">
         <!-- Button to close the overlay navigation ->
         <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
         <!-- Overlay content ->
         <div class="overlay-content">
           <p>{{ site.data.Director[i].Bio }}</p>
         </div>
        </div>
        </div>
      </div> -->
    </div>
   {% endfor %}
</div>
