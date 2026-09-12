
html_body = """
<!-- HEADER -->
<header>
  <div class="logo" onclick="showScreen('landing')"><span style="font-size:1.3rem">🌱</span> KhetiLink AI</div>
  <span class="location-pill">📍 Gujarat</span>
  <div class="header-right">
    <div class="lang-grp">
      <button class="lang-btn active">ગુ</button>
      <button class="lang-btn">हि</button>
      <button class="lang-btn">EN</button>
    </div>
    <button class="icon-btn">🔔<span class="badge"></span></button>
    <button class="icon-btn">👤</button>
  </div>
</header>
<nav class="bottom-nav">
  <button class="nav-item active" id="nav-dashboard" onclick="showScreen('dashboard')"><span class="nav-icon">🏠</span>Dashboard</button>
  <button class="nav-item" id="nav-prices" onclick="showScreen('prices')"><span class="nav-icon">📈</span>Prices</button>
  <button class="nav-item ai-nav" id="nav-advisor" onclick="showScreen('advisor')"><span class="nav-icon">🤖</span>AI Advisor</button>
  <button class="nav-item" id="nav-buyers" onclick="showScreen('buyers')"><span class="nav-icon">🤝</span>Buyers</button>
  <button class="nav-item" id="nav-produce" onclick="showScreen('produce')"><span class="nav-icon">🌾</span>My Farm</button>
</nav>
<div id="toast"></div>

<!-- LANDING -->
<div id="screen-landing" class="screen active">
  <div class="hero">
    <div class="hero-badge">🤖 Agentic AI &bull; IBM Granite LLM</div>
    <h1 class="hero-title">Sell Smarter.<br/><span>Earn Better.</span></h1>
    <p class="hero-sub">AI-powered market intelligence and direct buyer connections for Gujarat's cotton and groundnut farmers.</p>
    <div class="hero-btns">
      <button class="btn-primary" onclick="showScreen('dashboard')">🚀 Start Selling Smarter</button>
      <button class="btn-secondary" onclick="showScreen('prices')">📈 Explore Market Prices</button>
    </div>
  </div>
  <div class="impact-section">
    <div class="demo-note">⚠️ Demo Market Data — Simulated values for demonstration purposes only. Not live mandi prices.</div>
    <div class="impact-grid">
      <div class="impact-card"><div class="impact-icon">📈</div><div><div class="impact-title">Better Price Decisions</div><div class="impact-desc">Understand real-time market trends before selling. Know when to sell for the best price.</div></div></div>
      <div class="impact-card"><div class="impact-icon">🤝</div><div><div class="impact-title">Direct Market Access</div><div class="impact-desc">Connect directly with ginners, processors and exporters. Reduce dependency on middlemen.</div></div></div>
      <div class="impact-card"><div class="impact-icon">💰</div><div><div class="impact-title">Better Income Potential</div><div class="impact-desc">Compare multiple buyer offers with AI matching. Make informed selling decisions every time.</div></div></div>
      <div class="impact-card"><div class="impact-icon">🤖</div><div><div class="impact-title">Explainable AI</div><div class="impact-desc">Every recommendation explained clearly. Powered by IBM Granite LLM on IBM Cloud.</div></div></div>
    </div>
    <button class="btn-primary" style="width:100%;margin-top:10px" onclick="showScreen('arch')">🏗️ View AI Architecture</button>
  </div>
  <div class="site-footer">
    <div class="footer-logo">🌱 KhetiLink AI</div>
    <div>AI-powered market intelligence for Gujarat's cotton &amp; groundnut farmers.</div>
    <div style="margin-top:6px;color:rgba(255,255,255,.5);font-size:.75rem">Created by <strong style="color:#fff">Khushi Patel</strong></div>
    <div class="footer-tech">
      <span class="footer-tag">IBM Granite LLM</span>
      <span class="footer-tag">IBM Cloud</span>
      <span class="footer-tag">Agentic AI</span>
      <span class="footer-tag">IBM Bob</span>
    </div>
  </div>
</div>

<!-- DASHBOARD -->
<div id="screen-dashboard" class="screen">
  <div class="container">
    <div style="margin-bottom:16px">
      <div style="font-size:1.2rem;font-weight:800;color:var(--text)">Namaste, Farmer 👋</div>
      <div style="font-size:.83rem;color:var(--muted);margin-top:2px">Here's your market intelligence today.</div>
    </div>
    <div class="demo-note">⚠️ Demo Market Data — Values are simulated for demonstration purposes.</div>
    <div class="price-grid">
      <div class="price-chip" onclick="showScreen('prices')">
        <div class="crop-label">🌿 Cotton</div>
        <div class="price-val">&#8377;7,150</div>
        <div class="price-unit">per Quintal</div>
        <div class="trend up">&#8593; 2.4% today</div>
      </div>
      <div class="price-chip" onclick="showScreen('prices')">
        <div class="crop-label">&#129386; Groundnut</div>
        <div class="price-val">&#8377;5,820</div>
        <div class="price-unit">per Quintal</div>
        <div class="trend up">&#8593; 1.1% today</div>
      </div>
    </div>
    <div class="ai-card">
      <div class="ai-card-label">🤖 Market &amp; Buyer Intelligence Agent</div>
      <div class="ai-card-crop">Cotton &bull; 25 Quintals &bull; Grade A</div>
      <div class="rec-badge wait">&#9203; WAIT &amp; MONITOR</div>
      <div class="ai-row"><span class="ai-row-label">Current Mandi Price</span><span class="ai-row-val">&#8377;7,150/q</span></div>
      <div class="ai-row"><span class="ai-row-label">Expected 7-Day Price</span><span class="ai-row-val">&#8377;7,400&#8211;&#8377;7,550/q</span></div>
      <div class="ai-row"><span class="ai-row-label">Best Buyer Offer</span><span class="ai-row-val">&#8377;7,350/q</span></div>
      <div class="ai-row"><span class="ai-row-label">Best Buyer</span><span class="ai-row-val">Shree Gujarat Ginners</span></div>
      <div class="ai-row"><span class="ai-row-label">AI Match Score</span><span class="ai-row-val">92%</span></div>
      <div class="conf-bar"><div class="conf-fill" style="width:84%"></div></div>
      <div style="font-size:.7rem;opacity:.65;margin-top:4px">AI Confidence: 84%</div>
      <button class="ai-btn" onclick="showScreen('advisor')">&#128269; View AI Reasoning</button>
    </div>
    <div class="section-label" style="margin-top:0">Quick Actions</div>
    <div class="quick-grid">
      <div class="quick-item" onclick="showScreen('prices')"><div class="q-icon">📈</div><div class="q-label">Market Prices</div><div class="q-sub">Cotton &amp; Groundnut</div></div>
      <div class="quick-item" onclick="showScreen('buyers')"><div class="q-icon">🤝</div><div class="q-label">Find Buyers</div><div class="q-sub">AI-matched buyers</div></div>
      <div class="quick-item" onclick="showScreen('advisor')"><div class="q-icon">🤖</div><div class="q-label">AI Advisor</div><div class="q-sub">Get recommendation</div></div>
      <div class="quick-item" onclick="showScreen('income')"><div class="q-icon">💰</div><div class="q-label">Income View</div><div class="q-sub">This season</div></div>
    </div>
  </div>
</div>

<!-- PRICES -->
<div id="screen-prices" class="screen">
  <div class="container">
    <div class="page-title">📈 Price Intelligence</div>
    <div class="page-sub">Understand today's market and upcoming price trends.</div>
    <div class="demo-note">⚠️ Demo Market Data — Not live mandi prices.</div>
    <div class="chart-tabs" style="margin-bottom:10px">
      <button class="chart-tab active" id="crop-cotton" onclick="switchCrop('cotton',this)">🌿 Cotton</button>
      <button class="chart-tab" id="crop-groundnut" onclick="switchCrop('groundnut',this)">&#129386; Groundnut</button>
    </div>
    <div class="chart-tabs">
      <button class="chart-tab active" id="range-7d" onclick="switchRange('7d',this)">7 Days</button>
      <button class="chart-tab" id="range-30d" onclick="switchRange('30d',this)">30 Days</button>
      <button class="chart-tab" id="range-today" onclick="switchRange('today',this)">Today</button>
    </div>
    <div class="chart-wrap">
      <canvas id="priceChart" height="200"></canvas>
      <div class="chart-legend">
        <div class="legend-item"><div class="legend-dot" style="background:#2e7d32"></div>Historical</div>
        <div class="legend-item"><div class="legend-dot" style="background:#f9a825"></div>AI Forecast</div>
      </div>
    </div>
    <div class="stat-grid">
      <div class="stat-card"><div class="stat-label">Current Price</div><div class="stat-val" id="stat-current">&#8377;7,150/q</div><div class="stat-sub trend up">&#8593; +2.4% today</div></div>
      <div class="stat-card"><div class="stat-label">7-Day Forecast</div><div class="stat-val" id="stat-forecast">&#8377;7,420/q</div><div class="stat-sub" style="color:var(--green)">AI Predicted</div></div>
      <div class="stat-card"><div class="stat-label">Market Trend</div><div class="stat-val" id="stat-trend" style="color:var(--green)">&#8593; Bullish</div><div class="stat-sub">Price rising</div></div>
      <div class="stat-card"><div class="stat-label">AI Confidence</div><div class="stat-val" id="stat-conf">84%</div><div class="stat-sub">High</div></div>
    </div>
    <div class="card" style="margin-top:0">
      <div style="font-size:.9rem;font-weight:800;color:var(--text);margin-bottom:10px">📊 Market Summary</div>
      <div style="font-size:.83rem;color:var(--muted);line-height:1.7" id="market-summary">Cotton prices are on an upward trend. The current mandi price of &#8377;7,150/q is 2.4% above yesterday. AI forecasts prices reaching &#8377;7,400&#8211;&#8377;7,550/q over the next 7 days based on recent procurement patterns and seasonal demand indicators.</div>
    </div>
    <button class="analyze-btn" onclick="showScreen('advisor')" style="margin-top:14px">🤖 Get AI Selling Advice</button>
  </div>
</div>

<!-- BUYERS -->
<div id="screen-buyers" class="screen">
  <div id="buyer-list-view">
    <div class="container">
      <div class="page-title">🤝 Find the Right Buyer</div>
      <div class="page-sub">AI-matched buyers based on your crop, quantity, quality and location.</div>
      <div class="filter-scroll">
        <button class="filter-pill active" onclick="filterBuyers('all',this)">All</button>
        <button class="filter-pill" onclick="filterBuyers('cotton',this)">🌿 Cotton</button>
        <button class="filter-pill" onclick="filterBuyers('groundnut',this)">&#129386; Groundnut</button>
        <button class="filter-pill" onclick="filterBuyers('pickup',this)">🚚 Pickup Avail.</button>
        <button class="filter-pill" onclick="filterBuyers('highprice',this)">💰 Highest Price</button>
        <button class="filter-pill" onclick="filterBuyers('near',this)">📍 Near (&lt;25km)</button>
      </div>
      <div id="buyer-cards-container"></div>
    </div>
  </div>
  <div id="buyer-detail-view" class="detail-panel">
    <div class="detail-header-bar">
      <button class="detail-back" onclick="showBuyerList()">&#8592; Back to Buyers</button>
      <div class="detail-name" id="detail-name">Shree Gujarat Ginners</div>
      <div class="detail-type-lbl" id="detail-type">Cotton Buyer &bull; Gin Factory</div>
      <div class="detail-price-big" id="detail-price">&#8377;7,350</div>
      <div class="detail-unit-lbl">per Quintal</div>
      <div class="detail-vs-lbl" id="detail-vs">Market Average: &#8377;7,150/q &nbsp;|&nbsp; &#8377;200/q above mandi</div>
      <span class="detail-match-badge" id="detail-match">🤖 AI Match: 92%</span>
    </div>
    <div class="why-section">
      <div class="why-title">🤖 Why this buyer?</div>
      <div id="why-rows"></div>
    </div>
    <div class="detail-btns">
      <button class="btn-offer" onclick="showToast('Offer sent successfully!')">📤 Send Offer</button>
      <button class="btn-contact" onclick="showToast('Opening contact details...')">📞 Contact Buyer</button>
      <button class="btn-compare" onclick="showToast('Compare feature coming soon!')">⚖️ Compare Buyers</button>
    </div>
  </div>
</div>

<!-- AI ADVISOR -->
<div id="screen-advisor" class="screen">
  <div class="container">
    <div class="page-title">🤖 AI Market Advisor</div>
    <div class="page-sub">One AI agent. Market prices + buyer opportunities + selling recommendation.</div>
    <div class="card">
      <div style="font-size:.9rem;font-weight:800;color:var(--text);margin-bottom:12px">Tell the AI about your produce</div>
      <div class="form-group">
        <label class="form-label">Crop</label>
        <select class="form-control" id="adv-crop"><option>Cotton</option><option>Groundnut</option></select>
      </div>
      <div class="form-group">
        <label class="form-label">Quantity (Quintals)</label>
        <input class="form-control" type="number" id="adv-qty" value="25" min="1"/>
      </div>
      <div class="form-group">
        <label class="form-label">Quality Grade</label>
        <select class="form-control" id="adv-grade"><option>Grade A</option><option>Grade B</option><option>Grade C</option></select>
      </div>
      <div class="form-group">
        <label class="form-label">Location</label>
        <select class="form-control" id="adv-location">
          <option>Ahmedabad, Gujarat</option><option>Rajkot, Gujarat</option><option>Bhavnagar, Gujarat</option><option>Surendranagar, Gujarat</option><option>Junagadh, Gujarat</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Storage Available?</label>
        <div class="toggle-row">
          <button class="toggle-btn active" id="stor-yes" onclick="setStorage(true)">&#10003; Yes</button>
          <button class="toggle-btn" id="stor-no" onclick="setStorage(false)">&#10007; No</button>
        </div>
      </div>
      <button class="analyze-btn" onclick="runAnalysis()">&#128269; Analyze My Selling Options</button>
    </div>
    <div id="analysis-anim">
      <div class="anim-title">🤖 KhetiLink AI is analyzing...</div>
      <div class="anim-step" id="as1"><div class="anim-check" id="ac1">&#10003;</div>Checking mandi prices</div>
      <div class="anim-step" id="as2"><div class="anim-check" id="ac2">&#10003;</div>Analyzing recent price trends</div>
      <div class="anim-step" id="as3"><div class="anim-check" id="ac3">&#10003;</div>Forecasting short-term prices</div>
      <div class="anim-step" id="as4"><div class="anim-check" id="ac4">&#10003;</div>Searching suitable buyers</div>
      <div class="anim-step" id="as5"><div class="anim-check" id="ac5">&#10003;</div>Comparing buyer offers</div>
      <div class="anim-step" id="as6"><div class="anim-check" id="ac6">&#10003;</div>Checking quantity compatibility</div>
      <div class="anim-step" id="as7"><div class="anim-check" id="ac7">&#10003;</div>Evaluating market opportunity</div>
      <div class="anim-step" id="as8"><div class="anim-check" id="ac8">&#10003;</div>Generating recommendation</div>
      <div id="anim-complete" style="display:none;margin-top:10px;font-size:.85rem;font-weight:700;color:var(--green)">&#10003; Analysis Complete</div>
    </div>
    <div id="ai-result">
      <div class="result-card">
        <div class="result-label">AI Recommendation</div>
        <div class="result-rec" id="res-rec">&#9203; WAIT &amp; MONITOR</div>
        <div class="result-row"><span>Current Mandi Price</span><span id="res-price">&#8377;7,150/q</span></div>
        <div class="result-row"><span>Expected Price</span><span id="res-exp">&#8377;7,400&#8211;&#8377;7,550/q</span></div>
        <div class="result-row"><span>Best Current Buyer</span><span id="res-buyer">&#8377;7,350/q</span></div>
        <div class="result-row"><span>Best Buyer Name</span><span id="res-bname">Shree Gujarat Ginners</span></div>
        <div class="result-row"><span>AI Confidence</span><span id="res-conf">84%</span></div>
        <div class="result-row"><span>Potential Opportunity</span><span id="res-opp">&#8377;6,250&#8211;&#8377;10,000</span></div>
        <div class="result-row"><span>Risk Level</span><span id="res-risk">Medium</span></div>
      </div>
      <div class="card" style="margin-bottom:12px">
        <div style="font-size:.9rem;font-weight:800;color:var(--text);margin-bottom:12px">&#128269; AI Decision Factors</div>
        <div class="factor-row"><div class="factor-name">Price Trend</div><div class="factor-bar-wrap"><div class="factor-bar" style="width:85%"></div></div><div class="factor-sign">+++</div></div>
        <div class="factor-row"><div class="factor-name">Buyer Demand</div><div class="factor-bar-wrap"><div class="factor-bar" style="width:70%"></div></div><div class="factor-sign">++</div></div>
        <div class="factor-row"><div class="factor-name">Buyer Offer</div><div class="factor-bar-wrap"><div class="factor-bar" style="width:68%"></div></div><div class="factor-sign">++</div></div>
        <div class="factor-row"><div class="factor-name">Market Opportunity</div><div class="factor-bar-wrap"><div class="factor-bar" style="width:72%"></div></div><div class="factor-sign">++</div></div>
        <div class="factor-row"><div class="factor-name">Storage Cost</div><div class="factor-bar-wrap"><div class="factor-bar neg" style="width:35%"></div></div><div class="factor-sign neg">-</div></div>
        <div class="factor-row"><div class="factor-name">Market Risk</div><div class="factor-bar-wrap"><div class="factor-bar neg" style="width:40%"></div></div><div class="factor-sign neg">-</div></div>
        <div style="margin-top:10px;font-size:.8rem;color:var(--muted)">Overall Confidence: <strong style="color:var(--green)" id="conf-display">84%</strong></div>
      </div>
      <div class="insight-box" id="ai-insight">Current buyer offers are competitive, but the market trend suggests that prices may improve over the next few days. The AI therefore recommends monitoring the market before making the final sale.</div>
      <button class="btn-primary" style="width:100%;margin-bottom:14px" onclick="showScreen('buyers')">🤝 View Matched Buyers</button>
    </div>
    <div class="section-label" style="margin-top:0">🎙️ Ask KhetiLink AI</div>
    <div class="voice-card" onclick="triggerVoice()">
      <div class="voice-icon">🎙️</div>
      <div class="voice-title">Ask in your language</div>
      <div class="voice-sub">Tap and speak — get AI answer instantly</div>
      <div class="voice-langs"><span class="voice-lang">ગુજરાતી</span><span class="voice-lang">हिन्दी</span><span class="voice-lang">English</span></div>
    </div>
    <div class="section-label" style="margin-top:0">Example Questions</div>
    <div class="example-q" onclick="showVoiceResp('guj')"><div class="q-text">"મારો કપાસ ક્યારે વેચવો?"</div><div class="q-lang">ગુજરાતી — When should I sell my cotton?</div></div>
    <div class="voice-resp" id="voice-resp-guj"><strong>🤖 KhetiLink AI:</strong><br/>"હાલના ભાવ અને બજારના ટ્રેન્ડ પ્રમાણે થોડા દિવસ રાહ જોવી યોગ્ય હોઈ શકે છે. નજીકના ખરીદદારોમાં &#8377;7,350 પ્રતિ ક્વિન્ટલ ઉપલબ્ધ છે. AI અનુમાન: &#8377;7,400&#8211;&#8377;7,550 ભાવ આગળ વધી શકે."</div>
    <div class="example-q" onclick="showVoiceResp('hin')"><div class="q-text">"आज मूंगफली का भाव क्या है?"</div><div class="q-lang">हिन्दी — What is today's groundnut price?</div></div>
    <div class="voice-resp" id="voice-resp-hin"><strong>🤖 KhetiLink AI:</strong><br/>"आज मूंगफली का मंडी भाव &#8377;5,820/क्विंटल है। पिछले सप्ताह से 1.1% की बढ़ोतरी हुई है। AI का अनुमान: &#8377;5,900&#8211;&#8377;6,000 तक पहुंच सकता है। श्रेष्ठ खरीदार &#8377;5,950/क्विंटल दे रहे हैं।"</div>
    <div class="example-q" onclick="showVoiceResp('eng')"><div class="q-text">"Which buyer offers the best price for my cotton?"</div><div class="q-lang">English</div></div>
    <div class="voice-resp" id="voice-resp-eng"><strong>🤖 KhetiLink AI:</strong><br/>"For Grade A cotton in Gujarat, Shree Gujarat Ginners offers the best price at &#8377;7,350/q — &#8377;200 above the current mandi average. AI match score: 92%. Pickup available, 18 km away."</div>
  </div>
</div>

<!-- MY PRODUCE -->
<div id="screen-produce" class="screen">
  <div class="container">
    <div class="page-title">🌾 My Produce</div>
    <div class="page-sub">Your current crop inventory and AI recommendations.</div>
    <div class="demo-note">⚠️ Demo data — Update your actual inventory for real recommendations.</div>
    <div class="produce-card">
      <div class="produce-header"><div class="produce-icon">🌿</div><div><div class="produce-name">Cotton</div><div class="produce-detail">25 Quintals &bull; Grade A &bull; Harvested Oct 2024</div></div></div>
      <div class="produce-vals">
        <div class="p-val-box"><div class="p-val-label">Market Value</div><div class="p-val">&#8377;1,78,750</div></div>
        <div class="p-val-box"><div class="p-val-label">Best Buyer</div><div class="p-val" style="color:var(--green)">&#8377;1,83,750</div></div>
        <div class="p-val-box"><div class="p-val-label">Expected Max</div><div class="p-val">&#8377;1,88,750</div></div>
        <div class="p-val-box"><div class="p-val-label">Opportunity</div><div class="p-val" style="color:var(--green)">+&#8377;5,000</div></div>
      </div>
      <div class="p-rec"><span class="p-rec-label">AI Recommendation</span><span class="p-rec-val">&#9203; WAIT &amp; MONITOR</span></div>
      <button class="view-btn" style="margin-top:10px" onclick="showScreen('advisor')">🤖 Get AI Advice</button>
    </div>
    <div class="produce-card">
      <div class="produce-header"><div class="produce-icon">&#129386;</div><div><div class="produce-name">Groundnut</div><div class="produce-detail">40 Quintals &bull; Grade A &bull; Harvested Sep 2024</div></div></div>
      <div class="produce-vals">
        <div class="p-val-box"><div class="p-val-label">Market Value</div><div class="p-val">&#8377;2,32,800</div></div>
        <div class="p-val-box"><div class="p-val-label">Best Buyer</div><div class="p-val" style="color:var(--green)">&#8377;2,38,000</div></div>
        <div class="p-val-box"><div class="p-val-label">Expected Max</div><div class="p-val">&#8377;2,40,000</div></div>
        <div class="p-val-box"><div class="p-val-label">Opportunity</div><div class="p-val" style="color:var(--green)">+&#8377;5,200</div></div>
      </div>
      <div class="p-rec"><span class="p-rec-label">AI Recommendation</span><span class="p-rec-val" style="color:#1565c0">&#128176; SELL NOW</span></div>
      <button class="view-btn" style="margin-top:10px" onclick="showScreen('buyers')">🤝 Find Buyers</button>
    </div>
    <button class="btn-primary" style="width:100%;margin-top:4px" onclick="showToast('Add produce feature coming soon!')">+ Add New Produce</button>
  </div>
</div>

<!-- INCOME -->
<div id="screen-income" class="screen">
  <div class="container">
    <div class="page-title">💰 Income View</div>
    <div class="page-sub">This season's estimated revenue and potential earnings.</div>
    <div class="demo-note">⚠️ Estimated values based on demo market data.</div>
    <div class="income-hero">
      <div class="income-hero-label">This Season — Total Produce</div>
      <div class="income-hero-val">85 Quintals</div>
      <div class="income-hero-sub">Cotton 25q + Groundnut 40q + Other 20q</div>
      <div class="opp-row"><span class="opp-label">Estimated Revenue</span><span class="opp-val">&#8377;6,18,800</span></div>
      <div class="opp-row" style="padding-top:8px;margin-top:8px;border-top:1px solid rgba(255,255,255,.1)"><span class="opp-label">Potential Revenue</span><span class="opp-val">&#8377;6,43,000</span></div>
      <div class="opp-row" style="padding-top:8px;margin-top:8px;border-top:1px solid rgba(255,255,255,.1)"><span class="opp-label">&#127919; Opportunity</span><span class="opp-val">+&#8377;24,200</span></div>
    </div>
    <div class="chart-wrap">
      <div style="font-size:.88rem;font-weight:700;color:var(--text);margin-bottom:12px">Actual vs Potential Revenue</div>
      <canvas id="incomeChart" height="180"></canvas>
      <div class="chart-legend" style="margin-top:12px">
        <div class="legend-item"><div class="legend-dot" style="background:#2e7d32"></div>Estimated Revenue</div>
        <div class="legend-item"><div class="legend-dot" style="background:#f9a825"></div>Potential Revenue</div>
      </div>
    </div>
    <div class="insight-box"><strong>🤖 AI Insight:</strong> Better buyer matching and improved selling timing may increase potential revenue by approximately &#8377;24,200 this season. The biggest opportunity is in cotton, where waiting for the right buyer could add &#8377;5,000 in value.</div>
    <div class="stat-grid">
      <div class="stat-card"><div class="stat-label">Cotton Revenue</div><div class="stat-val">&#8377;1,78,750</div><div class="stat-sub">25 Quintals</div></div>
      <div class="stat-card"><div class="stat-label">Groundnut Revenue</div><div class="stat-val">&#8377;2,32,800</div><div class="stat-sub">40 Quintals</div></div>
      <div class="stat-card"><div class="stat-label">Cotton Potential</div><div class="stat-val" style="color:var(--green)">&#8377;1,83,750</div><div class="stat-sub trend up">+&#8377;5,000</div></div>
      <div class="stat-card"><div class="stat-label">Groundnut Potential</div><div class="stat-val" style="color:var(--green)">&#8377;2,38,000</div><div class="stat-sub trend up">+&#8377;5,200</div></div>
    </div>
  </div>
</div>

<!-- ARCHITECTURE -->
<div id="screen-arch" class="screen">
  <div class="container">
    <div class="page-title">&#127959;&#65039; AI Agent Architecture</div>
    <div class="page-sub">How KhetiLink AI's Agentic AI system works — built with IBM Bob.</div>
    <div class="arch-card">
      <div class="arch-title">&#129302; Market &amp; Buyer Intelligence Agent</div>
      <div class="arch-flow">
        <div class="arch-node">&#128119; FARMER</div>
        <div class="arch-arrow">&#8595;</div>
        <div class="arch-node main">&#127807; KhetiLink AI Platform</div>
        <div class="arch-arrow">&#8595;</div>
        <div class="arch-node main" style="font-size:.82rem">&#129302; Market &amp; Buyer Intelligence Agent</div>
        <div class="arch-arrow">&#8595;</div>
        <div class="arch-split">
          <div class="arch-branch">
            <div class="arch-node" style="min-width:0;font-size:.75rem;padding:8px 10px">&#128200; Mandi<br/>Intelligence</div>
            <div style="font-size:.68rem;color:var(--muted);margin-top:4px;text-align:center">Prices &bull; Trends<br/>Forecasts &bull; Seasons</div>
          </div>
          <div class="arch-branch">
            <div class="arch-node" style="min-width:0;font-size:.75rem;padding:8px 10px">&#127981; Buyer<br/>Intelligence</div>
            <div style="font-size:.68rem;color:var(--muted);margin-top:4px;text-align:center">Matching &bull; Offers<br/>Location &bull; Ratings</div>
          </div>
        </div>
        <div class="arch-arrow">&#8595;</div>
        <div class="arch-node ibm">&#129504; IBM Granite LLM</div>
        <div class="arch-arrow">&#8595;</div>
        <div class="arch-node cloud">&#9729;&#65039; IBM Cloud</div>
        <div class="arch-arrow">&#8595;</div>
        <div class="arch-node" style="background:#f3e5f5;border-color:#6a1b9a;color:#6a1b9a">&#128736;&#65039; IBM Bob (Dev Environment)</div>
        <div class="arch-arrow">&#8595;</div>
        <div class="arch-node">&#128161; Explainable AI Recommendation</div>
      </div>
      <div class="tech-pills">
        <span class="tech-pill granite">IBM Granite LLM</span>
        <span class="tech-pill cloud">IBM Cloud</span>
        <span class="tech-pill agentic">Agentic AI</span>
        <span class="tech-pill bob">IBM Bob</span>
      </div>
    </div>
    <div class="arch-card">
      <div class="arch-title">&#128203; Agent Decision Flow</div>
      <div style="font-size:.83rem;color:var(--muted);line-height:2.1">
        <div>1. &#128119; <strong>Farmer</strong> enters crop, quantity, quality, location</div>
        <div>2. &#128200; Agent fetches <strong>current mandi prices</strong></div>
        <div>3. &#128202; Agent analyzes <strong>price trends &amp; forecasts</strong></div>
        <div>4. &#127981; Agent <strong>searches &amp; matches buyers</strong></div>
        <div>5. &#129504; <strong>IBM Granite LLM</strong> weighs all factors</div>
        <div>6. &#128161; Agent generates <strong>SELL / WAIT / STORE recommendation</strong></div>
        <div>7. &#128269; AI provides <strong>transparent decision factors</strong></div>
        <div>8. &#128119; Farmer makes <strong>informed selling decision</strong></div>
      </div>
    </div>
    <div class="arch-card">
      <div class="arch-title">&#127775; Impact Story</div>
      <div style="font-size:.83rem;color:var(--muted);line-height:2.2">
        <div style="color:var(--green);font-weight:700">FARMER</div>
        <div>&#8595; Current Market Price</div>
        <div>&#8595; AI Analyzes Price + Buyer Options</div>
        <div>&#8595; Best Buyers Identified</div>
        <div>&#8595; AI Recommends SELL / WAIT</div>
        <div>&#8595; Farmer Makes Informed Decision</div>
        <div>&#8595; Better Market Access</div>
        <div style="color:var(--green);font-weight:700">&#8595; Better Income Potential</div>
      </div>
    </div>
    <div class="site-footer" style="margin:0 -16px">
      <div class="footer-logo">&#127807; KhetiLink AI</div>
      <div>AI-powered market intelligence for Gujarat's cotton &amp; groundnut farmers.</div>
      <div style="margin-top:6px;color:rgba(255,255,255,.5);font-size:.75rem">Created by <strong style="color:#fff">Khushi Patel</strong></div>
      <div class="footer-tech">
        <span class="footer-tag">IBM Granite LLM</span>
        <span class="footer-tag">IBM Cloud</span>
        <span class="footer-tag">Agentic AI</span>
        <span class="footer-tag">IBM Bob</span>
      </div>
    </div>
  </div>
</div>
"""

print(f"HTML body chars: {len(html_body)}")
with open("body.html", "w", encoding="utf-8") as f:
    f.write(html_body)
print("Written body.html")
