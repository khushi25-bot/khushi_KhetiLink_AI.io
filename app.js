
// ─── DATA ───────────────────────────────────────────────────────────────
const BUYERS = [
  {id:1,name:'Shree Gujarat Ginners',type:'Cotton Buyer · Gin Factory',crop:'cotton',price:7350,dist:18,pickup:true,rating:4.7,match:92,qty:'10–50q',grade:'Grade A',aboveMandi:200,
   why:['Accepts Grade A cotton','Quantity matches your 25 quintals','Offers ₹200/q above current mandi average','Located only 18 km away','Pickup available — no transport cost','Strong transaction history & reliable payments']},
  {id:2,name:'Patel Cotton Industries',type:'Cotton Processor',crop:'cotton',price:7280,dist:8,pickup:false,rating:4.4,match:86,qty:'5–30q',grade:'Grade A/B',aboveMandi:130,
   why:['Accepts Grade A/B cotton','Only 8 km away — minimal transport','Competitive price at ₹7,280/q','Established processor with 10+ years','Flexible payment terms available']},
  {id:3,name:'Gujarat Agro Traders',type:'Cotton & Groundnut Broker',crop:'cotton',price:7200,dist:22,pickup:true,match:78,rating:4.2,qty:'20–100q',grade:'Grade A/B/C',aboveMandi:50,
   why:['Accepts all cotton grades','Large quantity capacity — up to 100q','Pickup available','Broad crop portfolio buyer']},
  {id:4,name:'Saurashtra Oil Mills',type:'Groundnut Processor',crop:'groundnut',price:5950,dist:12,pickup:true,rating:4.6,match:89,qty:'10–80q',grade:'Grade A',aboveMandi:130,
   why:['Accepts Grade A groundnut','Offers ₹130/q above current mandi','Pickup available within 12 km','Leading oil mill in Saurashtra','Consistent buyer — reliable payments']},
  {id:5,name:'Junagadh Groundnut Co.',type:'Groundnut Exporter',crop:'groundnut',price:5900,dist:35,pickup:false,rating:4.5,match:82,qty:'50–200q',grade:'Grade A',aboveMandi:80,
   why:['Export quality groundnut buyer','Higher volume requirements (50q+)','Good price for large quantities','Reputed exporter with 15+ years']},
  {id:6,name:'Rajkot Commodities',type:'Multi-Crop Trader',crop:'cotton',price:7150,dist:5,pickup:true,rating:4.1,match:71,qty:'5–50q',grade:'All Grades',aboveMandi:0,
   why:['Very close — only 5 km away','Accepts all cotton grades','Pickup available','Offers mandi price — no premium']},
];

const COTTON_DATA = {
  '7d': {
    labels:['Day -7','Day -6','Day -5','Day -4','Day -3','Day -2','Yesterday','Today','Day +1','Day +2','Day +3','Day +4','Day +5','Day +6','Day +7'],
    hist:[7020,7040,7010,7080,7090,7100,7110,7150,null,null,null,null,null,null,null],
    forecast:[null,null,null,null,null,null,null,7150,7180,7220,7280,7350,7390,7420,7480],
    current:'₹7,150/q',forecast_sum:'₹7,420/q',trend:'↑ Bullish',conf:'84%',
    summary:'Cotton prices are on an upward trend. The current mandi price of ₹7,150/q is 2.4% above yesterday. AI forecasts prices reaching ₹7,400–₹7,550/q over the next 7 days based on procurement patterns and seasonal demand.'
  },
  '30d': {
    labels:['Week -4','Week -3','Week -2','Week -1','This Week','Week +1','Week +2','Week +3','Week +4'],
    hist:[6900,6950,7000,7050,7150,null,null,null,null],
    forecast:[null,null,null,null,7150,7250,7350,7420,7500],
    current:'₹7,150/q',forecast_sum:'₹7,500/q',trend:'↑ Bullish',conf:'78%',
    summary:'Over the past 30 days, cotton prices have risen by approximately 3.6% from ₹6,900 to ₹7,150/q. AI forecasts continued upward movement driven by increased gin factory demand and reduced arrivals in mandis.'
  },
  today: {
    labels:['9 AM','10 AM','11 AM','12 PM','1 PM','2 PM','3 PM','4 PM','5 PM','Forecast 6 PM'],
    hist:[7100,7110,7120,7130,7140,7145,7148,7150,7150,null],
    forecast:[null,null,null,null,null,null,null,null,7150,7170],
    current:'₹7,150/q',forecast_sum:'₹7,170/q',trend:'↑ Steady',conf:'91%',
    summary:'Today cotton has traded steadily from ₹7,100 at market open to ₹7,150/q at close. AI expects slight evening gain to ₹7,170 based on demand from major gin factories in Ahmedabad.'
  }
};

