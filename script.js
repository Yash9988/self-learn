document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.filter-buttons button');
    const projectCards = document.querySelectorAll('.project-card');
    const floatBtn = document.querySelector('.floating-button');

    // Attach filter-button handlers
    buttons.forEach(btn =>
        btn.addEventListener('click', () =>
            filterProjects(btn.dataset.category, btn)
        )
    );

    // Filter & toggle display
    function filterProjects(category, clickedBtn) {
        buttons.forEach(b => b.classList.remove('selected'));
        clickedBtn.classList.add('selected');

        projectCards.forEach(card => {
            const tags = card.dataset.tags
                .split(',')
                .map(t => t.trim().toLowerCase());

            // show or hide
            card.style.display = (category === 'all' || tags.includes(category))
                ? 'block'
                : 'none';
        });
    }

    // Floating back-to-top
    floatBtn.addEventListener('click', () =>
        window.scrollTo({ top: 0, behavior: 'smooth' })
    );
    window.addEventListener('scroll', () =>
        floatBtn.classList.toggle('show', window.scrollY > 100)
    );

    // initial load
    filterProjects('all', document.querySelector('[data-category="all"]'));
});

function openInNewTab() {
    window.open("./assets/files/Resume.pdf", "_blank"); // Assuming report.pdf is in the same directory
}