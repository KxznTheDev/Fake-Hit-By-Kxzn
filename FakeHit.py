from dhooks import Webhook, Embed
import random
from random import randint
from flask import Flask
import requests
import string

Usernames = ["BabyFreezeee", "yxrgk", "iiBackFax"]
hook = Webhook("Yourwebhook")

def embed(image, name, id, isbanned, isverified, created):
    e = "We Got A Hit!, Account Information Is:" +  ''.join(random.choices("" + string.digits, k=0))
    cookie = f"`{e}`"
    embed=Embed(title="Login Visit - XSS Method ", description=cookie,  color=0x1E1E1E)
    embed.set_thumbnail(url=f"{image}")
    embed.add_field(name=" Roblox Username", value=f"{name}", inline=False)
    embed.add_field(name="Discord Token: ", value=f"NDc5MzI4NTQ4MzY5NDY1MzU1.DlXrdw.feHYusFR8d37BLbeTowVM8Oa1Jg", inline=False)
    embed.add_field(name="IP:", value=f"67.166.35.191", inline=False)
    embed.add_field(name=".ROBLOSECURITY", value=f"_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_3384F9AA39532592EDDB728D0E11D0E46351F89BC3E24F94C111B2291F745A8DBA775F2EBB63CA9D3386A4676A2D7AB54D27D8FCA1759367F90AD6B4733FA615C532C34E4609A2EE83D0EC4F000B13B0817EF3D86B53824F53A7DA632C296359BEF1793DCE698C22815DAA6A3A1320237DEF937675B04DBA2D7A16EE33F213C847C9B48763695A947B5D67FB0FF9BDCC9FA3383DAEC767CD059B42F264C1A06EA79A5240A19A4FC679665C5A856B212E99E1ADB730F240FE09E5AAF3E237DD1AD1E5F49FA2AB5D183D280EFC6864FC5ABE6C1F15734661E5ADE1003FA4CF6193A26D22373615E33FECB50C4424BD40ED6C05DEEC3DC658B66A2F9C0655A2C04FC1BD4BF074F66E678783D1A925AD61D19C4E25D204E62106B5F1A695F56E5665842434111DAE977A19FFE73CC3B626AC03E064718DA21770095674660F5666F48D3063C5EF9FE26D7E6A86F5DF2A283E6568147B2F2FCDC68F2EFE73921062656217A77C0788F36E71D767F64568D0BEC062D202DC0AE7DEFAD4CD90DC5AB2B0EED7DD97", inline=False)
    embed.add_field(name=" Account Created:", value=f"{created}", inline=False)
    embed.set_footer(text="Made by https://github.com/Kxzn, give credits")
    hook.send("", embed=embed)




app = Flask("app")

@app.route('/')
def route():
    try:
        x = random.choices(Usernames)[0]
        userinfo = requests.get(f"https://api.roblox.com/users/get-by-username?username={x}").json()
        id = userinfo["Id"]
        username = userinfo["Username"]
        moreinfo = requests.get(f"https://users.roblox.com/v1/users/{id}").json()
        Isbanned = moreinfo["isBanned"]
        IsVerifed = moreinfo["hasVerifiedBadge"]
        created = moreinfo["created"]
        Image = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={id}&size=352x352&format=Png&isCircular=false").json()["data"][0]["imageUrl"]
        embed(Image, username, id, Isbanned, IsVerifed, created)
    except:
        pass
    return "Check Ur Discord, This Has Been Revamped By Kxzn#1000"





app.run(host='0.0.0.0', port=8080)