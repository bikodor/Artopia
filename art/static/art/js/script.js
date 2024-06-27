"use strict";
function onEntry(entry) {
    entry.forEach(change => {
        if (change.isIntersecting) {
            change.target.classList.add('element-show');
        }
    });
}
let options = {
    threshold: [0.5] };
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.animation');

for (let elm of elements) {
    observer.observe(elm);
}


function openFullscreen(img) {
  var modal = document.getElementById("modal");
  var modalImg = document.getElementById("modal-content");
  modal.style.display = "block";
  modalImg.src = img.src;
}

function closeFullscreen() {
  var modal = document.getElementById("modal");
  modal.style.display = "none";
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("burger").addEventListener("click", function(){
    document.querySelector("a.animation").classList.toggle("hide")
    document.querySelector("nav").classList.toggle("open")})

})

