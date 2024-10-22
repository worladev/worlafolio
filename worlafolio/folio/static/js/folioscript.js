const projectSliders = document.querySelectorAll(".project-slider")

if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    addAnimation();
}

function addAnimation() {
    projectSliders.forEach((slider) => {
        slider.setAttribute("data-animated", true);

        const projectSliderInner = slider.querySelector('.project-slider-inner');
        const sliderContent = Array.from(projectSliderInner.children);

        sliderContent.forEach(item => {
            const duplicatedItem = item.cloneNode(true);
            duplicatedItem.setAttribute('aria-hidden', true);
            projectSliderInner.appendChild(duplicatedItem);
        });
    });
}
