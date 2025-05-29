let slideIndex = 0;
let slides = [];
let intervalID;
const API_BASE = 'http://localhost:5000';
const slideshow = document.querySelector('.slideshow');
const nextButton = document.querySelector('.next');
const prevButton = document.querySelector('.prev');
const homeButton = document.getElementById('home');
const searchBar = document.getElementById('searchBar');
const productsButton = document.getElementById('toProducts');
const aboutButton = document.getElementById('about');

/* ========== SLIDESHOW ========== */

if (slideshow) {
    function showNextSlide() {
        slideIndex = (slideIndex + 1) % slides.length;
        showSlide(slideIndex);
    }

    function showPrevSlide() {
        slideIndex = (slideIndex - 1 + slides.length) % slides.length;
        showSlide(slideIndex);
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

    fetchPopularProducts();
    intervalID = setInterval(showNextSlide, 3000);
}

async function fetchPopularProducts() {
    const response = await fetch('http://localhost:5000/popular-products');
    const data = await response.json();
    renderSlides(data);
}

function renderSlides(products) {
    const container = document.getElementById('slideshow-container');
    container.innerHTML = ''; // Clear existing

    products.forEach((product, index) => {
        const slide = document.createElement('div');
        slide.className = 'slide';
        if (index === 0) slide.classList.add('active');
        slide.innerHTML = `<img src="${product.image_url}" alt="${product.name}" /><p>${product.name}</p>`;
        container.appendChild(slide);
    });
    slides = document.querySelectorAll('.slide');
}

function showSlide(index) {
    slides.forEach((s, i) => s.classList.toggle('active', i === index));
}

/* ========== PRODUCTS ========== */

async function fetchAllProducts() {
    const response = await fetch(`${API_BASE}/search?q=`);
    const products = await response.json();
    renderProducts(products);
}

function renderProducts(products) {
    const grid = document.getElementById('products-grid');
    grid.innerHTML = "";

    products.forEach(product => {
        const card = document.createElement("div");
        card.className = "product-card";

        const imageContainer = document.createElement("div");
        imageContainer.className = "image-container";

        const img = document.createElement("img");
        img.src = product.image_url || "images/placeholder.jpg";
        img.alt = product.name;
        img.addEventListener("click", () => likeProduct(product._id));

        const overlay_text = document.createElement("div");
        overlay_text.className = "overlay-text";
        overlay_text.textContent = product.description;

        imageContainer.appendChild(img);
        imageContainer.appendChild(overlay_text);

        card.appendChild(imageContainer)

        const name = document.createElement("div");
        name.className = "name";
        name.textContent = product.name;

        const likes = document.createElement("div");
        likes.className = "likes";
        likes.textContent = `❤️ ${product.likes}`;

        card.appendChild(name);
        card.appendChild(likes);
        grid.appendChild(card);
  });
}

async function likeProduct(productID){
    try{
        await fetch(`${API_BASE}/like`,
            {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({ product_id: productID })
        });
        await fetchAllProducts();
    }
    catch(error){
        console.log("Error liking product:", error);
    }
}

/* ========== SEARCH BAR ========== */

if (searchBar) {
    document.getElementById('searchBar')
        .addEventListener('input', async (e) => {
            const query = e.target.value.trim();
            if (query.length === 0) {
                await fetchAllProducts();
                return;
            }
            const response = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`);
            const results = await response.json();
            renderProducts(results);
        });
    document.getElementById('searchBar')
        .addEventListener('submit', (e) => {
            e.preventDefault();
        });
}

/* ========== BUTTONS ========== */

if (homeButton) {
    homeButton.addEventListener('click', () => {
         window.location.href = 'homepage.html';
    });
    fetchAllProducts();
}

if (productsButton) {
    productsButton.addEventListener('click', () => {
        window.location.href = 'products.html';
    });
}
if (aboutButton) {
    aboutButton.addEventListener('click', () => {
         alert('2025 Project NIS-07-01:' +
             '\nBill Zervos - AEM: 4442' +
             '\nAndreas Darsaklis - AEM: 4403' +
             '\nPavlos Gotovas - AEM: 4519\n');
    });
}