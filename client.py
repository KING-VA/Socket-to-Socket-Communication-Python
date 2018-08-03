import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "your_IP"
port = 5060
data = ""
s.connect((host, port))

def ts(st):
    s.send(st.encode())
    data = s.recv(4096).decode()
    
    print(data)
    return data

data_1 = ""
data_1 = s.recv(4096).decode()
print(data_1)
while True:
    r = raw_input("Enter:")
    m = ts(r)
    if (m == "Welcome V."):
        print("Authorized Access. Unlocking your Computer")
        break
    elif (m == "User Unauthorized. Ending Connection"):
        break
s.close
