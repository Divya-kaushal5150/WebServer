# import socket module
from socket import *
# In order to terminate the program
import sys

Server='localhost'

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind((Server, port))
  
  #Fill in start
  #Enable server to listen for incoming connections (max 1 connection)
  serverSocket.listen(1)
  #print("Server is waiting for a connection...")
  #Fill in end

  while True:
    #Establish the connection
    
    #print('Ready to serve...')
    # Accept an incoming connection
    connectionSocket, addr = serverSocket.accept()#Fill in start -are you accepting connections?     
    #print(f"Connection established with {addr}") #Fill in end
    
    try:
      #Fill in start -a client is sending you a message
      # Receive a message from the client
      message = connectionSocket.recv(1024).decode('utf-8', errors='ignore')
      #print(f"Message received from client: {message}")
      #Fill in end 
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:],'rb') #fill in start #fill in end)
      #fill in end
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      file_content = f.read()       
      #Content-Type is an example on how to send a header as bytes. There are more!
      #outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      headers = (
        "HTTP/1.1 200 OK\r\n"  
        "Content-Type: text/html; charset=UTF-8\r\n"  
        "Content-Length: 1024\r\n"  
        "Connection: close\r\n"  
        "\r\n"  
      )


      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      #Fill in end
               
      #for i in f: #for line in file
      #Fill in start - append your html file contents #Fill in end 
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      # Combine headers and file content into a single response
      full_response = headers.encode() + file_content

      # Send the combined response (headers + file content)
      connectionSocket.sendall(full_response)

      #print(f"Sent {filename} to the client.")

      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as FileNotFoundError:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      # If the file is not found, send a 404 response
      error_message = "<html><body><h1>404 Not Found</h1></body></html>"
      error_headers = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n"
            "Content-Length: " + str(len(error_message)) + "\r\n"
            "Connection: close\r\n"
            "\r\n"
      )

      # Combine error headers and message into a single response
      full_error_response = error_headers.encode() + error_message.encode()

      # Send the combined error response
      connectionSocket.sendall(full_error_response)

      #print("File not found. Sent 404 response.")

      #Fill in end


      #Close client socket
      #Fill in start
      # Close the client connection
      connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data
if __name__ == "__main__":
  webServer(13331)
