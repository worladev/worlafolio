const wrapper = document.querySelector('.testimonial-wrapper');
const items = document.querySelectorAll('.testimonial-item');
let index = 0;

function cloneItems(){
    items.forEach(item => {
        const clone = item.cloneNode(true);
        wrapper.appendChild(clone);
    });
}


function slideProjects(){
    index++;
    if (index >= items.length) {
        index = 0;
    }
    const offset = -index * (items[0].clientWidth + 20);
    wrapper.style.transform = 'translateX(${offset}px';
}

function initSlider(){
    cloneItems();
    setInterval(slideProjects, 2000);
}

initSlider();
