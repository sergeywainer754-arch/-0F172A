from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

<script>
const tg = window.Telegram.WebApp;
tg.ready();

const isAndroid = /Android/i.test(navigator.userAgent);
const isIOS = /iPhone|iPad|iPod/i.test(navigator.userAgent);

// ✅ Android — fullscreen
if (isAndroid && tg.requestFullscreen) {
    tg.requestFullscreen();
}

// ✅ iPhone — тоже fullscreen
if (isIOS && tg.requestFullscreen) {
    tg.requestFullscreen();
}

// ПК — просто expand
if (!isAndroid && !isIOS) {
    tg.expand();
}

tg.setHeaderColor('#1c1c1c');
tg.setBackgroundColor('#1c1c1c');

function updateLayout() {

    const safeTop = tg.safeAreaInset ? tg.safeAreaInset.top : 0;
    const contentTop = tg.contentSafeAreaInset ? tg.contentSafeAreaInset.top : 0;

    // 👇 вот тут регулируем высоту
    const topPadding = safeTop + contentTop + 28;

    document.querySelector('.container').style.paddingTop = topPadding + 'px';

    const h = tg.viewportStableHeight || tg.viewportHeight;
    if (h) {
        document.documentElement.style.height = h + 'px';
        document.body.style.height = h + 'px';
    }
}

window.addEventListener('DOMContentLoaded', updateLayout);
tg.onEvent('viewportChanged', updateLayout);
tg.onEvent('safeAreaChanged', updateLayout);

setTimeout(updateLayout, 300);
setTimeout(updateLayout, 800);

</script>

<title>ROCKET VPN</title>
<style>
:root {
  --bg:    #1c1c1c;
  --card:  #2b2b2b;
  --card2: #333333;
  --accent:        #7B61FF;
  --accent2:       #9B85FF;
  --accent-soft:   rgba(123,97,255,0.15);
  --accent-border: rgba(123,97,255,0.3);
  --green:  #4CD964;
  --red:    #FF3B30;
  --orange: #FF9500;
  --blue:   #2AABEE;
  --text:   #FFFFFF;
  --text2:  #AAAAAA;
  --text3:  #555555;
  --divider: rgba(255,255,255,0.06);
  --r:  20px;
  --r2: 24px;
}

* { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }

html, body {
  height: 100%;
  background: var(--bg);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: var(--text);
  font-size: 15px;
  overflow: hidden;
}

.container {
  max-width: 500px;
  margin: 0 auto;
  padding-top: 12px;
  padding-bottom: 86px;
  height: 100%;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}

.page { display: none; }
.page.active { display: block; animation: fadeUp 0.2s ease; }
@keyframes fadeUp { from{opacity:0;transform:translateY(6px)} to{opacity:1;transform:translateY(0)} }

.spacer { height: 8px; }

.section-label {
  padding: 10px 16px 5px;
  font-size: 13px; font-weight: 600;
  color: var(--text2);
  text-transform: uppercase; letter-spacing: 0.5px;
}

.section {
  background: var(--card);
  border-radius: var(--r2);
  margin: 8px 12px;
  overflow: hidden;
}
.section .section-label { padding: 14px 16px 6px; }

