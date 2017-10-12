import json
from channels import  Channel,Group
from channels.sessions import enforce_ordering, channel_session

from .models import People, ChatMessage


# Connected to websocket.connect
def msg_consumer(message):
    # Save to model
    fromid=message.content['fromid']
    toid = message.content['toid']
    msg = message.content['msg']
    topeople=People.objects.get(id=toid)
    to_channel=topeople.reply_channel

    sendornot = int(message.content['sendornot'])
    chatmessage = ChatMessage.objects.create(
        fromid=fromid,
        toid=toid,
        text=msg,
    )
    # Broadcast to listening sockets
    if sendornot:
        Channel(to_channel).send({
            "text":json.dumps({
                "fromid": fromid,
                "msg": msg,
            }),
        })
        chatmessage.issent = 1
    else:
        chatmessage.issent = 0
    chatmessage.save()

@channel_session
def ws_usualconnect(message):

    message.reply_channel.send({"accept": True})






@channel_session
def ws_message(message):
    # Parse the query string

    msssg = json.loads(message["text"])

    id = msssg['id']
    toid = msssg['toid']
    msg = msssg['msg']


    if toid == 'first':
        people_exist = People.objects.filter(id=id)

        if not people_exist:
            people = People.objects.create(id=id, reply_channel=message.reply_channel.name)
        else:
            people = people_exist[0]
            people.reply_channel = message.reply_channel.name

        chatmsgs = ChatMessage.objects.filter(toid=id).filter(issent=0)

        message.channel_session["id"] =id
        for chatmsg in chatmsgs:
            message.reply_channel.send({
                'text':json.dumps({
                    'fromid': chatmsg.fromid,
                    'msg': chatmsg.text,
                })
            })
            chatmsg.issent = 1
            chatmsg.save()
        people.online = 1
        people.save()
    else:
        frompeople = People.objects.get(id=id)
        topeople = People.objects.get(id=toid)

        frompeople_online = frompeople.online
        topeople_online = topeople.online

        sendornot = frompeople_online * topeople_online

        Channel("chat-messages").send({

            "msg": msg,
            "fromid":id,
            "toid":toid,
            "sendornot": sendornot,

        })


@channel_session
def ws_disconnect(message):
    id=message.channel_session['id']
    people= People.objects.get(id=id)
    people.online = 0
    people.save()
