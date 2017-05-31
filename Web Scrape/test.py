#!/usr/bin/python 3
import requests
from lxml import html
from time import sleep
from datetime import datetime

# Login Information
EMAIL = ""
PIN = ""


# Page URLS
login_url = "https://www.puregym.com/Login/"
member_url = "https://www.puregym.com/members/"
ajax_url = "https://www.puregym.com/api/members/login/"

# Main function


def scrape():
    session_requests = requests.session()

    result = session_requests.get(login_url)

    tree = html.fromstring(result.text)
    token = tree.xpath("//input[@name='__RequestVerificationToken']/@value")
    cook = result.cookies
    payload = {
        "email": EMAIL,
        "pin": PIN,
        "associateAccount": "false"
    }
    result = session_requests.post(
        login_url,
        data=payload,
        headers={'referer': login_url,
                 '__RequestVerificationToken': str(token),
                 'Connection': 'keep-alive',
                 'Content-Type': 'application/json'},
        cookies=cook
    )
    status = result.status_code
    time = datetime.now().time()
    if status == 200:
        print(str(time) + ': ' + 'login Sucessful')
    else:
        print(str(time) + ': ' + 'login Unsucessful!')
        print('code: ' + str(status))
        quit()

    result = session_requests.get(
        member_url,
        headers={'referer': login_url,
                 '__RequestVerificationToken': str(token),
                 'Connection': 'keep-alive'},
        cookies=cook
    )
    return_url = result.url
    print(return_url)
    status = result.status_code
    print('Scrape returned code: ' + str(status))
    tree = html.fromstring(result.content)
    heading = tree.xpath(".//p[@class='para para--footer float-left']/text()")
    members = tree.xpath(
        './/a[@class="text-link text-link--forgotten-pin"]/text()')
    print('text', members)
    print(heading)


if __name__ == '__main__':
    while True:
        try:
            scrape()
            sleep(60)
        except KeyboardInterrupt:
            print('Quitting')
            exit()
