def sendPush(title, msg, registration_tokens, dataObject=None):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(title=title, body=msg),
        data=dataObject,
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)
    print('Successfully sent message:', response)
  
title = "Title of the notification"
msg = "Content of the notification"
token = "Token of the android device to which the message should be send"
sendPush(title,msg,token)
