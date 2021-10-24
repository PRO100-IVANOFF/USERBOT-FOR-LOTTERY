from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
from defs import ran
from random import randint, choice as ch

app = Client("project")

global reg
reg = []
global sos
sos = 0

#запуск регистрации
@app.on_message(filters.command("lot", prefixes=".") & filters.me)
def lot(_, msg):
    global sos
    sos = 1
    winers = []
    i = 0
    
    list1 = msg.text.split(".lot ")[1]
    list1 = list1.split(", ")
    
    msg.edit("Регистрация открыта!\nЛотерея начнётся через 2 часа\n\nКоманды:\n`.reg` - зарегестрироваться\n`.list` - посмотреть список участников")
    msg.pin()
    sleep(60*120)
    if len(reg) >= 5:
        msg.reply("Лотерея начнётся через **30s**")
        sleep(25)
        while i < 3:
            g = ran(reg)
            if g in winers:
                pass
            else:
                winers.append(g)
                i += 1
        for f in range(5, 0, -1):
            msg.reply(f"Начало через **{f}s**")
            sleep(1)
        msg.reply("Лотерея начинается, смотри закреп!")
        sleep(1.5)
        sos = 2
        msg.edit(f"Лотерея начинается!\n\nПризы:\n1. {list1[0]}\n2. {list1[2]}\n3. {list1[1]}\n\nПожелаем друг другу удачи!")
        sleep(8)
        wins = [f"Первый победитель - это {winers[0]} и он получает **{list1[2]}**\n", f"Второй - {winers[1]} и он получает **{list1[0]}**\n", f"Третий победитель ждет награды - это {winers[2]} и он получает **{list1[1]}**\n"]
        txt = ""
        
        for f in wins:
            txt += f
            msg.edit(f"Победители:\n{txt}\n@pro100_ivan_off - создатель")
            sleep(2)
    else:
        msg.reply("Лотерея отменена из-за недостатка участников!")
    reg.clear()
    sos = 0

#команда регистрации
@app.on_message(filters.command("reg", prefixes="."))
def regs(_, msg):
    username = "@"+msg.from_user.username
    if sos == 0:
        msg.reply("Регистрация ещё не началась!")
    elif sos == 2:
        msg.reply("К сожалению регистрация закончилась!")
    else:
        if username in reg:
            msg.reply('Вы уже зарегистрированы!')
        else:
            msg.reply('Регистрация прошла успешно!')
            reg.append(f"{username}")

#команда для просмотра списка участников
@app.on_message(filters.command("list", prefixes="."))
def member(_, msg):
    members = ""
    if sos == 0:
        msg.reply("Регистрация ещё не началась!")
    
    else:
        if len(reg) == 0:
            msg.reply("Ещё никто не зарегистрировался!\n**Что бы зарегистрироваться просто напиши** `.reg`")
        else:
            for mem in reg:
                members += mem+"\n"
            msg.reply(f"Список участников:\n{members}")

#команда для добавления участников в список
@app.on_message(filters.command("add", prefixes=".") & filters.me)
def add(_,msg):
    username = msg.text.split()[1]
    if sos == 0:
        msg.reply("Регистрация ещё не началась!")
        
    elif sos == 2:
        msg.reply("Поздно, регистрация уже началась!")
        
    else:
        if username in reg:
            msg.reply("Пользователь уже участвует!")
        else:
            reg.append(username)
            msg.reply("Пользователь добавлен в список участников!")

app.run()