/* Fragment Highlight version 0.1 */

//*** This JavaScript highlight code is copyright 2003 by David Dorward; http://dorward.me.uk
//*** Re-use or modification permitted provided the previous line is included and
//*** modifications are indicated

/*********** Start of JavaScript Library *********/

//*** This JavaScript library is copyright 2002 by Gavin Kistner and Refinery; www.refinery.com
//*** Re-use or modification permitted provided the previous line is included

//Adds a new class to an object, preserving existing classes
function AddClass(obj,cName){ KillClass(obj,cName); return obj.className+=(obj.className.length>0?' ':'')+cName; }

//Removes a particular class from an object, preserving other existing classes.
function KillClass(obj,cName){ return obj.className=obj.className.replace(new RegExp("^"+cName+"\\b\\s*|\\s*\\b"+cName+"\\b",'g'),''); }

/*********** End of JavaScript Library ***********/

/* Fragment Highlight */

/* Indicates area that has been linked to if fragment identifiers have
 * been used. Especially useful in situations where a short fragment
 * is near the end of a page. */

var fragHLed = '';
var fragExclude = ('header');

Array.prototype.search = function(myVariable) { for(x in this) if(x == myVariable) return true; return false; }

/* Highlight link target if the visitor arrives at the page with a # */

function fragHLload() {
    fragHL(location.hash.substring(1));
}

/* Highlight link target from an onclick event after unhighlighting the old one */

function fragHL(frag) {
    if (fragHLed.length > 0 && document.getElementById(fragHLed)) {
	KillClass(document.getElementById(fragHLed),'fragment');
    }
    if (frag.length > 0 && document.getElementById(frag)) {
	fragHLed = frag;
	AddClass (document.getElementById(frag),'fragment');
    }
}

/* Add onclick events to all <a> with hrefs that include a "#"  */

function fragHLlink() {
    if (document.getElementsByTagName) {
	var an = document.getElementsByTagName('a');
	for (i=0; i<an.length; i++) {
	    if (an.item(i).getAttribute('href').indexOf('#') >= 0) {
		var fragment = an.item(i).getAttribute('href').substring(an.item(i).getAttribute('href').indexOf('#') + 1);
		if (fragExclude.search(fragment)) {
		    var evn = "fragHL('" + fragment + "')";
		    var fun = new Function('e',evn);
		    an.item(i).onclick = fun;
		}
	    } 
	}
    }
} 

/* Init the script */

window.onload = function(){
    fragHLload();
    fragHLlink();
};
