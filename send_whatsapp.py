from twilio.rest import Client
# Substitua com suas credenciais da conta Twilio
account_sid = "Seu_Account"
auth_token = "Seu_Token"
client = Client(account_sid, auth_token)

#Número do sandbox do Twilio (fixo)
#Substitua pelo numero do Twilio
from_whatsapp_number = 'whatsapp:+14*******'
#Substitua pelo seu numero de whatsapp
to_whatsapp_number = 'whatsapp:+554********'
message = client.messages.create(
body='ola essa é uma mensagem de teste',
from_=from_whatsapp_number,
to=to_whatsapp_number
)
print(f'Mensagem eniada com SID: {message.sid}')

