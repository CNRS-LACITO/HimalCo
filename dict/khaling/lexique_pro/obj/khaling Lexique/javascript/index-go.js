/* Go to lexical entry from Index page - and highlight it */

function go(a,b) 
{ 
    parent.basefrm.location="../lexicon/" + a + ".htm#e" + b; 
    parent.basefrm.fragHLload();
}
