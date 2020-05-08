# Installer four ultralight weewx skin
# F.Stuyk, 2020

from setup
import ExtensionInstaller

def loader():
    return UltralightInstaller()

class UltralightInstaller(ExtensionInstaller):
    def __init__(self):
    super(UltralightInstaller, self).__init__(
        version = "1.0",
        name = 'Ultralight',
        description = 'An ultra light weight skin',
        author = "F.Stuyk",
        author_email = "bonjour81@runbox.com",
        config = {
            'StdReport': {
                'Ultralight': {
                    'skin': 'Ultralight',
                    'HTML_ROOT': 'ultra'
                }
            }
        },
        files = [('skins/Ultralight', ['skins/Ultralight/index.html.tmpl',
                'skins/Ultralight/manifest.json.tmpl'
            ]),
            ('skins/Ultralight/js', ['skins/Ultralight/js/collapsible.js']),
            ('skins/Ultralight/css', ['skins/Ultralight/css/mobile.css']),
            ('skins/Ultralight/images', ['skins/Ultralight/images/arrow_down.gif',
                'skins/Ultralight/images/arrow_up.gif',
                'skins/Ultralight/images/b.gif',
                'skins/Ultralight/images/nav-current.jpg',
                'skins/Ultralight/images/nav.jpg'
            ])
            
        ]
    )
