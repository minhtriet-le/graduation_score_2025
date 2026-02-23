/* ════════════════════════════════════════════════════════════
   MINIMALIST THEME - ENHANCED INTERACTIONS
   ════════════════════════════════════════════════════════════ */

(function() {
  'use strict';

  // ──────────────────────────────────────────────────────────
  // INITIALIZATION
  // ──────────────────────────────────────────────────────────

  document.addEventListener('DOMContentLoaded', function() {
    initNavbar();
    initSidebar();
    initScrollProgress();
    initTabs();
    initBackToTop();
    initLightbox();
    initCommentBoxes();
    initAnimations();
    setupResponsiveness();
  });

  // ──────────────────────────────────────────────────────────
  // NAVBAR & HAMBURGER MENU
  // ──────────────────────────────────────────────────────────

  function initNavbar() {
    const hamburger = document.getElementById('hamburger');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = navMenu.querySelectorAll('a');

    // Hamburger menu toggle
    if (hamburger) {
      hamburger.addEventListener('click', () => {
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
        hamburger.classList.toggle('active');
      });
    }

    // Close sidebar on overlay click
    if (overlay) {
      overlay.addEventListener('click', () => {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
        hamburger.classList.remove('active');
      });
    }

    // Update active nav link on scroll
    window.addEventListener('scroll', () => {
      updateActiveNavLink();
    });

    // Close sidebar when clicking a link
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
        if (hamburger) hamburger.classList.remove('active');
      });
    });
  }

  function updateActiveNavLink() {
    const navLinks = document.querySelectorAll('#nav-menu a');
    let current = '';

    navLinks.forEach(link => {
      const section = document.querySelector(link.getAttribute('href'));
      if (section && section.offsetTop <= window.scrollY + 100) {
        current = link;
      }
    });

    navLinks.forEach(link => link.classList.remove('active'));
    if (current) current.classList.add('active');
  }

  // ──────────────────────────────────────────────────────────
  // SIDEBAR
  // ──────────────────────────────────────────────────────────

  function initSidebar() {
    const sidebarGroups = document.querySelectorAll('.sidebar-group');
    const sidebarSearch = document.getElementById('sidebar-search');

    // Open first group by default
    if (sidebarGroups[0]) {
      sidebarGroups[0].classList.add('open');
    }

    // Group toggle
    sidebarGroups.forEach(group => {
      const label = group.querySelector('.sidebar-group-label');
      label.addEventListener('click', () => {
        group.classList.toggle('open');
      });
    });

    // Sidebar search
    if (sidebarSearch) {
      sidebarSearch.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const links = document.querySelectorAll('.sidebar-link');

        links.forEach(link => {
          const text = link.textContent.toLowerCase();
          link.style.display = text.includes(query) ? 'flex' : 'none';
        });
      });
    }

    // Sidebar link active state
    const sidebarLinks = document.querySelectorAll('.sidebar-link');
    sidebarLinks.forEach(link => {
      link.addEventListener('click', function() {
        sidebarLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
      });
    });

    // Update active sidebar link on scroll
    window.addEventListener('scroll', () => {
      updateActiveSidebarLink();
    });
  }

  function updateActiveSidebarLink() {
    const sidebarLinks = document.querySelectorAll('.sidebar-link');
    let current = null;

    sidebarLinks.forEach(link => {
      const target = link.getAttribute('data-target');
      const section = document.getElementById(target);
      if (section && section.offsetTop <= window.scrollY + 100) {
        current = link;
      }
    });

    sidebarLinks.forEach(link => link.classList.remove('active'));
    if (current) current.classList.add('active');
  }

  // ──────────────────────────────────────────────────────────
  // SCROLL PROGRESS BAR
  // ──────────────────────────────────────────────────────────

  function initScrollProgress() {
    const progressBar = document.getElementById('read-progress');
    
    window.addEventListener('scroll', () => {
      const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrolled = (window.scrollY / windowHeight) * 100;
      if (progressBar) {
        progressBar.style.width = scrolled + '%';
      }
    });
  }

  // ──────────────────────────────────────────────────────────
  // TABS
  // ──────────────────────────────────────────────────────────

  function initTabs() {
    const tabBars = document.querySelectorAll('.tab-bar');

    tabBars.forEach(bar => {
      const target = bar.getAttribute('data-target');
      const container = document.getElementById(target);
      
      if (!container) return;

      const buttons = bar.querySelectorAll('.tab-btn');
      const panes = container.querySelectorAll('.tab-pane');

      // Set first tab as active
      if (buttons.length > 0) {
        buttons[0].classList.add('active');
      }
      if (panes.length > 0) {
        panes[0].classList.add('active');
      }

      // Tab click handler
      buttons.forEach((btn, index) => {
        btn.addEventListener('click', () => {
          // Remove active from all
          buttons.forEach(b => b.classList.remove('active'));
          panes.forEach(p => p.classList.remove('active'));

          // Add active to clicked
          btn.classList.add('active');
          if (panes[index]) {
            panes[index].classList.add('active');
          }
        });
      });
    });
  }

  // ──────────────────────────────────────────────────────────
  // BACK TO TOP BUTTON
  // ──────────────────────────────────────────────────────────

  function initBackToTop() {
    const backToTop = document.getElementById('back-to-top');

    if (!backToTop) return;

    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTop.classList.add('show');
      } else {
        backToTop.classList.remove('show');
      }
    });

    backToTop.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // ──────────────────────────────────────────────────────────
  // LIGHTBOX FOR IMAGES
  // ──────────────────────────────────────────────────────────

  function initLightbox() {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxClose = document.getElementById('lightbox-close');
    
    if (!lightbox) return;

    // Click on images in chart cards
    const chartImages = document.querySelectorAll('.chart-card-body img');
    chartImages.forEach(img => {
      img.style.cursor = 'pointer';
      img.addEventListener('click', function() {
        lightboxImg.src = this.src;
        lightbox.classList.add('active');
      });
    });

    // Close lightbox
    if (lightboxClose) {
      lightboxClose.addEventListener('click', () => {
        lightbox.classList.remove('active');
      });
    }

    // Close on backdrop click
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) {
        lightbox.classList.remove('active');
      }
    });

    // Close on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lightbox.classList.contains('active')) {
        lightbox.classList.remove('active');
      }
    });
  }

  // ──────────────────────────────────────────────────────────
  // COMMENT BOXES (EDITABLE)
  // ──────────────────────────────────────────────────────────

  function initCommentBoxes() {
    const commentBoxes = document.querySelectorAll('.comment-box');

    commentBoxes.forEach(box => {
      const placeholder = box.getAttribute('data-placeholder') || '';
      
      // Show placeholder text initially
      if (!box.textContent.trim()) {
        box.textContent = placeholder;
        box.style.opacity = '0.6';
      }

      box.addEventListener('focus', function() {
        if (this.textContent === placeholder) {
          this.textContent = '';
          this.style.opacity = '1';
        }
      });

      box.addEventListener('blur', function() {
        if (!this.textContent.trim()) {
          this.textContent = placeholder;
          this.style.opacity = '0.6';
        }
      });
    });
  }

  // ──────────────────────────────────────────────────────────
  // ANIMATIONS
  // ──────────────────────────────────────────────────────────

  function initAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('slide-in');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    // Observe chart cards
    document.querySelectorAll('.chart-card, .panel').forEach(el => {
      observer.observe(el);
    });

    // Animate stat cards on view
    const statCards = document.querySelectorAll('.stat-card');
    const statObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.animation = 'slideIn 0.6s ease-out forwards';
          statObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    statCards.forEach((card, index) => {
      card.style.animationDelay = `${index * 0.1}s`;
      statObserver.observe(card);
    });
  }

  // ──────────────────────────────────────────────────────────
  // RESPONSIVENESS SETUP
  // ──────────────────────────────────────────────────────────

  function setupResponsiveness() {
    // Handle window resize
    let resizeTimer;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        const sidebar = document.getElementById('sidebar');
        const hamburger = document.getElementById('hamburger');
        const overlay = document.getElementById('sidebar-overlay');

        // Close sidebar on larger screens
        if (window.innerWidth > 768) {
          sidebar.classList.remove('active');
          overlay.classList.remove('active');
          if (hamburger) hamburger.classList.remove('active');
        }
      }, 250);
    });
  }

  // ──────────────────────────────────────────────────────────
  // UTILITY FUNCTIONS
  // ──────────────────────────────────────────────────────────

  // Smooth scroll to section
  window.scrollToSection = function(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  // Copy to clipboard
  window.copyToClipboard = function(text) {
    navigator.clipboard.writeText(text).then(() => {
      console.log('Copied to clipboard');
    });
  };

})();
