const btnOpen = document.getElementById('btn-open')


btnOpen.addEventListener('click', () => {
    let menu = document.getElementById('menu')
    if (btnOpen.className == 'icon i-close') {
        menu.style.display = 'none'
        btnOpen.className = 'icon i-open'
    } else {
        menu.style.display = 'flex'
        btnOpen.className = 'icon i-close'
    }
})