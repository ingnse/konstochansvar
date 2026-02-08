/**
 * Main JavaScript for Konst och Ansvar website
 * Handles mobile menu, smooth scrolling, and other interactive features
 */

(function() {
    'use strict';

    // Mobile Menu Toggle
    const initMobileMenu = () => {
        const menuToggle = document.querySelector('.mobile-menu-toggle');
        const navigation = document.querySelector('.main-navigation');
        
        if (!menuToggle || !navigation) return;

        menuToggle.addEventListener('click', () => {
            const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
            menuToggle.setAttribute('aria-expanded', !isExpanded);
            navigation.classList.toggle('mobile-menu-open');
            document.body.classList.toggle('menu-open');
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navigation.contains(e.target) && !menuToggle.contains(e.target)) {
                menuToggle.setAttribute('aria-expanded', 'false');
                navigation.classList.remove('mobile-menu-open');
                document.body.classList.remove('menu-open');
            }
        });
    };

    // Smooth scroll for anchor links
    const initSmoothScroll = () => {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
                if (href === '#') return;
                
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    };

    // Lazy load images
    const initLazyLoading = () => {
        if ('loading' in HTMLImageElement.prototype) {
            // Native lazy loading supported
            const images = document.querySelectorAll('img[loading="lazy"]');
            images.forEach(img => {
                img.addEventListener('load', function() {
                    this.classList.add('loaded');
                });
            });
        } else {
            // Fallback for browsers without native lazy loading
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/lozad/dist/lozad.min.js';
            script.onload = () => {
                const observer = lozad('.lozad', {
                    loaded: function(el) {
                        el.classList.add('loaded');
                    }
                });
                observer.observe();
            };
            document.body.appendChild(script);
        }
    };

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            initMobileMenu();
            initSmoothScroll();
            initLazyLoading();
        });
    } else {
        initMobileMenu();
        initSmoothScroll();
        initLazyLoading();
    }
})();

