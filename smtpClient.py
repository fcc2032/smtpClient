from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    clientSocket.recv(1024).decode()
    # Fill in end
    
    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    clientSocket.recv(1024).decode()

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailCommand = 'MAIL FROM:fcc2032@nyu.edu\r\n'
    clientSocket.send(mailCommand.encode())
    clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptCommand = 'RCPT TO:Postmaster\r\n'
    clientSocket.send(rcptCommand.encode())
    clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA \r\n'
    clientSocket.send(dataCommand.encode())
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT \r\n'
    clientSocket.send(quitCommand.encode())
    clientSocket.recv(1024).decode()    
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
