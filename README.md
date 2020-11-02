# Videos-Table-App

The Videos Table App is a simple app that gives a nice presentation to your video media account at Kaltura inc.

# Accessing the app
1. User can access the app at https://kaltura-dan.herokuapp.com/videos_data/

# Featers
The app is importing your last 20 entries (media) from your Kaltura account and displays them in a table.

1. user can sort the table by the columnns by pressing the column title.
2. User can filter the search resault using the free text field, the table will be filttered dynamically regardlles to the pagination.

# API end point

media add- end point: https://kaltura-dan.herokuapp.com/apiurl TODO

get all media - by using GET method with this API end point:  https://kaltura-dan.herokuapp.com/api
you will get a dictionary with all your media names and id's.

``` swift
https://kaltura-dan.herokuapp.com/api
```

output:










Log in:

Use GET method on this endpoint:https://auth-rest-api-app.herokuapp.com/login
in the Authorization set the type for Basic Auth
and fill the user name and password fields of the user you created

optional existing users you can log in with:

Anna - Anna_password
Bill - Bill_password
Corey - Corey_passsword

copy the token You got without the ""

Header section:
set the Key to x-access-token
        Value <paste the Token>
    
the Token is valid for 30 min!!!

writing a message - use POST method on this endpoint: https://auth-rest-api-app.herokuapp.com/msg

user should declare in the header 
Content-Type: application/json

user should provide 3 parameters in the body (receiver, subject, body) in JSON format.

``` swift
{"receiver": "Spiderman",
"subject": "message for Spider",
"body": "If you spell Chuck Norris in Scrabble, you win. Forever."}
```



Get all unread messages of the logged-in user (as a sender or as reciver) -  use GET method on this endpoint: https://auth-rest-api-app.herokuapp.com/msg/unread

Note if you'll do it 2 times in a raw the second request will return an empty response becasue the first request has "read" the messages.

Get all messages of the logged-in user (as a sender or as a receiver) -  use GET method on this endpoint: https://auth-rest-api-app.herokuapp.com/msg/all


  
Read a specific message -  use GET method on this endpoint: https://auth-rest-api-app.herokuapp.com/msg/id
        
The user should declare the message-id number he would like to read.
  
  
 Delete message - use DELETE method on this endpoint: https://auth-rest-api-app.herokuapp.com/msg/id
The user should declare the message-id he wishes to delete.
  
  
# Message Content
the message contains the following parameters :

- [x] ID
- [x] Sender
- [x] Receiver
- [x] Subject
- [x] Body
- [x] Date Posted
- [x] Boolean parameter if the message was read:
 True stand for the message has been read False stands for the message has not read
 
 Get all users:
 
 use GET method on this endpoint: https://auth-rest-api-app.herokuapp.com/user
 Note no need to be logged in for this request 
 
.