const GROUNDNUT_DATA = {
  '7d': {
    labels:['Day -7','Day -6','Day -5','Day -4','Day -3','Day -2','Yesterday','Today','Day +1','Day +2','Day +3','Day +4','Day +5','Day +6','Day +7'],
    hist:[5740,5760,5770,5790,5800,5810,5815,5820,null,null,null,null,null,null,null],
    forecast:[null,null,null,null,null,null,null,5820,5840,5860,5880,5900,5920,5950,5990],
    current:'₹5,820/q',forecast_sum:'₹5,950/q',trend:'↑ Moderate',conf:'79%',
    summary:'Groundnut prices show steady upward movement. Current mandi price is ₹5,820/q, up 1.1% from yesterday. AI forecasts ₹5,900–₹6,000/q over 7 days driven by oil mill demand and post-harvest market dynamics.'
  },
  '30d': {
    labels:['Week -4','Week -3','Week -2','Week -1','This Week','Week +1','Week +2','Week +3','Week +4'],
    hist:[5600,5650,5700,5750,5820,null,null,null,null],
    forecast:[null,null,null,null,5820,5880,5930,5970,6010],
    current:'₹5,820/q',forecast_sum:'₹6,010/q',trend:'↑ Bullish',conf:'75%',
    summary:'Groundnut has gained 3.9% over the past month. Strong oil mill procurement is the primary driver. 30-day AI forecast targets ₹6,000–₹6,050/q if current demand holds steady.'
  },
  today: {
    labels:['9 AM','10 AM','11 AM','12 PM','1 PM','2 PM','3 PM','4 PM','5 PM','Forecast 6 PM'],
    hist:[5790,5795,5800,5805,5810,5815,5818,5820,5820,null],
    forecast:[null,null,null,null,null,null,null,null,5820,5835],
    current:'₹5,820/q',forecast_sum:'₹5,835/q',trend:'↑ Steady',conf:'88%',
    summary:'Groundnut trading steadily today. Opened at ₹5,790 and closed at ₹5,820/q. AI expects ₹5,835 by close driven by late afternoon oil mill procurement.'
  }
};

const AI_RESULTS = {
  cotton: {
    rec:'⏳ WAIT & MONITOR', recClass:'wait',
    price:'₹7,150/q',exp:'₹7,400–₹7,550/q',buyer:'₹7,350/q',bname:'Shree Gujarat Ginners',conf:'84%',opp:'₹6,250–₹10,000',risk:'Medium',
    insight:'Current buyer offers are competitive, but the market trend suggests that prices may improve over the next few days. The AI therefore recommends monitoring the market before making the final sale.',
    factors:[{name:'Price Trend',val:85,sign:'+++',neg:false},{name:'Buyer Demand',val:70,sign:'++',neg:false},{name:'Buyer Offer',val:68,sign:'++',neg:false},{name:'Market Opportunity',val:72,sign:'++',neg:false},{name:'Storage Cost',val:35,sign:'-',neg:true},{name:'Market Risk',val:40,sign:'-',neg:true}]
  },
  groundnut: {
    rec:'💰 SELL NOW', recClass:'sell',
    price:'₹5,820/q',exp:'₹5,900–₹6,000/q',buyer:'₹5,950/q',bname:'Saurashtra Oil Mills',conf:'79%',opp:'₹5,200–₹8,000',risk:'Low-Medium',
    insight:'Current groundnut buyer offers at ₹5,950/q are already above forecast levels. Oil mill demand is strong right now. AI recommends selling now to capture the current premium before seasonal supply increases.',
    factors:[{name:'Buyer Offer',val:88,sign:'+++',neg:false},{name:'Demand Strength',val:80,sign:'+++',neg:false},{name:'Price Trend',val:65,sign:'++',neg:false},{name:'Market Opportunity',val:70,sign:'++',neg:false},{name:'Supply Risk',val:30,sign:'-',neg:true},{name:'Storage Cost',val:25,sign:'-',neg:true}]
  }
};

// ─── STATE ──────────────────────────────────────────────────────────────
let currentCrop = 'cotton';
let currentRange = '7d';
let priceChart = null;
let incomeChart = null;
let storageAvail = true;

// ─── NAVIGATION ─────────────────────────────────────────────────────────
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const el = document.getElementById('screen-'+id);
  if (el) { el.classList.add('active'); window.scrollTo(0,0); }

  // nav highlight
  const navMap = {dashboard:'nav-dashboard',prices:'nav-prices',advisor:'nav-advisor',buyers:'nav-buyers',produce:'nav-produce'};
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  const navId = navMap[id];
  if (navId) {
    const btn = document.getElementById(navId);
    if (btn) btn.classList.add('active');
  }

  // lazy init charts
  if (id === 'prices') setTimeout(() => initPriceChart(), 100);
  if (id === 'income') setTimeout(() => initIncomeChart(), 100);
  if (id === 'buyers') renderBuyerCards('all');
}

