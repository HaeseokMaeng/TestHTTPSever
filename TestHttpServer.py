from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from os import listdir
from os.path import isfile, join
import pathlib

g_allow_debug_log = True
g_allow_debug_trace = True

def V_TRACE (*log_str) :
    if not g_allow_debug_log:
        return
    print(log_str)

def V_LOG(log_format, *args) :
    if not g_allow_debug_log :
        return
    print(log_format.format(*args))



class MyHandler(SimpleHTTPRequestHandler) :
    def do_GET(self):
        current_path = pathlib.Path().absolute()

        V_TRACE('self.requestline : ', self.requestline)
        V_TRACE('self.path : ', self.path[1:])
        V_TRACE('current_path : ' , current_path)
        
        if self.path.endswith('.my1'):
            # read file and write to response..  
            target_path = join(current_path, self.path[1:])
            
            V_TRACE('target_path : ', target_path)
            f = open(target_path, 'rb')
            tmpBuffer = f.read()
            bBuffer = bytearray(tmpBuffer)
            bBuffer.append(0)
            f.close()

            # V_TRACE (myBuffer)
            
            #bBuffer = myBuffer.encode()
            r = self.wfile.write(bBuffer)
            
            V_TRACE("size : ", r)
            
            # print("current_path :", current_path)
            # onlyfiles = [f for f in listdir(current_path) if isfile(join(current_path, f))]
            
            # self.send_response_only(200, "OK")
            # self.send_header('Content-Type', 'text/plain')
            # self.end_headers()
            
            # for file_name in onlyfiles :
                # print("- ", file_name)
            
            # self.wfile.write(b'Hello World')
            
        else :
            super().do_GET()

        
if __name__ == '__main__' :
    server = HTTPServer(('', 8888), MyHandler)
    V_TRACE('Start WebServer on Port 8888....')
    V_TRACE('Press ^C to Quit WebServer.')
    server.serve_forever()