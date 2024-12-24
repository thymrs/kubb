function adjustHeight() {
    document.querySelector('.section').style.height = `${window.innerHeight}px`;
    // Repeat for other elements as necessary
}

window.addEventListener('resize', adjustHeight);
adjustHeight(); // Initial adjustment