// ─── TOAST ──────────────────────────────────────────────────────────────
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2800);
}

// ─── PRICE CHART ────────────────────────────────────────────────────────
function initPriceChart() {
  const data = (currentCrop === 'cotton' ? COTTON_DATA : GROUNDNUT_DATA)[currentRange];
  const ctx = document.getElementById('priceChart');
  if (!ctx) return;
  if (priceChart) { priceChart.destroy(); }

  // Update stats
  document.getElementById('stat-current').textContent = data.current;
  document.getElementById('stat-forecast').textContent = data.forecast_sum;
  document.getElementById('stat-trend').textContent = data.trend;
  document.getElementById('stat-conf').textContent = data.conf;
  document.getElementById('market-summary').textContent = data.summary;

  priceChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.labels,
      datasets: [
        {
          label: 'Historical',
          data: data.hist,
          borderColor: '#2e7d32',
          backgroundColor: 'rgba(46,125,50,.08)',
          borderWidth: 2.5,
          tension: 0.35,
          pointRadius: 3,
          pointBackgroundColor: '#2e7d32',
          spanGaps: false
        },
        {
          label: 'AI Forecast',
          data: data.forecast,
          borderColor: '#f9a825',
          backgroundColor: 'rgba(249,168,37,.07)',
          borderWidth: 2.5,
          borderDash: [6,4],
          tension: 0.35,
          pointRadius: 3,
          pointBackgroundColor: '#f9a825',
          spanGaps: false
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: ctx => ctx.raw ? '₹' + ctx.raw.toLocaleString('en-IN') + '/q' : null
          }
        }
      },
      scales: {
        x: { grid: { display: false }, ticks: { font: { size: 10 }, maxRotation: 45 } },
        y: {
          grid: { color: 'rgba(0,0,0,.05)' },
          ticks: {
            font: { size: 10 },
            callback: v => '₹' + v.toLocaleString('en-IN')
          }
        }
      }
    }
  });
}

function switchCrop(crop, btn) {
  currentCrop = crop;
  document.querySelectorAll('[id^="crop-"]').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  initPriceChart();
}

function switchRange(range, btn) {
  currentRange = range;
  document.querySelectorAll('[id^="range-"]').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  initPriceChart();
}

// ─── INCOME CHART ───────────────────────────────────────────────────────
function initIncomeChart() {
  const ctx = document.getElementById('incomeChart');
  if (!ctx) return;
  if (incomeChart) { incomeChart.destroy(); }
  incomeChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Cotton', 'Groundnut', 'Other'],
      datasets: [
        { label: 'Estimated Revenue', data: [178750, 232800, 207250], backgroundColor: '#2e7d32' },
        { label: 'Potential Revenue', data: [183750, 238000, 221250], backgroundColor: '#f9a825' }
      ]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: { font: { size: 11 } } },
        y: {
          grid: { color: 'rgba(0,0,0,.05)' },
          ticks: { font: { size: 10 }, callback: v => '₹' + (v/1000).toFixed(0) + 'k' }
        }
      }
    }
  });
}

// ─── BUYERS ─────────────────────────────────────────────────────────────
function renderBuyerCards(filter) {
  const c = document.getElementById('buyer-cards-container');
  if (!c) return;
  let list = [...BUYERS];
  if (filter === 'cotton') list = list.filter(b => b.crop === 'cotton');
  else if (filter === 'groundnut') list = list.filter(b => b.crop === 'groundnut');
  else if (filter === 'pickup') list = list.filter(b => b.pickup);
  else if (filter === 'highprice') list = [...list].sort((a,b) => b.price - a.price);
  else if (filter === 'near') list = list.filter(b => b.dist < 25);

  c.innerHTML = list.map((b,i) => `
    <div class="buyer-card" onclick="showBuyerDetail(${b.id})">
      ${i===0 && filter==='all'?'<div class="top-badge">⭐ TOP MATCH</div>':''}
      <div class="buyer-top">
        <div><div class="buyer-name">🏭 ${b.name}</div><div class="buyer-type">${b.type}</div></div>
        <span class="match-pill">🤖 ${b.match}%</span>
      </div>
      <div class="buyer-price">₹${b.price.toLocaleString('en-IN')} <span>/ Quintal</span></div>
      <div class="buyer-meta">
        <span class="meta-tag">📍 ${b.dist} km</span>
        <span class="meta-tag">${b.pickup?'🚚 Pickup':'🏪 Mill Only'}</span>
        <span class="meta-tag"><span class="star">★</span> ${b.rating}</span>
        <span class="meta-tag">📦 ${b.qty}</span>
        ${b.aboveMandi>0?`<span class="meta-tag" style="color:var(--green);font-weight:600">+₹${b.aboveMandi} above mandi</span>`:''}
      </div>
      <button class="view-btn">View Buyer →</button>
    </div>
  `).join('');
}

