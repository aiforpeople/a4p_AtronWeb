(function(){
if(!document.documentElement.classList.contains('js')) return;
function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
function ease(t){return t*t*(3-2*t);}
function band(v,a,b){return clamp((v-a)/(b-a),0,1);}
function ok(m){return m&&m.complete&&m.naturalWidth;}
var acts=[].map.call(document.querySelectorAll('.act'),function(el){
  var cv=el.querySelector('canvas');
  return {el:el, cv:cv, cx:cv.getContext('2d'), n:+el.dataset.n, dir:el.dataset.dir, fx:+(el.dataset.fx||.5), bg:el.dataset.bg||'#cfd0d3', scrim:+(el.dataset.scrim||0), ax:el.dataset.ax?+el.dataset.ax:null, ay:+(el.dataset.ay||0), ar:+(el.dataset.ar||.03), top:el.querySelector('.top'), next:null,
    b1:el.querySelector('.b1'), b2:el.querySelector('.b2'), b3:el.querySelector('.b3'), clock:el.querySelector('.clock'), hint:el.querySelector('.hint'),
    imgs:null, p:0, W:0, H:0, dpr:1, portrait:false, last:''};
});
acts.forEach(function(a,i){ a.next=acts[i+1]||null; a.prev=acts[i-1]||null; a.stage=a.el.querySelector('.stage'); });
function load(a){
  if(a.imgs) return; a.imgs=[];
  if(a.n>=5){ a.hiA=new Image(); a.hiB=new Image(); a.hiA.onload=a.hiB.onload=function(){ a.last=''; draw(a); }; a.hiA.src=a.dir+'/a.webp'; a.hiB.src=a.dir+'/b.webp'; }   // crisp stills for the resting poses; the softer video frames only show while things move
  for(var i=1;i<=a.n;i++){ (function(i){ var im=new Image(); im.decoding='async'; im.onload=function(){ a.last=''; draw(a); }; im.src=a.dir+'/'+('0'+i).slice(-2)+'.webp'; a.imgs[i-1]=im; })(i); }
}
function size(a){
  a.dpr=Math.min(devicePixelRatio||1,2); a.W=a.cv.clientWidth; a.H=a.cv.clientHeight; a.cv.width=Math.round(a.W*a.dpr); a.cv.height=Math.round(a.H*a.dpr);
  a.portrait=a.W/a.H<1; a.last=''; draw(a);
}
function rect(a,im){
  var ar=16/9, w,h,x,y;   // every scene is 16:9; video frames are a hair off and get stretched to match the stills
  if(a.portrait){ h=a.H*.60; w=h*ar; x=clamp(a.W/2-a.fx*w,a.W-w,0); y=0; }        // portrait: top 60%, centred on the act's subject
  else { var s=Math.max(a.W/(ar*900),a.H/900); w=ar*900*s; h=900*s; x=(a.W-w)*(a.fx<.5?0:1); y=(a.H-h)/2; }   // landscape: cover, pinned to the subject's side
  return {x:x,y:y,w:w,h:h};
}
function nearest(a,i){ var im=a.imgs&&a.imgs[i]; if(a.imgs) for(var d=1; !ok(im)&&d<a.n; d++){ im=ok(a.imgs[i-d])?a.imgs[i-d]:(ok(a.imgs[i+d])?a.imgs[i+d]:im); } return im; }
function rgba(hex,al){ var n=parseInt(hex.slice(1),16); return 'rgba('+(n>>16)+','+((n>>8)&255)+','+(n&255)+','+al+')'; }
// paints one act exactly as its stage shows it (background, picture, text-side scrim) in the size of the given act's canvas
function paint(cx,v,a,im,im2,al){
  cx.fillStyle=a.bg; cx.fillRect(0,0,v.W,v.H);
  if(ok(im)){ var r=rect({W:v.W,H:v.H,portrait:v.portrait,fx:a.fx},im); cx.drawImage(im,r.x,r.y,r.w,r.h); if(im2){ cx.globalAlpha=al; cx.drawImage(im2,r.x,r.y,r.w,r.h); cx.globalAlpha=1; } }
  var g;
  if(v.portrait){ g=cx.createLinearGradient(0,v.H,0,v.H*.44); g.addColorStop(0,a.bg); g.addColorStop(.715,a.bg); g.addColorStop(1,rgba(a.bg,0)); cx.fillStyle=g; cx.fillRect(0,v.H*.44,v.W,v.H*.56+1); }
  else if(a.scrim>0){ var L=a.el.classList.contains('L'); g=cx.createLinearGradient(L?0:v.W,0,L?v.W*.58:v.W*.42,0); g.addColorStop(0,rgba(a.bg,a.scrim)); g.addColorStop(.31,rgba(a.bg,a.scrim)); g.addColorStop(1,rgba(a.bg,0)); cx.fillStyle=g; cx.fillRect(0,0,v.W,v.H); }
}
function draw(a){
  if(!a.W) return;
  var p=a.p, cx=a.cx, im, im2=null, al=0, nx=a.next, t=nx&&a.ax!==null?band(p,.90,1):0;
  if(a.n<5){ al=ease(band(p,.24,.42)); im=nearest(a,0); if(al>0&&a.imgs&&ok(a.imgs[a.n-1])) im2=a.imgs[a.n-1]; al=Math.round(al*50)/50; }   // stills: cross-dissolve
  else { im=nearest(a,clamp(Math.floor(band(p,.16,.50)*(a.n-1)),0,a.n-1));
    if(p<.16&&ok(a.hiA)){ im2=a.hiA; al=1-ease(band(p,.12,.16)); } else if(p>.5&&ok(a.hiB)){ im2=a.hiB; al=ease(band(p,.5,.55)); }
    al=Math.round(al*40)/40; if(al<=0) im2=null; }                                                              // video frames: scrub
  var nim=t>0&&nx.imgs?(ok(nx.hiA)?nx.hiA:nearest(nx,0)):null;
  var key=(ok(im)?im.src:'-')+'|'+(im2?al:0)+'|'+(t>0?t.toFixed(3)+(ok(nim)?'y':'n'):'');
  if(key!==a.last){ a.last=key;
    cx.setTransform(a.dpr,0,0,a.dpr,0,0); cx.globalAlpha=1;
    if(t>0&&ok(im)){
      // exit: the camera pushes into a round object of this scene; the next scene opens inside it
      var r=rect(a,im), ox=r.x+r.w*a.ax, oy=r.y+r.h*a.ay; ox=clamp(ox,0,a.W); oy=clamp(oy,0,a.H);
      var e=t*t*(3-2*t), z=1+e*e*7, R=a.ar*r.w*z*(1+e*.6)+e*e*e*Math.hypot(a.W,a.H)*1.05, k=1.5-.5*e;
      cx.save(); cx.translate(ox,oy); cx.scale(z,z); cx.translate(-ox,-oy); paint(cx,a,a,im,im2,al); cx.restore();
      cx.save(); cx.beginPath(); cx.arc(ox,oy,R,0,6.2832); cx.clip();
      cx.fillStyle=nx.bg; cx.fillRect(0,0,a.W,a.H);
      var nr=ok(nim)?rect({W:a.W,H:a.H,portrait:a.portrait,fx:nx.fx},nim):{x:0,y:0,w:a.W,h:a.H}, sx=nr.x+nr.w*nx.fx, sy=nr.y+nr.h*.5, m=(1-e)*(1-e);   // the next scene's subject starts inside the opening, then settles into place
      cx.translate((ox-sx)*m,(oy-sy)*m); cx.translate(sx,sy); cx.scale(k,k); cx.translate(-sx,-sy); paint(cx,a,nx,nim,null,0); cx.restore();
      if(e<.98){ cx.beginPath(); cx.arc(ox,oy,R,0,6.2832); cx.lineWidth=Math.max(1.5,R*.035*(1-e)); cx.strokeStyle='rgba(0,0,0,'+(.55*(1-e))+')'; cx.stroke(); }
    } else paint(cx,a,a,im,im2,al);
  }
  var mid=a.portrait?'':'translateY(-50%) ', out=nx&&a.ax!==null?1-ease(band(p,.85,.895)):1;
  if(a.b1){ var o1=1-ease(band(p,.10,.18)); a.b1.style.opacity=o1; a.b1.style.transform=mid+'translateY('+(-24*(1-o1))+'px)'; a.b1.style.pointerEvents=o1<.5?'none':'auto'; }
  var i2=ease(band(p,.42,.50)), o2=i2*(1-ease(band(p,.60,.65))); a.b2.style.opacity=o2; a.b2.style.transform=mid+'translateY('+(24*(1-i2)-18*ease(band(p,.60,.65)))+'px)'; a.b2.style.pointerEvents=o2<.5?'none':'auto';
  var i3=ease(band(p,.65,.72)), o3=i3*out; a.b3.style.opacity=o3; a.b3.style.transform=mid+'translateY('+(24*(1-i3))+'px)'; a.b3.style.pointerEvents=o3<.5?'none':'auto';
  if(a.top) a.top.style.opacity=out;
  if(a.hint) a.hint.style.opacity=1-band(p,.02,.1);
  var c0=a.b1?.19:.04, oc=ease(band(p,c0,c0+.06))*(1-ease(band(p,.36,.42))); a.clock.style.opacity=oc; a.clock.style.transform=a.portrait?'':'translateY(calc(-50svh + 110px))';
}
function tickAct(a){
  var r=a.el.getBoundingClientRect(), vh=innerHeight;
  if(a.prev){ var hid=r.top>.5; if(hid!==a.hid){ a.hid=hid; a.stage.style.visibility=hid?'hidden':'visible'; } }   // acts overlap by one screen: stay hidden until the previous exit has finished
  if(r.top<vh*2.5&&r.bottom>-vh*1.5){ load(a); if(a.next&&r.top<vh) load(a.next); }          // fetch frames a little before the act arrives
  if(r.bottom<-vh||r.top>vh*2) return;
  var p=clamp(-r.top/(r.height-vh),0,1); if(p!==a.p||!a.last||p>.89){ a.p=p; draw(a); }
}
// some iOS in-app browsers throttle scroll events: poll every frame instead
(function tick(){ acts.forEach(tickAct); requestAnimationFrame(tick); })();
addEventListener('resize',function(){ acts.forEach(size); });
acts.forEach(size);
window.__ready=true;
})();
