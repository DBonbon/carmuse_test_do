!function(){"use strict";var e,t={34972:function(e,t,n){var r=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};t.__esModule=!0;var o=r(n(73609));o.default.widget("IKS.hallorequireparagraphs",{options:{editable:null,uuid:"",blockElements:["dd","div","dl","figure","form","ul","ol","table","p","h1","h2","h3","h4","h5","h6"]},cleanupContentClone:function(e){e.html().length&&!o.default(this.options.blockElements.toString(),e).length&&this.options.editable.execute("formatBlock","p")}})},73609:function(e){e.exports=jQuery}},n={};function r(e){var o=n[e];if(void 0!==o)return o.exports;var i=n[e]={id:e,loaded:!1,exports:{}};return t[e].call(i.exports,i,i.exports,r),i.loaded=!0,i.exports}r.m=t,e=[],r.O=function(t,n,o,i){if(!n){var u=1/0;for(f=0;f<e.length;f++){n=e[f][0],o=e[f][1],i=e[f][2];for(var l=!0,a=0;a<n.length;a++)(!1&i||u>=i)&&Object.keys(r.O).every((function(e){return r.O[e](n[a])}))?n.splice(a--,1):(l=!1,i<u&&(u=i));l&&(e.splice(f--,1),t=o())}return t}i=i||0;for(var f=e.length;f>0&&e[f-1][2]>i;f--)e[f]=e[f-1];e[f]=[n,o,i]},r.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return r.d(t,{a:t}),t},r.d=function(e,t){for(var n in t)r.o(t,n)&&!r.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},r.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),r.hmd=function(e){return(e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:function(){throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.j=61,function(){var e={61:0};r.O.j=function(t){return 0===e[t]};var t=function(t,n){var o,i,u=n[0],l=n[1],a=n[2],f=0;for(o in l)r.o(l,o)&&(r.m[o]=l[o]);if(a)var c=a(r);for(t&&t(n);f<u.length;f++)i=u[f],r.o(e,i)&&e[i]&&e[i][0](),e[u[f]]=0;return r.O(c)},n=self.webpackChunkwagtail=self.webpackChunkwagtail||[];n.forEach(t.bind(null,0)),n.push=t.bind(null,n.push.bind(n))}(),r.O(void 0,[751],(function(){return r(34972)}));var o=r.O(void 0,[751],(function(){return r(90971)}));o=r.O(o)}();
//# sourceMappingURL=hallo-requireparagraphs.js.map