!function(){"use strict";var e,t={45585:function(e,t,n){var r=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};t.__esModule=!0;var o=r(n(73609));window.createPageChooser=function(e,t,n){var r=o.default("#"+e+"-chooser"),a=r.find(".title"),i=o.default("#"+e),u=r.find(".edit-link"),l=r.data("chooserUrl"),c=null;i.val()&&(c={id:i.val(),parentId:t,adminTitle:a.text(),editUrl:u.attr("href")});var f={getState:function(){return c},getValue:function(){return c&&c.id},setState:function(e){e?(i.val(e.id),a.text(e.adminTitle),r.removeClass("blank"),u.attr("href",e.editUrl)):(i.val(""),r.addClass("blank")),c=e},getTextLabel:function(e){if(!c)return null;var t=c.adminTitle;return e&&e.maxLength&&t.length>e.maxLength?t.substring(0,e.maxLength-1)+"…":t},focus:function(){o.default(".action-choose",r).focus()},openChooserModal:function(){var e=l;c&&c.parentId&&(e+=c.parentId+"/");var t={page_type:n.model_names.join(",")};n.can_choose_root&&(t.can_choose_root="true"),n.user_perms&&(t.user_perms=n.user_perms),ModalWorkflow({url:e,urlParams:t,onload:PAGE_CHOOSER_MODAL_ONLOAD_HANDLERS,responses:{pageChosen:function(e){f.setState(e)}}})},clear:function(){f.setState(null)}};return o.default(".action-choose",r).on("click",(function(){f.openChooserModal()})),o.default(".action-clear",r).on("click",(function(){f.clear()})),f}},73609:function(e){e.exports=jQuery}},n={};function r(e){var o=n[e];if(void 0!==o)return o.exports;var a=n[e]={id:e,loaded:!1,exports:{}};return t[e].call(a.exports,a,a.exports,r),a.loaded=!0,a.exports}r.m=t,e=[],r.O=function(t,n,o,a){if(!n){var i=1/0;for(c=0;c<e.length;c++){n=e[c][0],o=e[c][1],a=e[c][2];for(var u=!0,l=0;l<n.length;l++)(!1&a||i>=a)&&Object.keys(r.O).every((function(e){return r.O[e](n[l])}))?n.splice(l--,1):(u=!1,a<i&&(i=a));u&&(e.splice(c--,1),t=o())}return t}a=a||0;for(var c=e.length;c>0&&e[c-1][2]>a;c--)e[c]=e[c-1];e[c]=[n,o,a]},r.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return r.d(t,{a:t}),t},r.d=function(e,t){for(var n in t)r.o(t,n)&&!r.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},r.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),r.hmd=function(e){return(e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:function(){throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.j=957,function(){var e={957:0};r.O.j=function(t){return 0===e[t]};var t=function(t,n){var o,a,i=n[0],u=n[1],l=n[2],c=0;for(o in u)r.o(u,o)&&(r.m[o]=u[o]);if(l)var f=l(r);for(t&&t(n);c<i.length;c++)a=i[c],r.o(e,a)&&e[a]&&e[a][0](),e[i[c]]=0;return r.O(f)},n=self.webpackChunkwagtail=self.webpackChunkwagtail||[];n.forEach(t.bind(null,0)),n.push=t.bind(null,n.push.bind(n))}(),r.O(void 0,[751],(function(){return r(45585)}));var o=r.O(void 0,[751],(function(){return r(90971)}));o=r.O(o)}();
//# sourceMappingURL=page-chooser.js.map