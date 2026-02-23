/**
 * app.js  –  Main application logic
 * Graduation Score Analysis 2025
 */
(function () {
  'use strict';

  /* ============================================================
     1. DOM READY
     ============================================================ */
  document.addEventListener('DOMContentLoaded', init);

  function init() {
    initSidebar();
    initTabs();
    initLightbox();
    initScrollSpy();
    initReadProgress();
    initBackToTop();
    initSidebarSearch();
    initHamburger();
    initCommentPersist();
  }

  /* ============================================================
     2. SIDEBAR – collapsible groups
     ============================================================ */
  function initSidebar() {
    document.querySelectorAll('.sidebar-group-label').forEach(label => {
      label.addEventListener('click', () => {
        const group = label.closest('.sidebar-group');
        group.classList.toggle('open');
      });
    });

    // Open group that contains the active link
    const activeLink = document.querySelector('.sidebar-link.active');
    if (activeLink) {
      const group = activeLink.closest('.sidebar-group');
      if (group) group.classList.add('open');
    } else {
      // Open first group by default
      const first = document.querySelector('.sidebar-group');
      if (first) first.classList.add('open');
    }
  }

  /* ============================================================
     3. TABS
     ============================================================ */
  function initTabs() {
    document.querySelectorAll('.tab-bar').forEach(bar => {
      const buttons = bar.querySelectorAll('.tab-btn');
      const target  = bar.dataset.target;   // e.g. "tab-group-1"

      buttons.forEach(btn => {
        btn.addEventListener('click', () => {
          const paneId = btn.dataset.pane;

          // Update buttons
          buttons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');

          // Update panes
          const container = target
            ? document.getElementById(target)
            : bar.closest('.section') || document;

          container.querySelectorAll('.tab-pane').forEach(p => {
            p.classList.toggle('active', p.id === paneId);
          });
        });
      });

      // Activate first tab by default
      if (buttons.length) buttons[0].click();
    });
  }

  /* ============================================================
     4. LIGHTBOX
     ============================================================ */
  function initLightbox() {
    const overlay = document.getElementById('lightbox');
    const lbImg   = document.getElementById('lightbox-img');
    const lbClose = document.getElementById('lightbox-close');

    if (!overlay || !lbImg) return;

    // Attach click to all chart images
    document.querySelectorAll('.chart-card-body img, .panel-img-wrap img').forEach(img => {
      img.addEventListener('click', () => {
        lbImg.src = img.src;
        lbImg.alt = img.alt;
        overlay.classList.add('open');
        document.body.style.overflow = 'hidden';
      });
    });

    function closeLightbox() {
      overlay.classList.remove('open');
      document.body.style.overflow = '';
    }

    overlay.addEventListener('click', e => {
      if (e.target === overlay) closeLightbox();
    });

    if (lbClose) lbClose.addEventListener('click', closeLightbox);

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeLightbox();
    });
  }

  /* ============================================================
     5. SCROLL SPY – highlight sidebar link of current section
     ============================================================ */
  function initScrollSpy() {
    const anchors = Array.from(document.querySelectorAll('.section-anchor[id]'));
    const links   = Array.from(document.querySelectorAll('.sidebar-link[data-target]'));
    if (!anchors.length || !links.length) return;

    const OFFSET = 100;

    function getActive() {
      const scrollY = window.scrollY + OFFSET;
      let active = anchors[0];

      for (const anchor of anchors) {
        if (anchor.getBoundingClientRect().top + window.scrollY <= scrollY) {
          active = anchor;
        }
      }
      return active;
    }

    let lastId = '';

    function update() {
      const current = getActive();
      if (!current || current.id === lastId) return;
      lastId = current.id;

      links.forEach(link => {
        const isActive = link.dataset.target === current.id;
        link.classList.toggle('active', isActive);
        if (isActive) {
          const group = link.closest('.sidebar-group');
          if (group && !group.classList.contains('open')) {
            group.classList.add('open');
          }
          // Smooth scroll sidebar item into view
          link.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        }
      });
    }

    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  /* ============================================================
     6. READ PROGRESS BAR
     ============================================================ */
  function initReadProgress() {
    const bar = document.getElementById('read-progress');
    if (!bar) return;

    function update() {
      const scrollTop    = document.documentElement.scrollTop;
      const scrollHeight = document.documentElement.scrollHeight;
      const clientHeight = document.documentElement.clientHeight;
      const pct = scrollTop / (scrollHeight - clientHeight) * 100;
      bar.style.width = Math.min(pct, 100) + '%';
    }

    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  /* ============================================================
     7. BACK TO TOP
     ============================================================ */
  function initBackToTop() {
    const btn = document.getElementById('back-to-top');
    if (!btn) return;

    window.addEventListener('scroll', () => {
      btn.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });

    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ============================================================
     8. SIDEBAR SEARCH
     ============================================================ */
  function initSidebarSearch() {
    const input = document.getElementById('sidebar-search');
    if (!input) return;

    const links = Array.from(document.querySelectorAll('.sidebar-link'));

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();

      links.forEach(link => {
        const text = link.textContent.toLowerCase();
        link.classList.toggle('hidden', q.length > 0 && !text.includes(q));
      });

      // Open all groups when searching
      if (q.length > 0) {
        document.querySelectorAll('.sidebar-group').forEach(g => g.classList.add('open'));
      }
    });
  }

  /* ============================================================
     9. HAMBURGER (mobile sidebar)
     ============================================================ */
  function initHamburger() {
    const btn     = document.getElementById('hamburger');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');

    if (!btn || !sidebar) return;

    function open() {
      sidebar.classList.add('open');
      if (overlay) overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function close() {
      sidebar.classList.remove('open');
      if (overlay) overlay.classList.remove('open');
      document.body.style.overflow = '';
    }

    btn.addEventListener('click', () => {
      sidebar.classList.contains('open') ? close() : open();
    });

    if (overlay) overlay.addEventListener('click', close);

    // Close on nav link click (mobile)
    sidebar.querySelectorAll('.sidebar-link').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 768) close();
      });
    });
  }

  /* ============================================================
     10. PERSIST COMMENTS IN localStorage
     ============================================================ */
  function initCommentPersist() {
    const boxes = document.querySelectorAll('.comment-box.editable[data-key]');

    boxes.forEach(box => {
      const key = 'comment_' + box.dataset.key;

      // Restore saved content
      const saved = localStorage.getItem(key);
      if (saved) box.textContent = saved;

      // Save on input
      box.addEventListener('input', () => {
        localStorage.setItem(key, box.textContent);
      });
    });
  }

})();
