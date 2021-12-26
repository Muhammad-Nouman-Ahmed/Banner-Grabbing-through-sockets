import socket
ip = 'google.com'
port = 80
payload1 = b''
payload2 = b'GET / HTTP/1.0\r\n\r\n'
payload3 = b'OPTIONS / HTTP/1.0\r\n\r\n'
payload4 = b'OPTIONS / RTSP/1.0\r\n\r\n'
payload5 = b'GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0\r\n\r\n'
payload6 = b'\x6C\0\x0B\0\0\0\0\0\0\0\0\0'
payloads_list = [payload1, payload2, payload3, payload4, payload5, payload6]
count = 0
for payload in payloads_list:
    count += 1
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((ip, port))
        sock.send(payload)
        data = sock.recv(1024)
        print("[*] Payload " + str(count))
        print(data)
    except socket.timeout as e:
        print("[*] Payload " + str(count) + ' ' + str(e))
    except Exception as e:
        print("[*] Payload " + str(count) + ' ' + str(e))
    finally:
        sock.close()
print("-----------------------------------------")