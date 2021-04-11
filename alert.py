import requests
from bs4 import BeautifulSoup
import smtplib
import config
import time

url = 'https://www.farfetch.com/me/shopping/women/golden-goose-may-sneakers-item-13547263.aspx?shortlink=b9f5e5d2&pid' \
      '=app-product-share&c=screenshotbanner_nativeshare&is_retargeting=true '
url2 = 'https://www.farfetch.com/me/shopping/men/golden-goose-superstar-low-top-sneakers-item-15557289.aspx?shortlink' \
      '=b9f5e5d2&pid=app-product-share&c=screenshotbanner_nativeshare&is_retargeting=true '
url3 = 'https://www.farfetch.com/me/shopping/women/off-white-foating-arrow-low-top-sneakers-item-16069852.aspx' \
      '?shortlink=b9f5e5d2&pid=app-product-share&c=screenshotbanner_nativeshare&is_retargeting=true '

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.114 Safari/537.36'
}


def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    cont = soup.select_one('div._7dad7e')

    try:
        price = cont.select_one('span').get_text()
        price_int = int(price[0:3])
        if price_int < 200:
            send_mail()
        else:
            pass
    except:
        pass


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config.USER, config.PASSWORD)

    subject = 'Cijena za Gollden Goose je pala'
    body = 'Cijena za Zlatne Golden Goose je pala ispod 200 eura, kupuj odma ako ima' \
           'broja i ne ciganisi se.\n' \
           'Evo ti link crna: https://www.farfetch.com/me/shopping/women/golden-goose-may-sneakers-item-13547263.aspx?shortlink=b9f5e5d2&pid' \
      '=app-product-share&c=screenshotbanner_nativeshare&is_retargeting=true'

    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(
        'andrealmijovic@gmail.com',
        'andrealalic2@gmail.com',
        msg
    )
    server.quit()


def check_price2():
    page = requests.get(url2, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    cont = soup.select_one('div._7dad7e')

    try:
        price = cont.select_one('span').get_text()
        price_int = int(price[0:3])
        if price_int < 200:
            send_mail2()
        else:
            pass
    except:
        pass


def send_mail2():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config.USER, config.PASSWORD)

    subject = 'Cijena za Gollden Goose je pala'
    body = 'Cijena za Superstar low-top sneakers Golden Goose je pala ispod 200 eura, kupuj odma ako ima' \
           'broja i ne ciganisi se.\n' \
           'Evo ti link crna: https://www.farfetch.com/me/shopping/men/golden-goose-superstar-low-top-sneakers-item-15557289.aspx?shortlink' \
      '=b9f5e5d2&pid=app-product-share&c=screenshotbanner_nativeshare&is_retargeting=true'

    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(
        'andrealmijovic@gmail.com',
        'andrealalic2@gmail.com',
        msg
    )
    server.quit()


def check_price3():
  page = requests.get(url3, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  cont = soup.select_one('div._7dad7e')

  try:
      price = cont.select_one('span').get_text()
      price_int = int(price[0:3])
      if price_int < 200:
          send_mail3()
      else:
          pass
  except:
      pass


def send_mail3():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config.USER, config.PASSWORD)

    subject = 'Cijena za Gollden Goose je pala'
    body = 'Cijena za Off-White je pala ispod 200 eura, kupuj odma ako ima' \
           'broja i ne ciganisi se.\n' \
           'Evo ti link crna: https://www.farfetch.com/me/shopping/women/off-white-foating-arrow-low-top-sneakers-item-16069852.aspx' \
      '?shortlink=b9f5e5d2&pid=app-product-share&c=screenshotbanner_nativeshare&is_retargeting=true'

    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(
        'andrealmijovic@gmail.com',
        'andrealalic2@gmail.com',
        msg
    )
    server.quit()


while True:
    check_price()
    check_price2()
    check_price3()
    time.sleep(43200)
