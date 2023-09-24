from socket import *


# This is not a well-formed email message (see RFC2822)
msg = ("From: futurefriend@gmail.com\r\n"
       "To: wrigjaso@isu.edu\r\n"
       "Subject: Urgent!\r\n"
       "Date: Sun, 16 February 2020 15:20:00 -0700\r\n"
       "\r\n"# An empty line to separate the header from the body.
       "I have urgent information from the future for you. I've recently learned how dependable and reliable SMTP "
       "protocol is. I have no doubt, unless for some strange reason this email is carelessly deleted immediately "
       "upon receipt, that you will be able to act upon the information you are about to receive. In just a little "
       "over one month toilet paper will become scarce and nearly unobtainable. Please, heed my warning and stock up "
       "now, before it is too late. There is no point in both of us being caught off guard in these dark times."
       "\n"
       "With care,\n"
       "You're friend from the future"
       "\n"
       "\n"
       "P.S. Dogecoin peaks at $0.68\r\n")

# This -is- the correct way to end a message after the data command
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google Mail server) and call it mailserver
mailserver = "simplesmtp.thought.net"
mailport = 8025 # "fill me in"

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)# Creating the socket.
clientSocket.connect((mailserver, mailport)) # Telling the socket where we are connecting to.
#Fill in end

# NOTE: you should write better handling for return messages. The
# code below might work, but it does NOT handle multiline responses.
# Please consult RFC5321 for details.

recv = clientSocket.recv(1024).decode()
print(f"Connecting:\n\t{recv}")
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(f"heloCommand:\n\t{recv1}")
if recv1[:3] != '250':
    print('250 reply not received from server.')



# Send MAIL FROM command and print server response.
# Fill in start
myEmail = "bartrya2@isu.edu"# Made this a variable to make it easier to change the MAIL FROM, just in case.
mailFromCommand = f"MAIL FROM:<{myEmail}>\r\n"# This is what will be sent to the server.

clientSocket.send(mailFromCommand.encode())# Sending it to the server. encode() changes to bytes.

# Using the same structure from the code given above from Professor Wright.
recv2 = clientSocket.recv(1024).decode()# decode() takes it out of bytes
print(f"mailFromCommand:\n\t{recv2}")
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start
receivingEmail = "simplesmtp.thought.net"# Made this a variable to make it easier to change the RCPT TO, just in case.
rcptToCommand = f"RCPT TO:<{receivingEmail}>\r\n"# This is what will be sent to the server.

clientSocket.send(rcptToCommand.encode())# Sending it to the server. encode() changes to bytes.

# Following the same structure from the code given above from Professor Wright
recv3 = clientSocket.recv(1024).decode()# decode() takes it out of bytes
print(f"rcptToCommand:\n\t{recv2}")
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end


# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())# This is what will be sent to the server.

# Following the same structure from the code given above from Professor Wright
recv4 = clientSocket.recv(1024).decode()
print(f"dataCommand:\n\t{recv4}")
if recv4[:3] != '354':
    print('354 response not received from server.k')

# Fill in end


# Send message data.
# Fill in start
clientSocket.send(msg.encode())# Sending the email
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())# Ending the email

recv5 = clientSocket.recv(1024).decode()
print(f"endmsg:\n\t{recv5}")
if recv5[:3] != '250':
    print('250 response not received from server.')
# Fill in end


# Send QUIT command and get server response.
# Fill in start
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())# This is what will be sent to the server.

# Following the same structure from the code given above from Professor Wright
recv6 = clientSocket.recv(1024).decode()
print(f"quitCommand:\n\t{recv6}")
if recv6[:3] != '221':
    print("221 response not received from the server.")

# Fill in end
