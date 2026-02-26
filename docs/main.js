// ---- Rain ----
(function initRain() {
  const canvas = document.getElementById('rain');
  const ctx = canvas.getContext('2d');
  let drops = [];
  const COUNT = 120;
  const WIND = 1.5;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  function createDrop() {
    return {
      x: Math.random() * canvas.width * 1.2,
      y: Math.random() * -canvas.height,
      len: 12 + Math.random() * 18,
      speed: 4 + Math.random() * 6,
      opacity: 0.03 + Math.random() * 0.07,
      width: 0.5 + Math.random() * 0.5
    };
  }

  function init() {
    resize();
    drops = [];
    for (let i = 0; i < COUNT; i++) {
      const d = createDrop();
      d.y = Math.random() * canvas.height;
      drops.push(d);
    }
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (const d of drops) {
      ctx.beginPath();
      ctx.moveTo(d.x, d.y);
      ctx.lineTo(d.x + WIND * 2, d.y + d.len);
      ctx.strokeStyle = `rgba(180, 175, 165, ${d.opacity})`;
      ctx.lineWidth = d.width;
      ctx.stroke();

      d.y += d.speed;
      d.x += WIND;

      if (d.y > canvas.height + d.len) {
        Object.assign(d, createDrop());
      }
    }
    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', resize);
  init();
  draw();
})();

// ---- Scroll Reveals ----
(function initReveals() {
  const targets = document.querySelectorAll('.step, .passage, .epigraph, .coda, .lineage');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
  });

  targets.forEach(t => observer.observe(t));

  // Reveal epigraph immediately on load
  setTimeout(() => {
    document.querySelector('.epigraph')?.classList.add('revealed');
  }, 500);
})();
