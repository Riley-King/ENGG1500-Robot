import network
import socket
import time
import os

MAX_TERMINAL_BUFFER = 8192

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("", "")

if wlan.status() != 3:
    raise RuntimeError("Failed To Connect To Network")
else:
    print(f"Connected! Status: {wlan.ifconfig()}")


websock = socket.socket()
websock.bind((wlan.ifconfig()[0], 80))
websock.listen(1)
websock.settimeout(0.25)
def killWeb():
    websock.close()


terminal = ""
__post_terminal = "</div> <form action=\"/cmd\" method=\"get\"><input name=\"cmd\" type=\"text\" style=\"width:38%;\"><input name=\"endcmd\" type=\"submit\" style=\"display:none; width:0%; height:0px;\"></form>"
def log(s):
    global terminal
    terminal += f"<div>{str(s)}</div>"
    if len(terminal) > MAX_TERMINAL_BUFFER:
        terminal = terminal[(MAX_TERMINAL_BUFFER-len(terminal)):]
def clear_log():
    global terminal
    terminal = "<b>Terminal</b> <br> <div id=\"term\" style=\"width: 40%; height: 300px; overflow: scroll; margin:left; font-family:monospace;\">"
clear_log()

web_pages = {}
# Recursively loads all files in a directory and adds it to web_pages dictionary
# If noConcatPath is true, the path will not be concatenated to the index
def loadHTMLRecurse(path, noConcatPath=False):
    for fName, fType, iNode, unk in os.ilistdir(path):
        if fType == 0x4000:
            loadHTMLRecurse(path + "/fName")
        elif fType == 0x8000:
            f = open(path + "/" + fName, "r")
            if noConcatPath: web_pages["/"+fName] = f.read()
            else: web_pages["/" + path + "/" + fName] = f.read()
            print("-   Loaded " + path + "/" + fName)
            f.close()

def __GET_REQ(req):
    path_pos = 0
    for i in range(len(req)):
        if req[i] == " " or req[i] == "?":
            path_pos = i
            break

    print(f"Request for page: \"{req[:path_pos]}\"")
    return req[:path_pos], path_pos

def handleCMD(cmd):
    if cmd == "clear":
        clear_log()
    else:
        log(f"Tried to run command \"{cmd}\"")
        print(f"Tried to run command \"{cmd}\"")
def update_webserver():
    global terminal

    while True:
        try:
            cl, addr = websock.accept()

            req = str(cl.recv(1024))

            if req[2:5] == "GET":
                path, idx = __GET_REQ(req[6:])

                cl.send("HTTP/1.1 200 OK\n")
                cl.send("Content-type: text/html\n")
                cl.send("Connection: close\n\n")

                if path == "/term":
                    cl.sendall(f"{terminal}{__post_terminal}")
                elif path == "/cmd":
                    idx = req.find("?cmd=")
                    if idx != -1:
                        idx_end = req.find("&")
                        handleCMD(req[idx + 5:idx_end])
                    cl.send("<meta http-equiv=\"refresh\" content=\"7; url='./term'\"/>")
                else:
                    cl.sendall(web_pages[path])
            else:
                cl.send("HTTP/1.1 404 Not Found\n")
                cl.send("Connection: close\n\n")
                print(f"Unknown request: {req}")

            cl.close()

        except Exception as e:
            break
