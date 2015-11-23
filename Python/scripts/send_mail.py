import smtplib

fromaddr = 'madhok.raahil@gmail.com'
toaddrs  = 'madhok.raahil@gmail.com'
msg = "THIS IS A TEST"


# Credentials (if needed)
username = "madhok.raahil@gmail.com"
password = "raamad1990"

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()