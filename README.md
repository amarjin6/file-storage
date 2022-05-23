![GitHub language count](https://img.shields.io/github/languages/count/amarjin6/file-storage?logo=python&logoColor=green)
![GitHub repo size](https://img.shields.io/github/repo-size/amarjin6/file-storage?color=yellow&logo=gitbook)
![GitHub commit merge status](https://img.shields.io/github/commit-status/amarjin6/file-storage/master/9b8548a9b5af50cd7a5cae83bedc1699c096bdf3?color=purple&logo=pypi)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/amarjin6/file-storage?color=green&logo=Stackbit&logoColor=orange)
![GitHub watchers](https://img.shields.io/github/watchers/amarjin6/file-storage?logo=wechat)

# File storage

## 💡**Main idea**💡

Implement a remote file storage that provides a REST API over the HTTP protocol. When implementing, it is allowed to use a web framework that implements HTTP routing and work with HTTP calls. The request URL path defines the logical location of the file in the repository: **http://storage.com/path/to/file.txt** - describes the file file.txt located at /path/to.
List of supported features:
* uploading a file to storage with overwriting using the PUT method;
* getting a file from storage using the GET method;
* getting a list of directory files using the GET method (it is recommended to use JSON as the data format
  for the response);
* getting information about the file (size in bytes and date of last modification) in the form of HTTP headers
  without getting the file content using the HEAD method;
* deleting a file/directory from storage using the DELETE method.

HTTP status codes must be used correctly.

## ⚒️**How to Run**⚒️

### **1. Create file**

Sending a create request:
* Use PUT-request with URI: “/folder[1]/../folder[n]/file.csv”
* Add request data: -d [YOUR_DATA]
* Send a request.

Example: Sending a create request

    -d Example -X PUT http://127.0.0.1:8000/storage/example.txt


Example: a server response
If the request succeeds, the server returns the HTTP 200 OK status code.

    File created!

#### Status code
 
 200 - File created
 
 400 - Bad request


### **2. Download file**

Sending a download request:
* Use HTTP-request GET with URI: “/folder[1]/../folder[n]/file.png”
* Send a request.


Example: Sending a download request

    -X GET http://127.0.0.1:8000/storage/img/pic.png


Example: a server response
If the request succeeds, the server returns the HTTP 200 OK status code and a file.

    File successfully downloaded!

#### Status code

  200 - Successful request
  
  400 - Bad request
  
  404 - Not found


### **3. Delete file**

Sending a delete request:
* Use HTTP-request DELETE with URI: “/folder[1]/../folder[n]/file.txt”
* Send a request

Example: Sending a delete request

    -X DELETE http://127.0.0.1:8000/storage/trash/remove.txt


Example: a server response
If the request succeeds the server returns the HTTP 200 OK status code.

    Removed successfully!


#### Status code

  200 - Successful request
  
  400 - Bad request
  
  404 - Not found 


### **4. File info**

Sending an info request:
* Use HTTP-request --head with URI: “/folder[1]/../folder[n]/file.py”
* Send a request

Example: Sending a info request

    -I http://127.0.0.1:8000/path/file.py


Example: a server response
If the request succeeds the server returns the HTTP 200 OK status code.

    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.2 Python/3.10.1
    Date: Mon, 23 May 2022 15:39:52 GMT
    Content-Type: text/html; charset=utf-8
    Size: 15b
    Last-modified: Mon May 23 17:59:11 2022
    Created: Mon May 23 17:54:09 2022
    Permissions: 33206
    Content-Length: 0
    Connection: close


#### Status code

  200 - Successful request
  
  400 - Bad request
  
  404 - Not found 


### **5. Catalog info**

Sending an info request:
* Use HTTP-request GET with URI: “/folder[1]/../folder[n]”
* Send a request

Example: Sending a info request

    -X GET http://127.0.0.1:8000/path


Example: a server response
If the request succeeds the server returns the HTTP 200 OK status code.

    ["example.txt", "product-1.png", "product-2.png", "product-3.png"]


#### Status code

  200 - Successful request
  
  400 - Bad request
  
  404 - Not found

## 🥽**Preview**🥽

![preview](https://user-images.githubusercontent.com/86531927/169858739-bd33f46d-8a3e-47a0-b2fa-8221ac7c28fa.jpg)

# Flask REST API HTTP