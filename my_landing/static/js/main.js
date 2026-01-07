// Сюда вставим ваш JS

tailwind.config = {
    theme: {
        container: {
            center: true,
            padding: '1rem',
            screens: {
                sm: '640px',
                md: '768px',
                lg: '1024px',
                xl: '1280px',
                '2xl': '1280px', // Limit max width to 1280px on larger screens
            },
        },
        extend: {
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
            },
            colors: {
                brand: {
                    50: '#F0F9FF',
                    100: '#E0F2FE',
                    500: '#0EA5E9',
                    600: '#0284C7',
                    900: '#0C4A6E',
                },
                slate: {
                    850: '#151F32', // Глубокий темный для футера
                }
            },
            boxShadow: {
                'widget': '0 4px 20px -2px rgba(0, 0, 0, 0.05), 0 0 0 1px rgba(0,0,0,0.03)',
                'floating': '0 10px 40px -10px rgba(0, 0, 0, 0.15)',
            },
            borderRadius: {
                '4xl': '2rem',
            }
        }
    }
}

function scrollPortfolio(direction) {
    const container = document.getElementById('portfolio-container');
    const scrollAmount = container.clientWidth * 0.8; // Scroll 80% of width
    const maxScroll = container.scrollWidth - container.clientWidth;
    const threshold = 10; // Tolerance for scroll position

    if (direction === 'left') {
        if (container.scrollLeft <= threshold) {
            // If at the start, loop to the end
            container.scrollTo({ left: maxScroll, behavior: 'smooth' });
        } else {
            container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        }
    } else {
        if (container.scrollLeft >= maxScroll - threshold) {
            // If at the end, loop to the start
            container.scrollTo({ left: 0, behavior: 'smooth' });
        } else {
            container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.msg-enter').forEach(el => observer.observe(el));
});