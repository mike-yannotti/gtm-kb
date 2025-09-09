# GTM Knowledge Base

> Choose a path to start exploring.

<div class="grid cards" markdown>
- :material-cash-multiple: **Cost Optimization**  
  _Reduce spend & complexity._  
  [:material-arrow-right-bold: Open](pain-points/cost-optimization/index.md)
- :material-speedometer: **Performance & Scale**  
  _Throughput, latency, growth._  
  [:material-arrow-right-bold: Open](pain-points/performance-scale/index.md)
- :material-shield-lock: **Resiliency & Ransomware**  
  _RPO/RTO, immutability._  
  [:material-arrow-right-bold: Open](pain-points/resiliency-ransomware/index.md)
- :material-sitemap-outline: **Technical**  
  _Domains → Vendors (ranked)._  
  [:material-arrow-right-bold: Browse](technical/compute/index.md)
</div>

## Recently Added
- Brand colors + UI polish
- Cards on homepage
- Strict build validation enabled

---

_Last updated: <span class="kb-updated-home" data-ts="{{ build_date | d('') }}">{{ build_date }}</span>_

<script>
(function(){
  var el = document.querySelector('.kb-updated-home');
  if (!el) return;
  var s = el.getAttribute('data-ts') || el.textContent;
  if (!s) return;
  var d = new Date(s);
  if (isNaN(d)) { el.textContent = s; return; }
  function pad(n){ return n.toString().padStart(2,'0'); }
  var h = d.getHours(), ampm = h>=12?'PM':'AM'; h = h%12||12;
  el.textContent = pad(d.getMonth()+1)+'/'+pad(d.getDate())+'/'+d.getFullYear()+' '+h+':'+pad(d.getMinutes())+' '+ampm;
})();
</script>
