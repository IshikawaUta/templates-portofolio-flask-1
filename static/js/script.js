document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelector('.typed-text')) {
        var typed = new Typed('.typed-text', {
            strings: document.querySelector('.typed-text').dataset.typedItems.split(', '),
            loop: true,
            typeSpeed: 70,
            backSpeed: 30,
            backDelay: 1500,
        });
    }

    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });

            const navbarCollapse = document.getElementById('navbarNav');
            if (navbarCollapse.classList.contains('show')) {
                new bootstrap.Collapse(navbarCollapse, {
                    toggle: false
                }).hide();
            }
        });
    });

    const animateElements = document.querySelectorAll('.animate__animated');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate__fadeIn', 'animate__fadeInLeft', 'animate__fadeInRight', 'animate__fadeInUp', 'animate__fadeInDown');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    animateElements.forEach(element => {
        observer.observe(element);
    });
});
document.addEventListener('DOMContentLoaded', function() {
            const alerts = document.querySelectorAll('#notification-container .alert');

            alerts.forEach(alert => {
                alert.classList.remove('show');
                alert.classList.add('fade-in-right');

                setTimeout(() => {
                    alert.classList.remove('fade-in-right');
                    alert.classList.add('fade-out-right');

                    alert.addEventListener('animationend', () => {
                        alert.remove();
                    }, { once: true });
                }, 3000);
            });
        });