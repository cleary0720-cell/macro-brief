/* subscribe.js — The Macro Brief
   Single source of truth for all subscribe form logic.
   Includes Cloudflare Turnstile bot protection. */

(function () {
    var WORKER   = 'https://beehiiv-proxy.cleary0720.workers.dev';
    var SITE_KEY = '0x4AAAAAADPi_-iaraiFFwM9';

    /* ── Load Turnstile script once ── */
    function loadTurnstile() {
        return new Promise(function (resolve) {
            if (window.turnstile) { resolve(); return; }
            var s = document.createElement('script');
            s.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit';
            s.async = true;
            s.onload = resolve;
            document.head.appendChild(s);
        });
    }

    /* ── Get a Turnstile token for a given container element ── */
    function getToken(container) {
        return loadTurnstile().then(function () {
            return new Promise(function (resolve, reject) {
                container.innerHTML = '';
                window.turnstile.render(container, {
                    sitekey: SITE_KEY,
                    size: 'invisible',
                    callback: resolve,
                    'error-callback': function () { reject(new Error('Security check failed. Please try again.')); },
                    'expired-callback': function () { reject(new Error('Security check expired. Please try again.')); }
                });
                window.turnstile.execute(container);
            });
        });
    }

    /* ── Validate email format ── */
    function validEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    /* ── Main newsletter form (index.html, about.html) ── */
    var nlForm = document.getElementById('nl-form');
    if (nlForm) {
        var nlTurnstile = document.createElement('div');
        nlForm.appendChild(nlTurnstile);

        nlForm.addEventListener('submit', async function (e) {
            e.preventDefault();
            var email     = (document.getElementById('nl-email') || {}).value || '';
            var firstName = (document.getElementById('nl-fname') || {}).value || '';
            var lastName  = (document.getElementById('nl-lname') || {}).value || '';
            var btn       = document.getElementById('nl-btn');
            var errEl     = document.getElementById('nl-error');

            email = email.trim();
            if (!validEmail(email)) {
                if (errEl) { errEl.textContent = '⚠ Please enter a valid email address.'; errEl.style.display = 'block'; }
                return;
            }

            if (btn) { btn.textContent = 'Verifying…'; btn.disabled = true; }
            if (errEl) errEl.style.display = 'none';

            try {
                var token = await getToken(nlTurnstile);
                var body = { email: email, reactivate_existing: false, send_welcome_email: true, 'cf-turnstile-response': token };
                if (firstName.trim()) body.first_name = firstName.trim();
                if (lastName.trim())  body.last_name  = lastName.trim();

                if (btn) btn.textContent = 'Subscribing…';
                var res = await fetch(WORKER, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(body)
                });

                if (!res.ok) {
                    var data = await res.json().catch(function () { return {}; });
                    throw new Error(data.message || ('Request failed (' + res.status + ')'));
                }

                nlForm.style.display = 'none';
                var success = document.getElementById('nl-success');
                if (success) success.style.display = 'block';
                localStorage.setItem('tmb-subscribed', '1');

            } catch (err) {
                if (btn) { btn.textContent = "Subscribe — It's Free →"; btn.disabled = false; }
                if (errEl) { errEl.textContent = '⚠ ' + (err.message || 'Something went wrong. Please try again.'); errEl.style.display = 'block'; }
            }
        });
    }

    /* ── Sticky bar ── */
    var stickyBar = document.getElementById('sticky-bar');
    if (stickyBar) {
        if (localStorage.getItem('tmb-subscribed') || localStorage.getItem('bar-dismissed')) {
            /* already subscribed or dismissed — never show */
        } else {
            var shown = false;
            window.addEventListener('scroll', function () {
                if (shown) return;
                if (window.scrollY > 400) {
                    stickyBar.style.display = 'block';
                    shown = true;
                }
            });
        }

        var stickyTurnstile = document.createElement('div');
        stickyTurnstile.style.display = 'none';
        document.body.appendChild(stickyTurnstile);
    }

    window.dismissBar = function () {
        if (stickyBar) stickyBar.style.display = 'none';
        localStorage.setItem('bar-dismissed', '1');
    };

    window.stickySubmit = async function (e) {
        e.preventDefault();
        var emailEl = document.getElementById('sticky-email');
        var submitBtn = e.target ? e.target.querySelector('button[type="submit"]') : null;
        var email = emailEl ? emailEl.value.trim() : '';
        if (!validEmail(email)) return;

        if (submitBtn) { submitBtn.textContent = 'Checking…'; submitBtn.disabled = true; }

        try {
            var token = await getToken(stickyTurnstile);
            await fetch(WORKER, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: email, utm_source: 'sticky-bar', 'cf-turnstile-response': token })
            });
        } catch (_) {}

        var form = document.getElementById('sticky-form');
        var success = document.getElementById('sticky-success');
        if (form) form.style.display = 'none';
        if (success) success.style.display = 'block';
        localStorage.setItem('tmb-subscribed', '1');
        setTimeout(window.dismissBar, 3000);
    };

    /* ── About page form ── */
    var abForm = document.getElementById('ab-form');
    if (abForm) {
        var abTurnstile = document.createElement('div');
        abForm.appendChild(abTurnstile);

        abForm.addEventListener('submit', async function (e) {
            e.preventDefault();
            var email = (document.getElementById('ab-email') || {}).value || '';
            var fname = (document.getElementById('ab-fname') || {}).value || '';
            var lname = (document.getElementById('ab-lname') || {}).value || '';
            var btn   = document.getElementById('ab-btn');
            var succ  = document.getElementById('ab-success');
            var errEl = document.getElementById('ab-error');

            email = email.trim();
            if (!validEmail(email)) {
                if (errEl) { errEl.textContent = '⚠ Please enter a valid email address.'; errEl.style.display = 'block'; }
                return;
            }

            if (btn) { btn.textContent = 'Verifying…'; btn.disabled = true; }

            try {
                var token = await getToken(abTurnstile);
                var body = { email: email, reactivate_existing: false, send_welcome_email: true, 'cf-turnstile-response': token };
                if (fname.trim()) body.first_name = fname.trim();
                if (lname.trim()) body.last_name  = lname.trim();

                if (btn) btn.textContent = 'Subscribing…';
                var res = await fetch(WORKER, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(body)
                });

                if (!res.ok) throw new Error('Request failed');
                if (succ) succ.style.display = 'block';
                abForm.style.display = 'none';
                localStorage.setItem('tmb-subscribed', '1');
            } catch (err) {
                if (btn) { btn.textContent = 'Subscribe Free →'; btn.disabled = false; }
                if (errEl) { errEl.textContent = '⚠ ' + (err.message || 'Something went wrong. Please try again.'); errEl.style.display = 'block'; }
            }
        });
    }

})();
