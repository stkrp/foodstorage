# foodstorage
Instagram clone created for studying Django REST framework.

---

# Auth
Docs: [[http://www.django-rest-framework.org/api-guide/authentication/]]

Utils: `sudo apt-get install httpie`

### Register

```
http -f POST http://127.0.0.1:8000/users/ username="test2" password="123"
```

```
HTTP/1.0 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Date: Fri, 05 Feb 2016 11:34:45 GMT
Location: http://127.0.0.1:8002/users/5/
Server: WSGIServer/0.2 CPython/3.4.3+
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN
{
    "email": "", 
    "first_name": "", 
    "last_name": "", 
    "url": "http://127.0.0.1:8002/users/5/", 
    "username": "test2"
}
```


### Login

```
http -f POST http://127.0.0.1:8000/auth/ username="test" password="123qweRTY"
```


```
HTTP/1.0 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Date: Thu, 04 Feb 2016 19:49:37 GMT
Server: WSGIServer/0.2 CPython/3.4.3+
Vary: Cookie
X-Frame-Options: SAMEORIGIN
{
    "token": "55038152598fb752bb1f8ba9ebb6ce1c936ffd16"
}
```

### Authenticate

```
http -f PATCH http://127.0.0.1:8000/photos/1/ title="cURL patch title 1" Authorization:"Token 5aa4a8ffe4afcb7867ad25059594c77ad3cd1c4b"
```

```
HTTP/1.0 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Date: Thu, 04 Feb 2016 20:05:29 GMT
Server: WSGIServer/0.2 CPython/3.4.3+
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "avg_rating": 9, 
    "created_at": "2016-02-03T13:04:32.028529Z", 
    "file": "http://127.0.0.1:8000/media/qweqwe", 
    "modified_at": "2016-02-04T20:05:29.456258Z", 
    "title": "cURL patch title 1", 
    "url": "http://127.0.0.1:8000/photos/2/", 
    "user": "http://127.0.0.1:8000/users/2/"
}
```