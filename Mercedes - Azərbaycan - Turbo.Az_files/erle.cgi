
function httplize(s){return ((/^\/\//).test(s) ? ((location.protocol == 'https:')?'https:':'http:') : '') + s} 
var ar_q = '';
if(ar_q.indexOf("ad_google")!=-1){
	var ar_e = ar_q.indexOf("100=");ar_q = ar_q.slice(ar_e+4); ar_q=ar_q.split(';');
	var CgiHref =unescape(ar_q[0])+'https://ad.adriver.ru/cgi-bin/click.cgi?sid=220552&ad=732548&bid=8346581&bt=43&bn=6&pz=0&nid=0&ref=https:%2f%2fturbo.az%2fautos%3fq%255Bmake%255D%255B%255D%3d4&custom=&xpid=DxgmHYrtNX1S-kaW5acouuBP7OETphlET0hTLPx6U7QFHlE5PsGQsVQUVjGbCvcdwCRc9Ci01ay_DyXRT2iLXO6zFNg2J';
}else{
	var CgiHref = 'https://ad.adriver.ru/cgi-bin/click.cgi?sid=220552&ad=732548&bid=8346581&bt=43&bn=6&pz=0&nid=0&ref=https:%2f%2fturbo.az%2fautos%3fq%255Bmake%255D%255B%255D%3d4&erir=&custom=&xpid=DxgmHYrtNX1S-kaW5acouuBP7OETphlET0hTLPx6U7QFHlE5PsGQsVQUVjGbCvcdwCRc9Ci01ay_DyXRT2iLXO6zFNg2J';
}
var ar_bt=43;
var ar_siteid = 220552;
var Mirror = 'https://mlb1.adriver.ru';
var bid = 8346581;
var sliceid = 2978637;
var ar_adid = 732548;
var ar_pz=0;
var ar_sz='%2fautos%3fq%255Bmake%255D%255B%255D%3d4';
var ar_nid=0;
var ar_pass='';
var ar_bn=6;
var ar_geozoneid=378;
var Path = '/images/0008346/0008346581/';
var Comp0 = '0/script.js';
var Width = 0;
var Height = 100;
var date = 'Sun, 25 Dec 2022 14:57:07 GMT';
var Uid = 918271932726;
var Target = '_blank';
var Alt = 'AdRiver';
var CompPath = Mirror + Path + '0/';
var RndNum4NoCash = 944979068;
var ar_ntype = 0;
var ar_tns = 0;
var ar_rhost='ad.adriver.ru';
var ar_exposure_price = 0;
var ar_xpid = 'DxgmHYrtNX1S-kaW5acouuBP7OETphlET0hTLPx6U7QFHlE5PsGQsVQUVjGbCvcdwCRc9Ci01ay_DyXRT2iLXO6zFNg2J';
if (typeof(ar_tansw) != 'undefined') clearInterval(ar_tansw);
var ar_script = '<script src="' + Mirror + Path + Comp0 + '?944979068" type="text/javascript" charset="windows-1251"><\/script>';
function loadScript(req){try {var head = parent.document.getElementsByTagName('head')[0],s = parent.document.createElement('script');s.setAttribute('type', 'text/javascript');s.setAttribute('charset', 'windows-1251');s.setAttribute('src', req.split('rnd').join(Math.round(Math.random()*9999999)));s.onreadystatechange = function(){if(/loaded|complete/.test(this.readyState)){head.removeChild(s);s.onload = null;}};s.onload = function(){head.removeChild(s);};head.insertBefore(s, head.firstChild);}catch(e){}}
if (typeof(ar_bnum)=='undefined') {var ar_bnum = 1;}
var ad_id = 'ad_ph_' + ar_bnum;
if (typeof(window.parent.AdriverViewability)=="undefined"){window.parent.AdriverViewability = true;loadScript("//content.adriver.ru/banners/0002186/0002186173/0/AV.js")}
window.parent.adriverviewability = window.parent.adriverviewability || {};
window.parent.adriverviewability.v = window.parent.adriverviewability.v || [];
window.parent.adriverviewability.v.push (function (){window.parent.adriverviewability[ad_id] = new window.parent.AdriverViewability('//ad.adriver.ru/cgi-bin/event.cgi?xpid=DxgmHYrtNX1S-kaW5acouuBP7OETphlET0hTLPx6U7QFHlE5PsGQsVQUVjGbCvcdwCRc9Ci01ay_DyXRT2iLXO6zFNg2J&bid=8346581&type=',0,ad_id);});
document.write(ar_script);
	  
(function initAdMarking() {
        try {
            if (window.parent.AdR && window.parent.AdR.AdMarking) {
                new window.parent.AdR.AdMarking({
                    
                    containerid: 'ad_ph_' + ar_bnum,
                    erirId: ""
                });
            } else {
                var script = parent.document.createElement("script"),
                    opt = { once: true };
                script.setAttribute('src', 'https://content.adriver.ru/ad-marking.js');
                script.setAttribute('charset', 'UTF-8');
                function scriptEventHandler(event) {
                    script.parentNode.removeChild(script);
                    if (event.type === "error") return;
                    if (window.parent.AdR) initAdMarking();
                }
                script.addEventListener("load", scriptEventHandler, opt);
                script.addEventListener("error", scriptEventHandler, opt);
                parent.document.head.appendChild(script);
            }
        } catch (_) {}
    })();

(function (o) {
	var i, w = o.c || window, d = document, y = 31;
	function oL(){
		if (!w.postMessage || !w.addEventListener) {return;}
		if (w.document.readyState == 'complete') {return sL();}
		w.addEventListener('load', sL, false);
	}
	function sL(){try{i.contentWindow.postMessage('pgLd', '*');}catch(e){}}
	function mI(u, oL){
		var i = d.createElement('iframe'); i.setAttribute('src', o.hl(u)); i.onload = oL; with(i.style){width = height = '10px'; position = 'absolute'; top = left = '-10000px'} d.body.appendChild(i);
		return i;
	}
	function st(u, oL){
		if (d.body){return i = mI(u, oL)}
		if(y--){setTimeout(function(){st(u, oL)}, 100)}
	}
	st(o.hl('https://content.adriver.ru/banners/0002186/0002186173/0/s.html?732548&0&0&0&944979068&0&918271932726&378&85.132.11.176&javascript&' + (o.all || 0)), oL);
}({
	hl: function httplize(s){return ((/^\/\//).test(s) ? ((location.protocol == 'https:')?'https:':'http:') : '') + s},
        
        c: parent,
        
	
	all: 1
	
}));
