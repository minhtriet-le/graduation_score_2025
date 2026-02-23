/**
 * charts.js  –  Chart interactions, stat counters, language bar chart
 * Graduation Score Analysis 2025
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initLangBars();
    initCounters();
    initChartTags();
  });

  /* ============================================================
     1. ANIMATED LANGUAGE BARS
     ============================================================ */
  function initLangBars() {
    const bars = document.querySelectorAll('.lang-bar-fill[data-pct]');
    if (!bars.length) return;

    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          el.style.width = el.dataset.pct + '%';
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.2 });

    bars.forEach(bar => {
      bar.style.width = '0%';
      observer.observe(bar);
    });
  }

  /* ============================================================
     2. ANIMATED STAT COUNTERS
     ============================================================ */
  function initCounters() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });

    counters.forEach(el => observer.observe(el));
  }

  function animateCounter(el) {
    const raw    = el.dataset.count.replace(/,/g, '');
    const target = parseFloat(raw);
    const isFloat = raw.includes('.');
    const decimals = isFloat ? (raw.split('.')[1] || '').length : 0;
    const suffix  = el.dataset.suffix || '';
    const duration = 900; // ms
    const start   = performance.now();

    function tick(now) {
      const elapsed = Math.min(now - start, duration);
      const eased   = 1 - Math.pow(1 - elapsed / duration, 3);
      const current = target * eased;

      if (isFloat) {
        el.textContent = current.toFixed(decimals) + suffix;
      } else {
        el.textContent = Math.round(current).toLocaleString('vi-VN') + suffix;
      }

      if (elapsed < duration) requestAnimationFrame(tick);
      else el.textContent = (isFloat ? target.toFixed(decimals) : target.toLocaleString('vi-VN')) + suffix;
    }

    requestAnimationFrame(tick);
  }

  /* ============================================================
     3. CHART ANNOTATION TAGS (auto-generate from stats)
     ============================================================ */
  function initChartTags() {
    // Tags defined inline via data-tags="..." attribute on .chart-card
    document.querySelectorAll('.chart-card[data-tags]').forEach(card => {
      const wrap = card.querySelector('.chart-annotations');
      if (!wrap) return;

      const tags = card.dataset.tags.split(',').map(t => t.trim()).filter(Boolean);
      tags.forEach(tag => {
        const [label, color] = tag.split(':');
        const span = document.createElement('span');
        span.className = `badge badge-${color || 'blue'}`;
        span.textContent = label;
        wrap.appendChild(span);
      });
    });
  }

})();
