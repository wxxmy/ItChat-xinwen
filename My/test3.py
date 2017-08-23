# coding-utf-8
import itchat

itchat.auto_login(hotReload=True)
friends = itchat.get_friends('Scrapy')
chatroom = itchat.get_chatrooms()
print(friends)
print(chatroom)
#'Uin': 1855486016
itchat.send('你好xmyasdf',toUserName='@535d9f708c3cc4b39639545bd293388ae11d5b64ba2a6691e20b6b3b25110e7c')

