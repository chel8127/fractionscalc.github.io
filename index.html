<!DOCTYPE html>

<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fraction Calculator</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@300;400;500&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:#0d0f14;--surface:#13161e;--surface2:#1a1f2b;--surface3:#222838;
    --border:#2a3045;--border2:#3a4560;
    --accent:#6c8fff;--accent2:#a78bfa;
    --text:#e8eaf0;--text2:#9aa0b8;--text3:#5a6280;
    --success:#4ade80;--err:#f87171;
    --glow:rgba(108,143,255,0.18);
    --radius:14px;--radius-sm:8px;
  }
  .theme-violet{--accent:#a78bfa;--accent2:#e879f9;--glow:rgba(167,139,250,0.18);}
  .theme-emerald{--accent:#34d399;--accent2:#6ee7b7;--glow:rgba(52,211,153,0.18);--bg:#0a0f0d;--surface:#0f1610;--surface2:#162018;--surface3:#1e2d22;--border:#243628;--border2:#2e4a34;}
  .theme-amber{--accent:#fbbf24;--accent2:#f97316;--glow:rgba(251,191,36,0.15);--bg:#0f0e09;--surface:#18160a;--surface2:#231f0e;--surface3:#2e2912;--border:#3d3614;--border2:#524817;}
  .theme-rose{--accent:#fb7185;--accent2:#f43f5e;--glow:rgba(251,113,133,0.15);--bg:#100a0d;--surface:#180f13;--surface2:#22141a;--surface3:#2d1b22;--border:#3d2030;--border2:#52293f;}
  .theme-cyan{--accent:#22d3ee;--accent2:#67e8f9;--glow:rgba(34,211,238,0.15);--bg:#060f12;--surface:#0b1820;--surface2:#102030;--surface3:#162b3e;--border:#1c3448;--border2:#244460;}

*{margin:0;padding:0;box-sizing:border-box;}
body{background:var(–bg);color:var(–text);font-family:‘Syne’,sans-serif;min-height:100vh;overflow-x:hidden;transition:background .4s,color .4s;}
body::before{content:’’;position:fixed;inset:0;background-image:linear-gradient(var(–border) 1px,transparent 1px),linear-gradient(90deg,var(–border) 1px,transparent 1px);background-size:60px 60px;opacity:.22;pointer-events:none;z-index:0;}
body::after{content:’’;position:fixed;top:-40%;left:50%;transform:translateX(-50%);width:900px;height:600px;background:radial-gradient(ellipse,var(–glow) 0%,transparent 70%);pointer-events:none;z-index:0;transition:background .4s;}

.container{max-width:980px;margin:0 auto;padding:28px 20px 80px;position:relative;z-index:1;}

header{display:flex;align-items:center;justify-content:space-between;margin-bottom:32px;flex-wrap:wrap;gap:14px;}
.logo{display:flex;flex-direction:column;line-height:1;}
.logo-title{font-family:‘DM Serif Display’,serif;font-size:2rem;letter-spacing:-.02em;background:linear-gradient(135deg,var(–text) 40%,var(–accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.logo-sub{font-family:‘DM Mono’,monospace;font-size:.68rem;color:var(–text3);letter-spacing:.18em;text-transform:uppercase;margin-top:4px;}
.header-right{display:flex;align-items:center;gap:14px;flex-wrap:wrap;}

.lang-row{display:flex;gap:4px;}
.lang-btn{cursor:pointer;border:1px solid var(–border);background:var(–surface2);color:var(–text3);font-family:‘DM Mono’,monospace;font-size:.7rem;letter-spacing:.1em;padding:5px 10px;border-radius:6px;transition:all .18s;text-transform:uppercase;}
.lang-btn:hover{border-color:var(–accent);color:var(–accent);}
.lang-btn.active{background:var(–accent);color:var(–bg);border-color:var(–accent);font-weight:700;}

.theme-row{display:flex;gap:7px;align-items:center;}
.theme-label{font-size:.68rem;color:var(–text3);font-family:‘DM Mono’,monospace;letter-spacing:.1em;}
.theme-dot{width:21px;height:21px;border-radius:50%;cursor:pointer;border:2px solid transparent;transition:transform .2s,border-color .2s;}
.theme-dot:hover{transform:scale(1.2);}
.theme-dot.active{border-color:var(–text);}
.theme-dot[data-theme=“default”]{background:linear-gradient(135deg,#6c8fff,#a78bfa);}
.theme-dot[data-theme=“violet”]{background:linear-gradient(135deg,#a78bfa,#e879f9);}
.theme-dot[data-theme=“emerald”]{background:linear-gradient(135deg,#34d399,#6ee7b7);}
.theme-dot[data-theme=“amber”]{background:linear-gradient(135deg,#fbbf24,#f97316);}
.theme-dot[data-theme=“rose”]{background:linear-gradient(135deg,#fb7185,#f43f5e);}
.theme-dot[data-theme=“cyan”]{background:linear-gradient(135deg,#22d3ee,#67e8f9);}

.card{background:var(–surface);border:1px solid var(–border);border-radius:var(–radius);overflow:hidden;margin-bottom:18px;transition:background .4s,border-color .4s;}
.input-section{padding:24px 26px;border-bottom:1px solid var(–border);}
.section-title{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;color:var(–text3);font-family:‘DM Mono’,monospace;margin-bottom:14px;}

.expression-display{background:var(–bg);border:1px solid var(–border2);border-radius:var(–radius);padding:18px 22px;min-height:76px;margin-bottom:16px;display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-family:‘DM Mono’,monospace;position:relative;overflow:hidden;}
.expression-display::before{content:’’;position:absolute;inset:0;background:linear-gradient(90deg,var(–glow) 0%,transparent 60%);pointer-events:none;}
@keyframes fadeSlide{from{opacity:0;transform:translateY(-5px)}to{opacity:1;transform:translateY(0)}}
.expr-token{display:inline-flex;align-items:center;gap:4px;animation:fadeSlide .18s ease;}
.token-whole,.token-decimal{font-size:1.9rem;color:var(–text);line-height:1;}
.token-frac{display:inline-flex;flex-direction:column;align-items:center;gap:1px;vertical-align:middle;}
.frac-num,.frac-den{font-size:.95rem;color:var(–text);line-height:1.1;}
.frac-line{width:100%;height:1.5px;background:var(–accent);border-radius:2px;min-width:20px;}
.token-mixed{display:inline-flex;align-items:center;gap:5px;}
.token-op{font-size:1.5rem;color:var(–accent);font-weight:700;padding:0 3px;line-height:1;}
.expr-placeholder{color:var(–text3);font-size:.82rem;font-family:‘DM Mono’,monospace;}

.input-tabs{display:flex;gap:6px;margin-bottom:14px;flex-wrap:wrap;}
.tab-btn{cursor:pointer;border:1px solid var(–border);background:var(–surface2);color:var(–text3);font-family:‘Syne’,sans-serif;font-size:.75rem;font-weight:700;letter-spacing:.05em;padding:7px 14px;border-radius:var(–radius-sm);transition:all .18s;}
.tab-btn:hover{border-color:var(–accent2);color:var(–accent2);}
.tab-btn.active{background:var(–surface3);border-color:var(–accent);color:var(–accent);}

.keypad-area{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.keypad-panel{background:var(–surface2);border:1px solid var(–border);border-radius:var(–radius);padding:14px;transition:background .4s;}
.panel-title{font-size:.62rem;letter-spacing:.18em;text-transform:uppercase;color:var(–text3);font-family:‘DM Mono’,monospace;margin-bottom:10px;}

.tab-pane{display:none;}
.tab-pane.active{display:block;}
.entry-builder{display:flex;flex-direction:column;gap:9px;}
.entry-inputs{display:grid;gap:7px;}
.cols-1{grid-template-columns:1fr;}
.cols-3{grid-template-columns:1fr 1fr 1fr;}
.entry-field-wrap{display:flex;flex-direction:column;gap:3px;}
.field-label{font-size:.58rem;color:var(–text3);font-family:‘DM Mono’,monospace;letter-spacing:.1em;text-transform:uppercase;}
.entry-field{background:var(–surface3);border:1px solid var(–border);border-radius:var(–radius-sm);color:var(–text);font-family:‘DM Mono’,monospace;font-size:1.05rem;padding:8px 10px;text-align:center;width:100%;outline:none;transition:border-color .2s,box-shadow .2s;}
.entry-field:focus{border-color:var(–accent);box-shadow:0 0 0 3px var(–glow);}
.entry-field::placeholder{color:var(–text3);}
.frac-divider{display:flex;align-items:flex-end;justify-content:center;padding-bottom:8px;font-size:1.5rem;color:var(–accent);font-family:‘DM Serif Display’,serif;}

.btn{cursor:pointer;border:none;border-radius:var(–radius-sm);font-family:‘Syne’,sans-serif;font-weight:700;font-size:.8rem;letter-spacing:.05em;transition:all .18s;display:flex;align-items:center;justify-content:center;gap:5px;}
.btn-add{background:var(–surface3);color:var(–text);padding:9px 12px;border:1px solid var(–border2);flex:1;}
.btn-add:hover{background:var(–border2);border-color:var(–accent);color:var(–accent);}
.btn-sm{padding:6px 10px;font-size:.72rem;background:var(–surface3);color:var(–text2);border:1px solid var(–border);border-radius:var(–radius-sm);}
.btn-sm:hover{border-color:var(–accent2);color:var(–accent2);}
.btn-sm.danger:hover{border-color:var(–err);color:var(–err);}
.entry-row{display:flex;gap:7px;flex-wrap:wrap;}

.ops-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:7px;margin-bottom:9px;}
.btn-op{padding:10px 6px;font-size:1.25rem;background:var(–surface3);color:var(–accent);border:1px solid var(–border);border-radius:var(–radius-sm);cursor:pointer;transition:all .18s;font-family:‘Syne’,sans-serif;font-weight:700;}
.btn-op:hover{background:var(–glow);border-color:var(–accent);transform:scale(1.06);}
.btn-op.active-op{background:var(–accent);color:var(–bg);border-color:var(–accent);}
.control-row{display:flex;gap:7px;}
.btn-primary{flex:1;background:var(–accent);color:var(–bg);padding:11px 14px;font-size:.83rem;border-radius:var(–radius-sm);box-shadow:0 4px 18px var(–glow);cursor:pointer;border:none;font-family:‘Syne’,sans-serif;font-weight:700;transition:all .18s;}
.btn-primary:hover{opacity:.88;transform:translateY(-1px);box-shadow:0 6px 26px var(–glow);}
.btn-secondary{background:var(–surface3);color:var(–text2);padding:11px 13px;border:1px solid var(–border);cursor:pointer;font-family:‘Syne’,sans-serif;font-weight:700;font-size:.8rem;border-radius:var(–radius-sm);transition:all .18s;}
.btn-secondary:hover{border-color:var(–err);color:var(–err);}

.result-section{padding:24px 26px;}
.result-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;flex-wrap:wrap;gap:8px;}
.big-result{display:flex;align-items:center;justify-content:center;gap:18px;padding:22px;background:var(–bg);border:1px solid var(–border2);border-radius:var(–radius);margin-bottom:18px;flex-wrap:wrap;}
.big-frac{display:flex;flex-direction:column;align-items:center;gap:3px;}
.big-frac-num,.big-frac-den{font-family:‘DM Serif Display’,serif;font-size:2.6rem;color:var(–text);line-height:1;}
.big-frac-line{width:100%;height:3px;background:linear-gradient(90deg,var(–accent),var(–accent2));border-radius:3px;min-width:55px;}
.big-whole{font-family:‘DM Serif Display’,serif;font-size:2.8rem;color:var(–text);line-height:1;}
.result-sep{color:var(–border2);font-size:1.8rem;}
.result-decimal{font-family:‘DM Mono’,monospace;font-size:1.05rem;color:var(–accent2);background:var(–surface3);padding:5px 13px;border-radius:var(–radius-sm);border:1px solid var(–border);}

.methods-grid{display:grid;gap:10px;}
@keyframes methodIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.method-card{background:var(–surface2);border:1px solid var(–border);border-radius:var(–radius);overflow:hidden;animation:methodIn .3s ease both;transition:background .4s,border-color .2s;}
.method-card:hover{border-color:var(–border2);}
.method-card:nth-child(1){animation-delay:.04s}.method-card:nth-child(2){animation-delay:.08s}.method-card:nth-child(3){animation-delay:.12s}.method-card:nth-child(4){animation-delay:.16s}.method-card:nth-child(5){animation-delay:.2s}
.method-header{display:flex;align-items:center;gap:9px;padding:13px 16px;cursor:pointer;user-select:none;border-bottom:1px solid transparent;transition:border-color .2s;}
.method-card.open .method-header{border-bottom-color:var(–border);}
.method-num{width:25px;height:25px;border-radius:6px;background:var(–glow);border:1px solid var(–accent);display:flex;align-items:center;justify-content:center;font-family:‘DM Mono’,monospace;font-size:.66rem;color:var(–accent);flex-shrink:0;}
.method-name{flex:1;font-size:.8rem;font-weight:700;letter-spacing:.04em;color:var(–text2);}
.chevron{color:var(–text3);font-size:.65rem;transition:transform .25s;flex-shrink:0;}
.method-card.open .chevron{transform:rotate(180deg);}
.method-body{display:none;padding:14px 16px;}
.method-card.open .method-body{display:block;}
.step-list{display:flex;flex-direction:column;gap:9px;}
.step{display:flex;gap:10px;align-items:flex-start;}
.step-num{width:21px;height:21px;border-radius:50%;background:var(–surface3);border:1px solid var(–border2);display:flex;align-items:center;justify-content:center;font-family:‘DM Mono’,monospace;font-size:.62rem;color:var(–text3);flex-shrink:0;margin-top:1px;}
.step-content{flex:1;font-size:.8rem;color:var(–text2);line-height:1.65;}
.step-content .formula{display:inline-flex;align-items:center;gap:5px;background:var(–surface3);border-radius:5px;padding:3px 9px;margin:3px 0;font-family:‘DM Mono’,monospace;font-size:.76rem;color:var(–text);border:1px solid var(–border);}
.inline-frac{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;gap:1px;margin:0 2px;}
.inline-frac .fn{font-size:.7em;line-height:1.1;}
.inline-frac .fl{width:100%;height:1px;background:var(–accent);min-width:14px;}
.inline-frac .fd{font-size:.7em;line-height:1.1;}
.highlight{color:var(–accent);font-weight:700;}
.tag{display:inline-block;padding:2px 7px;border-radius:4px;font-size:.62rem;font-family:‘DM Mono’,monospace;letter-spacing:.08em;text-transform:uppercase;}
.tag-best{background:rgba(74,222,128,.12);color:var(–success);border:1px solid rgba(74,222,128,.3);}

.empty-state{text-align:center;padding:36px 20px;color:var(–text3);}
.empty-icon{font-size:2.4rem;margin-bottom:10px;opacity:.45;}
.empty-text{font-family:‘DM Mono’,monospace;font-size:.78rem;line-height:1.8;}
.error-box{background:rgba(248,113,113,.08);border:1px solid rgba(248,113,113,.3);border-radius:var(–radius-sm);padding:12px 16px;color:var(–err);font-family:‘DM Mono’,monospace;font-size:.8rem;display:flex;align-items:center;gap:7px;}

@media(max-width:600px){.keypad-area{grid-template-columns:1fr;}.logo-title{font-size:1.5rem;}.big-frac-num,.big-frac-den,.big-whole{font-size:1.9rem;}.input-tabs{gap:4px;}.tab-btn{padding:5px 9px;font-size:.68rem;}}
@keyframes pulse-glow{0%{box-shadow:0 0 0 0 var(–glow)}70%{box-shadow:0 0 0 10px transparent}100%{box-shadow:0 0 0 0 transparent}}
.pulse{animation:pulse-glow .5s ease;}
</style>

</head>
<body>
<div class="container">
  <header>
    <div class="logo">
      <span class="logo-title" data-i18n="title">Дроби</span>
      <span class="logo-sub" data-i18n="subtitle">Калькулятор · до 10 методов решения</span>
    </div>
    <div class="header-right">
      <div class="lang-row">
        <button class="lang-btn active" onclick="setLang('ru',this)">RU</button>
        <button class="lang-btn" onclick="setLang('uk',this)">UK</button>
        <button class="lang-btn" onclick="setLang('en',this)">EN</button>
      </div>
      <div class="theme-row">
        <span class="theme-label" data-i18n="theme">тема</span>
        <div class="theme-dot active" data-theme="default" onclick="setTheme('default',this)"></div>
        <div class="theme-dot" data-theme="violet"  onclick="setTheme('violet',this)"></div>
        <div class="theme-dot" data-theme="emerald" onclick="setTheme('emerald',this)"></div>
        <div class="theme-dot" data-theme="amber"   onclick="setTheme('amber',this)"></div>
        <div class="theme-dot" data-theme="rose"    onclick="setTheme('rose',this)"></div>
        <div class="theme-dot" data-theme="cyan"    onclick="setTheme('cyan',this)"></div>
      </div>
    </div>
  </header>

  <div class="card">
    <div class="input-section">
      <div class="section-title" data-i18n="expression">выражение</div>
      <div class="expression-display" id="exprDisplay">
        <span class="expr-placeholder" data-i18n="placeholder">Введите числа и выберите операцию…</span>
      </div>

```
  <div class="input-tabs">
    <button class="tab-btn active" onclick="switchTab('int',this)"  data-i18n="tabInt">Целое</button>
    <button class="tab-btn"        onclick="switchTab('dec',this)"  data-i18n="tabDec">Десятичное</button>
    <button class="tab-btn"        onclick="switchTab('frac',this)" data-i18n="tabFrac">Дробь</button>
    <button class="tab-btn"        onclick="switchTab('mixed',this)" data-i18n="tabMixed">Смешанное</button>
  </div>

  <div class="keypad-area">
    <div class="keypad-panel">
      <div class="panel-title" data-i18n="panelInput">Ввод числа</div>

      <!-- INTEGER -->
      <div class="tab-pane active" id="pane-int">
        <div class="entry-builder">
          <div class="entry-inputs cols-1">
            <div class="entry-field-wrap">
              <span class="field-label" data-i18n="integer">Число</span>
              <input class="entry-field" id="iInt" type="number" placeholder="42" step="1">
            </div>
          </div>
          <div class="entry-row">
            <button class="btn btn-add" onclick="addFromTab()" data-i18n="add">＋ Добавить</button>
            <button class="btn btn-sm danger" onclick="clearEntry()" data-i18n="clear">✕</button>
          </div>
        </div>
      </div>

      <!-- DECIMAL -->
      <div class="tab-pane" id="pane-dec">
        <div class="entry-builder">
          <div class="entry-inputs cols-1">
            <div class="entry-field-wrap">
              <span class="field-label" data-i18n="decimal">Десятичное (напр. 3.14)</span>
              <input class="entry-field" id="iDec" type="number" placeholder="3.14" step="any">
            </div>
          </div>
          <div class="entry-row">
            <button class="btn btn-add" onclick="addFromTab()" data-i18n="add">＋ Добавить</button>
            <button class="btn btn-sm danger" onclick="clearEntry()" data-i18n="clear">✕</button>
          </div>
        </div>
      </div>

      <!-- FRACTION -->
      <div class="tab-pane" id="pane-frac">
        <div class="entry-builder">
          <div class="entry-inputs cols-3">
            <div class="entry-field-wrap">
              <span class="field-label" data-i18n="numerator">Числитель</span>
              <input class="entry-field" id="fNum" type="number" placeholder="3">
            </div>
            <div class="frac-divider">/</div>
            <div class="entry-field-wrap">
              <span class="field-label" data-i18n="denominator">Знаменатель</span>
              <input class="entry-field" id="fDen" type="number" placeholder="4" min="1">
            </div>
          </div>
          <div class="entry-row">
            <button class="btn btn-add" onclick="addFromTab()" data-i18n="add">＋ Добавить</button>
            <button class="btn btn-sm" onclick="toggleSign()" data-i18n="sign">± знак</button>
            <button class="btn btn-sm danger" onclick="clearEntry()" data-i18n="clear">✕</button>
          </div>
        </div>
      </div>

      <!-- MIXED -->
      <div class="tab-pane" id="pane-mixed">
        <div class="entry-builder">
          <div class="entry-inputs cols-3">
            <div class="entry-field-wrap">
              <span class="field-label" data-i18n="wholeP">Целая</span>
              <input class="entry-field" id="mWhole" type="number" placeholder="1" min="0">
            </div>
            <div class="entry-field-wrap">
              <span class="field-label" data-i18n="numerator">Числит.</span>
              <input class="entry-field" id="mNum" type="number" placeholder="2" min="0">
            </div>
            <div class="entry-field-wrap">
              <span class="field-label" data-i18n="denominator">Знамен.</span>
              <input class="entry-field" id="mDen" type="number" placeholder="3" min="1">
            </div>
          </div>
          <div class="entry-row">
            <button class="btn btn-add" onclick="addFromTab()" data-i18n="add">＋ Добавить</button>
            <button class="btn btn-sm" onclick="toggleSign()" data-i18n="sign">± знак</button>
            <button class="btn btn-sm danger" onclick="clearEntry()" data-i18n="clear">✕</button>
          </div>
        </div>
      </div>
    </div>

    <div class="keypad-panel">
      <div class="panel-title" data-i18n="panelOp">Операция и управление</div>
      <div class="ops-grid">
        <button class="btn-op" data-op="+" onclick="selectOp('+',this)">＋</button>
        <button class="btn-op" data-op="-" onclick="selectOp('-',this)">－</button>
        <button class="btn-op" data-op="*" onclick="selectOp('*',this)">×</button>
        <button class="btn-op" data-op="/" onclick="selectOp('/',this)">÷</button>
      </div>
      <div class="control-row">
        <button class="btn-primary" onclick="calculate()" data-i18n="solve">= Решить</button>
        <button class="btn-secondary" onclick="removeLastToken()">⌫</button>
        <button class="btn-secondary" onclick="clearAll()">AC</button>
      </div>
    </div>
  </div>
</div>

<div class="result-section">
  <div class="result-header">
    <div class="section-title" style="margin:0" data-i18n="methods">методы решения</div>
    <div id="methodCount" style="font-size:.68rem;color:var(--text3);font-family:'DM Mono',monospace;"></div>
  </div>
  <div id="resultArea">
    <div class="empty-state">
      <div class="empty-icon">⅗</div>
      <div class="empty-text" data-i18n="emptyHint">Введите два числа, выберите операцию<br>и нажмите <strong style="color:var(--accent)">= Решить</strong></div>
    </div>
  </div>
</div>
```

  </div>
</div>

<script>
// ── I18N ──────────────────────────────────────────────────────────────────────
const I18N = {
  ru:{
    title:'Дроби',subtitle:'Калькулятор · до 10 методов решения',
    theme:'тема',expression:'выражение',
    placeholder:'Введите числа и выберите операцию…',
    tabInt:'Целое',tabDec:'Десятичное',tabFrac:'Дробь',tabMixed:'Смешанное',
    panelInput:'Ввод числа',panelOp:'Операция и управление',
    integer:'Число',decimal:'Десятичное (напр. 3,14)',
    numerator:'Числитель',denominator:'Знаменатель',
    wholeP:'Целая',sign:'± знак',add:'＋ Добавить',clear:'✕',solve:'= Решить',
    methods:'методы решения',
    emptyHint:'Введите два числа, выберите операцию<br>и нажмите <strong style="color:var(--accent)">= Решить</strong>',
    of:'из',methodsOf:'методов',best:'Лучший',
    mStd:'Стандартный (НОК знаменателей)',mStdSame:'Стандартный (одинак. знаменатели)',
    mMul:'Умножение дробей',mDiv:'Деление дробей',
    mMixed:'Через смешанные числа',mGcdLcm:'Метод НОД/НОК (упрощение)',
    mNumLine:'Числовая прямая (десятичные)',mCross:'Перекрёстное умножение',
    mPrime:'Разложение на простые',mEuclid:'Алгоритм Евклида',
    mDirect:'Прямая формула',mVisual:'Визуальная схема',mVerify:'Проверка обратным действием',
    opAdd:'сложение',opSub:'вычитание',opMul:'умножение',opDiv:'деление',
    errTwo:'Нужно минимум два числа!',errOp:'Выберите операцию (+ − × ÷)!',
    errZeroDen:'Знаменатель не может быть 0!',errZeroNum:'Введите число!',
    errDivZero:'Деление на ноль!',errCalc:'Ошибка вычисления',
    sGcd:'НОД',sLcm:'НОК',sReduce:'Сокращаем',sResult:'Результат',
    sApply:'Применяем формулу',sFinalAns:'Конечный ответ',
    sToDec:'Переводим в десятичные',sToFrac:'Переводим обратно в дробь',
    sFlip:'Переворачиваем вторую дробь',sMulInstead:'Заменяем деление на умножение',
    sNums:'Числители',sDens:'Знаменатели',
    sEqDen:'Знаменатели одинаковы',sAddDir:'складываем числители напрямую',
    sDenStays:'Знаменатель остаётся',sFindLcm:'Находим НОК',sBring:'Приводим дроби',
    sConvMix:'Переводим в смешанные',sWorkSep:'Работаем с целыми и дробными частями отдельно.',
    sBackImpr:'Переводим обратно и выполняем',sTotal:'Итог',
    sMulN:'Умножаем числители',sMulD:'Умножаем знаменатели',sGet:'Получаем',
    sSimpl:'Сокращаем (НОД =',sCrossN:'Числитель (крест)',sCrossD:'Знаменатель',
    sBefore:'До сокращения',sCommon:'Сокращаем общие множители',
    sEuclid:'Алгоритм Евклида для НОД',sAfter:'После приведения',
    sWasRes:'Результат был',sApplyRev:'Применяем обратную операцию',
    sMatchInit:'✓ Совпадает с исходным',sCorrect:'верно!',
    sCheckRes:'Результат проверки',sImposs:'Проверка невозможна (деление на 0)',
    sN1:'Число 1',sN2:'Число 2',sResOf:'Результат',sDecConv:'Как десятичное',
  },
  uk:{
    title:'Дроби',subtitle:'Калькулятор · до 10 методів розвʼязання',
    theme:'тема',expression:'вираз',
    placeholder:'Введіть числа та оберіть операцію…',
    tabInt:'Ціле',tabDec:'Десяткове',tabFrac:'Дріб',tabMixed:'Мішане',
    panelInput:'Введення числа',panelOp:'Операція та керування',
    integer:'Число',decimal:'Десяткове (напр. 3,14)',
    numerator:'Чисельник',denominator:'Знаменник',
    wholeP:'Ціла',sign:'± знак',add:'＋ Додати',clear:'✕',solve:'= Розвʼязати',
    methods:'методи розвʼязання',
    emptyHint:'Введіть два числа, оберіть операцію<br>і натисніть <strong style="color:var(--accent)">= Розвʼязати</strong>',
    of:'з',methodsOf:'методів',best:'Найкращий',
    mStd:'Стандартний (НСК знаменників)',mStdSame:'Стандартний (однак. знаменники)',
    mMul:'Множення дробів',mDiv:'Ділення дробів',
    mMixed:'Через мішані числа',mGcdLcm:'Метод НСД/НСК (спрощення)',
    mNumLine:'Числова пряма (десяткові)',mCross:'Хресне множення',
    mPrime:'Розкладання на прості',mEuclid:'Алгоритм Евкліда',
    mDirect:'Пряма формула',mVisual:'Візуальна схема',mVerify:'Перевірка оберненою дією',
    opAdd:'додавання',opSub:'віднімання',opMul:'множення',opDiv:'ділення',
    errTwo:'Потрібно мінімум два числа!',errOp:'Оберіть операцію (+ − × ÷)!',
    errZeroDen:'Знаменник не може бути 0!',errZeroNum:'Введіть число!',
    errDivZero:'Ділення на нуль!',errCalc:'Помилка обчислення',
    sGcd:'НСД',sLcm:'НСК',sReduce:'Скорочуємо',sResult:'Результат',
    sApply:'Застосовуємо формулу',sFinalAns:'Остаточна відповідь',
    sToDec:'Переводимо в десяткові',sToFrac:'Переводимо назад у дріб',
    sFlip:'Перевертаємо другий дріб',sMulInstead:'Замінюємо ділення на множення',
    sNums:'Чисельники',sDens:'Знаменники',
    sEqDen:'Знаменники однакові',sAddDir:'додаємо чисельники напряму',
    sDenStays:'Знаменник залишається',sFindLcm:'Знаходимо НСК',sBring:'Зводимо дроби',
    sConvMix:'Переводимо у мішані',sWorkSep:'Працюємо з цілими та дробовими частинами окремо.',
    sBackImpr:'Переводимо назад і виконуємо',sTotal:'Підсумок',
    sMulN:'Множимо чисельники',sMulD:'Множимо знаменники',sGet:'Отримуємо',
    sSimpl:'Скорочуємо (НСД =',sCrossN:'Чисельник (хресний)',sCrossD:'Знаменник',
    sBefore:'До скорочення',sCommon:'Скорочуємо спільні множники',
    sEuclid:'Алгоритм Евкліда для НСД',sAfter:'Після зведення',
    sWasRes:'Результат був',sApplyRev:'Застосовуємо обернену операцію',
    sMatchInit:'✓ Збігається з вихідним',sCorrect:'вірно!',
    sCheckRes:'Результат перевірки',sImposs:'Перевірка неможлива (ділення на 0)',
    sN1:'Число 1',sN2:'Число 2',sResOf:'Результат',sDecConv:'Як десяткове',
  },
  en:{
    title:'Fractions',subtitle:'Calculator · up to 10 solving methods',
    theme:'theme',expression:'expression',
    placeholder:'Enter numbers and select an operation…',
    tabInt:'Integer',tabDec:'Decimal',tabFrac:'Fraction',tabMixed:'Mixed',
    panelInput:'Enter number',panelOp:'Operation & controls',
    integer:'Number',decimal:'Decimal (e.g. 3.14)',
    numerator:'Numerator',denominator:'Denominator',
    wholeP:'Whole',sign:'± sign',add:'＋ Add',clear:'✕',solve:'= Solve',
    methods:'solving methods',
    emptyHint:'Enter two numbers, select an operation<br>and press <strong style="color:var(--accent)">= Solve</strong>',
    of:'of',methodsOf:'methods',best:'Best',
    mStd:'Standard (LCM of denominators)',mStdSame:'Standard (same denominators)',
    mMul:'Fraction multiplication',mDiv:'Fraction division',
    mMixed:'Via mixed numbers',mGcdLcm:'GCD/LCM method (simplification)',
    mNumLine:'Number line (decimals)',mCross:'Cross-multiplication',
    mPrime:'Prime factorization',mEuclid:'Euclidean algorithm',
    mDirect:'Direct formula',mVisual:'Visual diagram',mVerify:'Verification by inverse',
    opAdd:'addition',opSub:'subtraction',opMul:'multiplication',opDiv:'division',
    errTwo:'At least two numbers required!',errOp:'Select an operation (+ − × ÷)!',
    errZeroDen:'Denominator cannot be 0!',errZeroNum:'Enter a number!',
    errDivZero:'Division by zero!',errCalc:'Calculation error',
    sGcd:'GCD',sLcm:'LCM',sReduce:'Reduce',sResult:'Result',
    sApply:'Apply the formula for',sFinalAns:'Final answer',
    sToDec:'Convert to decimal',sToFrac:'Convert back to fraction',
    sFlip:'Flip the second fraction',sMulInstead:'Change division to multiplication',
    sNums:'Numerators',sDens:'Denominators',
    sEqDen:'Denominators are equal',sAddDir:'add numerators directly',
    sDenStays:'Denominator stays',sFindLcm:'Find LCM',sBring:'Bring fractions to common denom.',
    sConvMix:'Convert to mixed numbers',sWorkSep:'Work with whole and fractional parts separately.',
    sBackImpr:'Convert back to improper and perform',sTotal:'Total',
    sMulN:'Multiply numerators',sMulD:'Multiply denominators',sGet:'Get',
    sSimpl:'Reduce (GCD =',sCrossN:'Numerator (cross)',sCrossD:'Denominator',
    sBefore:'Before reduction',sCommon:'Cancel common factors',
    sEuclid:'Euclidean algorithm for GCD',sAfter:'After reducing',
    sWasRes:'Result was',sApplyRev:'Apply inverse operation',
    sMatchInit:'✓ Matches initial',sCorrect:'correct!',
    sCheckRes:'Verification result',sImposs:'Verification impossible (division by zero)',
    sN1:'Number 1',sN2:'Number 2',sResOf:'Result of',sDecConv:'As decimal',
  }
};

let currentLang='ru';
function t(k){ return (I18N[currentLang]||I18N.ru)[k] || (I18N.ru[k]||k); }

function applyI18n(){
  document.querySelectorAll('[data-i18n]').forEach(el=>{
    const k=el.getAttribute('data-i18n');
    if(k==='emptyHint'||k==='placeholder') el.innerHTML=t(k);
    else el.textContent=t(k);
  });
}

function setLang(lang,el){
  currentLang=lang;
  document.documentElement.lang=lang;
  document.querySelectorAll('.lang-btn').forEach(b=>b.classList.remove('active'));
  el.classList.add('active');
  applyI18n();
  if(lastResult) showResults(lastA,lastB,lastOp,lastResult);
  else refreshDisplay();
}

// ── THEME ─────────────────────────────────────────────────────────────────────
function setTheme(name,el){
  document.body.className=name==='default'?'':'theme-'+name;
  document.querySelectorAll('.theme-dot').forEach(d=>d.classList.remove('active'));
  el.classList.add('active');
}

// ── TABS ──────────────────────────────────────────────────────────────────────
let currentTab='int';
function switchTab(tab,el){
  currentTab=tab;
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  el.classList.add('active');
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  document.getElementById('pane-'+tab).classList.add('active');
}

// ── STATE ─────────────────────────────────────────────────────────────────────
let tokens=[], selectedOp=null, currentSign=1;
let lastA=null,lastB=null,lastOp=null,lastResult=null;

// ── MATH ──────────────────────────────────────────────────────────────────────
function gcd(a,b){a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b];}return a||1;}
function lcm(a,b){return Math.abs(a*b)/gcd(a,b);}
function frac(n,d=1){
  if(d===0)return null;
  if(d<0){n=-n;d=-d;}
  const g=gcd(Math.abs(n),d);
  return{n:n/g,d:d/g};
}
// decimal → fraction  e.g. 3.14 → 314/100
function decToFrac(v){
  if(!isFinite(v))return null;
  const s=String(v),dot=s.indexOf('.');
  if(dot===-1)return frac(Math.round(v));
  const dec=s.length-dot-1,denom=Math.pow(10,dec);
  return frac(Math.round(v*denom),denom);
}
function tokenToFrac(tok){
  if(tok.kind==='dec'){
    const f=decToFrac(tok.absVal);
    return f?frac(tok.sign*f.n,f.d):null;
  }
  const w=tok.whole||0,n=tok.num||0,d=tok.den||1;
  if(d===0)return null;
  return frac(tok.sign*(w*d+n),d);
}
function fracAdd(a,b){return frac(a.n*b.d+b.n*a.d,a.d*b.d);}
function fracSub(a,b){return frac(a.n*b.d-b.n*a.d,a.d*b.d);}
function fracMul(a,b){return frac(a.n*b.n,a.d*b.d);}
function fracDiv(a,b){if(b.n===0)return null;return frac(a.n*b.d,a.d*b.n);}
function fracToStr(f){
  if(!f)return '?';
  if(f.d===1)return `${f.n}`;
  const w=Math.trunc(f.n/f.d),r=Math.abs(f.n%f.d);
  if(w!==0&&r!==0)return `${w} ${r}/${f.d}`;
  return r===0?`${f.n}`:`${f.n}/${f.d}`;
}
function fracToDec(f){
  if(!f)return 'N/A';
  return (f.n/f.d).toFixed(8).replace(/0+$/,'').replace(/\.$/,'');
}

// ── RENDER TOKEN ──────────────────────────────────────────────────────────────
function renderToken(tok){
  if(tok.type==='op'){const s={'+':'＋','-':'－','*':'×','/':'÷'};return `<span class="token-op">${s[tok.value]}</span>`;}
  const sg=tok.sign<0?'−':'';
  if(tok.kind==='dec') return `<span class="expr-token token-decimal">${sg}${tok.absVal}</span>`;
  if(tok.kind==='int') return `<span class="expr-token token-whole">${sg}${tok.whole}</span>`;
  const w=tok.whole||0,n=tok.num||0,d=tok.den||1;
  if(w&&n) return `<span class="expr-token token-mixed"><span class="token-whole">${sg}${w}</span><span class="token-frac"><span class="frac-num">${n}</span><span class="frac-line"></span><span class="frac-den">${d}</span></span></span>`;
  if(n)    return `<span class="expr-token token-frac"><span class="frac-num">${sg}${n}</span><span class="frac-line"></span><span class="frac-den">${d}</span></span>`;
  return `<span class="expr-token token-whole">${sg}${w}</span>`;
}
function refreshDisplay(){
  const el=document.getElementById('exprDisplay');
  if(!tokens.length){el.innerHTML=`<span class="expr-placeholder">${t('placeholder')}</span>`;return;}
  el.innerHTML=tokens.map(renderToken).join('');
}

// ── INPUT ACTIONS ─────────────────────────────────────────────────────────────
function selectOp(op,el){
  document.querySelectorAll('.btn-op').forEach(b=>b.classList.remove('active-op'));
  el.classList.add('active-op');selectedOp=op;
}
function toggleSign(){currentSign*=-1;}
function clearEntry(){
  ['iInt','iDec','fNum','fDen','mWhole','mNum','mDen'].forEach(id=>{const e=document.getElementById(id);if(e)e.value='';});
  currentSign=1;
}

function addFromTab(){
  let tok=null;
  if(currentTab==='int'){
    const v=document.getElementById('iInt').value;
    if(v===''||v===null){showError(t('errZeroNum'));return;}
    const n=parseInt(v);
    if(!isFinite(n)){showError(t('errZeroNum'));return;}
    tok={type:'num',kind:'int',whole:Math.abs(n),num:0,den:1,sign:n<0?-1:currentSign};
  } else if(currentTab==='dec'){
    const v=document.getElementById('iDec').value;
    if(v===''||v===null){showError(t('errZeroNum'));return;}
    const n=parseFloat(v);
    if(!isFinite(n)){showError(t('errZeroNum'));return;}
    tok={type:'num',kind:'dec',absVal:Math.abs(n),sign:n<0?-1:currentSign};
  } else if(currentTab==='frac'){
    const nn=parseInt(document.getElementById('fNum').value)||0;
    const dd=parseInt(document.getElementById('fDen').value)||1;
    if(dd===0){showError(t('errZeroDen'));return;}
    if(nn===0){showError(t('errZeroNum'));return;}
    tok={type:'num',kind:'frac',whole:0,num:Math.abs(nn),den:Math.abs(dd),sign:nn<0?-1:currentSign};
  } else {
    const ww=parseInt(document.getElementById('mWhole').value)||0;
    const nn=parseInt(document.getElementById('mNum').value)||0;
    const dd=parseInt(document.getElementById('mDen').value)||1;
    if(dd===0){showError(t('errZeroDen'));return;}
    if(ww===0&&nn===0){showError(t('errZeroNum'));return;}
    tok={type:'num',kind:'mixed',whole:Math.abs(ww),num:Math.abs(nn),den:Math.abs(dd),sign:currentSign};
  }
  const numToks=tokens.filter(t2=>t2.type==='num');
  if(numToks.length>=1){
    if(!selectedOp){showError(t('errOp'));return;}
    tokens.push({type:'op',value:selectedOp});
    document.querySelectorAll('.btn-op').forEach(b=>b.classList.remove('active-op'));
    selectedOp=null;
  }
  tokens.push(tok);currentSign=1;clearEntry();refreshDisplay();
}
function removeLastToken(){tokens.pop();refreshDisplay();}
function clearAll(){
  tokens=[];selectedOp=null;currentSign=1;
  document.querySelectorAll('.btn-op').forEach(b=>b.classList.remove('active-op'));
  refreshDisplay();
  document.getElementById('resultArea').innerHTML=`<div class="empty-state"><div class="empty-icon">⅗</div><div class="empty-text">${t('emptyHint')}</div></div>`;
  document.getElementById('methodCount').textContent='';
  lastA=lastB=lastOp=lastResult=null;
}

// ── CALCULATE ─────────────────────────────────────────────────────────────────
function calculate(){
  const numToks=tokens.filter(t2=>t2.type==='num');
  const opToks=tokens.filter(t2=>t2.type==='op');
  if(numToks.length<2){showError(t('errTwo'));return;}
  const a=tokenToFrac(numToks[0]),b=tokenToFrac(numToks[1]);
  const op=opToks[0]?.value||'+';
  if(!a||!b){showError(t('errCalc'));return;}
  if(op==='/'&&b.n===0){showError(t('errDivZero'));return;}
  let result;
  switch(op){case '+':result=fracAdd(a,b);break;case '-':result=fracSub(a,b);break;case '*':result=fracMul(a,b);break;case '/':result=fracDiv(a,b);break;}
  if(!result){showError(t('errCalc'));return;}
  lastA=a;lastB=b;lastOp=op;lastResult=result;
  showResults(a,b,op,result);
  const ra=document.getElementById('resultArea');ra.classList.remove('pulse');void ra.offsetWidth;ra.classList.add('pulse');
}
function showError(msg){document.getElementById('resultArea').innerHTML=`<div class="error-box">⚠️ ${msg}</div>`;}

// ── BIG RESULT ────────────────────────────────────────────────────────────────
function renderBigResult(f){
  if(!f)return '';
  const w=Math.trunc(f.n/f.d),r=Math.abs(f.n%f.d),dec=fracToDec(f);
  let html='<div class="big-result">';
  if(f.d===1){html+=`<div class="big-whole">${f.n}</div>`;}
  else if(w!==0&&r!==0){
    html+=`<div class="big-whole">${w}</div><div class="big-frac"><div class="big-frac-num">${r}</div><div class="big-frac-line"></div><div class="big-frac-den">${f.d}</div></div>`;
    html+=`<span class="result-sep">=</span><div class="big-frac"><div class="big-frac-num">${f.n}</div><div class="big-frac-line"></div><div class="big-frac-den">${f.d}</div></div>`;
  } else {html+=`<div class="big-frac"><div class="big-frac-num">${f.n}</div><div class="big-frac-line"></div><div class="big-frac-den">${f.d}</div></div>`;}
  html+=`<span class="result-sep" style="font-size:1.1rem">≈</span><div class="result-decimal">${dec}</div></div>`;
  return html;
}

// ── HELPERS FOR METHODS ───────────────────────────────────────────────────────
function ih(n,d){
  if(d===1||d===0)return `<span class="highlight">${n}</span>`;
  return `<span class="inline-frac"><span class="fn highlight">${n}</span><span class="fl"></span><span class="fd highlight">${d}</span></span>`;
}
function opN(op){return {'+':t('opAdd'),'-':t('opSub'),'*':t('opMul'),'/':t('opDiv')}[op];}
function opS(op){return {'+':'＋','-':'－','*':'×','/':'÷'}[op];}
function drawBar(f){
  const pct=Math.min(Math.max((f.n/f.d)*100,0),100);
  return `<div style="display:inline-block;width:110px;height:11px;background:var(--surface3);border-radius:3px;border:1px solid var(--border);overflow:hidden;vertical-align:middle;margin-left:7px;"><div style="width:${pct}%;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:3px;"></div></div>`;
}
function primes(n){n=Math.abs(n);if(n<=1)return '1';const f=[];for(let i=2;i<=n;i++)while(n%i===0){f.push(i);n/=i;}return f.join('×');}
function euclidSteps(a,b){const st=[];let x=Math.abs(a),y=Math.abs(b);while(y){st.push(`${x}=${Math.floor(x/y)}×${y}+${x%y}`);[x,y]=[y,x%y];}return st;}

// ── METHODS ───────────────────────────────────────────────────────────────────
function getMethods(a,b,op,result){
  const M=[];

  // 1 — Standard
  if(op==='+'||op==='-'){
    const ow=opS(op);
    if(a.d===b.d){
      M.push({name:t('mStdSame'),steps:[
        `${t('sEqDen')}: <span class="highlight">${a.d}</span> — ${t('sAddDir')}.`,
        `<span class="formula">${ih(a.n,1)} ${ow} ${ih(b.n,1)} = ${ih(a.n+(op==='+'?b.n:-b.n),1)}</span>`,
        `${t('sDenStays')}: <span class="highlight">${result.d}</span>`,
        `${t('sResult')}: <span class="formula">${ih(result.n,result.d)}</span>`
      ]});
    } else {
      const L=lcm(a.d,b.d),ma=L/a.d,mb=L/b.d,na=a.n*ma,nb=b.n*mb;
      M.push({name:t('mStd'),steps:[
        `${t('sFindLcm')}(${a.d},${b.d}) = <span class="highlight">${L}</span>`,
        `${t('sBring')}: ${ih(a.n,a.d)} → ${ih(na,L)} (×${ma}),  ${ih(b.n,b.d)} → ${ih(nb,L)} (×${mb})`,
        `<span class="formula">${ih(na,1)} ${ow} ${ih(nb,1)} = ${ih(na+(op==='+'?nb:-nb),1)}</span>`,
        `${t('sResult')}: <span class="formula">${ih(result.n,result.d)}</span>`
      ]});
    }
  }
  if(op==='*'){M.push({name:t('mMul'),steps:[
    `${t('sMulN')}: <span class="highlight">${a.n} × ${b.n} = ${a.n*b.n}</span>`,
    `${t('sMulD')}: <span class="highlight">${a.d} × ${b.d} = ${a.d*b.d}</span>`,
    `${t('sGet')}: <span class="formula">${ih(a.n*b.n,a.d*b.d)}</span>`,
    `${t('sSimpl')} ${gcd(Math.abs(a.n*b.n),a.d*b.d)}): <span class="formula">${ih(result.n,result.d)}</span>`
  ]});}
  if(op==='/'){M.push({name:t('mDiv'),steps:[
    `${t('sFlip')}: ${ih(b.n,b.d)} → ${ih(b.d,b.n)}`,
    `${t('sMulInstead')}: ${ih(a.n,a.d)} × ${ih(b.d,b.n)}`,
    `${t('sNums')}: <span class="highlight">${a.n}×${b.d}=${a.n*b.d}</span>`,
    `${t('sDens')}: <span class="highlight">${a.d}×${b.n}=${a.d*b.n}</span>`,
    `${t('sReduce')}: <span class="formula">${ih(result.n,result.d)}</span>`
  ]});}

  // 2 — Mixed
  M.push({name:t('mMixed'),steps:[
    `${t('sConvMix')}: <span class="highlight">${fracToStr(a)}</span>, <span class="highlight">${fracToStr(b)}</span>`,
    op==='+'||op==='-'?t('sWorkSep'):`${t('sBackImpr')} ${opN(op)}.`,
    `${t('sTotal')}: <span class="formula">${fracToStr(result)}</span> = <span class="formula">${ih(result.n,result.d)}</span>`
  ]});

  // 3 — GCD/LCM
  if(op==='+'||op==='-'){
    const g1=gcd(Math.abs(a.n),a.d),g2=gcd(Math.abs(b.n),b.d),L=lcm(a.d,b.d);
    M.push({name:t('mGcdLcm'),steps:[
      `${t('sGcd')}(${Math.abs(a.n)},${a.d})=${g1} → ${ih(a.n/g1,a.d/g1)}`,
      `${t('sGcd')}(${Math.abs(b.n)},${b.d})=${g2} → ${ih(b.n/g2,b.d/g2)}`,
      `${t('sLcm')}(${a.d},${b.d})=<span class="highlight">${L}</span>`,
      `${t('sResult')}: <span class="formula">${ih(result.n,result.d)}</span>`
    ]});
  }

  // 4 — Number line
  if(op==='+'||op==='-'){
    const da=(a.n/a.d).toFixed(4),db=(b.n/b.d).toFixed(4),dr=(result.n/result.d).toFixed(4);
    M.push({name:t('mNumLine'),steps:[
      `${t('sToDec')}: <span class="highlight">${fracToStr(a)} ≈ ${da}</span>`,
      `${t('sToDec')}: <span class="highlight">${fracToStr(b)} ≈ ${db}</span>`,
      `${da} ${opS(op)} ${db} ≈ <span class="highlight">${dr}</span>`,
      `${t('sToFrac')}: <span class="formula">${ih(result.n,result.d)}</span>`
    ]});
  }

  // 5 — Cross multiplication
  if(op==='+'||op==='-'){
    const top=op==='+'?a.n*b.d+b.n*a.d:a.n*b.d-b.n*a.d,bot=a.d*b.d,g=gcd(Math.abs(top),bot);
    M.push({name:t('mCross'),steps:[
      `${t('sCrossN')}: (${a.n}×${b.d}) ${op} (${b.n}×${a.d})`,
      `= <span class="highlight">${a.n*b.d} ${op} ${b.n*a.d} = ${top}</span>`,
      `${t('sCrossD')}: <span class="highlight">${a.d}×${b.d}=${bot}</span>`,
      `${t('sBefore')}: <span class="formula">${ih(top,bot)}</span>`,
      `${t('sGcd')}(${Math.abs(top)},${bot})=${g} → <span class="formula">${ih(result.n,result.d)}</span>`
    ]});
  }

  // 6 — Prime factors
  if(op==='*'||op==='/'){
    M.push({name:t('mPrime'),steps:[
      `${a.n}: <span class="highlight">${primes(a.n)}</span>,  ${a.d}: <span class="highlight">${primes(a.d)}</span>`,
      `${b.n}: <span class="highlight">${primes(b.n)}</span>,  ${b.d}: <span class="highlight">${primes(b.d)}</span>`,
      op==='*'?`<span class="formula">${ih(a.n*b.n,a.d*b.d)}</span>`:`<span class="formula">${ih(a.n*b.d,a.d*b.n)}</span>`,
      `${t('sCommon')}: <span class="formula">${ih(result.n,result.d)}</span>`
    ]});
  }

  // 7 — Euclid
  {
    const L=lcm(a.d,b.d),es=euclidSteps(a.d,b.d).slice(0,3);
    M.push({name:t('mEuclid'),steps:[
      `${t('sEuclid')} (${a.d},${b.d}):`,
      ...es.map(s=>`<span class="formula">${s}</span>`),
      `${t('sGcd')}=${gcd(a.d,b.d)}, ${t('sLcm')}=${L}`,
      `${t('sAfter')}: <span class="formula">${ih(result.n,result.d)}</span>`
    ]});
  }

  // 8 — Direct formula (BEST)
  {
    const fm={
      '+': `${ih(a.n,a.d)} ＋ ${ih(b.n,b.d)} = ${ih(a.n*b.d+b.n*a.d,a.d*b.d)} = ${ih(result.n,result.d)}`,
      '-': `${ih(a.n,a.d)} － ${ih(b.n,b.d)} = ${ih(a.n*b.d-b.n*a.d,a.d*b.d)} = ${ih(result.n,result.d)}`,
      '*': `${ih(a.n,a.d)} × ${ih(b.n,b.d)} = ${ih(a.n*b.n,a.d*b.d)} = ${ih(result.n,result.d)}`,
      '/': `${ih(a.n,a.d)} ÷ ${ih(b.n,b.d)} = ${ih(a.n,a.d)} × ${ih(b.d,b.n)} = ${ih(a.n*b.d,a.d*b.n)} = ${ih(result.n,result.d)}`
    };
    M.push({name:t('mDirect'),best:true,steps:[
      `${t('sApply')} ${opN(op)}:`,
      `<span class="formula">${fm[op]}</span>`,
      `${t('sFinalAns')}: <span class="highlight">${fracToStr(result)}</span>`
    ]});
  }

  // 9 — Visual
  M.push({name:t('mVisual'),steps:[
    `${t('sN1')}: <span class="highlight">${fracToStr(a)}</span> ≈ <span class="highlight">${(a.n/a.d*100).toFixed(1)}%</span> ${drawBar(a)}`,
    `${t('sN2')}: <span class="highlight">${fracToStr(b)}</span> ≈ <span class="highlight">${(b.n/b.d*100).toFixed(1)}%</span> ${drawBar(b)}`,
    `${t('sResOf')} ${opN(op)}: <span class="highlight">${fracToStr(result)}</span> ≈ <span class="highlight">${(result.n/result.d*100).toFixed(1)}%</span> ${drawBar(result)}`
  ]});

  // 10 — Verify
  {
    const rop={'+':'-','-':'+','*':'/','/':`*`}[op];
    let check;
    switch(rop){case '+':check=fracAdd(result,b);break;case '-':check=fracSub(result,b);break;case '*':check=fracMul(result,b);break;case '/':check=b.n!==0?fracDiv(result,b):null;break;}
    const rs={'+':'＋','-':'－','*':'×','/':'÷'}[rop];
    M.push({name:t('mVerify'),steps:[
      `${t('sWasRes')}: <span class="formula">${ih(result.n,result.d)}</span>`,
      `${t('sApplyRev')} (${rs}): <span class="highlight">${fracToStr(b)}</span>`,
      check?`<span class="formula">${ih(result.n,result.d)} ${rs} ${ih(b.n,b.d)} = ${ih(check.n,check.d)}</span>`:`<em>${t('sImposs')}</em>`,
      check&&check.n===a.n&&check.d===a.d
        ?`${t('sMatchInit')} <span class="highlight">${fracToStr(a)}</span> — <span class="highlight" style="color:var(--success)">${t('sCorrect')}</span>`
        :`${t('sCheckRes')}: <span class="formula">${check?ih(check.n,check.d):'—'}</span>`
    ]});
  }

  return M.slice(0,10);
}

// ── SHOW RESULTS ──────────────────────────────────────────────────────────────
function showResults(a,b,op,result){
  const methods=getMethods(a,b,op,result);
  document.getElementById('methodCount').textContent=`${methods.length} ${t('of')} 10 ${t('methodsOf')}`;
  let html=renderBigResult(result)+'<div class="methods-grid">';
  methods.forEach((m,i)=>{
    html+=`<div class="method-card ${i===0?'open':''}" id="mc${i}">
      <div class="method-header" onclick="toggleMethod(${i})">
        <div class="method-num">${String(i+1).padStart(2,'0')}</div>
        <div class="method-name">${m.name}</div>
        ${m.best?`<span class="tag tag-best">${t('best')}</span>`:''}
        <span class="chevron">▼</span>
      </div>
      <div class="method-body"><div class="step-list">
        ${m.steps.map((s,si)=>`<div class="step"><div class="step-num">${si+1}</div><div class="step-content">${s}</div></div>`).join('')}
      </div></div>
    </div>`;
  });
  document.getElementById('resultArea').innerHTML=html+'</div>';
}
function toggleMethod(i){document.getElementById('mc'+i).classList.toggle('open');}

// ── KEYBOARD ──────────────────────────────────────────────────────────────────
document.addEventListener('keydown',e=>{
  if(e.key==='Enter'&&!e.shiftKey){
    if(document.activeElement&&document.activeElement.classList.contains('entry-field'))addFromTab();
    else calculate();
  }
});
</script>

</body>
</html>
