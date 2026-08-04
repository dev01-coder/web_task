/* ============================================
   OZAIR ILYAS - PORTFOLIO JAVASCRIPT
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {

    // === Theme Toggle (Dark/Light Mode) ===
    const themeToggle = document.getElementById('themeToggle');
    const html = document.documentElement;

    function setTheme(theme) {
        html.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const current = html.getAttribute('data-theme');
            setTheme(current === 'dark' ? 'light' : 'dark');
        });
    }

    // === Navbar Scroll Effect ===
    const nav = document.getElementById('mainNav');
    function handleNavScroll() {
        if (!nav) return;
        if (window.scrollY > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    }
    window.addEventListener('scroll', handleNavScroll);
    handleNavScroll();

    // === Active Nav Link ===
    const currentPath = window.location.pathname;
    document.querySelectorAll('.navbar-nav .nav-link').forEach(function (link) {
        var href = link.getAttribute('href');
        if (href === currentPath || href === currentPath.replace(/\/$/, '') || (currentPath === '/' && href === '/')) {
            link.classList.add('active');
        }
    });

    // === Close Mobile Nav on Link Click ===
    document.querySelectorAll('.navbar-nav .nav-link').forEach(function (link) {
        link.addEventListener('click', function () {
            var collapseEl = document.getElementById('navbarNav');
            if (collapseEl) {
                var bsCollapse = bootstrap.Collapse.getInstance(collapseEl);
                if (bsCollapse) bsCollapse.hide();
            }
        });
    });

    // === Close Mobile Nav on Close Button Click ===
    var navCloseBtn = document.getElementById('navCloseBtn');
    if (navCloseBtn) {
        navCloseBtn.addEventListener('click', function () {
            var collapseEl = document.getElementById('navbarNav');
            if (collapseEl) {
                var bsCollapse = bootstrap.Collapse.getInstance(collapseEl);
                if (bsCollapse) bsCollapse.hide();
            }
        });
    }

    // === Backdrop Click to Close Mobile Nav ===
    var navBackdrop = document.getElementById('navBackdrop');
    if (navBackdrop) {
        navBackdrop.addEventListener('click', function () {
            var collapseEl = document.getElementById('navbarNav');
            if (collapseEl) {
                var bsCollapse = bootstrap.Collapse.getInstance(collapseEl);
                if (bsCollapse) bsCollapse.hide();
            }
        });
    }

    // === Toggle backdrop + toggler active class on nav show/hide ===
    var navbarNav = document.getElementById('navbarNav');
    var navbarToggler = document.querySelector('.navbar-toggler');
    if (navbarNav) {
        navbarNav.addEventListener('show.bs.collapse', function () {
            if (navBackdrop) navBackdrop.classList.add('active');
            if (navbarToggler) navbarToggler.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
        navbarNav.addEventListener('hide.bs.collapse', function () {
            if (navBackdrop) navBackdrop.classList.remove('active');
            if (navbarToggler) navbarToggler.classList.remove('active');
            document.body.style.overflow = '';
        });
    }

    // === Back to Top Button ===
    var backToTop = document.getElementById('backToTop');
    function handleBackToTop() {
        if (!backToTop) return;
        if (window.scrollY > 400) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    }
    window.addEventListener('scroll', handleBackToTop);
    if (backToTop) {
        backToTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // === Scroll Reveal Animation ===
    var revealElements = document.querySelectorAll('.reveal');
    if (revealElements.length > 0) {
        var revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

        revealElements.forEach(function (el) {
            revealObserver.observe(el);
        });
    }

    // === Typing Animation for Hero Subtitle ===
    var typingEl = document.querySelector('.typing-text');
    if (typingEl) {
        var phrases = [
            'Healthcare AI Specialist',
            'Machine Learning Engineer',
            'LLM & RAG Expert',
            'Python Developer',
            'Cloud Architect'
        ];
        var phraseIndex = 0;
        var charIndex = 0;
        var isDeleting = false;
        var typingSpeed = 80;

        function typeEffect() {
            var currentPhrase = phrases[phraseIndex];

            if (isDeleting) {
                typingEl.textContent = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
                typingSpeed = 40;
            } else {
                typingEl.textContent = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
                typingSpeed = 80;
            }

            if (!isDeleting && charIndex === currentPhrase.length) {
                typingSpeed = 2000;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
                typingSpeed = 300;
            }

            setTimeout(typeEffect, typingSpeed);
        }
        typeEffect();
    }

    // === Progress Bar Animation ===
    var progressBars = document.querySelectorAll('.progress-bar[data-level]');
    if (progressBars.length > 0) {
        var progressObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var level = entry.target.getAttribute('data-level');
                    entry.target.style.width = level + '%';
                    entry.target.setAttribute('aria-valuenow', level);
                    progressObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });

        progressBars.forEach(function (bar) {
            bar.style.width = '0%';
            progressObserver.observe(bar);
        });
    }

    // === Contact Form Handling (Netlify Forms) ===
    var contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            var submitBtn = contactForm.querySelector('button[type="submit"]');
            var originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span class="spinner"></span> Sending...';
            submitBtn.disabled = true;

            var formData = new FormData(contactForm);

            fetch('/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams(formData).toString()
            })
            .then(function (response) {
                if (response.ok) {
                    window.location.href = '/thank-you/';
                } else {
                    showToast('Something went wrong. Please try again.', 'error');
                }
            })
            .catch(function () {
                showToast('Network error. Please check your connection.', 'error');
            })
            .finally(function () {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
        });
    }

    // === Toast Notification ===
    function showToast(message, type) {
        var container = document.getElementById('toastContainer');
        if (!container) return;

        var toast = document.createElement('div');
        toast.className = 'toast-notification toast-' + (type || 'info');

        var icon = type === 'success' ? 'fa-check-circle' : type === 'error' ? 'fa-exclamation-circle' : 'fa-info-circle';
        toast.innerHTML = '<i class="fas ' + icon + '"></i> ' + message;

        container.appendChild(toast);

        requestAnimationFrame(function () {
            toast.classList.add('show');
        });

        setTimeout(function () {
            toast.classList.remove('show');
            setTimeout(function () {
                if (toast.parentNode) toast.parentNode.removeChild(toast);
            }, 400);
        }, 4000);
    }

    // Make showToast globally available
    window.showToast = showToast;

    // === Smooth Scrolling for Anchor Links ===
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            var targetId = this.getAttribute('href');
            if (targetId === '#') return;
            var target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // === AI Code Rain + Neural Network Canvas Background ===
    function initAICanvas(canvas) {
        if (!canvas) return;
        var ctx = canvas.getContext('2d');
        var isMobile = window.innerWidth < 768;
        var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (isReducedMotion) return;

        function getTheme() {
            return document.documentElement.getAttribute('data-theme') || 'dark';
        }
        function getColors() {
            var theme = getTheme();
            if (theme === 'light') {
                return {
                    rain: [30, 60, 110],
                    rainHead: [14, 100, 180],
                    particle: [14, 100, 180],
                    particleGlow: [14, 165, 233],
                    connection: [14, 100, 180],
                    scan: [14, 100, 180],
                    hex: [14, 100, 180],
                    mouseGlow: [14, 165, 233]
                };
            }
            return {
                rain: [130, 180, 170],
                rainHead: [100, 255, 218],
                particle: [100, 255, 218],
                particleGlow: [100, 255, 218],
                connection: [100, 255, 218],
                scan: [100, 255, 218],
                hex: [100, 255, 218],
                mouseGlow: [100, 255, 218]
            };
        }
        var colors = getColors();

        var themeToggle = document.getElementById('themeToggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', function () {
                setTimeout(function () { colors = getColors(); }, 50);
            });
        }

        function rgba(rgb, a) {
            return 'rgba(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ',' + a + ')';
        }

        function resize() {
            canvas.width = canvas.offsetWidth * (window.devicePixelRatio || 1);
            canvas.height = canvas.offsetHeight * (window.devicePixelRatio || 1);
            ctx.scale(window.devicePixelRatio || 1, window.devicePixelRatio || 1);
        }
        resize();

        var W = function () { return canvas.offsetWidth; };
        var H = function () { return canvas.offsetHeight; };

        var CODE_TERMS = [
            'def train()', 'model.fit()', 'import torch', 'import tf',
            'class AI', 'nn.Linear', 'optimizer.step()', 'loss.backward()',
            'transformer', 'attention', 'embedding', 'tokenize',
            'GPT-4', 'LLM', 'RAG', 'fine-tune', 'pretrained',
            'accuracy', 'epoch', 'batch', 'gradient',
            'CNN', 'RNN', 'LSTM', 'BERT', 'GAN',
            'TensorFlow', 'PyTorch', 'sklearn', 'pandas',
            'GPU', 'CUDA', 'TPU', 'float16',
            'softmax', 'relu', 'sigmoid', 'dropout',
            'backprop', 'weights', 'bias', 'neuron',
            'True', 'False', 'None',
            'async', 'await', 'yield', 'lambda',
            'SELECT *', 'JOIN', 'WHERE', 'GROUP BY',
            'for i in', 'while True', 'if __name__',
            'np.array', 'pd.DataFrame', 'plt.plot()',
            'accuracy_score', 'confusion_matrix', 'roc_auc',
            'precision', 'recall', 'f1_score',
            'pipeline', 'fit_transform', 'cross_val',
            'docker', 'k8s', 'REST API', 'Flask',
            'git commit', 'git push', 'main.py',
            'print("AI")', 'return pred', 'data = []',
            '{ model: }', '[embeddings]', '(logits)',
            'selfAttention', 'multiHead', 'layerNorm',
            'tokenizer.encode', 'model.generate',
            'batch_size=32', 'lr=0.001', 'epochs=100'
        ];

        var fontSize = isMobile ? 11 : 14;
        var columns = [];

        function initColumns() {
            var colWidth = fontSize * 2.5;
            var columnCount = Math.floor(W() / colWidth);
            columns = [];
            for (var i = 0; i < columnCount; i++) {
                columns.push({
                    x: i * colWidth + fontSize,
                    y: Math.random() * H() * -1,
                    speed: 0.6 + Math.random() * 1.4,
                    chars: [],
                    maxChars: 6 + Math.floor(Math.random() * 10),
                    termTimer: 0,
                    termInterval: 4 + Math.floor(Math.random() * 8)
                });
            }
        }
        initColumns();

        function getRandomTerm() {
            return CODE_TERMS[Math.floor(Math.random() * CODE_TERMS.length)];
        }

        function drawCodeRain() {
            ctx.font = fontSize + 'px "JetBrains Mono", monospace';
            for (var i = 0; i < columns.length; i++) {
                var col = columns[i];
                col.y += col.speed;
                col.termTimer++;
                if (col.termTimer >= col.termInterval) {
                    col.termTimer = 0;
                    col.termInterval = 4 + Math.floor(Math.random() * 8);
                    col.chars.push({ text: getRandomTerm() });
                    if (col.chars.length > col.maxChars) col.chars.shift();
                }
                for (var j = 0; j < col.chars.length; j++) {
                    var ch = col.chars[j];
                    var yPos = col.y - (col.chars.length - j) * (fontSize * 1.7);
                    if (yPos > H() + 50 || yPos < -50) continue;
                    var distFromHead = (col.chars.length - 1 - j) / col.chars.length;
                    var alpha = (1 - distFromHead * 0.7) * 0.32;
                    if (j === col.chars.length - 1) {
                        ctx.fillStyle = rgba(colors.rainHead, alpha + 0.22);
                    } else {
                        ctx.fillStyle = rgba(colors.rain, alpha);
                    }
                    ctx.fillText(ch.text, col.x, yPos);
                }
                if (col.y - col.chars.length * (fontSize * 1.7) > H()) {
                    col.y = Math.random() * H() * -0.5;
                    col.chars = [];
                    col.speed = 0.6 + Math.random() * 1.4;
                }
            }
        }

        var particles = [];
        var particleCount = isMobile ? 15 : 35;
        var connectionDistance = isMobile ? 80 : 120;

        function initParticles() {
            particleCount = isMobile ? 15 : 35;
            connectionDistance = isMobile ? 80 : 120;
            particles = [];
            for (var i = 0; i < particleCount; i++) {
                particles.push({
                    x: Math.random() * W(),
                    y: Math.random() * H(),
                    vx: (Math.random() - 0.5) * 0.3,
                    vy: (Math.random() - 0.5) * 0.3,
                    radius: isMobile ? 1.2 : 1.8,
                    pulse: Math.random() * Math.PI * 2
                });
            }
        }
        initParticles();

        var mouse = { x: -1000, y: -1000 };
        canvas.addEventListener('mousemove', function (e) {
            var rect = canvas.getBoundingClientRect();
            mouse.x = e.clientX - rect.left;
            mouse.y = e.clientY - rect.top;
        });
        canvas.addEventListener('mouseleave', function () {
            mouse.x = -1000; mouse.y = -1000;
        });

        function drawParticles() {
            for (var i = 0; i < particles.length; i++) {
                var p = particles[i];
                p.x += p.vx; p.y += p.vy; p.pulse += 0.015;
                if (p.x < 0 || p.x > W()) p.vx *= -1;
                if (p.y < 0 || p.y > H()) p.vy *= -1;
                p.x = Math.max(0, Math.min(W(), p.x));
                p.y = Math.max(0, Math.min(H(), p.y));
                var dx = p.x - mouse.x, dy = p.y - mouse.y;
                var dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 100) {
                    var force = (100 - dist) / 100 * 0.015;
                    p.vx += (dx / dist) * force;
                    p.vy += (dy / dist) * force;
                }
                p.vx *= 0.999; p.vy *= 0.999;
            }
            for (var i = 0; i < particles.length; i++) {
                for (var j = i + 1; j < particles.length; j++) {
                    var dx = particles[i].x - particles[j].x;
                    var dy = particles[i].y - particles[j].y;
                    var dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < connectionDistance) {
                        var alpha = (1 - dist / connectionDistance) * 0.08;
                        ctx.beginPath();
                        ctx.strokeStyle = rgba(colors.connection, alpha);
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
            for (var i = 0; i < particles.length; i++) {
                var p = particles[i];
                var glow = Math.sin(p.pulse) * 0.5 + 0.5;
                var r = p.radius + glow;
                ctx.beginPath();
                ctx.arc(p.x, p.y, r + 3, 0, Math.PI * 2);
                ctx.fillStyle = rgba(colors.particleGlow, glow * 0.04);
                ctx.fill();
                ctx.beginPath();
                ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
                ctx.fillStyle = rgba(colors.particle, 0.18 + glow * 0.12);
                ctx.fill();
            }
            if (mouse.x > 0 && mouse.y > 0) {
                var grad = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 120);
                grad.addColorStop(0, rgba(colors.mouseGlow, 0.03));
                grad.addColorStop(1, rgba(colors.mouseGlow, 0));
                ctx.beginPath();
                ctx.arc(mouse.x, mouse.y, 120, 0, Math.PI * 2);
                ctx.fillStyle = grad;
                ctx.fill();
            }
        }

        var scanLines = [];
        function initScanLines() {
            scanLines = [];
            var count = isMobile ? 2 : 3;
            for (var i = 0; i < count; i++) {
                scanLines.push({
                    y: Math.random() * H(),
                    speed: 0.15 + Math.random() * 0.3,
                    width: 80 + Math.random() * 160,
                    alpha: 0.01 + Math.random() * 0.015
                });
            }
        }
        initScanLines();

        function drawScanLines() {
            for (var i = 0; i < scanLines.length; i++) {
                var sl = scanLines[i];
                sl.y += sl.speed;
                if (sl.y > H() + 10) { sl.y = -10; sl.width = 80 + Math.random() * 160; }
                var gradient = ctx.createLinearGradient(W() / 2 - sl.width / 2, 0, W() / 2 + sl.width / 2, 0);
                gradient.addColorStop(0, rgba(colors.scan, 0));
                gradient.addColorStop(0.5, rgba(colors.scan, sl.alpha));
                gradient.addColorStop(1, rgba(colors.scan, 0));
                ctx.fillStyle = gradient;
                ctx.fillRect(W() / 2 - sl.width / 2, sl.y, sl.width, 1);
            }
        }

        var hexFrame = 0;
        var aiVisible = true;
        var aiObserver = new IntersectionObserver(function (entries) {
            aiVisible = entries[0].isIntersecting;
        }, { threshold: 0 });
        aiObserver.observe(canvas);

        function animate() {
            if (!aiVisible) { requestAnimationFrame(animate); return; }
            ctx.clearRect(0, 0, W(), H());
            hexFrame++;
            if (hexFrame % 6 === 0) {
                var hexSize = isMobile ? 55 : 75;
                var hexH = hexSize * Math.sqrt(3);
                ctx.strokeStyle = rgba(colors.hex, 0.012);
                ctx.lineWidth = 0.5;
                for (var row = -1; row < H() / hexH + 1; row++) {
                    for (var col = -1; col < W() / (hexSize * 1.5) + 1; col++) {
                        var cx = col * hexSize * 1.5;
                        var cy = row * hexH + (col % 2 ? hexH / 2 : 0);
                        var r = hexSize * 0.45;
                        ctx.beginPath();
                        for (var k = 0; k < 6; k++) {
                            var angle = Math.PI / 3 * k - Math.PI / 6;
                            var hx = cx + r * Math.cos(angle);
                            var hy = cy + r * Math.sin(angle);
                            if (k === 0) ctx.moveTo(hx, hy); else ctx.lineTo(hx, hy);
                        }
                        ctx.closePath(); ctx.stroke();
                    }
                }
            }
            drawCodeRain();
            drawScanLines();
            drawParticles();
            requestAnimationFrame(animate);
        }
        animate();
    }

    // Initialize all AI canvases
    var allCanvases = document.querySelectorAll('#ai-canvas, .ai-page-canvas');
    allCanvases.forEach(function (c) { initAICanvas(c); });

    // === Profile Neural Network Canvas ===
    function initProfileCanvas() {
        var canvas = document.getElementById('profile-canvas');
        if (!canvas) return;
        var ctx = canvas.getContext('2d');
        var isMobile = window.innerWidth < 768;

        function getTheme() {
            return document.documentElement.getAttribute('data-theme') || 'dark';
        }

        function getProfileColors() {
            var theme = getTheme();
            if (theme === 'light') {
                return {
                    node: [14, 165, 233],
                    nodeGlow: [56, 189, 248],
                    connection: [14, 165, 233],
                    orbit: [14, 165, 233]
                };
            }
            return {
                node: [100, 255, 218],
                nodeGlow: [100, 255, 218],
                connection: [100, 255, 218],
                orbit: [100, 255, 218]
            };
        }

        var colors = getProfileColors();
        var themeToggle = document.getElementById('themeToggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', function () {
                setTimeout(function () { colors = getProfileColors(); }, 50);
            });
        }

        function rgba(rgb, a) {
            return 'rgba(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ',' + a + ')';
        }

        var profileImg = canvas.parentElement.querySelector('.hero-profile-img');
        var overshoot = 90;
        function resize() {
            var imgW = profileImg ? profileImg.offsetWidth : 400;
            var imgH = profileImg ? profileImg.offsetHeight : 400;
            var dpr = window.devicePixelRatio || 1;
            canvas.width = (imgW + overshoot * 2) * dpr;
            canvas.height = (imgH + overshoot * 2) * dpr;
            ctx.scale(dpr, dpr);
            canvas.style.width = (imgW + overshoot * 2) + 'px';
            canvas.style.height = (imgH + overshoot * 2) + 'px';
        }
        resize();
        window.addEventListener('resize', resize);

        var W = function () { return canvas.width / (window.devicePixelRatio || 1); };
        var H = function () { return canvas.height / (window.devicePixelRatio || 1); };
        var centerX = function () { return profileImg ? profileImg.offsetWidth / 2 + overshoot : W() / 2; };
        var centerY = function () { return profileImg ? profileImg.offsetHeight / 2 + overshoot : H() / 2; };

        var nodeCount = isMobile ? 25 : 40;
        var nodes = [];

        function initNodes() {
            nodes = [];
            for (var i = 0; i < nodeCount; i++) {
                var angle = (Math.PI * 2 / nodeCount) * i;
                var radius = 210 + Math.random() * 70;
                nodes.push({
                    angle: angle,
                    radius: radius,
                    speed: 0.003 + Math.random() * 0.006,
                    size: 1.5 + Math.random() * 2,
                    pulse: Math.random() * Math.PI * 2,
                    drift: (Math.random() - 0.5) * 0.5
                });
            }
        }
        initNodes();

        var mouseX = -1000, mouseY = -1000;
        canvas.parentElement.addEventListener('mousemove', function (e) {
            var rect = canvas.getBoundingClientRect();
            mouseX = e.clientX - rect.left;
            mouseY = e.clientY - rect.top;
        });
        canvas.parentElement.addEventListener('mouseleave', function () {
            mouseX = -1000; mouseY = -1000;
        });

        var profileVisible = true;
        var profileObserver = new IntersectionObserver(function (entries) {
            profileVisible = entries[0].isIntersecting;
        }, { threshold: 0 });
        profileObserver.observe(canvas.parentElement);

        function animate() {
            if (!profileVisible) { requestAnimationFrame(animate); return; }
            ctx.clearRect(0, 0, W(), H());

            var cx = centerX();
            var cy = centerY();

            // Draw orbital rings
            ctx.strokeStyle = rgba(colors.orbit, 0.06);
            ctx.lineWidth = 0.5;
            for (var r = 200; r <= 290; r += 30) {
                ctx.beginPath();
                ctx.arc(cx, cy, r, 0, Math.PI * 2);
                ctx.stroke();
            }

            // Update and get node positions
            var positions = [];
            for (var i = 0; i < nodes.length; i++) {
                var n = nodes[i];
                n.angle += n.speed;
                n.pulse += 0.02;
                var x = cx + Math.cos(n.angle) * n.radius + Math.sin(n.pulse) * n.drift;
                var y = cy + Math.sin(n.angle) * n.radius + Math.cos(n.pulse) * n.drift;
                positions.push({ x: x, y: y, size: n.size, pulse: n.pulse });

                // Mouse repulsion
                var dx = x - mouseX, dy = y - mouseY;
                var dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 100) {
                    var force = (100 - dist) / 100 * 2;
                    positions[i].x += (dx / dist) * force;
                    positions[i].y += (dy / dist) * force;
                }
            }

            // Draw connections
            for (var i = 0; i < positions.length; i++) {
                for (var j = i + 1; j < positions.length; j++) {
                    var dx = positions[i].x - positions[j].x;
                    var dy = positions[i].y - positions[j].y;
                    var dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 120) {
                        var alpha = (1 - dist / 120) * 0.2;
                        ctx.beginPath();
                        ctx.strokeStyle = rgba(colors.connection, alpha);
                        ctx.lineWidth = 0.6;
                        ctx.moveTo(positions[i].x, positions[i].y);
                        ctx.lineTo(positions[j].x, positions[j].y);
                        ctx.stroke();
                    }
                }
            }

            // Draw nodes
            for (var i = 0; i < positions.length; i++) {
                var p = positions[i];
                var glow = Math.sin(p.pulse) * 0.5 + 0.5;
                var r = p.size + glow * 1.5;

                // Glow
                ctx.beginPath();
                ctx.arc(p.x, p.y, r + 4, 0, Math.PI * 2);
                ctx.fillStyle = rgba(colors.nodeGlow, glow * 0.15);
                ctx.fill();

                // Core
                ctx.beginPath();
                ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
                ctx.fillStyle = rgba(colors.node, 0.5 + glow * 0.3);
                ctx.fill();
            }

            requestAnimationFrame(animate);
        }
        animate();
    }

    initProfileCanvas();

    // === Project Filter (for Projects page) ===
    var filterBtns = document.querySelectorAll('.filter-btn');
    if (filterBtns.length > 0) {
        filterBtns.forEach(function (btn) {
            btn.addEventListener('click', function () {
                filterBtns.forEach(function (b) { b.classList.remove('active'); });
                btn.classList.add('active');

                var filter = btn.getAttribute('data-filter');
                var cards = document.querySelectorAll('.project-card');

                cards.forEach(function (card) {
                    if (filter === 'all' || card.getAttribute('data-category').includes(filter)) {
                        card.style.display = '';
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(20px)';
                        setTimeout(function () {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, 50);
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(20px)';
                        setTimeout(function () {
                            card.style.display = 'none';
                        }, 300);
                    }
                });
            });
        });
    }

});
