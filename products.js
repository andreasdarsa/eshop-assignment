let i = 0;
let intervalID;
const API_BASE = 'http://localhost:5000';
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

async function fetchAllProducts() {
    const response = await fetch(`${API_BASE}/search?q=`);
    const products = await response.json();
    renderProducts(products);
}

function renderProducts(products) {
    const container = document.getElementById('productListContainer');
    container.innerHTML = '';

    products.forEach(product => {
        const div = document.createElement('div');
        div.className = 'product-item';
        div.innerHTML = `<span class="name">${product.name}</span>`;
        container.appendChild(div);
    });
}

if (homeButton) {
    homeButton.addEventListener('click', () => {
         window.location.href = 'homepage.html';
    });
    fetchAllProducts();
}
if (searchButton) {
    searchButton.addEventListener('click', () => {
        const searchBar = document.getElementById('searchBar');
        searchBar.classList.toggle('show');
    });
    document.getElementById('searchBar').addEventListener('submit', async (e) => {
        e.preventDefault();
        const query = document.getElementById('searchBarInput').value;
        const response = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`);
        const results = await response.json();
        renderProducts(results);
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