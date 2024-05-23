import os
import pyautogui as MrRobot

username = os.getenv('INSTAGRAM_USER')
password = os.getenv('INSTAGRAM_PASS')

if not username or not password:
    raise ValueError('Variáveis de ambiente não foram definidas para INSTAGRAM_USER e INSTAGRAM_PASS.')

def login_field(image_path):
    location = MrRobot.locateCenterOnScreen(image_path)
    if location is not None:
        MrRobot.click(location)
    else:
        raise ValueError(f'Imagem {image_path} não foi encontrada na tela.')

MrRobot.press('win')
MrRobot.typewrite('chrome')
MrRobot.press('enter')
MrRobot.sleep(1)
MrRobot.typewrite('www.instagram.com')
MrRobot.press('enter')
MrRobot.sleep(4)
MrRobot.press('tab', presses=2)
MrRobot.typewrite(username)
MrRobot.press('tab')
MrRobot.typewrite(password)
MrRobot.press('enter')



