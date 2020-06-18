import telebot
import mysql.connector

import mytoken


from datetime import datetime
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_belajarbot')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang=datetime.now()

class Mybot:
    def _init_(self):
        self.message

    @myBot.message_handler(commands=['start'])
    def start(message):
        teks = mytoken.BAHASA + "\n-- admin & developer @devaabel - SMK Taruna Bhakti -- "+"\n" \
                        "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['eng'])
    def eng(message):
        teks = mytoken.SAPAE + "\n-- admin & developer @devaabel - SMK Taruna Bhakti -- "+"\n" \
                        "today's date "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['ind'])
    def ind(message):
        teks = mytoken.SAPAI + "\n-- admin & developer @devaabel - SMK Taruna Bhakti -- "+"\n" \
                        "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['tlg'])
    def tlg(message):
        teks = mytoken.TLG
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['help'])
    def help(message):
        teks = mytoken.HELP
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['tentang'])
    def tentang(message):
        teks = mytoken.TENTANG
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['about'])
    def about(message):
        teks = mytoken.ABOUT
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['pp'])
    def foto(message):
        photo = open('img/zuck.png', 'rb')
        myBot.send_photo(message.from_user.id, photo)
        teks = "Hello There"
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query="select nipd,nama,kelas from tabel_siswa "
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        kumpulData=''
        if(jmldata>0):
            # print(data)
            no=0
            for x in data:
                no += 1
                kumpulData =kumpulData+ str(x)
                print(kumpulData)
                kumpulData = kumpulData.replace('(', '')
                kumpulData = kumpulData.replace(')', '\n')
                kumpulData = kumpulData.replace("'", '')
                kumpulData = kumpulData.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(kumpulData))

print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)
