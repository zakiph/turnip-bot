from discord.ext import commands
import discord, base64, time, pickle
from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

bot = commands.Bot(command_prefix='!')
TOKEN = 'your token here'

class User:
    days = None
    def __init__(self, uid):
        self.uid = uid.id
        self.days = {"buy": '', "mo-am": '', "mo-pm": '', "tu-am": '', "tu-pm": '', "we-am": '', "we-pm": '', "th-am": '', "th-pm": '', "fr-am": '', "fr-pm": '', "sa-am": '', "sa-pm": ''}

    def addbuy(self, buy):
        self.days["buy"] = buy

    def addday(self, day, price):
        if day in self.days:
            self.days[day] = price
        else:
            Exception

def init():
    #cap = DesiredCapabilities().FIREFOX
    #cap["marionette"] = False
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://ac-turnip.com/")
    assert "Turnip" in driver.title
    return [driver, driver.find_elements_by_tag_name("input"), driver.find_element_by_xpath("//canvas[1]")]

def assign(elem, d):
    for index, (key, value) in enumerate(d.items()):
        elem[index].send_keys(value)
    time.sleep(2)

def canvas(c, d, di):
    assign(init[1], di)
    foreground = Image.open(BytesIO(base64.b64decode(d.execute_script("return arguments[0].toDataURL('image/png').substring(21);", c))))
    background = Image.open(BytesIO(base64.b64decode(b'iVBORw0KGgoAAAANSUhEUgAAA4QAAAGQCAYAAAD2lq6fAAAACXBIWXMAAAsTAAALEwEAmpwYAAAGvGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDIgNzkuMTYwOTI0LCAyMDE3LzA3LzEzLTAxOjA2OjM5ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOCAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIwLTA0LTE2VDIxOjE4OjE0KzAyOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMC0wNC0xOFQxNzo0Mjo1NiswMjowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMC0wNC0xOFQxNzo0Mjo1NiswMjowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo2MzdmY2U5Yi1jODAxLWMxNDctOGIyMS1mZmU3N2VlM2EzMDYiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6OGI5YzUyNmQtZTgyNi1iYzQ1LWJkMTAtZDJjNzNmZWU1ZjQxIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6OGI5YzUyNmQtZTgyNi1iYzQ1LWJkMTAtZDJjNzNmZWU1ZjQxIj4gPHhtcE1NOkhpc3Rvcnk+IDxyZGY6U2VxPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0iY3JlYXRlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo4YjljNTI2ZC1lODI2LWJjNDUtYmQxMC1kMmM3M2ZlZTVmNDEiIHN0RXZ0OndoZW49IjIwMjAtMDQtMTZUMjE6MTg6MTQrMDI6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE4IChXaW5kb3dzKSIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6MDJmZGNlZDEtZWNjOC01NDQ1LWIzZDgtNDRkNWEyZTE1MzZmIiBzdEV2dDp3aGVuPSIyMDIwLTA0LTE4VDE3OjM4OjM3KzAyOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOCAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249InNhdmVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjYzN2ZjZTliLWM4MDEtYzE0Ny04YjIxLWZmZTc3ZWUzYTMwNiIgc3RFdnQ6d2hlbj0iMjAyMC0wNC0xOFQxNzo0Mjo1NiswMjowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTggKFdpbmRvd3MpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDwvcmRmOlNlcT4gPC94bXBNTTpIaXN0b3J5PiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PjVXmyEAAArFSURBVHic7d0xTltLAEDRwSRRJDZAR8UKsoAUdKzk18k6kjoroUvBArICV3RsAClKAv6NjR4OEUT5H5N3z5Es4Wc/eWSJ4mrGM3ur1Wr8roury5MxxvH6AQAAO/f1+tu7XY/hb/N6/9XH7Wvfb368uV7dvN3FeOZif29x/nLx4ssj3jr9ns//4COXY4zl0cHh59+9ce+xQXhxdflh+tw/HAAAwPOwHfdHB4fvH3Pfg0E4DUERCAAA8LxN4/ChMPxlEK6XhZ6OIQQBAAD+NpMwPPvVctJ7g/Di6vKfMcaxEAQAAPi7rcNweXRw+Gn7tcX2BTEIAAAwH+u2O1633h13gnCze6gYBAAAmI9JFJ5Mr2/PEJ6KQQAAgPlZt97p9NptEG4fKwEAAMD8TNvvzgyh2UEAAID52m6+xRhmBwEAAEo2DXg7Q2h2EAAAYP6m7ffTsRMAAAA0LLa3HQUAAGD+Lq4uTxbDuYMAAAApm3MJF2OM410PBgAAgCd37DeEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYIQAAAgShACAABECUIAAIAoQQgAABAlCAEAAKIEIQAAQJQgBAAAiBKEAAAAUYsxxnLXgwAAAODJLRdjjOXr/Vcfdz0SAAAAnsa6AZeLo4PDz7seDAAAAE/r6ODws98QAgAARN0GoWWjAAAA8zdtv8UYYxwdHL7f3XAAAAB4SpsGvLNk1CwhAADAfG03320QmiUEAACYv2n7bW8qc2aWEAAAYH7WrXc2vXYnCNdHUDiXEAAAYEY25w5uHzv407ETRweHn4YoBAAAmIVJDH7afm1vtVrde9PF1eXJGON0jDG+Xn9797+OEAAAgP/UZJLvbHtmcOOXQbhxcXX5YfO3MAQAAHjepqs9H9o89MEg3JiG4RjiEAAA4LnY/snfY0+ReHQQTq2Xkx6vHwAAsHMmLH7fffuGfL/58eZ6dfN2F+OZi/29xfnLxYsvj3jr9Hs+/4OPXI57Nox5jH8B5i7g/e35CKwAAAAASUVORK5CYII=')))
    background.paste(foreground, (8, 8), foreground)
    d.find_element_by_css_selector(".MuiButtonBase-root.MuiButton-root.jss153.MuiButton-contained.yellow.MuiButton-containedSizeSmall.MuiButton-sizeSmall").click()
    time.sleep(1)
    d.find_elements_by_css_selector(".MuiButtonBase-root.MuiButton-root.jss153.MuiButton-contained.yellow.MuiButton-containedSizeSmall.MuiButton-sizeSmall")[1].click()
    output = BytesIO()
    background.save(output, 'PNG')
    output.seek(0)
    return output