function filterBuyers(filter, btn) {
  document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  renderBuyerCards(filter);
}

function showBuyerDetail(id) {
  const b = BUYERS.find(x => x.id === id);
  if (!b) return;
  document.getElementById('detail-name').textContent = b.name;
  document.getElementById('detail-type').textContent = b.type;
  document.getElementById('detail-price').textContent = '₹' + b.price.toLocaleString('en-IN');
  const mandiPrice = b.crop === 'cotton' ? 7150 : 5820;
  document.getElementById('detail-vs').textContent = `Market Average: ₹${mandiPrice.toLocaleString('en-IN')}/q  |  ${b.aboveMandi>0?'₹'+b.aboveMandi+'/q above mandi':'At mandi price'}`;
  document.getElementById('detail-match').textContent = `🤖 AI Match: ${b.match}%`;
  document.getElementById('why-rows').innerHTML = b.why.map(w=>`<div class="why-row"><span class="why-check">✓</span>${w}</div>`).join('');
  document.getElementById('buyer-list-view').style.display = 'none';
  document.getElementById('buyer-detail-view').classList.add('active');
  window.scrollTo(0,0);
}

function showBuyerList() {
  document.getElementById('buyer-list-view').style.display = '';
  document.getElementById('buyer-detail-view').classList.remove('active');
}

// ─── AI ADVISOR ─────────────────────────────────────────────────────────
function setStorage(val) {
  storageAvail = val;
  document.getElementById('stor-yes').classList.toggle('active', val);
  document.getElementById('stor-no').classList.toggle('active', !val);
}

function runAnalysis() {
  const crop = document.getElementById('adv-crop').value.toLowerCase();
  const animEl = document.getElementById('analysis-anim');
  const resultEl = document.getElementById('ai-result');
  animEl.style.display = 'block';
  resultEl.style.display = 'none';
  // Reset steps
  for(let i=1;i<=8;i++){
    document.getElementById('as'+i).classList.remove('visible');
    document.getElementById('ac'+i).classList.remove('done');
  }
  document.getElementById('anim-complete').style.display='none';
  // Animate steps
  const delay = 420;
  for(let i=1;i<=8;i++){
    (function(n){
      setTimeout(()=>{
        document.getElementById('as'+n).classList.add('visible');
        setTimeout(()=>document.getElementById('ac'+n).classList.add('done'), 200);
      }, n*delay);
    })(i);
  }
  setTimeout(()=>{
    document.getElementById('anim-complete').style.display='block';
    showResult(crop);
  }, 8*delay+600);
}

function showResult(crop) {
  const d = AI_RESULTS[crop === 'cotton' ? 'cotton' : 'groundnut'];
  document.getElementById('res-rec').textContent = d.rec;
  document.getElementById('res-price').textContent = d.price;
  document.getElementById('res-exp').textContent = d.exp;
  document.getElementById('res-buyer').textContent = d.buyer;
  document.getElementById('res-bname').textContent = d.bname;
  document.getElementById('res-conf').textContent = d.conf;
  document.getElementById('res-opp').textContent = d.opp;
  document.getElementById('res-risk').textContent = d.risk;
  document.getElementById('conf-display').textContent = d.conf;
  document.getElementById('ai-insight').textContent = d.insight;

  // Factor bars
  const factorContainer = document.querySelector('#ai-result .card .factor-row:first-of-type').parentElement;
  const factorRows = factorContainer.querySelectorAll('.factor-row');
  d.factors.forEach((f,i)=>{
    if(factorRows[i]){
      factorRows[i].querySelector('.factor-name').textContent = f.name;
      const bar = factorRows[i].querySelector('.factor-bar');
      bar.style.width = f.val+'%';
      bar.classList.toggle('neg', f.neg);
      const sign = factorRows[i].querySelector('.factor-sign');
      sign.textContent = f.sign;
      sign.classList.toggle('neg', f.neg);
    }
  });

  document.getElementById('ai-result').style.display = 'block';
  document.getElementById('ai-result').scrollIntoView({behavior:'smooth',block:'start'});
}

// ─── VOICE ──────────────────────────────────────────────────────────────
function triggerVoice() {
  showToast('🎙️ Voice feature — tap an example question below');
}

function showVoiceResp(lang) {
  ['guj','hin','eng'].forEach(l => {
    const el = document.getElementById('voice-resp-'+l);
    if (el) el.style.display = l===lang ? 'block' : 'none';
  });
  document.getElementById('voice-resp-'+lang).scrollIntoView({behavior:'smooth',block:'nearest'});
}

// ─── INIT ────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  renderBuyerCards('all');
});
