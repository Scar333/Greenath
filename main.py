from get_html import get_html
from data_html import data_html, data_merger
from send_mail import send_mail



df = {}


def main():
    url = 'https://www.moex.com/ru/derivatives/currency-rate.aspx?currency=USD_RUB'

    

    data_html(get_html(url))
    data_merger()
    
    from data_html import size
    print(send_mail(size))



if __name__ == '__main__':
    main()
