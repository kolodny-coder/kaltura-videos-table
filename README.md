# Videos-Table-App

The Videos Table App is a simple app that gives a nice presentation to your video media account at Kaltura inc.

# Accessing the app
1. User can access the app at https://kaltura-dan.herokuapp.com/videos_data/

# Featers
The app is importing your last 20 entries (media) from your Kaltura account and displays them in a table.

1. user can sort the table by the columnns by pressing the column title.
2. User can filter the search resault using the free text field, the table will be filttered dynamically regardlles to the pagination.

# API end point



GET ALL MEDIA - by using GET method with this API end point:  https://kaltura-dan.herokuapp.com/api
you will get a dictionary with all your media names and id's.

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


DELETE MEDIA - by using DELETE method with this API end point and specifing the id you fthe entry you want to delete:

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

some basicks API test written in Python unittest frame work

# Preforamnce tests






