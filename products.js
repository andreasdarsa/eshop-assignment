let i = 0;
let intervalID;
const slides = document.getElementsByClassName('slide');
const slideshow = document.querySelector('.slideshow');
const nextButton = document.querySelector('.next');
const prevButton = document.querySelector('.prev');
const homeButton = document.getElementById('home');
const searchButton = document.getElementById('search');
const productsButton = document.getElementById('toProducts');
const aboutButton = document.getElementById('about');

if (slideshow) {
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

    nextButton.addEventListener('click', () => {
        showNextSlide();
        restartInterval();
    });

    prevButton.addEventListener('click', () => {
        showPrevSlide();
        restartInterval();
    });

    intervalID = setInterval(showNextSlide, 3000);
}

if (homeButton) {
    homeButton.addEventListener('click', () => {
         window.location.href = 'homepage.html';
    });
}
if (searchButton) {
    searchButton.addEventListener('click', () => {
        const searchBar = document.getElementById('searchBar');
        searchBar.classList.toggle('show');
    });
}
if (productsButton) {
    productsButton.addEventListener('click', () => {
        window.location.href = 'products.html';
    });
}
if (aboutButton) {
    aboutButton.addEventListener('click', () => {
         alert('2025 Project NIS-07-01:\nBill Zervos - AEM: 4442\nAndreas Darsaklis - AEM: 4403\nname3 - AEM3\n');
    });
}