# Stratus API Unit Test Coverage

## Diclaimer:
I started wrting these unit tests today and am most of the way through Circle (which is 80% of the app).
In the file `spec.json`, you'll find the tests that are done so far. They are in the following format:

    {
        "url": "[the request url]",
        "label": "[a label for running]",
        "[http method]": {
            "[http status code]": {
                "[the name of the test]": {
                    "path": {}, # Path parameters replaced into URL wildcards (all caps)
                    "data": {}, # All POST parameters
                    "cookies": {} # Cookies for authorization (currently using `sessionid`)
                }
            }
        }
    },

## Usage:
`python3 test_api.py [label] [http_status] [http_method]

## Examples:

Test all timeline posts for non-authorized writes (POST 401)
`python3 test_api.py cir_tim 401 POST`

## Results:
After running an individual test, you will get a result back like this:

In the first block, you'll see the request characteristics, the status you wanted to recieve, and the status you actually got.
If the status you got matches what you wanted, the test is marked as 'PASSED'.

In the second block is inforation about the request, and a JSON dump of the request parameters.

In the third block, there is request response and status code.

	--------------------------------------------------------------------------------
	test:   post to profile timline
	method: POST
	url:    http://localhost:8000/circle/api/DrPib/timeline

	wanted: 200
	got:    200
	result: PASSED
	--------------------------------------------------------------------------------

	- - - - - - - - - - - - - - - - - - - - - - 
	method:   POST
	status:   200
	request:  post to profile timline
	- - - - - - - - - - - - - - - - - - - - - - 

	{
	    "post_type": "media",
	    "url": "https://google.com/?no=matter&how=fast&i=run",
	    "provider": "Breitbart Media Outlet",
	    "type": "photo",
	    "title": "Title of my post",
	    "text": "The joke is that both the words ending in the same sylable that rhyme.",
	    "html": "<html>how to meet ladies</html>"
	}

	- - - - - - - - - - - - - - - - - - - - - - 
	status:    200
	response:
	- - - - - - - - - - - - - - - - - - - - - - 

	{
	    "method": "create_user_timeline",
	    "args": [
		"akleinhans",
		"DrPib",
		{
		    "url": "https://google.com/?no=matter&how=fast&i=run",
		    "provider": "Breitbart Media Outlet",
		    "type": "photo",
		    "title": "Title of my post",
		    "text": "The joke is that both the words ending in the same sylable that rhyme.",
		    "html": "<html>how to meet ladies</html>"
		}
	    ]
	}

	--------------------------------------------------------------------------------

## Running all tests:
All tests previously ran are in the `DONELIST`. Before deployment, these should all be ran.
When you run them, a shorter version of the result is printed, and then a cumulative summary at then end.
If everything is okay, you should see `All tests PASSED`, otherwise failed tests will show up in red.

	--------------------------------------------------------------------------------
	test:   load groups list
	url:    http://localhost:8000/circle/api/groups/10
	method: GET
	wanted: 200
	result: PASSED
	--------------------------------------------------------------------------------
	test:   read group profile videos
	url:    http://localhost:8000/circle/api/groups/SomeGroup/videos/3
	method: GET
	wanted: 200
	result: PASSED
	--------------------------------------------------------------------------------
	test:   read profile albums
	url:    http://localhost:8000/circle/api/DrPib/albums/3
	method: GET
	wanted: 200
	result: PASSED
	--------------------------------------------------------------------------------
	test:   read group profile photos
	url:    http://localhost:8000/circle/api/groups/SomeGroup/photos/3
	method: GET
	wanted: 200
	result: PASSED
	--------------------------------------------------------------------------------
	test:   read group members list
	url:    http://localhost:8000/circle/api/groups/GROUP_NAME/members/3
	method: GET
	wanted: 200
	result: PASSED
	--------------------------------------------------------------------------------
	test:   read group profile timeline
	url:    http://localhost:8000/circle/api/groups/SomeGroup/timeline/3
	method: GET
	wanted: 200
	result: PASSED
	--------------------------------------------------------------------------------
	--------------------------------------------------------------------------------
	Finshed
	    tests ran:      63
	    PASSED          63
	    FAILED:         0
	All tests PASSED
