import urllib2
from bs4 import BeautifulSoup
import subprocess


class Client(object):

    def get_html(self, web):
        f = urllib2.urlopen(web)
        html = f.read()
        f.close()
        return html

    def get_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find("div", "dotd-title")
        title = elements.text
        return title.strip()

    # def send_message(self, title):
    #    message = "The free ebook is: " + title
    #    TOKEN = 'xxxxxxxxxxx'
    #    mi_bot = telebot.TeleBot(TOKEN)
    #    mi_bot.send_message(xxxxxxxx, message)

    def main(self):
        html = self.get_html('https://www.packtpub.com/packt/offers/free-learning/')
        title = self.get_title(html)
        message = "The free ebook is: " + title
        subprocess.Popen(['notify-send', message])


if __name__ == "__main__":
    client = Client()
    client.main()