init = init()

def save_data(data):
    with open("bin.dat", "wb") as f:
        pickle.dump(data, f)

def load_data():
    try:
        with open("bin.dat", "rb") as f:
            u = pickle.load(f)
    except:
        u = []
        print("failed to load savedata")
    return u

users = load_data()

def newUser(m):
    for x in users:
        if x.uid == m.id:
            break
    else:
        users.append(User(m))

@bot.command(description="sets your purchase price", brief="sets your purchase price", help="\nexample: \n!pp 93")
async def pp(ctx, price: int):
    try:
        newUser(ctx.author)
        for x in users:
            if x.uid == ctx.author.id:
                x.addbuy(price)
                await ctx.send("purchase price is " + str(x.days["buy"]) + " for " + ctx.author.mention)
                save_data(users)
                break
    except:
        await ctx.send("format: !pp [purchase price]")

@bot.command(description="adds a days[am or pm] price", help="the day argument must be of the format [day]-[am or pm]\nyou must use the first two letters of the days name #[mo, tu, we, th, fr, sa]\nthe price argument is just the price for the day\n\nexample: \n!add mo-pm 105 #here we set monday pm as 105", usage="!add <day>-<am/pm> <price>", brief="sets a given day as a given price")
async def add(ctx, day, price: int):
    try:
        newUser(ctx.author)
        for x in users:
            if x.uid == ctx.author.id:
                x.addday(day, price)
                await ctx.send(day + " registered as " + str(x.days[day]) + " for " + ctx.author.mention)
                save_data(users)
                break
    except:
        await ctx.send("format: !add [mo, tu, we, th, fr, sa]-[am, pm] [price]")

@bot.command(description="prints chart using your data", brief="prints chart")
async def print(ctx):
    newUser(ctx.author)
    for x in users:
        if x.uid == ctx.author.id:
            await ctx.send('Predictions for ' + ctx.author.mention, file=discord.File(canvas(init[2], init[0], x.days), 'chart.png'))
            break

@bot.command(description="clears your data", brief="clears data")
async def clear(ctx):
    for x in users:
        if x.uid == ctx.author.id:
            x.days = x.days.fromkeys(x.days, '')
            save_data(users)
            await ctx.send("data cleared")

bot.run(TOKEN)