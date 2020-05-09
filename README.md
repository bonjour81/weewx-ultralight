# weewx-ultralight

### An Ultra lightweight skin for weewx

![Screenshot](https://i.ibb.co/ZXL0D79/screen-ultralight1.png)

This skin request ~10kB download from your browser, so it's very friendly with extremly slow connexion (ie GPRS).
Graphs are loaded only when you click on relevant menu to reduce as much as possible the network traffic.

Here is a screenshot of Firefox inspector:
![Firefox inspector](https://i.ibb.co/dJ0tY0H/screen-ultralight2.png)

Favicon can be modified or removed in case you need even less kB !

[A demo page is visible here](https://www.meteosaintsulpice.fr/ultra/)

<a href="https://validator.w3.org/unicorn/check?ucn_uri=https%3A%2F%2Fwww.meteosaintsulpice.fr%2Fultra%2F&ucn_lang=fr&ucn_task=conformance#">
<img src="https://www.w3.org/html/logo/badge/html5-badge-h-css3-semantics.png" width="165" height="64" alt="HTML5 Powered with CSS3 / Styling, and Semantics" title="HTML5 Powered with CSS3 / Styling, and Semantics">
</a>

### For installation:
```
wget -O ultralight.gz https://github.com/bonjour81/weewx-ultralight/tarball/master 
sudo wee_extension --install ultralight.gz 
```

### For un-install:
```
sudo wee_extension --uninstall ultralight
```
