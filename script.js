/* ═══════════════════════════════════════════════════════════════
   1WIN FAN SITE — JAVASCRIPT
   ═══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ─── STICKY HEADER (always visible) ───
  const header = document.getElementById('siteHeader');

  // ─── MOBILE NAV TOGGLE ───
  const hamburger = document.getElementById('hamburger');
  const mainNav = document.getElementById('mainNav');

  if (hamburger && mainNav) {
    hamburger.addEventListener('click', function () {
      hamburger.classList.toggle('active');
      mainNav.classList.toggle('nav-open');
    });

    // Close on link click
    mainNav.querySelectorAll('.nav-link').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('active');
        mainNav.classList.remove('nav-open');
      });
    });
  }

  // ─── INTERSECTION OBSERVER — FADE IN ANIMATIONS ───
  const animElements = document.querySelectorAll('.anim-fade-up');

  if ('IntersectionObserver' in window) {
    const animObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          animObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    animElements.forEach(function (el) {
      animObserver.observe(el);
    });
  } else {
    // Fallback: show all
    animElements.forEach(function (el) {
      el.classList.add('visible');
    });
  }

  // ─── COUNTER ANIMATION ───
  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-target'), 10);
    if (isNaN(target)) return;

    const duration = 2000;
    const start = performance.now();
    const startVal = 0;

    function easeOutQuart(t) {
      return 1 - Math.pow(1 - t, 4);
    }

    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = easeOutQuart(progress);
      const current = Math.round(startVal + (target - startVal) * eased);
      el.textContent = current.toLocaleString();
      if (progress < 1) {
        requestAnimationFrame(update);
      }
    }

    requestAnimationFrame(update);
  }

  // Observe stat numbers
  const statNumbers = document.querySelectorAll('.stat-number[data-target]');
  if ('IntersectionObserver' in window && statNumbers.length > 0) {
    const counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    statNumbers.forEach(function (el) {
      counterObserver.observe(el);
    });
  }

  // ─── COPY PROMO CODE ───
  const copyBtn = document.getElementById('copyPromoBtn');
  const promoText = document.getElementById('promoCodeText');

  if (copyBtn && promoText) {
    copyBtn.addEventListener('click', function () {
      const text = promoText.textContent.trim();
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          showCopied();
        }).catch(function () {
          fallbackCopy(text);
        });
      } else {
        fallbackCopy(text);
      }
    });

    function fallbackCopy(text) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.left = '-9999px';
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand('copy');
        showCopied();
      } catch (e) { /* noop */ }
      document.body.removeChild(ta);
    }

    function showCopied() {
      var copyTextEl = copyBtn.querySelector('.copy-text');
      copyBtn.classList.add('copied');
      if (copyTextEl) copyTextEl.textContent = 'Copied!';
      setTimeout(function () {
        copyBtn.classList.remove('copied');
        if (copyTextEl) copyTextEl.textContent = 'Copy';
      }, 2000);
    }
  }

  // ─── FAQ ACCORDION ───
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(function (item) {
    var btn = item.querySelector('.faq-question');
    if (!btn) return;

    btn.addEventListener('click', function () {
      var isActive = item.classList.contains('active');

      // Close all
      faqItems.forEach(function (fi) {
        fi.classList.remove('active');
        var b = fi.querySelector('.faq-question');
        if (b) b.setAttribute('aria-expanded', 'false');
      });

      // Open clicked (if wasn't already open)
      if (!isActive) {
        item.classList.add('active');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // ─── HERO PARTICLES ───
  var canvas = document.getElementById('heroParticles');
  if (canvas) {
    var ctx = canvas.getContext('2d');
    var particles = [];
    var particleCount = 60;

    function resizeCanvas() {
      var hero = document.getElementById('hero');
      if (hero) {
        canvas.width = hero.offsetWidth;
        canvas.height = hero.offsetHeight;
      }
    }

    function createParticle() {
      return {
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 2 + 0.5,
        speedX: (Math.random() - 0.5) * 0.4,
        speedY: (Math.random() - 0.5) * 0.4,
        opacity: Math.random() * 0.5 + 0.1,
        color: Math.random() > 0.7 ? '#0075ff' : (Math.random() > 0.5 ? '#FFD700' : '#ffffff')
      };
    }

    function initParticles() {
      particles = [];
      for (var i = 0; i < particleCount; i++) {
        particles.push(createParticle());
      }
    }

    function drawParticles() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      particles.forEach(function (p) {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.globalAlpha = p.opacity;
        ctx.fill();

        p.x += p.speedX;
        p.y += p.speedY;

        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;
      });

      ctx.globalAlpha = 1;
      requestAnimationFrame(drawParticles);
    }

    resizeCanvas();
    initParticles();
    drawParticles();

    window.addEventListener('resize', function () {
      resizeCanvas();
    });
  }

  // ─── SMOOTH SCROLL FOR NAV LINKS ───
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        var offset = 80;
        var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

})();

/* ═══════════════════════════════════════════════════════════════
   MULTI-PAGE EXTENSIONS
   ═══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ─── DROPDOWN NAV TOGGLE ───
  var dropdownItems = document.querySelectorAll('.nav-item');
  var isMobile = function () { return window.innerWidth <= 768; };

  dropdownItems.forEach(function (item) {
    var link = item.querySelector('.nav-link');
    if (!link) return;

    // Desktop: hover
    item.addEventListener('mouseenter', function () {
      if (!isMobile()) item.classList.add('dropdown-open');
    });
    item.addEventListener('mouseleave', function () {
      if (!isMobile()) item.classList.remove('dropdown-open');
    });

    // Mobile: click
    link.addEventListener('click', function (e) {
      if (item.querySelector('.nav-dropdown') && isMobile()) {
        e.preventDefault();
        item.classList.toggle('dropdown-open');
      }
    });
  });

  // Close dropdowns on outside click
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-item')) {
      dropdownItems.forEach(function (item) {
        item.classList.remove('dropdown-open');
      });
    }
  });

  // ─── ACTIVE NAV LINK DETECTION ───
  var currentPage = window.location.pathname.split('/').pop() || 'index.html';
  var navLinks = document.querySelectorAll('.header-nav .nav-link');

  navLinks.forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href) return;
    var linkPage = href.split('/').pop().split('#')[0] || 'index.html';
    if (linkPage === currentPage) {
      link.classList.add('active');
    }
  });

  // Also check dropdown links
  var dropdownLinks = document.querySelectorAll('.nav-dropdown a');
  dropdownLinks.forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href) return;
    var linkPage = href.split('/').pop().split('#')[0] || 'index.html';
    if (linkPage === currentPage) {
      link.style.color = 'var(--white)';
      link.style.background = 'rgba(0,117,255,0.1)';
      // Also highlight parent
      var parentItem = link.closest('.nav-item');
      if (parentItem) {
        var parentLink = parentItem.querySelector('.nav-link');
        if (parentLink) parentLink.classList.add('active');
      }
    }
  });

  // ─── RE-INIT FAQ ACCORDION FOR SUBPAGES ───
  var subpageFaqItems = document.querySelectorAll('.faq-section .faq-item');
  subpageFaqItems.forEach(function (item) {
    var btn = item.querySelector('.faq-question');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var isActive = item.classList.contains('active');
      // Close all siblings
      var parent = item.parentElement;
      if (parent) {
        parent.querySelectorAll('.faq-item').forEach(function (fi) {
          fi.classList.remove('active');
          var b = fi.querySelector('.faq-question');
          if (b) b.setAttribute('aria-expanded', 'false');
        });
      }
      if (!isActive) {
        item.classList.add('active');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // ─── COPY BUTTONS ON SUBPAGES ───
  document.querySelectorAll('.copy-btn').forEach(function (btn) {
    if (btn.id === 'copyPromoBtn') return; // Already handled
    btn.addEventListener('click', function () {
      var codeEl = btn.closest('.promo-code-box, .cta-banner-row, .promo-box')
        ?.querySelector('.promo-code-text, .promo-code-inline');
      if (!codeEl) return;
      var text = codeEl.textContent.trim();
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          btn.classList.add('copied');
          var ct = btn.querySelector('.copy-text');
          if (ct) ct.textContent = 'Copied!';
          setTimeout(function () {
            btn.classList.remove('copied');
            if (ct) ct.textContent = 'Copy';
          }, 2000);
        });
      }
    });
  });

})();
