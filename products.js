let i = 0;
let intervalID;
const slides = document.getElementsByClassName('slide');
const nextButton = document.querySelector('.next');
const prevButton = document.querySelector('.prev');

function showNextSlide() {
    slides[i].classList.remove('active');
    i = (i + 1) % slides.length;
    slides[i].classList.add('active');
}

function showPrevSlide() {
    slides[i].classList.remove('active');
    i = (i - 1 + slides.length) % slides.length;
    slides[i].classList.add('active');
}

function restartInterval() {
    clearInterval(intervalID);
    intervalID = setInterval(showNextSlide, 3000);
}

nextButton.addEventListener('click',() => {
    showNextSlide();
    restartInterval();
});

prevButton.addEventListener('click',() => {
    showPrevSlide();
    restartInterval();
});

intervalID= setInterval(showNextSlide, 3000);