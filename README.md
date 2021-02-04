# Stratus API Unit Test Coverage

## URLs Done So Far:

    # Core 
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
	circle/api/messages
	circle/api/messages/CONVERSATION_ID
	circle/api/message/MESSAGE_ID
	circle/api/groups
	circle/api/groups/PAGE
	circle/api/groups/joined/PAGE
	circle/api/groups/manage/PAGE
	circle/api/groups/GROUP_NAME
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
	circle/api/pages/PAGE_NAME/timeline
	circle/api/pages/PAGE_NAME/timeline/PAGE
	circle/api/pages/PAGE_NAME/photos/PAGE
	circle/api/pages/PAGE_NAME/videos/PAGE
	circle/api/market/post/POST_ID
	circle/api/USER_NAME
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

## URLs Not Done:

    # Core 
	core/api/signup
	core/api/signup
	core/api/siginin
    # Circle
	circle/api/timeline
	circle/api/search/PAGE
	circle/api/search/hashtag/PAGE
	circle/api/search/articles/PAGE
	circle/api/search/users/PAGE
	circle/api/search/pages/PAGE
	circle/api/search/groups/PAGE
	circle/api/search/events/PAGE
	circle/api/people/PAGE
	circle/api/people/friend_requests/PAGE
	circle/api/people/friend_requests/sent/PAGE
	circle/api/blogs
	circle/api/blogs/PAGE
	circle/api/blogs/category/CATEGORY_ID/PAGE
	circle/api/blogs/post/POST_ID
	circle/api/market
	circle/api/market/PAGE
	circle/api/market/category/CATEGORY_ID/PAGE
	circle/api/market/post/POST_ID
    # Atrium
	atrium/api/timeline
	atrium/api/timeline/PAGE
	atrium/api/post/POST_ID
	atrium/api/messages
	atrium/api/messages/CONVERSATION_ID
	atrium/api/messages/CONVERSATION_ID/MESSAGE_ID
	atrium/api/trending/PAGE
	atrium/api/explore/PAGE
	atrium/api/explore/hashtag/PAGE
	atrium/api/explore/articles/PAGE
	atrium/api/explore/users/PAGE
	atrium/api/bookmarks
	atrium/api/bookmarks/BOOKMARK_ID
	atrium/api/bookmarks/PAGE
	atrium/api/blogs
	atrium/api/blogs/PAGE
	atrium/api/blogs/category/CATEGORY_ID/PAGE
	atrium/api/blogs/post/POST_ID
	atrium/api/USER_NAME
	atrium/api/USER_NAME/timeline
	atrium/api/USER_NAME/timeline/PAGE
	atrium/api/USER_NAME/following/PAGE
	atrium/api/USER_NAME/followers/PAGE
	atrium/api/USER_NAME/photos/PAGE
	atrium/api/USER_NAME/albums/PAGE
	atrium/api/USER_NAME/videos/PAGE
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
`python3 main.py cir_tim 401 POST`

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

