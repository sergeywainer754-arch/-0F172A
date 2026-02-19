from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<title>ROCKET VPN</title>
<style>
:root {
  --bg:      #1a1a1a;
  --card:    #252525;
  --card2:   #2f2f2f;
  --accent:  #7B61FF;
  --accent2: #9B85FF;
  --asoft:   rgba(123,97,255,0.15);
  --aborder: rgba(123,97,255,0.3);
  --green:   #4CD964;
  --red:     #FF3B30;
  --orange:  #FF9500;
  --blue:    #2AABEE;
  --text:    #fff;
  --text2:   #999;
  --text3:   #4a4a4a;
  --div:     rgba(255,255,255,0.07);
  --r:       18px;
  --r2:      22px;
  --nav-h:   74px;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0; padding: 0;
  -webkit-tap-highlight-color: transparent;
}

/*
  КРИТИЧЕСКИ ВАЖНО:
  html и body ЗАБЛОКИРОВАНЫ — не скроллятся, не двигаются.
  Высота = 100% окна. overflow = hidden.
*/
html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--bg);
  font-family: 'Inter', -apple-system, sans-serif;
  color: var(--text);
  font-size: 15px;
  /* env() safe-area НЕ работает в Telegram iOS — используем JS */
}

/*
  АРХИТЕКТУРА LAYOUT:

  #root  ← занимает весь экран (height задаётся JS = viewportStableHeight)
    ├── #content-area  ← скроллящаяся зона (flex:1, overflow-y:auto)
    │     └── .page (контент вкладок)
    └── (навбар снаружи, position:fixed)
*/

#root {
  position: fixed;
  top: 0; left: 0; right: 0;
  /* height задаётся через JS */
  display: flex;
  flex-direction: column;
  background: var(--bg);
  overflow: hidden;
  isolation: isolate;
}

/*
  Отступ сверху = высота шапки Telegram.
  Используем CSS-переменные которые Telegram SDK выставляет сам.
  Это надёжнее чем JS — применяется мгновенно без прыжков.
*/
#top-inset {
  flex-shrink: 0;
  height: var(--tg-content-safe-area-inset-top, var(--tg-safe-area-inset-top, 0px));
  min-height: 0;
  background: var(--bg);
}

/*
  ЕДИНСТВЕННАЯ СКРОЛЛЯЩАЯСЯ ЗОНА.
  flex:1 = занимает всё место между отступом сверху и навбаром.
  overflow-y:auto = скроллится только она.
*/
#content-area {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
  touch-action: pan-y;
  /* Место под навбар */
  padding-bottom: calc(var(--nav-h) + env(safe-area-inset-bottom, 0px));
}

/* ── PAGES ── */
.page { display: none; }
.page.active { display: block; animation: fi .15s ease; }
@keyframes fi { from{opacity:0} to{opacity:1} }
.spacer { height: 10px; }

/* ── SECTION ── */
.sl {
  padding: 10px 16px 5px;
  font-size: 11px; font-weight: 600;
  color: var(--text2); text-transform: uppercase; letter-spacing: 0.7px;
}
.section { background: var(--card); border-radius: var(--r2); margin: 6px 12px; overflow: hidden; }
.section > .sl { padding: 13px 16px 5px; }

