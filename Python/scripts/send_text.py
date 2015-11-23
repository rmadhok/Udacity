from twilio.rest import TwilioRestClient
 
#Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC2f3b2639796439f05c478ab49b81c429"
auth_token  = "451a693e5c5b44d32088831dfa86cd57"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
	body="Your dog is no longer",
    to="+18573529448",    # Replace with your phone number
    from_="+18704559785") # Replace with your Twilio number
    
print message.sid