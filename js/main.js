/* =============================================
   ST GREGORIOS - JavaScript Interactions
   =============================================
   - Sticky Navbar with scroll effect
   - Mobile menu
   - Hero image slider
   - Stat counter animation
   - Scroll-reveal animations
   - Testimonial carousel
   - Back-to-top button
   - Form validation
   - Gallery lightbox
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  // ===== Sticky Navbar =====
  const navbar = document.querySelector('.navbar-main');
  const topBar = document.querySelector('.top-bar');

  function handleScroll() {
    const scrollY = window.scrollY;
    if (scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll(); // Initial check

  // ===== Mobile Menu =====
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const mobileNav = document.querySelector('.mobile-nav');
  const mobileOverlay = document.querySelector('.mobile-overlay');
  const mobileLinks = document.querySelectorAll('.mobile-nav a');

  function toggleMobileMenu() {
    mobileMenuBtn.classList.toggle('active');
    mobileNav.classList.toggle('open');
    mobileOverlay.classList.toggle('active');
    document.body.style.overflow = mobileNav.classList.contains('open') ? 'hidden' : '';
  }

  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', toggleMobileMenu);
  }

  if (mobileOverlay) {
    mobileOverlay.addEventListener('click', toggleMobileMenu);
  }

  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (mobileNav.classList.contains('open')) {
        toggleMobileMenu();
      }
    });
  });

  // Mobile dropdown toggles
  const mobileDropdownToggles = document.querySelectorAll('.mobile-dropdown-toggle');
  mobileDropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const dropdown = toggle.nextElementSibling;
      const icon = toggle.querySelector('.dropdown-arrow');
      
      dropdown.classList.toggle('open');
      
      if (dropdown.classList.contains('open')) {
        dropdown.style.maxHeight = dropdown.scrollHeight + 'px';
      } else {
        dropdown.style.maxHeight = '0px';
      }

      if (icon) {
        icon.style.transform = dropdown.classList.contains('open') ? 'rotate(180deg)' : 'rotate(0)';
      }
    });
  });

  // ===== Hero Slider =====
  const heroSlides = document.querySelectorAll('.hero-slide');
  let currentSlide = 0;

  function nextHeroSlide() {
    if (heroSlides.length <= 1) return;
    heroSlides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % heroSlides.length;
    heroSlides[currentSlide].classList.add('active');
  }

  if (heroSlides.length > 0) {
    heroSlides[0].classList.add('active');
    setInterval(nextHeroSlide, 5000);
  }

  // ===== Scroll Reveal =====
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .stagger-children');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // ===== Stat Counter Animation =====
  const statNumbers = document.querySelectorAll('.stat-number');

  function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target'));
    const suffix = element.getAttribute('data-suffix') || '';
    const prefix = element.getAttribute('data-prefix') || '';
    const duration = 2000;
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;

    function updateCounter() {
      current += increment;
      if (current >= target) {
        element.textContent = prefix + target + suffix;
        return;
      }
      element.textContent = prefix + Math.floor(current) + suffix;
      requestAnimationFrame(updateCounter);
    }

    updateCounter();
  }

  const statObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        statObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  statNumbers.forEach(el => statObserver.observe(el));

  // ===== Testimonial Carousel =====
  const testimonialTrack = document.querySelector('.testimonial-track');
  const testimonialSlides = document.querySelectorAll('.testimonial-slide');
  const testimonialDots = document.querySelectorAll('.carousel-dot');
  let currentTestimonial = 0;
  let testimonialInterval;

  function goToTestimonial(index) {
    if (!testimonialTrack || testimonialSlides.length === 0) return;
    currentTestimonial = index;
    testimonialTrack.style.transform = `translateX(-${currentTestimonial * 100}%)`;
    
    testimonialDots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentTestimonial);
    });
  }

  function nextTestimonial() {
    const next = (currentTestimonial + 1) % testimonialSlides.length;
    goToTestimonial(next);
  }

  testimonialDots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      goToTestimonial(i);
      clearInterval(testimonialInterval);
      testimonialInterval = setInterval(nextTestimonial, 6000);
    });
  });

  if (testimonialSlides.length > 0) {
    testimonialInterval = setInterval(nextTestimonial, 6000);
  }

  // Touch support for testimonial carousel
  let touchStartX = 0;
  let touchEndX = 0;

  if (testimonialTrack) {
    testimonialTrack.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    testimonialTrack.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      const diff = touchStartX - touchEndX;
      if (Math.abs(diff) > 50) {
        if (diff > 0) {
          // Swipe left — next
          goToTestimonial((currentTestimonial + 1) % testimonialSlides.length);
        } else {
          // Swipe right — prev
          goToTestimonial((currentTestimonial - 1 + testimonialSlides.length) % testimonialSlides.length);
        }
        clearInterval(testimonialInterval);
        testimonialInterval = setInterval(nextTestimonial, 6000);
      }
    }, { passive: true });
  }

  // ===== Back to Top Button =====
  const backToTop = document.querySelector('.back-to-top');

  if (backToTop) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 600) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    }, { passive: true });

    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ===== Gallery Lightbox =====
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lightbox = document.querySelector('.lightbox');
  const lightboxImg = document.querySelector('.lightbox-img');
  const lightboxClose = document.querySelector('.lightbox-close');

  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      if (img && lightbox && lightboxImg) {
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  if (lightboxClose) {
    lightboxClose.addEventListener('click', closeLightbox);
  }

  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lightbox.classList.contains('active')) {
        closeLightbox();
      }
    });
  }

  function closeLightbox() {
    if (lightbox) {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  // ===== Form Handling =====
  const contactForm = document.querySelector('#contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Basic validation
      const inputs = contactForm.querySelectorAll('[required]');
      let isValid = true;
      
      inputs.forEach(input => {
        if (!input.value.trim()) {
          isValid = false;
          input.style.borderColor = '#EF4444';
          input.addEventListener('input', () => {
            input.style.borderColor = '';
          }, { once: true });
        }
      });

      const emailInput = contactForm.querySelector('[type="email"]');
      if (emailInput && emailInput.value && !isValidEmail(emailInput.value)) {
        isValid = false;
        emailInput.style.borderColor = '#EF4444';
      }

      if (isValid) {
        // Show success message
        const btn = contactForm.querySelector('button[type="submit"]');
        const originalText = btn.innerHTML;
        btn.innerHTML = '✓ Message Sent!';
        btn.style.background = '#10B981';
        btn.disabled = true;
        
        setTimeout(() => {
          btn.innerHTML = originalText;
          btn.style.background = '';
          btn.disabled = false;
          contactForm.reset();
        }, 3000);
      }
    });
  }

  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  // ===== Smooth scroll for anchor links =====
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        const navHeight = navbar ? navbar.offsetHeight : 0;
        const targetPosition = targetEl.getBoundingClientRect().top + window.scrollY - navHeight - 20;
        window.scrollTo({ top: targetPosition, behavior: 'smooth' });
      }
    });
  });

  // ===== Active nav link based on scroll position =====
  const sections = document.querySelectorAll('section[id]');
  
  function updateActiveNav() {
    const scrollY = window.scrollY + 200;
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');
      
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        document.querySelectorAll('.nav-link-item').forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${sectionId}` || 
              link.getAttribute('href') === `index.html#${sectionId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', updateActiveNav, { passive: true });

  // ===== Navbar dropdown close on outside click =====
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-dropdown')) {
      document.querySelectorAll('.dropdown-menu-custom').forEach(menu => {
        // Dropdowns are controlled via CSS :hover, so no JS needed for desktop
      });
    }
  });

  // ===== Lazy load images =====
  if ('IntersectionObserver' in window) {
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          imageObserver.unobserve(img);
        }
      });
    }, {
      rootMargin: '50px 0px'
    });

    lazyImages.forEach(img => imageObserver.observe(img));
  }

});
