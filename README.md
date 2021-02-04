# Stratus API Unit Test Coverage

This library is written in Python, but all the information you need is in `spec.json`. This Python code has nothing to do with the API except for running the tests and creating the spec. You are expected to use the spec and write a client in whatever language your platform requires. The requests are all the same and extreemly simple. There are three HTTP methods `POST`, `DELETE`, `GET`. Data will return a standard HTTP status code `401 Unauthorized`, `400 Bad Request`, `405 Method Not Supported`, `200 OK`. Data are just standard `POST` parameters, except for `GET` requests, in which they are URL encoded. If you run the tests, you will be able to see exactly what the URL is, but you should be able to use the `data` parameter in the spec. The `path` parameter in the spec is for replacing keywords in the URL path. Authentaction is done with a cookie's `sessionid` (you can put this in the header or do whatever you like. The spec does not specify the `BASE_URL`. You need to use whatever `BASE_URL` is availble and deployed at the time (or your local).

## Quickstart:

Run all the tests and make sure they all pass:

	python3 main.py all

Run the test for a successfull 200 response for a POST http request to post to a user's Atrium timeline:

	python3 main.py atr_pro_tim POST 200
	# atr_pro_tim -> "Atrium Profile Timeline" (see DONELIST in main.py)

## Usage:

	Usage:
	      $ python3 main.py [label] +| ([method|status] [status|method])")
	Examples:
	    Dump the current spec:
	      $ python3 main.py dumpspec > spec.json
	    Run all tests:
	      $ python3 main.py all
	    Run a single test for a label, method, and status:
	      $ python3 main.py [label] [method] [status]
	    Run all tests for a label:
	      $ python3 main.py [label]

## Running These Tests:

First, install requirements by running `pip3 install -r requirments.txt`.

You need some valid configuration. You can either set the `SESSION_ID` and `BASE_URL`
in `config.py` or set the values in your environment.

	# config.py

	SESSION_ID = os.getenv('SESSION_ID')
	if SESSION_ID is None:
	    SESSION_ID = '8okfl9z8yftehjw8btj3codtbuy46db1'

	BASE_URL =  os.getenv('BASE_URL')
	if BASE_URL is None:
	    BASE_URL = 'http://localhost:8000/'

## Tests:

Tests dumped in `spec.json` are simply what's in `tests.py`. `tests.py` is the *master list*
of tests done. Testing will *not* read from `spec.json`, only write to it. If you want to add
more tests, but them in `tests.py` and update the spec after by running:

	python3 main.py dumpspec > spec.json

## Example Posts, Groups, etc:

It's useful to have examples of Posts, Groups, Events, and other things, both valid and invalid.
You can find examples used multiple times in testing in `examples.py`.
Note that when you dump the spec, those examples are duplciated and there is no such single
reference of examples in the `spec.json`, only full layouts of them.

