# Videos-Table-App

The Videos Table App is a simple app that gives a nice presentation to your video media account at Kaltura inc.

# Accessing the app
1. User can access the app at https://kaltura-dan.herokuapp.com/videos_data/

# Features
The app is importing your last 20 entries (media) from your Kaltura account and displays them in a table.

1. user can sort the table by the columns by pressing the column title.
2. User can filter the search results using the free text field, the table will be filtered dynamically regardless of the pagination.

# API endpoint



GET ALL MEDIA - by using the GET method with this API endpoint:  https://kaltura-dan.herokuapp.com/api
you will get a dictionary with all your media names and ids.

``` swift
https://kaltura-dan.herokuapp.com/api
```

output:

```swift
{
  "entries": [
    {
      "id": "1_21nlmmjt", 
      "name": "Pexels Videos 2364298"
    }, 
    {
      "id": "1_8cx0to89", 
      "name": "Kaltura Video Solutions for Media Companies"
    }
  ]
}
```


DELETE MEDIA - by using the DELETE method with this API endpoint and specifying the id you the entry you want to delete:

``` swift
https://kaltura-dan.herokuapp.com/api/<id>
```
output:

``` swift
{'message': 'Entry item deleted!'}
```

# Testing the code


``` swift
KalturaClient/test_routes.py
```

some basics API test is written in the Python unittest framework

# Performance tests

The web page performance measured in 3 basic loads,
20 entries - Load time 1.54s
50 entries - Load time 3.14s
100 entries - Load time 1.88 s

full web performance stored here - https://my.pingdom.com/app/3/home

# Security
Secret Keys stores as environment variables on the server.
no authorization required to access the app



