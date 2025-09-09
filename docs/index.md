# GTM Knowledge Base

Welcome. Choose a path to start exploring.

<div class="kb-grid">

  <div class="kb-card">
    <h3>Cost Optimization</h3>
    <p>Reduce spend & complexity.</p>
    <a class="kb-link" href="pain-points/cost-optimization/">Open</a>
  </div>

  <div class="kb-card">
    <h3>Performance & Scale</h3>
    <p>Throughput, latency, growth.</p>
    <a class="kb-link" href="pain-points/performance-scale/">Open</a>
  </div>

  <div class="kb-card">
    <h3>Resiliency & Ransomware</h3>
    <p>RPO/RTO, immutability.</p>
    <a class="kb-link" href="pain-points/resiliency-ransomware/">Open</a>
  </div>

  <div class="kb-card">
    <h3>Technical</h3>
    <p>Domains → Vendors (ranked).</p>
    <a class="kb-link" href="technical/compute/">Browse</a>
  </div>

</div>

---

_Last updated: <span id="kb-updated-home"></span>_

<script>
(function(){
  var el = document.getElementById('kb-updated-home');
  if (!el) return;
  var d = new Date(document.lastModified);
  function pad(n){ return n.toString().padStart(2,'0'); }
  var h = d.getHours(), ampm = h>=12?'PM':'AM'; h = h%12||12;
  el.textContent = pad(d.getMonth()+1)+'/'+pad(d.getDate())+'/'+d.getFullYear()+' '+h+':'+pad(d.getMinutes())+' '+ampm;
})();
</script>