## URLs Done So Far:

    # Core 
	core/api/signup
	core/api/siginin
	core/api/settings
	core/api/settings/profile/basic
	core/api/settings/profile/work
	core/api/settings/profile/location
	core/api/settings/profile/education
	core/api/settings/profile/social
	core/api/settings/security/password
	core/api/settings/security/sessions
	core/api/settings/privacy
	core/api/settings/notifications
	core/api/settings/affiliates
	core/api/settings/verification
	core/api/settings/blocking
	core/api/settings/delete
    # Circle
	circle/api/timeline
	circle/api/timeline/PAGE
	circle/api/post/POST_ID
	circle/api/popular/PAGE
	circle/api/saved/PAGE
	circle/api/products/PAGE
	circle/api/articles/PAGE
	circle/api/people/PAGE
	circle/api/people/friend_requests/PAGE
	circle/api/people/friend_requests/sent/PAGE
	circle/api/search/PAGE
	circle/api/search/hashtag/PAGE
	circle/api/search/articles/PAGE
	circle/api/search/users/PAGE
	circle/api/search/pages/PAGE
	circle/api/search/groups/PAGE
	circle/api/search/events/PAGE
	circle/api/messages
	circle/api/messages/CONVERSATION_ID
	circle/api/message/MESSAGE_ID
	circle/api/groups
	circle/api/groups/PAGE
	circle/api/groups/joined/PAGE
	circle/api/groups/manage/PAGE
	circle/api/groups/GROUP_NAME
	circle/api/groups/GROUP_NAME/action
	circle/api/groups/GROUP_NAME/timeline
	circle/api/groups/GROUP_NAME/timeline/PAGE
	circle/api/groups/GROUP_NAME/members/PAGE
	circle/api/groups/GROUP_NAME/photos/PAGE
	circle/api/groups/GROUP_NAME/albums/PAGE
	circle/api/groups/GROUP_NAME/videos/PAGE
	circle/api/events
	circle/api/events/PAGE
	circle/api/events/going/PAGE
	circle/api/events/interested/PAGE
	circle/api/events/invited/PAGE
	circle/api/events/manage/PAGE
	circle/api/events/EVENT_NAME
	circle/api/events/EVENT_NAME/action
	circle/api/events/EVENT_NAME/timeline
	circle/api/events/EVENT_NAME/timeline/PAGE
	circle/api/events/EVENT_NAME/interested/PAGE
	circle/api/events/EVENT_NAME/invited/PAGE
	circle/api/events/EVENT_NAME/going/PAGE
	circle/api/events/EVENT_NAME/photos/PAGE
	circle/api/events/EVENT_NAME/albums/PAGE
	circle/api/events/EVENT_NAME/videos/PAGE
	circle/api/pages
	circle/api/pages/PAGE
	circle/api/pages/liked/PAGE
	circle/api/pages/manage/PAGE
	circle/api/pages/PAGE_NAME
	circle/api/pages/PAGE_NAME/action
	circle/api/pages/PAGE_NAME/timeline
	circle/api/pages/PAGE_NAME/timeline/PAGE
	circle/api/pages/PAGE_NAME/photos/PAGE
	circle/api/pages/PAGE_NAME/videos/PAGE
	circle/api/market/post/POST_ID
	circle/api/USER_NAME
	circle/api/USER_NAME/action
	circle/api/USER_NAME/timeline
	circle/api/USER_NAME/timeline/PAGE
	circle/api/USER_NAME/friends/PAGE
	circle/api/USER_NAME/following/PAGE
	circle/api/USER_NAME/followers/PAGE
	circle/api/USER_NAME/photos/PAGE
	circle/api/USER_NAME/albums/PAGE
	circle/api/USER_NAME/videos/PAGE
	circle/api/USER_NAME/groups/PAGE
	circle/api/USER_NAME/events/PAGE
    # Atrium
	atrium/api/timeline
	atrium/api/timeline/PAGE
	atrium/api/post/POST_ID
	atrium/api/explore/PAGE
	atrium/api/explore/hashtag/PAGE
	atrium/api/explore/articles/PAGE
	atrium/api/explore/users/PAGE
	atrium/api/messages
	atrium/api/messages/CONVERSATION_ID
	atrium/api/messages/CONVERSATION_ID/MESSAGE_ID
	atrium/api/USER_NAME
	atrium/api/USER_NAME/action
	atrium/api/USER_NAME/timeline
	atrium/api/USER_NAME/timeline/PAGE
	atrium/api/USER_NAME/following/PAGE
	atrium/api/USER_NAME/followers/PAGE
	atrium/api/USER_NAME/photos/PAGE
	atrium/api/USER_NAME/albums/PAGE
	atrium/api/USER_NAME/videos/PAGE

## URLs Not Done:

    # Circle
	circle/api/blogs
	circle/api/blogs/PAGE
	circle/api/blogs/category/CATEGORY_ID/PAGE
	circle/api/blogs/post/POST_ID
	circle/api/market
	circle/api/market/PAGE
	circle/api/market/category/CATEGORY_ID/PAGE
	circle/api/market/post/POST_ID
    # Atrium
	atrium/api/trending/PAGE
	atrium/api/bookmarks
	atrium/api/bookmarks/BOOKMARK_ID
	atrium/api/bookmarks/PAGE
	atrium/api/blogs
	atrium/api/blogs/PAGE
	atrium/api/blogs/category/CATEGORY_ID/PAGE
	atrium/api/blogs/post/POST_ID
    # Ads
	ads/api/wallet
	ads/api/campaigns
	ads/api/promoted
	ads/api/promoted/pages
	ads/api/promoted/posts

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

	python3 main.py cir_tim 401 POST

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

