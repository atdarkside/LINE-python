# coding: utf-8
from line import LineClient,LineGroup,LineContact
import time
import random
import socket


def auth(_id,_password,_token = None):
    try:
        if _token == None:
            print "ID:" + _id
            print "password:" + _password
            token = LineClient(id = _id,password = _password).authToken
            print token
            return LineClient(authToken = token)
        else:
            return LineClient(authToken = _token)
    except:
        print "auth Failed"
        raise




Id = ""
password = ""
Token = ""

client = auth(_id = Id, _password = password)

client.refreshContacts()
client.refreshGroups()

Groups = client.groups
room = client.rooms
friendIds = client._getAllContactIds()
groupIds = client._getGroupIdsJoined()

"""
print "friendIds:"
print friendIds
print "groupIds:"
print groupIds
"""

op_list = []

friendContacts = client._getContacts(friendIds)
groupContacts = client._getContacts(groupIds)

print "Groups:"
for cont in Groups:
    try:
        print cont.name.decode('utf-8')
    except:
        print "failed"

print "friends:"
for cont in friendContacts:
    try:
        print cont.displayName.decode('utf-8')
    except:
        print "failed"

"""
op_list.append(client.getContactByName(""))

i = 0
while i <= 200:
    for sender in op_list:
        sender.sendMessage("")
    print i
    i = i + 1
"""

"""
op_list.append(client.getContactByName(""))

print op_list

i = 0
while i <= 100:
    result = client.createRoomWithContacts(contacts = op_list)
    result.sendMessage("nullpo")
    print str(result).decode('utf-8') + str(i)
    i = i + 1
    if (i % 5) == 0:
        print "Re Auth"
        client = auth(_id = Id, _password = password)
        client.refreshContacts()
        client.refreshActiveRooms()
    time.sleep(random.uniform(3,8))
"""

"""
bucho = client.getContactByName("")

i = 0
while i <= 100:
    bucho.sendMessage("自動送信" + str(i))
    print str(i)
    i = i + 1
"""

"""
for gro in Groups:
    if gro.name == "テスト":
        print client.leaveGroup(gro)
"""

"""
for fri in friendContacts:
    if fri.displayName.decode('utf-8') == "".decode('utf-8'):
        op_list.append(fri.mid)

teller0423 = client.getContactByName("")

print teller0423.name.decode('utf-8')

print op_list

print client.createGroupWithContacts(name = ,contacts = op_list)
"""

"""
contact = client.getGroupByName("")

print contact

print contact.getMemberIds()
"""

"""

op_list.append()

pro = client._getProfile()
print pro.displayName.decode('utf-8')

"""

"""
groupContacts = client.createGroupWithContacts("test",op_list)

groupContacts.sendMessage("test")
reizou05.sendMessage("")

print client.findAndAddContactByUserid("")
"""

"""
room = client.createRoomWithContacts(atDark)

client.leaveRoom(room)
"""



while True:
      op_list = []
      for op in client.longPoll():
         op_list.append(op)
 
      for op in op_list:
         sender   = op[0]
         receiver = op[1]
         message  = op[2]
 
         print op_list 
         msg = message.text
         print "sender:"
         print (sender)
         print "msg:"
         print (msg)
         print "receiver:"
         print (receiver)

         try:
            if type(receiver) == LineGroup:
                print "Group."
                receiver.sendMessage("[%s] %s" % (sender.name,msg))
                print "send:" + msg.decode('utf-8')
            elif type(receiver) == LineContact:
                print "Individual."
                sender.sendMessage("(Auto reply) Sorry. I'm busy now. :(")
                print "send."
         except Exception, e:
           print "Send Faild"
