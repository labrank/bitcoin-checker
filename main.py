import time
import csv
import pprint

from bitcoin_price import Bitcoin

if __name__ == '__main__':
    bc = Bitcoin()
    bitcoin = bc.get_current_price()
    current_rate = new_rate = bc.float_price(bitcoin)

    print('El Bicoin cuesta ${} actualmente, rastreare continuamente '
          'para ayudarte a decidir si comprar o vender.'.format(current_rate))
    starttime = time.time()

    print('-' * 50)

    pprint.pprint(bitcoin)
    while True:
        bitcoin = bc.get_current_price()
        new_rate = bc.float_price(bitcoin)
        if current_rate > new_rate:
            print('El precio ahora es de ${} asi que VENDE'.format(new_rate/2))
        else:
            print('El precio ahora es de ${} asi que COMPRA'.format(new_rate))
        current_rate = new_rate
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))
        with open('bitcoin_history.csv', mode='a', newline='') as chart:
            chart = csv.writer(chart, delimiter=',')
            chart.writerow((time.asctime(), current_rate))
