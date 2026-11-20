(function(){
if(!document.documentElement.classList.contains('js')) return;
var IW=848, IH=480, PAPER='#cfd0d3';
function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
function ease(t){return t*t*(3-2*t);}
function band(v,a,b){return clamp((v-a)/(b-a),0,1);}
function ok(m){return m&&m.complete&&m.naturalWidth;}
var acts=[].map.call(document.querySelectorAll('.act'),function(el){
  var cv=el.querySelector('canvas');
  return {el:el, cv:cv, cx:cv.getContext('2d'), n:+el.dataset.n, dir:el.dataset.dir,
    ax:el.dataset.ax?+el.dataset.ax:null, ay:el.dataset.ay?+el.dataset.ay:null,
    b1:el.querySelector('.b1'), b2:el.querySelector('.b2'), clock:el.querySelector('.clock'), hint:el.querySelector('.hint'),
    lp:el.querySelector('svg.lead path'), lc:el.querySelector('svg.lead circle'),
    imgs:null, p:0, W:0, H:0, dpr:1, rect:null, portrait:false, last:''};
});
function load(a){
  if(a.imgs) return; a.imgs=[];
  for(var i=1;i<=a.n;i++){ (function(i){ var im=new Image(); im.decoding='async'; im.onload=function(){ a.last=''; draw(a); }; im.src=a.dir+'/'+('0'+i).slice(-2)+'.webp'; a.imgs[i-1]=im; })(i); }
}
function size(a){
  a.dpr=Math.min(devicePixelRatio||1,2); a.W=a.cv.clientWidth; a.H=a.cv.clientHeight; a.cv.width=Math.round(a.W*a.dpr); a.cv.height=Math.round(a.H*a.dpr);
  a.portrait=a.W/a.H<1; var s,x,y;
  if(a.portrait){ s=(a.W*1.55)/IW; x=-a.W*0.04; y=a.H*0.13; }   // portrait: left 65% of the frame, top half
  else { s=Math.max(a.W/IW,a.H/IH); x=0; y=(a.H-IH*s)/2; }
  a.rect={x:x,y:y,w:IW*s,h:IH*s}; a.last=''; draw(a);
}
function draw(a){
  if(!a.W||!a.rect) return;
  var p=a.p, r=a.rect, cx=a.cx, t=band(p,.22,.72)*(a.n-1), i0=clamp(a.n<5?Math.round(t):Math.floor(t),0,a.n-1), im=a.imgs&&a.imgs[i0];
  // still loading: show the nearest frame that has arrived
  if(a.imgs) for(var d=1; !ok(im)&&d<a.n; d++){ im=ok(a.imgs[i0-d])?a.imgs[i0-d]:(ok(a.imgs[i0+d])?a.imgs[i0+d]:im); }
  var key=(ok(im)?im.src:'-');
  if(key!==a.last){ a.last=key;
    cx.setTransform(a.dpr,0,0,a.dpr,0,0); cx.fillStyle=PAPER; cx.fillRect(0,0,a.W,a.H);
    if(ok(im)) cx.drawImage(im,r.x,r.y,r.w,r.h);
    if(a.portrait){ var g=cx.createLinearGradient(0,r.y+r.h-24,0,r.y+r.h); g.addColorStop(0,'rgba(207,208,211,0)'); g.addColorStop(1,PAPER); cx.fillStyle=g; cx.fillRect(0,r.y+r.h-24,a.W,25);
      g=cx.createLinearGradient(0,r.y,0,r.y+50); g.addColorStop(0,PAPER); g.addColorStop(1,'rgba(207,208,211,0)'); cx.fillStyle=g; cx.fillRect(0,r.y-1,a.W,51); }
  }
  var mid=a.portrait?'':'translateY(-50%) ';
  if(a.b1){ var o1=1-ease(band(p,.14,.26)); a.b1.style.opacity=o1; a.b1.style.transform=mid+'translateY('+(-24*(1-o1))+'px)'; a.b1.style.pointerEvents=o1<.5?'none':'auto'; }
  var o2=ease(band(p,.70,.82)); a.b2.style.opacity=o2; a.b2.style.transform=mid+'translateY('+(24*(1-o2))+'px)'; a.b2.style.pointerEvents=o2<.5?'none':'auto';
  if(a.hint) a.hint.style.opacity=1-band(p,.02,.1);
  var c0=a.b1?.24:.04, oc=ease(band(p,c0,c0+.08))*(1-ease(band(p,.62,.70))); a.clock.style.opacity=oc; a.clock.style.transform=a.portrait?'':'translateY(calc(-50svh + 110px))';
  if(a.ax===null){ a.lp.style.display='none'; a.lc.style.display='none'; return; }
  // leader line: object in the final pose -> the label
  var hx=r.x+r.w*a.ax, hy=r.y+r.h*a.ay, kb=a.b2.querySelector('.k').getBoundingClientRect(), sb=a.cv.getBoundingClientRect();
  var tx=kb.left-sb.left-14, ty=kb.top-sb.top+kb.height/2;
  if(a.portrait){ hx=r.x+r.w*(a.ax+.028); tx=kb.left-sb.left+3; a.lp.setAttribute('d','M'+hx+' '+hy+' L'+hx+' '+(ty-34)+' L'+tx+' '+(ty-34)+' L'+tx+' '+(ty-12)); }
  else { var mx=hx+(tx-hx)*.45; a.lp.setAttribute('d','M'+hx+' '+hy+' L'+mx+' '+ty+' L'+tx+' '+ty); }
  var L=a.lp.getTotalLength(); a.lp.style.strokeDasharray=L; a.lp.style.strokeDashoffset=L*(1-ease(band(p,.72,.84)));
  a.lc.setAttribute('cx',hx); a.lc.setAttribute('cy',hy); a.lc.style.opacity=band(p,.71,.74);
}
function tickAct(a){
  var r=a.el.getBoundingClientRect(), vh=innerHeight;
  if(r.top<vh*2.5&&r.bottom>-vh*1.5) load(a);          // fetch frames a little before the act arrives
  if(r.bottom<-vh||r.top>vh*2) return;                  // far away: nothing to draw
  var p=clamp(-r.top/(r.height-vh),0,1); if(p!==a.p||!a.last){ a.p=p; draw(a); }
}
// some iOS in-app browsers throttle scroll events: poll every frame instead
(function tick(){ acts.forEach(tickAct); requestAnimationFrame(tick); })();
addEventListener('resize',function(){ acts.forEach(size); });
acts.forEach(size);
if(document.fonts&&document.fonts.ready) document.fonts.ready.then(function(){ acts.forEach(function(a){ draw(a); }); });
window.__ready=true;
})();