/* ── KEY CARD ── */
.kc { background: var(--card); border-radius: var(--r2); margin: 6px 12px; overflow: hidden; }
.kc-top { padding: 14px 16px; display: flex; align-items: center; gap: 12px; }
.ki {
  width: 46px; height: 46px; border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  font-size: 21px; flex-shrink: 0;
}
.ki.on  { background: rgba(76,217,100,0.13); }
.ki.off { background: rgba(255,59,48,0.11); }
.ki-info { flex: 1; min-width: 0; }
.ki-id { font-size: 16px; font-weight: 700; }
.ki-meta { font-size: 13px; color: var(--text2); display: flex; align-items: center; gap: 7px; margin-top: 4px; }
.badge { font-size: 11px; font-weight: 600; padding: 2px 9px; border-radius: 30px; }
.b-ok { background: rgba(76,217,100,0.15); color: var(--green); }
.b-no { background: rgba(255,59,48,0.12); color: var(--red); }
.b-vl { background: var(--asoft); color: var(--accent2); font-size: 10px; padding: 2px 8px; border-radius: 30px; font-weight: 600; }
.ki-st { display: flex; align-items: center; gap: 5px; font-size: 13px; margin-top: 5px; }
.dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
.dot.g { background: var(--green); }
.dot.r { background: var(--red); animation: bl 1.4s infinite; }
@keyframes bl { 0%,100%{opacity:1} 50%{opacity:.3} }
.kc-div { height: 1px; background: var(--div); margin: 0 16px; }
.kc-act { display: flex; padding: 10px 12px; gap: 8px; }
.kb {
  flex: 1; padding: 12px; border-radius: var(--r); border: none;
  font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 600;
  cursor: pointer; transition: opacity .15s;
}
.kb:active { opacity: .75; }
.kb-g { background: var(--card2); color: var(--text); }
.kb-a { background: var(--accent); color: #fff; }
.kb-del {
  display: block; background: rgba(255,59,48,.1); color: var(--red);
  border: none; margin: 0 12px 12px; width: calc(100% - 24px);
  padding: 12px; border-radius: var(--r);
  font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 600; cursor: pointer;
}
.main-btn {
  width: calc(100% - 24px); margin: 6px 12px 10px; padding: 15px;
  border-radius: var(--r2); border: none; background: var(--accent); color: #fff;
  font-family: 'Inter', sans-serif; font-size: 16px; font-weight: 600; cursor: pointer;
  display: flex; align-items: center; justify-content: center; gap: 8px;
}
.main-btn:active { opacity: .85; }

/* ── BANNER ── */
.banner {
  margin: 6px 12px;
  background: linear-gradient(135deg,#2d1f66,#1e1450);
  border-radius: var(--r2); padding: 20px 18px;
  border: 1px solid var(--aborder); position: relative; overflow: hidden;
}
.banner::after {
  content:'🚀'; position:absolute; right:14px; top:50%;
  transform:translateY(-50%); font-size:50px; opacity:.12; pointer-events:none;
}
.banner h3 { font-size:16px; font-weight:700; margin-bottom:5px; }
.banner p  { font-size:13px; color:rgba(255,255,255,.6); margin-bottom:14px; line-height:1.5; }

/* ── BALANCE ── */
.balance {
  margin: 0 12px;
  background: linear-gradient(135deg,#2d1f66,#1e1450);
  border-radius: var(--r2); padding: 22px 20px;
  border: 1px solid var(--aborder); position: relative; overflow: hidden;
}
.balance::after {
  content:'🚀'; position:absolute; right:14px; top:50%;
  transform:translateY(-50%); font-size:48px; opacity:.1; pointer-events:none;
}
.bal-lbl { font-size:13px; color:rgba(255,255,255,.5); margin-bottom:5px; }
.bal-val { font-size:38px; font-weight:700; line-height:1; }
.bal-val span { font-size:22px; color:var(--accent2); margin-right:3px; }

/* ── LIST ── */
.li { display:flex; align-items:center; padding:12px 16px; gap:13px; border-bottom:1px solid var(--div); }
.li:last-child { border-bottom:none; }
.li:active { background:rgba(255,255,255,.03); }
.li-ic { width:40px; height:40px; border-radius:13px; display:flex; align-items:center; justify-content:center; font-size:18px; flex-shrink:0; }
.li-ic.p { background:var(--asoft); }
.li-ic.b { background:rgba(42,171,238,.12); }
.li-ic.g { background:rgba(76,217,100,.12); }
.li-ic.o { background:rgba(255,149,0,.12); }
.li-cnt { flex:1; min-width:0; }
.li-t { font-size:15px; font-weight:500; }
.li-s { font-size:13px; color:var(--text2); margin-top:2px; }
.li-r { display:flex; align-items:center; }
.li-v { font-size:15px; font-weight:600; }
.li-v.inc { color:var(--green); }
.li-v.exp { color:var(--red); }
.chev { color:var(--text3); font-size:20px; }

/* ── AMOUNT ── */
.amt-wrap {
  margin:0 16px 12px; background:#1e1e1e; border-radius:var(--r);
  display:flex; align-items:center; padding:0 14px;
  border:1.5px solid transparent; transition:border-color .2s;
}
.amt-wrap:focus-within { border-color:var(--accent); }
.amt-sym { font-size:22px; font-weight:700; color:var(--accent2); margin-right:6px; }
.amt-inp {
  background:transparent; border:none; outline:none;
  font-family:'Inter',sans-serif; font-size:28px; font-weight:700;
  color:var(--text); width:100%; padding:12px 0;
}
.q-row { display:flex; gap:7px; padding:0 16px 14px; }
.q-btn {
  flex:1; padding:10px 4px; border-radius:12px;
  border:1px solid var(--div); background:#1e1e1e; color:var(--text2);
  font-family:'Inter',sans-serif; font-size:14px; font-weight:600; cursor:pointer;
}
.q-btn.sel { border-color:var(--accent); color:var(--accent2); background:var(--asoft); }

/* ── REF ── */
.ref-stats { display:grid; grid-template-columns:1fr 1fr; }
.ref-stat { padding:18px 16px; text-align:center; border-right:1px solid var(--div); }
.ref-stat:last-child { border-right:none; }
.rsv { font-size:26px; font-weight:700; color:var(--accent2); margin-bottom:4px; }
.rsl { font-size:12px; color:var(--text2); }
.ref-link {
  display:flex; align-items:center; margin:0 16px 14px; background:#1e1e1e;
  border-radius:var(--r); padding:10px 12px; gap:10px; border:1px solid var(--aborder);
}
.rl-txt { flex:1; font-size:13px; color:var(--accent2); overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.cp-btn {
  background:var(--accent); color:#fff; border:none; border-radius:30px; padding:7px 14px;
  font-family:'Inter',sans-serif; font-size:13px; font-weight:600; cursor:pointer;
}

/* ── STEPS ── */
.step { display:flex; align-items:flex-start; gap:13px; padding:12px 16px; border-bottom:1px solid var(--div); }
.step:last-child { border-bottom:none; }
.step-n {
  width:28px; height:28px; border-radius:50%;
  background:var(--asoft); border:1.5px solid var(--aborder);
  display:flex; align-items:center; justify-content:center;
  font-size:12px; font-weight:700; color:var(--accent2); flex-shrink:0; margin-top:2px;
}
.step-t { font-size:14px; color:var(--text2); line-height:1.6; padding-top:3px; }
.step-t strong { color:var(--text); }

/* ── FAQ ── */
.faq-i { border-bottom:1px solid var(--div); overflow:hidden; }
.faq-i:last-child { border-bottom:none; }
.faq-q { display:flex; justify-content:space-between; align-items:center; padding:13px 16px; cursor:pointer; gap:12px; }
.faq-qt { font-size:15px; font-weight:500; }
.faq-ch {
  width:22px; height:22px; border-radius:50%; background:var(--card2);
  display:flex; align-items:center; justify-content:center;
  color:var(--text2); font-size:10px; flex-shrink:0;
  transition:transform .25s, background .2s;
}
.faq-i.open .faq-ch { transform:rotate(180deg); background:var(--asoft); color:var(--accent2); }
.faq-a { max-height:0; overflow:hidden; transition:max-height .3s ease; }
.faq-i.open .faq-a { max-height:300px; }
.faq-ai { padding:0 16px 14px; font-size:14px; color:var(--text2); line-height:1.65; }

/* ════════════════════════════════════
   BOTTOM NAV — position:fixed
   Большой овал, плавает над контентом
   ════════════════════════════════════ */
#bottom-nav {
  position: fixed;
  bottom: 0; left: 0; right: 0;
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  /* Фон под овалом = основной фон страницы */
  background: var(--bg);
  padding: 8px 0 env(safe-area-inset-bottom, 8px);
}

/* Большой овальный контейнер */
.nav-pill {
  display: flex;
  align-items: center;
  width: min(310px, 86vw);
  height: 54px;
  background: #111;
  border-radius: 100px;
  padding: 4px;
  gap: 2px;
}

/* Кнопка — занимает своё место внутри овала */
.nav-btn {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  height: 46px;
  border-radius: 100px;
  border: none;
  background: transparent;
  color: var(--text3);
  font-family: 'Inter', sans-serif;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
  padding: 0 2px;
}

.nav-btn.active {
  background: #2a2a2a;
  color: var(--accent2);
}

.nav-btn svg { display: block; }

.nav-label {
  font-size: 9px;
  font-weight: 600;
  white-space: nowrap;
  letter-spacing: 0.1px;
}

/* ── TOAST ── */
.toast {
  position: fixed; bottom: 90px; left: 50%;
  transform: translateX(-50%) translateY(16px);
  background: #333; color: #fff;
  padding: 10px 22px; border-radius: 30px;
  font-size: 14px; font-weight: 500;
  z-index: 9999; opacity: 0;
  transition: all .28s cubic-bezier(.34,1.3,.64,1);
  pointer-events: none; white-space: nowrap;
}
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
</style>
</head>
<body>

<div id="toast" class="toast"></div>

<!-- ROOT: фиксированный корень, высота = viewport -->
<div id="root">

  <!-- TOP INSET: пространство под шапку Telegram -->
  <div id="top-inset"></div>

  <!-- CONTENT AREA: ЕДИНСТВЕННАЯ скроллящаяся зона -->
  <div id="content-area">

    <!-- VPN -->
    <div id="vpnPage" class="page active">
      <div class="sl">Мои ключи</div>
      <div class="kc">
        <div class="kc-top">
          <div class="ki on">🛡️</div>
          <div class="ki-info">
            <div style="display:flex;align-items:center;gap:7px;margin-bottom:5px">
              <span class="ki-id">#ROCKET-7821</span><span class="badge b-vl">VLESS</span>
            </div>
            <div class="ki-meta"><span class="badge b-ok">Оплачен</span><span>· 2 устройства</span></div>
            <div class="ki-st" style="color:var(--green)"><div class="dot g"></div><span>До 15 марта 2026</span></div>
          </div>
        </div>
        <div class="kc-div"></div>
        <div class="kc-act">
          <button class="kb kb-g" onclick="showToast('📋 Ключ скопирован')">📋 Ваш ключ</button>
          <button class="kb kb-a">🚀 Продлить</button>
        </div>
      </div>
      <div class="kc">
        <div class="kc-top">
          <div class="ki off">🔑</div>
          <div class="ki-info">
            <div style="display:flex;align-items:center;gap:7px;margin-bottom:5px">
              <span class="ki-id">#ROCKET-4103</span><span class="badge b-vl">VLESS</span>
            </div>
            <div class="ki-meta"><span class="badge b-no">Не оплачен</span><span>· 1 устройство</span></div>
            <div class="ki-st" style="color:var(--red)"><div class="dot r"></div><span>Закончился</span></div>
          </div>
        </div>
        <div class="kc-div"></div>
        <div class="kc-act">
          <button class="kb kb-g" onclick="showToast('📋 Ключ скопирован')">📋 Ваш ключ</button>
          <button class="kb kb-a">🚀 Продлить</button>
        </div>
        <button class="kb-del">🗑 Удалить ключ</button>
      </div>
      <div class="banner">
        <h3>Нужно больше VPN?</h3>
        <p>Приобретите неограниченное количество ключей VPN</p>
        <button class="main-btn" style="margin:0;width:100%;border-radius:18px">🚀 Купить VPN</button>
      </div>
      <div class="spacer"></div>
    </div>

    <!-- WALLET -->
    <div id="walletPage" class="page">
      <div class="balance">
        <div class="bal-lbl">Баланс кошелька</div>
        <div class="bal-val"><span>₽</span>126.25</div>
      </div>
      <div class="spacer"></div>
      <div class="section">
        <div class="sl">Способ пополнения</div>
        <div class="li">
          <div class="li-ic b">⚡</div>
          <div class="li-cnt"><div class="li-t">СБП</div><div class="li-s">Система быстрых платежей</div></div>
          <div class="li-r"><span class="chev">›</span></div>
        </div>
        <div class="li" style="border-bottom:none">
          <div class="li-ic p">💳</div>
          <div class="li-cnt"><div class="li-t">Банковская карта</div><div class="li-s">Visa, MasterCard, МИР</div></div>
          <div class="li-r"><span class="chev">›</span></div>
        </div>
      </div>
      <div class="section" style="padding-top:10px">
        <div class="sl" style="padding-top:4px">Сумма пополнения</div>
        <div class="amt-wrap">
          <div class="amt-sym">₽</div>
          <input class="amt-inp" type="number" value="150" id="amtInput">
        </div>
        <div class="q-row">
          <button class="q-btn sel" onclick="setAmt(150,this)">150</button>
          <button class="q-btn" onclick="setAmt(300,this)">300</button>
          <button class="q-btn" onclick="setAmt(500,this)">500</button>
          <button class="q-btn" onclick="setAmt(1000,this)">1000</button>
          <button class="q-btn" onclick="setAmt('',this)">Своя</button>
        </div>
      </div>
      <button class="main-btn" onclick="showToast('⚡ Переход к оплате...')">⚡ Перейти к пополнению</button>
      <div class="section">
        <div class="sl">История операций</div>
        <div class="li">
          <div class="li-ic g">💳</div>
          <div class="li-cnt"><div class="li-t">Пополнение</div><div class="li-s">19 фев 2026, 14:23</div></div>
          <div class="li-r"><span class="li-v inc">+500 ₽</span></div>
        </div>
        <div class="li">
          <div class="li-ic p">🚀</div>
          <div class="li-cnt"><div class="li-t">Оплата VPN · #ROCKET-7821</div><div class="li-s">18 фев 2026, 10:05</div></div>
          <div class="li-r"><span class="li-v exp">−299 ₽</span></div>
        </div>
        <div class="li" style="border-bottom:none">
          <div class="li-ic o">👥</div>
          <div class="li-cnt"><div class="li-t">Реферальный бонус</div><div class="li-s">15 фев 2026, 09:40</div></div>
          <div class="li-r"><span class="li-v inc">+74.25 ₽</span></div>
        </div>
      </div>
      <div class="spacer"></div>
    </div>

    <!-- REF -->
    <div id="refPage" class="page">
      <div class="section">
        <div class="ref-stats">
          <div class="ref-stat"><div class="rsv">12</div><div class="rsl">Рефералов</div></div>
          <div class="ref-stat"><div class="rsv">₽740</div><div class="rsl">Заработано</div></div>
        </div>
      </div>
      <div class="section">
        <div class="sl">Ваша реферальная ссылка</div>
        <div style="padding:0 16px 8px;font-size:13px;color:var(--text2);line-height:1.5">
          Приглашайте друзей и получайте <strong style="color:var(--accent2)">20%</strong> от каждой их оплаты
        </div>
        <div class="ref-link">
          <div class="rl-txt">t.me/RocketVPNbot?start=ref_7821</div>
          <button class="cp-btn" onclick="showToast('✓ Ссылка скопирована')">Копировать</button>
        </div>
      </div>
      <div class="section">
        <div class="sl">Как это работает</div>
        <div class="step"><div class="step-n">1</div><div class="step-t"><strong>Поделитесь ссылкой</strong> с другом или в соцсетях</div></div>
        <div class="step"><div class="step-n">2</div><div class="step-t">Друг регистрируется и <strong>оплачивает VPN</strong></div></div>
        <div class="step"><div class="step-n">3</div><div class="step-t">Вы получаете <strong style="color:var(--accent2)">20% бонус</strong> автоматически на кошелёк</div></div>
      </div>
      <div class="spacer"></div>
    </div>

    <!-- FAQ -->
    <div id="faqPage" class="page">
      <div class="section">
        <div class="faq-i" onclick="toggleFaq(this)">
          <div class="faq-q"><span class="faq-qt">Как подключить VPN?</span><div class="faq-ch">▾</div></div>
          <div class="faq-a"><div class="faq-ai">Нажмите «Ваш ключ» — он скопируется. Установите v2rayNG (Android) или Streisand (iOS), импортируйте ключ. Готово — займёт 5 секунд.</div></div>
        </div>
        <div class="faq-i" onclick="toggleFaq(this)">
          <div class="faq-q"><span class="faq-qt">Почему VPN работает в России?</span><div class="faq-ch">▾</div></div>
          <div class="faq-a"><div class="faq-ai">Используем VLESS + Reality — протокол маскирует трафик под HTTPS крупных сайтов.</div></div>
        </div>
        <div class="faq-i" onclick="toggleFaq(this)">
          <div class="faq-q"><span class="faq-qt">Сколько устройств можно подключить?</span><div class="faq-ch">▾</div></div>
          <div class="faq-a"><div class="faq-ai">Базовый — 1 устройство, Стандарт — 3, Премиум — 5.</div></div>
        </div>
        <div class="faq-i" onclick="toggleFaq(this)">
          <div class="faq-q"><span class="faq-qt">Как продлить подписку?</span><div class="faq-ch">▾</div></div>
          <div class="faq-a"><div class="faq-ai">Пополните кошелёк, нажмите «Продлить» на ключе. Продление мгновенное, ключ не меняется.</div></div>
        </div>
        <div class="faq-i" onclick="toggleFaq(this)">
          <div class="faq-q"><span class="faq-qt">Есть ли пробный период?</span><div class="faq-ch">▾</div></div>
          <div class="faq-a"><div class="faq-ai">Да! Новым пользователям — 3 дня бесплатно при первом запуске. Карта не нужна.</div></div>
        </div>
        <div class="faq-i" onclick="toggleFaq(this)">
          <div class="faq-q"><span class="faq-qt">Что делать если VPN не работает?</span><div class="faq-ch">▾</div></div>
          <div class="faq-a"><div class="faq-ai">Проверьте срок действия ключа. Попробуйте переключить сервер. Напишите в поддержку — ответим в течение часа.</div></div>
        </div>
      </div>
      <div class="spacer"></div>
    </div>

  </div><!-- /content-area -->
</div><!-- /root -->

<!-- BOTTOM NAV: ПОЛНОСТЬЮ вне #root, position:fixed -->
<nav id="bottom-nav">
  <div class="nav-pill">
    <button class="nav-btn active" onclick="showPage('vpnPage',this)">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
        <path d="M12 2.5C12 2.5 6.5 7.5 6.5 13a5.5 5.5 0 0 0 11 0c0-5.5-5.5-10.5-5.5-10.5z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
        <circle cx="12" cy="13" r="2" fill="currentColor"/>
        <path d="M9.8 18.5L8.5 20.5M14.2 18.5L15.5 20.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
      <span class="nav-label">VPN</span>
    </button>
    <button class="nav-btn" onclick="showPage('walletPage',this)">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
        <rect x="2.5" y="6.5" width="19" height="12" rx="3" stroke="currentColor" stroke-width="1.8"/>
        <path d="M2.5 10.5h19" stroke="currentColor" stroke-width="1.8"/>
        <rect x="15.5" y="13" width="3.5" height="2.5" rx="1.2" fill="currentColor"/>
        <path d="M6.5 6.5V5.5a2 2 0 0 1 2-2h7a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.8"/>
      </svg>
      <span class="nav-label">Кошелёк</span>
    </button>
    <button class="nav-btn" onclick="showPage('refPage',this)">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
        <circle cx="9" cy="8" r="3" stroke="currentColor" stroke-width="1.8"/>
        <circle cx="17" cy="9" r="2.3" stroke="currentColor" stroke-width="1.6"/>
        <path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
        <path d="M17 14.5c2 .3 3.5 1.8 3.5 3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
      </svg>
      <span class="nav-label">Реф. прог.</span>
    </button>
    <button class="nav-btn" onclick="showPage('faqPage',this)">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
        <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/>
        <path d="M9.5 9.5a2.5 2.5 0 0 1 5 0c0 1.8-2.5 2.2-2.5 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
        <circle cx="12" cy="17.5" r="0.9" fill="currentColor"/>
      </svg>
      <span class="nav-label">FAQ</span>
    </button>
  </div>
</nav>

<script>
const tg = window.Telegram.WebApp;
tg.ready();

// Мобильные — fullscreen, ПК — expand
if (/Android|iPhone|iPad|iPod/i.test(navigator.userAgent)) {
  if (tg.requestFullscreen) tg.requestFullscreen();
  else tg.expand();
} else {
  tg.expand();
}

tg.setHeaderColor('#1a1a1a');
tg.setBackgroundColor('#1a1a1a');

const root = document.getElementById('root');
const topInset = document.getElementById('top-inset');
const contentArea = document.getElementById('content-area');

function applyLayout() {
  // Высота = стабильная высота viewport (не прыгает при drag)
  const h = tg.viewportStableHeight || tg.viewportHeight || window.innerHeight;
  root.style.height = h + 'px';

  // Отступ сверху = сумма двух inset:
  // 1. safeAreaInset.top        — notch/статусбар (нужен в fullscreen)
  // 2. contentSafeAreaInset.top — высота шапки Telegram (Закрыть / три точки)
  // env() не работает в Telegram iOS — только JS
  const sysTop     = (tg.safeAreaInset        && tg.safeAreaInset.top)        || 0;
  const contentTop = (tg.contentSafeAreaInset  && tg.contentSafeAreaInset.top) || 0;
  topInset.style.height = (sysTop + contentTop) + 'px';
}

// Вызываем при загрузке и на все события Telegram
applyLayout();
tg.onEvent('viewportChanged',        applyLayout);
tg.onEvent('safeAreaChanged',        applyLayout);
tg.onEvent('contentSafeAreaChanged', applyLayout);

function showPage(id, el) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  el.classList.add('active');
  contentArea.scrollTop = 0;
}

function toggleFaq(el) { el.classList.toggle('open'); }

function setAmt(val, btn) {
  document.querySelectorAll('.q-btn').forEach(b => b.classList.remove('sel'));
  btn.classList.add('sel');
  const inp = document.getElementById('amtInput');
  inp.value = val;
  if (!val) inp.focus();
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2200);
}
</script>
</body>
</html>"""
