# Installer four ultralight weewx skin
# F.Stuyk, 2020

from weecfg.extension import ExtensionInstaller

def loader():
    return ultralightInstaller()

class ultralightInstaller(ExtensionInstaller):
    def __init__(self):
        super(ultralightInstaller, self).__init__(
            version = "0.1",
            name = 'ultralight',
            description = 'An ultra light weight skin',
            author = "F.Stuyk",
            author_email = "bonjour81@runbox.com",
            config={
                'StdReport': {
                    'ultralight': {
                        'skin':'ultralight',
                        'HTML_ROOT':'ultra'}}},
            files=[('skins/ultralight',
                    ['skins/ultralight/index.html.tmpl',
                    'skins/ultralight/skin.conf']),
                   ('skins/ultralight/js',
                    ['skins/ultralight/js/collapsible.js']),
                   ('skins/ultralight/css',
                    ['skins/ultralight/css/mobile.css']),
                   ('skins/ultralight/images',
                    ['skins/ultralight/images/arrow_down.gif',
                     'skins/ultralight/images/arrow_up.gif',
                     'skins/ultralight/images/b.gif',
                     'skins/ultralight/images/nav-current.jpg',
                     'skins/ultralight/images/nav.jpg'])
                   ('skins/ultralight/favicon',
                    ['skins/ultralight/favicon/android-chrome-192x192.png',
                     'skins/ultralight/favicon/android-chrome-512x512.png',
                     'skins/ultralight/favicon/apple-touch-icon.png',
                     'skins/ultralight/favicon/browserconfig.xml',
                     'skins/ultralight/favicon/favicon.ico',
                     'skins/ultralight/favicon/favicon-16x16.png',
                     'skins/ultralight/favicon/favicon-32x32.png',
                     'skins/ultralight/favicon/mstile-70x70.png',
                     'skins/ultralight/favicon/mstile-144x144.png',
                     'skins/ultralight/favicon/mstile-150x150.png',
                     'skins/ultralight/favicon/mstile-310x150.png',
                     'skins/ultralight/favicon/mstile-310x310.png',
                     'skins/ultralight/favicon/safari-pinned-tab.svg',
                     'skins/ultralight/favicon/site.webmanifest'])
                   ]
            )  
