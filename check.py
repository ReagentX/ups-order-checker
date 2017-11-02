import re
import mechanize


def new_browser():
    """ Returns a new mechanize browser instance """

    browser = mechanize.Browser()
    browser.set_handle_robots(True)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    return browser


def fill_form(reference, country, zip_code):
    browser = new_browser()
    browser.open('https://wwwapps.ups.com/WebTracking/track?loc=en_US')

    browser.select_form(nr=4)
    browser.set_all_readonly(False)

    browser.form.controls[1].value = country
    browser.form.controls[3].value = reference
    browser.form.controls[11].value = [country]
    browser.form.controls[12].value = zip_code

    response = browser.submit()
    html = response.read()
    if 'UPS could not locate the shipment details for your request' in html:
        print "No shipment yet!"
    elif 'Shipping Information' in html:
        print "Shipped! Check https://wwwapps.ups.com/WebTracking/track?loc=en_US"
    else:
        print "Parameter error"


reference = raw_input("Enter reference number: ") #  Generally phone number, no parenthesis or dashes
country = raw_input("Enter 2-char country code: ").lower()[:2]
zip_code = raw_input("Enter zip code: ")

fill_form(reference, country, zip_code)
