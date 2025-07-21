const currentIndexMap = {};

function updateSlider(postId) {
    const slider = document.querySelector(`#slider-${postId} .slider-track`);
    const container = document.querySelector(`#slider-${postId}`);
    const images = document.querySelectorAll(`#slider-${postId} .slider-image`);
    const index = currentIndexMap[postId] || 0;
    const width = container.clientWidth;

    slider.style.transform = `translateX(-${index * width}px)`;
}

function prevSlide(postId) {
    const images = document.querySelectorAll(`#slider-${postId} .slider-image`);
    currentIndexMap[postId] = Math.max((currentIndexMap[postId] || 0) - 1, 0);
    updateSlider(postId);
}

function nextSlide(postId) {
    const images = document.querySelectorAll(`#slider-${postId} .slider-image`);
    currentIndexMap[postId] = Math.min((currentIndexMap[postId] || 0) + 1, images.length - 1);
    updateSlider(postId);
}

window.addEventListener('resize', () => {
    for (const postId in currentIndexMap) {
        updateSlider(postId);
    }
});