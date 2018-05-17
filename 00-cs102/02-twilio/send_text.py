from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "#####"
# Your Auth Token from twilio.com/console
auth_token  = "#####"

client = Client(account_sid, auth_token)

message = client.messages.create(
    # to="+16308050066",
    to="+#####",
    from_="+#####",
    body="Love, Check this out, I'm messaging from my computer.")

print(message.sid)
