# TestHTTPSever
testing server for reproducing in the same http response

It's implemented by using Pyhton3 

1) run like below.
    >> python TestHTTPServer.py

2) The default port is 8888.
   and general url is working by SimpleHTTPRequestHandler class but the file which has 'my1' extension will work differently.
   TestHTTPServer will read the 'my1' file and put out raw content without using SimpleHTTPRequestHandler

3) You should consider how to make 'my1' by using your applicaiton like HexEditor and etc.
   I just used WireShark and modified captured file by using Hex Editor.

   
