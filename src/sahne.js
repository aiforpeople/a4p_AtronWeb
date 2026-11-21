(function(){
if(!document.documentElement.classList.contains('js')) return;
function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
function ease(t){return t*t*(3-2*t);}
function band(v,a,b){return clamp((v-a)/(b-a),0,1);}
function ok(m){return m&&m.complete&&m.naturalWidth;}
var acts=[].map.call(document.querySelectorAll('.act'),function(el){
  var cv=el.querySelector('canvas');
  return {el:el, cv:cv, cx:cv.getContext('2d'), n:+el.dataset.n, dir:el.dataset.dir, fx:+(el.dataset.fx||.5), bg:el.dataset.bg||'#cfd0d3',
    b1:el.querySelector('.b1'), b2:el.querySelector('.b2'), clock:el.querySelector('.clock'), hint:el.querySelector('.hint'),
    imgs:null, p:0, W:0, H:0, dpr:1, portrait:false, last:''};
});
function load(a){
  if(a.imgs) return; a.imgs=[];
  for(var i=1;i<=a.n;i++){ (function(i){ var im=new Image(); im.decoding='async'; im.onload=function(){ a.last=''; draw(a); }; im.src=a.dir+'/'+('0'+i).slice(-2)+'.webp'; a.imgs[i-1]=im; })(i); }
}
function size(a){
  a.dpr=Math.min(devicePixelRatio||1,2); a.W=a.cv.clientWidth; a.H=a.cv.clientHeight; a.cv.width=Math.round(a.W*a.dpr); a.cv.height=Math.round(a.H*a.dpr);
  a.portrait=a.W/a.H<1; a.last=''; draw(a);
}
function rect(a,im){
  var ar=im.naturalWidth/im.naturalHeight, w,h,x,y;
  if(a.portrait){ h=a.H*.60; w=h*ar; x=clamp(a.W/2-a.fx*w,a.W-w,0); y=0; }        // portrait: top 60%, centred on the act's subject
  else { var s=Math.max(a.W/(ar*900),a.H/900); w=ar*900*s; h=900*s; x=(a.W-w)*(a.fx<.5?0:1); y=(a.H-h)/2; }   // landscape: cover, pinned to the subject's side
  return {x:x,y:y,w:w,h:h};
}
function nearest(a,i){ var im=a.imgs&&a.imgs[i]; if(a.imgs) for(var d=1; !ok(im)&&d<a.n; d++){ im=ok(a.imgs[i-d])?a.imgs[i-d]:(ok(a.imgs[i+d])?a.imgs[i+d]:im); } return im; }
function draw(a){
  if(!a.W) return;
  var p=a.p, cx=a.cx, im, im2=null, al=0;
  if(a.n<5){ al=ease(band(p,.36,.58)); im=nearest(a,0); if(al>0&&a.imgs&&ok(a.imgs[a.n-1])) im2=a.imgs[a.n-1]; al=Math.round(al*50)/50; }   // stills: cross-dissolve
  else { im=nearest(a,clamp(Math.floor(band(p,.22,.72)*(a.n-1)),0,a.n-1)); }                                                              // video frames: scrub
  var key=(ok(im)?im.src:'-')+'|'+(im2?al:0);
  if(key!==a.last){ a.last=key;
    cx.setTransform(a.dpr,0,0,a.dpr,0,0); cx.globalAlpha=1; cx.fillStyle=a.bg; cx.fillRect(0,0,a.W,a.H);
    if(ok(im)){ var r=rect(a,im); cx.drawImage(im,r.x,r.y,r.w,r.h); if(im2){ cx.globalAlpha=al; cx.drawImage(im2,r.x,r.y,r.w,r.h); cx.globalAlpha=1; } }
  }
  var mid=a.portrait?'':'translateY(-50%) ';
  if(a.b1){ var o1=1-ease(band(p,.14,.26)); a.b1.style.opacity=o1; a.b1.style.transform=mid+'translateY('+(-24*(1-o1))+'px)'; a.b1.style.pointerEvents=o1<.5?'none':'auto'; }
  var o2=ease(band(p,.66,.78)); a.b2.style.opacity=o2; a.b2.style.transform=mid+'translateY('+(24*(1-o2))+'px)'; a.b2.style.pointerEvents=o2<.5?'none':'auto';
  if(a.hint) a.hint.style.opacity=1-band(p,.02,.1);
  var c0=a.b1?.26:.06, oc=ease(band(p,c0,c0+.08))*(1-ease(band(p,.56,.64))); a.clock.style.opacity=oc; a.clock.style.transform=a.portrait?'':'translateY(calc(-50svh + 110px))';
}
function tickAct(a){
  var r=a.el.getBoundingClientRect(), vh=innerHeight;
  if(r.top<vh*2.5&&r.bottom>-vh*1.5) load(a);          // fetch frames a little before the act arrives
  if(r.bottom<-vh||r.top>vh*2) return;
  var p=clamp(-r.top/(r.height-vh),0,1); if(p!==a.p||!a.last){ a.p=p; draw(a); }
}
// some iOS in-app browsers throttle scroll events: poll every frame instead
(function tick(){ acts.forEach(tickAct); requestAnimationFrame(tick); })();
addEventListener('resize',function(){ acts.forEach(size); });
acts.forEach(size);
window.__ready=true;
})();
