import pyautogui as g
import numpy
import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def click_on_img(img='refresh.png'):
    button = g.locateCenterOnScreen(img)
    print(button)
    g.click(button[0], button[1])

def get_path_balace_image():
    path = 'balance.png'
    img = g.screenshot(region=(1512, 71, 100, 25))
    img.save(path)
    return path

def get_balance():
    balance = None
    img_path = get_path_balace_image()
    img = Image.open(img_path)
    balance = int(''.join(pytesseract.image_to_string(img, lang='eng').split()))
    print(balance)
    return balance


def get_path_price_image():
    path = 'price.png'
    img = g.screenshot(region=(729, 510, 467, 83))
    img.save(path)
    return path

def main():
    max_price = 45360
    #max_price = 15714
    all_coords = [1143, 489]
    buy_coords = [854, 608]
    close_btn = [1172, 454]
    refresh_btn = [1836, 119]
    purchase_btn = [1773, 183]
    ok_btn = [961, 576]

    while True:
        g.click(ok_btn[0], ok_btn[1])
        g.click(refresh_btn[0], refresh_btn[1])
        time.sleep(0.5)
        g.click(purchase_btn[0], purchase_btn[1])
        price = None

        def buy():
            g.click(all_coords[0], all_coords[1])
            g.click(buy_coords[0], buy_coords[1])
            print("Покупаем")

        try:
            img_path = get_path_price_image()
            img = Image.open(img_path)
            price = int("".join(pytesseract.image_to_string(img, lang='eng').split()).split('for')[1][:-2].replace('S', '5').replace('a', '0').replace('o', '0').replace('g', '0').replace('O', '0').replace('Q', '9').replace('i', '1').replace('@', '0').replace('e', '8').replace('s', '8').replace('d', '0'))
            print(price)
            if (int(str(max_price)[:3]) > int(str(price)[:3]) and (len(str(max_price)) >= len(str(price)))):
                buy()
            # elif (price < max_price and price > max_price*0.5):
            #     buy()
            else:
                print("Нахуй, цена кусается")
                g.click(close_btn[0], close_btn[1])
                time.sleep(1)
                g.click(refresh_btn[0], refresh_btn[1])
            time.sleep(4)
            g.click(ok_btn[0], ok_btn[1])
        except Exception as ex:
            print(f"Error {ex}")
            time.sleep(2)

if __name__ == '__main__':
    #get_balance()
    main()
    #print(get_path_price_item())