import webbrowser, dxinput, time
from win32api import GetKeyState 
from win32con import VK_NUMLOCK
def main(waste = 4):
    webbrowser.open('https://emory-integration.zerionsoftware.com/chemical_pickup')
    time.sleep(4)

    num = 0
    if GetKeyState(VK_NUMLOCK) == 1:
        num = 1
        dxinput.press('numlock')

    for i in range(5):
        dxinput.press('tab')
    dxinput.press('c')
    for i in range(16):
        dxinput.press('page down')
    dxinput.press('tab')
    dxinput.press('c')
    for i in range(2):
        dxinput.press('page down')
    dxinput.press('tab')
    dxinput.press('e')
    dxinput.press('tab')
    dxinput.paste('E220')
    dxinput.press('tab')
    dxinput.paste('Sheng Wang')
    dxinput.press('tab')
    dxinput.paste('swan343@emory.edu')
    dxinput.press('tab')
    dxinput.paste('4047272727')
    dxinput.press('tab')
    dxinput.paste('5gal liquid halogenated/green waste')
    for i in range(7):
        dxinput.press('tab')
    dxinput.press('5')
    for i in range(2):
        dxinput.press('tab')
    dxinput.paste(r'70% water / 30% acetonitrile / 0.1% TFA')
    for i in range(3):
        dxinput.combo(['shift',     'tab'])

    if waste > 0:
        dxinput.press(str(waste))
        for i in range(6):
            dxinput.press('tab')
        dxinput.press(str(waste))
        for i in range(4):
            dxinput.press('tab')
    
    if num == 1:
        dxinput.press('numlock')

main()