/* KEY CARD */
.key-card {
  background: var(--card);
  border-radius: var(--r2);
  margin: 8px 12px;
  overflow: hidden;
  transition: transform 0.1s;
}
.key-card:active { transform: scale(0.99); }
.key-card-top { padding: 16px; display: flex; align-items: center; gap: 13px; }
.key-icon {
  width: 48px; height: 48px; border-radius: 16px;
  display: flex; align-items: center; justify-content: center;
  font-size: 22px; flex-shrink: 0;
}
.key-icon.active-icon  { background: rgba(76,217,100,0.15); }
.key-icon.expired-icon { background: rgba(255,59,48,0.12); }
.key-info { flex: 1; min-width: 0; }
.key-id   { font-size: 16px; font-weight: 700; }
.key-meta { font-size: 13px; color: var(--text2); display: flex; align-items: center; gap: 8px; margin-top: 4px; }
.key-badge { font-size: 11px; font-weight: 600; padding: 2px 9px; border-radius: 30px; }
.badge-active  { background: rgba(76,217,100,0.15); color: var(--green); }
.badge-expired { background: rgba(255,59,48,0.12);  color: var(--red); }
.badge-vless   { background: var(--accent-soft); color: var(--accent2); font-size: 10px; padding: 2px 8px; border-radius: 30px; font-weight: 600; }
.key-status { display: flex; align-items: center; gap: 5px; font-size: 13px; margin-top: 5px; }
.status-dot { width: 6px; height: 6px; border-radius: 50%; }
.dot-green { background: var(--green); }
.dot-red   { background: var(--red); animation: blink 1.4s infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }
.key-divider { height: 1px; background: var(--divider); margin: 0 16px; }
.key-actions { display: flex; padding: 10px 12px; gap: 8px; }
.key-btn {
  flex: 1; padding: 12px;
  border-radius: var(--r); border: none;
  font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 600;
  cursor: pointer; transition: all 0.15s;
}
.key-btn:active { transform: scale(0.96); }
.btn-ghost  { background: var(--card2); color: var(--text); }
.btn-accent { background: var(--accent); color: #fff; }
.btn-accent:active { background: var(--accent2); }
.btn-danger-row {
  display: block; background: rgba(255,59,48,0.1); color: var(--red);
  border: none; margin: 0 12px 12px; width: calc(100% - 24px);
  padding: 12px; border-radius: var(--r);
  font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 600;
  cursor: pointer; transition: all 0.15s;
}
.btn-danger-row:active { transform: scale(0.98); }

.main-btn {
  width: calc(100% - 24px); margin: 6px 12px 10px; padding: 15px;
  border-radius: var(--r2); border: none;
  background: var(--accent); color: #fff;
  font-family: 'Inter', sans-serif; font-size: 16px; font-weight: 600;
  cursor: pointer; transition: all 0.15s;
  display: flex; align-items: center; justify-content: center; gap: 8px;
}
.main-btn:active { transform: scale(0.98); background: var(--accent2); }

/* BANNERS */
.buy-banner {
  margin: 8px 12px;
  background: linear-gradient(135deg, #2d1f66, #1e1450);
  border-radius: var(--r2); padding: 22px 18px;
  border: 1px solid var(--accent-border);
  position: relative; overflow: hidden;
}
.buy-banner::after {
  content: '🚀'; position: absolute; right: 18px; top: 50%;
  transform: translateY(-50%); font-size: 56px; opacity: 0.12; pointer-events: none;
}
.buy-banner h3 { font-size: 16px; font-weight: 700; margin-bottom: 6px; }
.buy-banner p  { font-size: 13px; color: rgba(255,255,255,0.6); margin-bottom: 16px; line-height: 1.5; }

.balance-block {
  margin: 0 12px 0;
  background: linear-gradient(135deg, #2d1f66, #1e1450);
  border-radius: var(--r2); padding: 24px 20px;
  border: 1px solid var(--accent-border);
  position: relative; overflow: hidden;
}
.balance-block::after {
  content: '🚀'; position: absolute; right: 18px; top: 50%;
  transform: translateY(-50%); font-size: 52px; opacity: 0.1; pointer-events: none;
}
.balance-lbl { font-size: 13px; color: rgba(255,255,255,0.5); margin-bottom: 6px; }
.balance-val { font-size: 40px; font-weight: 700; line-height: 1; }
.balance-val span { font-size: 24px; color: var(--accent2); margin-right: 4px; }

/* LIST */
.list-item {
  display: flex; align-items: center; padding: 13px 16px; gap: 13px;
  cursor: pointer; transition: background 0.1s; border-bottom: 1px solid var(--divider);
}
.list-item:last-child { border-bottom: none; }
.list-item:active { background: rgba(255,255,255,0.04); }
.li-icon {
  width: 40px; height: 40px; border-radius: 14px;
  display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0;
}
.li-icon.purple { background: var(--accent-soft); }
.li-icon.blue   { background: rgba(42,171,238,0.12); }
.li-icon.green  { background: rgba(76,217,100,0.12); }
.li-icon.orange { background: rgba(255,149,0,0.12); }
.li-content { flex: 1; min-width: 0; }
.li-title { font-size: 15px; font-weight: 500; }
.li-sub   { font-size: 13px; color: var(--text2); margin-top: 2px; }
.li-right { display: flex; align-items: center; gap: 6px; color: var(--text2); }
.li-value { font-size: 15px; font-weight: 600; }
.li-value.income  { color: var(--green); }
.li-value.expense { color: var(--red); }
.li-chevron { color: var(--text3); font-size: 14px; }

/* AMOUNT */
.amount-wrap {
  margin: 0 16px 12px; background: #222; border-radius: var(--r);
  display: flex; align-items: center; padding: 0 14px;
  border: 1.5px solid transparent; transition: border-color 0.2s;
}
.amount-wrap:focus-within { border-color: var(--accent); }
.amount-sym   { font-size: 22px; font-weight: 700; color: var(--accent2); margin-right: 6px; }
.amount-input {
  background: transparent; border: none; outline: none;
  font-family: 'Inter', sans-serif; font-size: 28px; font-weight: 700;
  color: var(--text); width: 100%; padding: 12px 0;
}
.quick-row { display: flex; gap: 7px; padding: 0 16px 14px; }
.q-btn {
  flex: 1; padding: 10px 4px; border-radius: var(--r);
  border: 1px solid var(--divider); background: #222; color: var(--text2);
  font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 600;
  cursor: pointer; transition: all 0.15s; text-align: center;
}
.q-btn.sel { border-color: var(--accent); color: var(--accent2); background: var(--accent-soft); }

/* REF */
.ref-stats { display: grid; grid-template-columns: 1fr 1fr; }
.ref-stat  { padding: 20px 16px; text-align: center; border-right: 1px solid var(--divider); }
.ref-stat:last-child { border-right: none; }
.ref-stat-val { font-size: 28px; font-weight: 700; color: var(--accent2); margin-bottom: 4px; }
.ref-stat-lbl { font-size: 12px; color: var(--text2); }
.ref-link-row {
  display: flex; align-items: center; margin: 0 16px 14px; background: #222;
  border-radius: var(--r); padding: 10px 12px; gap: 10px; border: 1px solid var(--accent-border);
}
.ref-link-txt { flex: 1; font-size: 13px; color: var(--accent2); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.copy-pill {
  background: var(--accent); color: #fff; border: none;
  border-radius: 30px; padding: 7px 14px;
  font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 600;
  cursor: pointer; flex-shrink: 0; transition: all 0.15s;
}
.copy-pill:active { background: var(--accent2); transform: scale(0.96); }

/* STEPS */
.step-item {
  display: flex; align-items: flex-start; gap: 13px;
  padding: 13px 16px; border-bottom: 1px solid var(--divider);
}
.step-item:last-child { border-bottom: none; }
.step-circle {
  width: 28px; height: 28px; border-radius: 50%;
  background: var(--accent-soft); border: 1.5px solid var(--accent-border);
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 700; color: var(--accent2);
  flex-shrink: 0; margin-top: 2px;
}
.step-text { font-size: 14px; color: var(--text2); line-height: 1.6; padding-top: 3px; }
.step-text strong { color: var(--text); }

/* FAQ */
.faq-item { border-bottom: 1px solid var(--divider); overflow: hidden; }
.faq-item:last-child { border-bottom: none; }
.faq-q { display: flex; justify-content: space-between; align-items: center; padding: 14px 16px; cursor: pointer; gap: 12px; }
.faq-q:active { background: rgba(255,255,255,0.03); }
.faq-q-text { font-size: 15px; font-weight: 500; }
.faq-chevron {
  width: 22px; height: 22px; border-radius: 50%; background: var(--card2);
  display: flex; align-items: center; justify-content: center;
  color: var(--text2); font-size: 11px; flex-shrink: 0;
  transition: transform 0.25s, background 0.2s;
}
.faq-item.open .faq-chevron { transform: rotate(180deg); background: var(--accent-soft); color: var(--accent2); }
.faq-ans { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }
.faq-item.open .faq-ans { max-height: 200px; }
.faq-ans-inner { padding: 0 16px 14px; font-size: 14px; color: var(--text2); line-height: 1.65; }

/* BOTTOM NAV */
.bottom-nav {
  position: fixed; bottom: 0; left: 0; right: 0;
  background: rgba(28,28,28,0.97);
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
  border-top: 1px solid var(--divider);
  border-radius: var(--r2) var(--r2) 0 0;
  display: flex; justify-content: space-around;
  padding: 8px 0 calc(8px + env(safe-area-inset-bottom, 16px));
  z-index: 100;
}
.nav-btn {
  background: none; border: none; color: var(--text3);
  font-size: 10px; font-weight: 500; font-family: 'Inter', sans-serif;
  display: flex; flex-direction: column; align-items: center; gap: 4px;
  cursor: pointer; transition: color 0.15s; padding: 4px 14px; line-height: 1;
}
.nav-icon-wrap { width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; }
.nav-btn.active { color: var(--accent2); }

/* TOAST */
.toast {
  position: fixed; bottom: 100px; left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: #3a3a3a; color: #fff;
  padding: 11px 22px; border-radius: 30px;
  font-size: 14px; font-weight: 500;
  z-index: 999; opacity: 0;
  transition: all 0.3s cubic-bezier(0.34,1.3,0.64,1);
  pointer-events: none; white-space: nowrap;
}
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
</style>
</head>
<body>

<div id="toast" class="toast"></div>

<div class="container">

  <!-- VPN -->
  <div id="vpnPage" class="page active">
    <div class="section-label">Мои ключи</div>

    <div class="key-card">
      <div class="key-card-top">
        <div class="key-icon active-icon">🛡️</div>
        <div class="key-info">
          <div style="display:flex;align-items:center;gap:7px;margin-bottom:5px">
            <span class="key-id">#ROCKET-7821</span>
            <span class="badge-vless">VLESS</span>
          </div>
          <div class="key-meta">
            <span class="key-badge badge-active">Оплачен</span>
            <span>· 2 устройства</span>
          </div>
          <div class="key-status" style="color:var(--green)">
            <div class="status-dot dot-green"></div>
            <span>До 15 марта 2026</span>
          </div>
        </div>
      </div>
      <div class="key-divider"></div>
      <div class="key-actions">
        <button class="key-btn btn-ghost" onclick="showToast('📋 Ключ скопирован')">📋 Ваш ключ</button>
        <button class="key-btn btn-accent">🚀 Продлить</button>
      </div>
    </div>

    <div class="key-card">
      <div class="key-card-top">
        <div class="key-icon expired-icon">🔑</div>
        <div class="key-info">
          <div style="display:flex;align-items:center;gap:7px;margin-bottom:5px">
            <span class="key-id">#ROCKET-4103</span>
            <span class="badge-vless">VLESS</span>
          </div>
          <div class="key-meta">
            <span class="key-badge badge-expired">Не оплачен</span>
            <span>· 1 устройство</span>
          </div>
          <div class="key-status" style="color:var(--red)">
            <div class="status-dot dot-red"></div>
            <span>Закончился</span>
          </div>
        </div>
      </div>
      <div class="key-divider"></div>
      <div class="key-actions">
        <button class="key-btn btn-ghost" onclick="showToast('📋 Ключ скопирован')">📋 Ваш ключ</button>
        <button class="key-btn btn-accent">🚀 Продлить</button>
      </div>
      <button class="btn-danger-row">🗑 Удалить ключ</button>
    </div>

    <div class="buy-banner">
      <h3>Нужно больше VPN?</h3>
      <p>Приобретите неограниченное<br>количество ключей VPN</p>
      <button class="main-btn" style="margin:0;width:100%;border-radius:20px">🚀 Купить VPN</button>
    </div>
    <div class="spacer"></div>
  </div>

  <!-- WALLET -->
  <div id="walletPage" class="page">
    <div class="balance-block">
      <div class="balance-lbl">Баланс кошелька</div>
      <div class="balance-val"><span>₽</span>126.25</div>
    </div>
    <div class="spacer"></div>
    <div class="section">
      <div class="section-label">Способ пополнения</div>
      <div class="list-item">
        <div class="li-icon blue">⚡</div>
        <div class="li-content"><div class="li-title">СБП</div><div class="li-sub">Система быстрых платежей</div></div>
        <div class="li-right"><span class="li-chevron">›</span></div>
      </div>
      <div class="list-item" style="border-bottom:none">
        <div class="li-icon purple">💳</div>
        <div class="li-content"><div class="li-title">Банковская карта</div><div class="li-sub">Visa, MasterCard, МИР</div></div>
        <div class="li-right"><span class="li-chevron">›</span></div>
      </div>
    </div>
    <div class="section" style="padding-top:12px">
      <div class="section-label" style="padding-top:2px">Сумма пополнения</div>
      <div class="amount-wrap">
        <div class="amount-sym">₽</div>
        <input class="amount-input" type="number" value="150" id="amtInput">
      </div>
      <div class="quick-row">
        <button class="q-btn sel" onclick="setAmt(150,this)">150</button>
        <button class="q-btn" onclick="setAmt(300,this)">300</button>
        <button class="q-btn" onclick="setAmt(500,this)">500</button>
        <button class="q-btn" onclick="setAmt(1000,this)">1000</button>
        <button class="q-btn" onclick="setAmt('',this)">Своя</button>
      </div>
    </div>
    <button class="main-btn" onclick="showToast('⚡ Переход к оплате...')">⚡ Перейти к пополнению</button>
    <div class="section">
      <div class="section-label">История операций</div>
      <div class="list-item">
        <div class="li-icon green">💳</div>
        <div class="li-content"><div class="li-title">Пополнение</div><div class="li-sub">19 фев 2026, 14:23</div></div>
        <div class="li-right"><span class="li-value income">+500 ₽</span></div>
      </div>
      <div class="list-item">
        <div class="li-icon purple">🚀</div>
        <div class="li-content"><div class="li-title">Оплата VPN · #ROCKET-7821</div><div class="li-sub">18 фев 2026, 10:05</div></div>
        <div class="li-right"><span class="li-value expense">−299 ₽</span></div>
      </div>
      <div class="list-item" style="border-bottom:none">
        <div class="li-icon orange">👥</div>
        <div class="li-content"><div class="li-title">Реферальный бонус</div><div class="li-sub">15 фев 2026, 09:40</div></div>
        <div class="li-right"><span class="li-value income">+74.25 ₽</span></div>
      </div>
    </div>
    <div class="spacer"></div>
  </div>

  <!-- REF -->
  <div id="refPage" class="page">
    <div class="section">
      <div class="ref-stats">
        <div class="ref-stat"><div class="ref-stat-val">12</div><div class="ref-stat-lbl">Рефералов</div></div>
        <div class="ref-stat"><div class="ref-stat-val">₽740</div><div class="ref-stat-lbl">Заработано</div></div>
      </div>
    </div>
    <div class="section">
      <div class="section-label">Ваша реферальная ссылка</div>
      <div style="padding:0 16px 8px;font-size:13px;color:var(--text2);line-height:1.5">
        Приглашайте друзей и получайте <strong style="color:var(--accent2)">20%</strong> от каждой их оплаты
      </div>
      <div class="ref-link-row">
        <div class="ref-link-txt">t.me/RocketVPNbot?start=ref_7821</div>
        <button class="copy-pill" onclick="showToast('✓ Ссылка скопирована')">Копировать</button>
      </div>
    </div>
    <div class="section">
      <div class="section-label">Как это работает</div>
      <div class="step-item"><div class="step-circle">1</div><div class="step-text"><strong>Поделитесь ссылкой</strong> с другом или в соцсетях</div></div>
      <div class="step-item"><div class="step-circle">2</div><div class="step-text">Друг регистрируется и <strong>оплачивает VPN</strong></div></div>
      <div class="step-item"><div class="step-circle">3</div><div class="step-text">Вы получаете <strong style="color:var(--accent2)">20% бонус</strong> автоматически на кошелёк</div></div>
    </div>
    <div class="spacer"></div>
  </div>

  <!-- FAQ -->
  <div id="faqPage" class="page">
    <div class="section">
      <div class="faq-item" onclick="toggleFaq(this)">
        <div class="faq-q"><span class="faq-q-text">Как подключить VPN?</span><div class="faq-chevron">▾</div></div>
        <div class="faq-ans"><div class="faq-ans-inner">Нажмите «Ваш ключ» — он скопируется. Установите v2rayNG (Android) или Streisand (iOS), импортируйте ключ. Готово — займёт 5 секунд.</div></div>
      </div>
      <div class="faq-item" onclick="toggleFaq(this)">
        <div class="faq-q"><span class="faq-q-text">Почему VPN работает в России?</span><div class="faq-chevron">▾</div></div>
        <div class="faq-ans"><div class="faq-ans-inner">Используем VLESS + Reality — протокол маскирует трафик под HTTPS крупных сайтов. DPI/ТСПУ Роскомнадзора не определяет и не блокирует его.</div></div>
      </div>
      <div class="faq-item" onclick="toggleFaq(this)">
        <div class="faq-q"><span class="faq-q-text">Сколько устройств можно подключить?</span><div class="faq-chevron">▾</div></div>
        <div class="faq-ans"><div class="faq-ans-inner">Базовый — 1 устройство, Стандарт — 3, Премиум — 5. Можно купить несколько ключей.</div></div>
      </div>
      <div class="faq-item" onclick="toggleFaq(this)">
        <div class="faq-q"><span class="faq-q-text">Как продлить подписку?</span><div class="faq-chevron">▾</div></div>
        <div class="faq-ans"><div class="faq-ans-inner">Пополните кошелёк, нажмите «Продлить» на ключе. Продление мгновенное, ключ не меняется.</div></div>
      </div>
      <div class="faq-item" onclick="toggleFaq(this)">
        <div class="faq-q"><span class="faq-q-text">Есть ли пробный период?</span><div class="faq-chevron">▾</div></div>
        <div class="faq-ans"><div class="faq-ans-inner">Да! Новым пользователям — 3 дня бесплатно автоматически при первом запуске. Карта не нужна.</div></div>
      </div>
      <div class="faq-item" onclick="toggleFaq(this)">
        <div class="faq-q"><span class="faq-q-text">Что делать если VPN не работает?</span><div class="faq-chevron">▾</div></div>
        <div class="faq-ans"><div class="faq-ans-inner">Проверьте срок действия ключа. Попробуйте переключить сервер. Если проблема осталась — напишите в поддержку, ответим в течение часа.</div></div>
      </div>
    </div>
    <div class="spacer"></div>
  </div>

</div>

<!-- BOTTOM NAV -->
<div class="bottom-nav">
  <button onclick="showPage('vpnPage',this)" class="nav-btn active">
    <div class="nav-icon-wrap">
      <svg width="26" height="26" viewBox="0 0 26 26" fill="none">
        <path d="M13 3C13 3 7 8 7 14a6 6 0 0 0 12 0c0-6-6-11-6-11z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
        <circle cx="13" cy="14" r="2.5" fill="currentColor" opacity="0.9"/>
        <path d="M10 21.5l-1.5 1.5M16 21.5l1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </div>
    VPN
  </button>
  <button onclick="showPage('walletPage',this)" class="nav-btn">
    <div class="nav-icon-wrap">
      <svg width="26" height="26" viewBox="0 0 26 26" fill="none">
        <rect x="3" y="7" width="20" height="13" rx="4" stroke="currentColor" stroke-width="1.6"/>
        <path d="M3 11h20" stroke="currentColor" stroke-width="1.6"/>
        <rect x="16" y="14" width="4" height="3" rx="1.5" fill="currentColor"/>
        <path d="M7 7V6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.6"/>
      </svg>
    </div>
    Кошелёк
  </button>
  <button onclick="showPage('refPage',this)" class="nav-btn">
    <div class="nav-icon-wrap">
      <svg width="26" height="26" viewBox="0 0 26 26" fill="none">
        <circle cx="10" cy="9" r="3.5" stroke="currentColor" stroke-width="1.6"/>
        <circle cx="18" cy="10.5" r="2.8" stroke="currentColor" stroke-width="1.5"/>
        <path d="M4 21c0-3.3 2.7-6 6-6s6 2.7 6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
        <path d="M18 15.5c1.9 0 3.5 1.6 3.5 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </div>
    Реф. прог.
  </button>
  <button onclick="showPage('faqPage',this)" class="nav-btn">
    <div class="nav-icon-wrap">
      <svg width="26" height="26" viewBox="0 0 26 26" fill="none">
        <circle cx="13" cy="13" r="10" stroke="currentColor" stroke-width="1.6"/>
        <path d="M10.5 10.5a2.5 2.5 0 0 1 5 0c0 1.5-2.5 2-2.5 3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
        <circle cx="13" cy="18" r="0.9" fill="currentColor"/>
      </svg>
    </div>
    FAQ
  </button>
</div>

<script>
function showPage(pageId, el) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(pageId).classList.add('active');
  el.classList.add('active');
  document.querySelector('.container').scrollTop = 0;
}

function toggleFaq(el) { el.classList.toggle('open'); }

function setAmt(val, btn) {
  document.getElementById('amtInput').value = val;
  document.querySelectorAll('.q-btn').forEach(b => b.classList.remove('sel'));
  btn.classList.add('sel');
  if (val === '') { document.getElementById('amtInput').value = ''; document.getElementById('amtInput').focus(); }
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2200);
}
</script>

</body>
</html>
"""





