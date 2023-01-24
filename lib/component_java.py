from jnius import autoclass

autoclass('java.lang.System').out.println('Hello world')
#Hello world

def verification_theme():
    settings = autoclass('Configuration')
    
    print(settings.UI_MODE_NIGHT_MASK)