// Pop-Up Embedder Script by David Battino, www.batmosphere.com
// Version 2006-05-31
// OK to use if this notice is included

function replaceAll( str, searchTerm, replaceWith, ignoreCase )	{
	var regex = "/"+searchTerm+"/g";
	if( ignoreCase ) regex += "i";
	return str.replace( eval(regex), replaceWith );
}

function BatmoAudioPop(filedesc,filepath,WindowNumber)
{
// Get Operating System
var isWin = navigator.userAgent.toLowerCase().indexOf("windows") != -1
if (isWin) {
    // Use MIME type = "application/x-mplayer2";
	visitorOS="Windows";
} else {
    // Use MIME type = "audio/mpeg"; // or audio/x-wav or audio/x-ms-wma, etc.
	visitorOS="Other";
}

// Get the MIME type of the audio file from its extension (for non-Windows browsers)
var mimeType = "audio/mpeg"; // assume MP3/M3U
var objTypeTag = "application/x-mplayer2"; // The Windows MIME type to load the WMP plug-in in Firefox, etc.

var theExtension = filepath.substr(filepath.lastIndexOf('.')+1, 3); // truncates .aiff to aif
if (theExtension.toLowerCase() == "wav") { mimeType = "audio/x-wav"};
if (theExtension.toLowerCase() == "aif") { mimeType = "audio/x-aiff"};
if (theExtension.toLowerCase() == "wma") { mimeType = "audio/x-ms-wma"};
if (theExtension.toLowerCase() == "mid") { mimeType = "audio/mid"};
// Add additional MIME types as desired

var audioFile = replaceAll(filepath, "%20", " ", false);
if (visitorOS != "Windows") {
objTypeTag = mimeType; // audio/mpeg, audio/x-wav, audio/x-ms-wma, etc.
};

    PlayerWin = window.open('',WindowNumber,'width=320,height=180,top=0,left=0,screenX=0,screenY=0,resizable=0,scrollbars=0,titlebar=0,toolbar=0,menubar=0,status=0,directories=0');

    PlayerWin.focus();
    PlayerWin.document.writeln("<html><head><title>" + filedesc + "</title></head>");
    PlayerWin.document.writeln("<body bgcolor='#0063A5'>"); // specify background img if desired
    PlayerWin.document.writeln("<div align='center'>");
    PlayerWin.document.writeln("<b style ='font-size:16px;font-family:Verdana,Lucida,sans-serif;line-height:1.6;color:white'>" + filedesc + "</b><br />");
    PlayerWin.document.writeln("<object width='280' height='69'>");
    PlayerWin.document.writeln("<param name='src' value='" + audioFile + "'>");
    PlayerWin.document.writeln("<param name='type' value='" + objTypeTag + "'>");
    PlayerWin.document.writeln("<param name='autostart' value='1'>");
    PlayerWin.document.writeln("<param name='showcontrols' value='1'>");
    PlayerWin.document.writeln("<param name='showstatusbar' value='1'>");
    PlayerWin.document.writeln("<embed src ='" + audioFile + "' type='" + objTypeTag + "' autoplay='true' width='280' height='69' controller='1' showstatusbar='1' bgcolor='#0063A5' kioskmode='true'>");
    PlayerWin.document.writeln("</embed></object></div>");
    PlayerWin.document.writeln("<form><div align='center'><input type='button' value='Close' onclick='javascript:window.close();'></div></form>");
    PlayerWin.document.writeln("</body></html>");

    PlayerWin.document.close(); // "Finalizes" new window
}
