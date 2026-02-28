/**
 * loader.js – Inject HTML section partials into page placeholders.
 *
 * Strategy:
 *  1. If window.__SECTIONS is defined (sections-data.js loaded), inject directly — works with file://
 *  2. Otherwise fall back to fetch() — requires a web server
 */
(function () {
  'use strict';

  var SECTIONS = [
    's1-overview',
    's2-pipeline',
    's3-theory',
    's4-subjects',
    's5-foreign',
    's6-cluster',
    's7-hypothesis',
    's8-corr',
  ];

  function injectSection(name, html) {
    var el = document.getElementById('section-' + name);
    if (el) el.outerHTML = html;
  }

  function injectAll(map) {
    SECTIONS.forEach(function (name) {
      if (map[name]) injectSection(name, map[name]);
    });
  }

  function reinitApp() {
    if (typeof window.__appInit === 'function') window.__appInit();
  }

  function loadViaInline() {
    injectAll(window.__SECTIONS);
    reinitApp();
  }

  function loadViaFetch() {
    var promises = SECTIONS.map(function (name) {
      return fetch('sections/' + name + '.html')
        .then(function (res) {
          if (!res.ok) throw new Error('HTTP ' + res.status + ' for ' + name);
          return res.text();
        })
        .then(function (html) { return { name: name, html: html }; });
    });

    Promise.all(promises)
      .then(function (results) {
        var map = {};
        results.forEach(function (r) { map[r.name] = r.html; });
        injectAll(map);
        reinitApp();
      })
      .catch(function (err) {
        console.error('[loader] fetch failed:', err);
      });
  }

  document.addEventListener('DOMContentLoaded', function () {
    if (window.__SECTIONS) {
      loadViaInline();
    } else {
      loadViaFetch();
    }
  });

})();
