from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">

<script src="https://telegram.org/js/telegram-web-app.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded" rel="stylesheet" />

<script>
const tg = window.Telegram.WebApp;

tg.ready();
tg.expand();

tg.setHeaderColor("#0f172a");
tg.setBackgroundColor("#0f172a");

function updateHeight() {
    document.documentElement.style.height = tg.viewportHeight + "px";
    document.body.style.height = tg.viewportHeight + "px";
}
updateHeight();
tg.onEvent('viewportChanged', updateHeight);
</script>

<style>
* { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  background: radial-gradient(circle at top left, #1e293b, #0f172a 60%, #020617);
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
  color: white;
  overflow-x: hidden;
}

.container {
  max-width: 500px;
  margin: 0 auto;
  padding-bottom: 110px;
}

.header {
  padding: 20px;
  font-size: 22px;
  font-weight: 700;
}

.page { display: none; padding: 20px; }
.page.active { display: block; }

.key-card {
  background: linear-gradient(145deg, #1e293b, #2563eb);
  padding: 18px;
  border-radius: 20px;
  margin-bottom: 20px;
  box-shadow: 0 15px 35px rgba(0,0,0,0.5);
}

.key-header {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  opacity: 0.8;
}

.key-id { font-size: 20px; font-weight: 700; margin: 10px 0; }
.status-expired { color: #ff4d4d; font-weight: 600; }

.key-buttons { display: flex; gap: 10px; margin-top: 12px; }

button { border: none; cursor: pointer; }

.btn-outline {
  flex: 1;
  padding: 10px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,0.4);
  background: transparent;
  color: white;
}

.btn-light {
  flex: 1;
  padding: 10px;
  border-radius: 12px;
  background: #e5e7eb;
  color: #111;
  font-weight: 600;
}

.btn-danger {
  margin-top: 12px;
  padding: 10px;
  border-radius: 14px;
  border: 1px solid #ff4d4d;
  background: transparent;
  color: #ff4d4d;
  width: 100%;
}

.button {
  margin-top: 15px;
  padding: 14px;
  border-radius: 14px;
  text-align: center;
  background: linear-gradient(135deg,#2563eb,#7c3aed);
  font-weight: 600;
}

.card {
  background: rgba(255,255,255,0.06);
  backdrop-filter: blur(20px);
  border-radius: 22px;
  padding: 20px;
  margin-bottom: 15px;
}

.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(15,23,42,0.9);
  backdrop-filter: blur(20px);
  display: flex;
  justify-content: space-around;
  padding: 16px 0;
  border-top: 1px solid rgba(255,255,255,0.08);
}

.nav-btn {
  background: none;
  border: none;
  color: #777;
  font-size: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
}

.nav-btn span { font-size: 22px; }
.nav-btn.active { color: #7c3aed; }
</style>
</head>

<body>

<div class="container">
<div class="header">🚀 MyVPN</div>

<!-- VPN -->
<div id="vpnPage" class="page active">
<h2>Мои ключи</h2>

<div class="key-card">
<div class="key-header">
<div>Не оплачен</div>
<div>VLESS</div>
</div>

<div class="key-id">#AID-41452</div>
<div>1 устройство</div>
<div class="status-expired">● Закончился</div>

<div class="key-buttons">
<button class="btn-outline">Ваш ключ</button>
<button class="btn-light">Продлить</button>
</div>

<button class="btn-danger">Удалить</button>
</div>

<div class="card">
<h3>Нужно больше VPN?</h3>
<p>Вы можете приобрести неограниченное количество ключей VPN</p>
<div class="button">Купить VPN</div>
</div>
</div>

<!-- WALLET -->
<div id="walletPage" class="page">
<div class="card">
<h3><span class="material-symbols-rounded">payments</span> Баланс</h3>
<div style="font-size:32px;font-weight:bold;margin:10px 0;">₽150.00</div>
<div class="button">Пополнить</div>
</div>

<div class="card">
<h3>📜 История операций</h3>
<p>18 янв — +₽150</p>
<p>10 янв — +₽300</p>
</div>
</div>

<!-- REF -->
<div id="refPage" class="page">
<div class="card">
<h3><span class="material-symbols-rounded">group</span> Реф.прог.</h3>
<p>Твоя ссылка:</p>
<div style="margin:10px 0;padding:10px;background:rgba(255,255,255,0.05);border-radius:12px;">
https://t.me/yourbot?start=1022670429
</div>
<div class="button">Скопировать</div>
</div>
</div>

<!-- FAQ -->
<div id="faqPage" class="page">
<div class="card">
<h3><span class="material-symbols-rounded">help</span> FAQ</h3>
<p>Инструкции по подключению VPN</p>
</div>
</div>

</div>

<div class="bottom-nav">
<button onclick="showPage('vpnPage', this)" class="nav-btn active">
<span class="material-symbols-rounded">vpn_lock</span>
VPN
</button>

<button onclick="showPage('walletPage', this)" class="nav-btn">
<span class="material-symbols-rounded">account_balance_wallet</span>
Кошелек
</button>

<button onclick="showPage('refPage', this)" class="nav-btn">
<span class="material-symbols-rounded">diversity_3</span>
Реф.прог.
</button>

<button onclick="showPage('faqPage', this)" class="nav-btn">
<span class="material-symbols-rounded">info</span>
FAQ
</button>
</div>

<script>
function showPage(pageId, el) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));

  document.getElementById(pageId).classList.add('active');
  el.classList.add('active');
}
</script>

</body>
</html>
"""