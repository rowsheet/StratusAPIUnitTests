SESSION_ID = '8okfl9z8yftehjw8btj3codtbuy46db1'
POST_EXAMPLES = {
    #---------------------------------------------------------------------------
    # INVALID POSTS 
    #---------------------------------------------------------------------------
    'valid_media': {
        'post_type': 'media',
        'url': 'https://google.com/?no=matter&how=fast&i=run',
        'provider': 'Breitbart Media Outlet',
        'type': 'photo',
        'title': 'Title of my post',
        'text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'html': '<html>how to meet ladies</html>',
    },
    #---------------------------------------------------------------------------
    # INVALID POSTS
    #---------------------------------------------------------------------------
    'invalid_post_type': {
        'post_type': 'foo',
    },
    'invalid_media_bad_url': {
        'post_type': 'media',
        'url': 'THIS IS NOT A URL',
        'provider': 'Breitbart Media Outlet',
        'type': 'photo',
        'title': 'Title of my post',
        'text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'html': '<html>how to meet ladies</html>',
    },
    'invalid_media_missing_provider': {
        'post_type': 'media',
        'url': 'https://google.com/?no=matter&how=fast&i=run',
        'type': 'photo',
        'title': 'Title of my post',
        'text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'html': '<html>how to meet ladies</html>',
    },
    'invalid_media_invalid_type': {
        'post_type': 'media',
        'url': 'https://google.com/?no=matter&how=fast&i=run',
        'provider': 'Breitbart Media Outlet',
        'type': 'NOT A VALID TYPE',
        'title': 'Title of my post',
        'text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'html': '<html>how to meet ladies</html>',
    },
    'invalid_media_missing_title': {
        'post_type': 'media',
        'url': 'https://google.com/?no=matter&how=fast&i=run',
        'provider': 'Breitbart Media Outlet',
        'type': 'photo',
        'title': 'Title of my post',
        'text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'html': '<html>how to meet ladies</html>',
    },
    'invalid_media_invalid_title': {
        'post_type': 'media',
        'url': 'https://google.com/?no=matter&how=fast&i=run',
        'provider': 'Breitbart Media Outlet',
        'type': 'photo',
        'title': '****INVALID TITLE CHARACTERS******',
        'text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'html': '<html>how to meet ladies</html>',
    },
}

TESTS = [
    # BLANK
    {
        'url': '_URL_',
        'label': '_LABEL_',
        'POST': {
        # 'GET': {
            '200': {
            # '400': {
                '_TEST_NAME_': {
                    'data': {
                    },
                    # 'data': None,
                    'headers': {
                    # 'headers': None,
                    },
                },
            },
        },
    },
    # TOP 
    #---------------------------------------------------------------------------
    # @TODO 'url': 'core/api/_index/',
    # @TODO 'url': 'core/api/signup',
    # @TODO 'url': 'core/api/signup',
    # @TODO 'url': 'core/api/siginin',
    # @TODO 'url': 'core/api/settings',
    # @TODO 'url': 'core/api/settings/profile',
    # @TODO 'url': 'core/api/settings/profile/basic',
    # @TODO 'url': 'core/api/settings/profile/work',
    # @TODO 'url': 'core/api/settings/profile/location',
    # @TODO 'url': 'core/api/settings/profile/education',
    # @TODO 'url': 'core/api/settings/profile/social',
    # @TODO 'url': 'core/api/settings/security',
    # @TODO 'url': 'core/api/settings/security/password',
    # @TODO 'url': 'core/api/settings/security/sessions',
    # @TODO 'url': 'core/api/settings/privacy',
    # @TODO 'url': 'core/api/settings/notifications',
    # @TODO 'url': 'core/api/settings/affiliates',
    # @TODO 'url': 'core/api/settings/verification',
    # @TODO 'url': 'core/api/settings/blocking',
    # @TODO 'url': 'core/api/settings/delete',
    # @TODO 'url': 'circle/api/_index',
    # @TODO 'url': 'circle/api/timeline',
    {
        'url': 'circle/api/timeline',
        'label': 'ctimeline',
        'POST': {
            '200': {
                'one': {
                    'data': {
                        'post_type': 'media',
                        'url': 'https://google.com/?no=matter&how=fast&i=run',
                        'provider': 'Breitbart Media Outlet',
                        'type': 'photo',
                        'title': 'Title of my post',
                        'text': 'The joke is that both the words ending in the same sylable that rhyme.',
                        'html': '<html>how to meet ladies</html>',
                    },
                    'headers': None,
                },
            },
            '400': {
                'Invlaid post_type': {
                    'data': {
                        'post_type': 'foo',
                        'url': 'https://google.com/?no=matter&how=fast&i=run',
                        'provider': 'Breitbart Media Outlet',
                        'type': 'photo',
                        'title': 'Title of my post',
                        'text': 'The joke is that both the words ending in the same sylable that rhyme.',
                        'html': '<html>how to meet ladies</html>',
                    },
                    'headers': None,
                },
            },
        },
    },
    # @TODO 'url': 'circle/api/timeline/PAGE',
    # @TODO 'url': 'circle/api/post/POST_ID',
    # @TODO 'url': 'circle/api/popular/PAGE',
    # @TODO 'url': 'circle/api/saved/PAGE',
    # @TODO 'url': 'circle/api/products/PAGE',
    # @TODO 'url': 'circle/api/articles/PAGE',
    # @TODO 'url': 'circle/api/search/PAGE',
    # @TODO 'url': 'circle/api/search/hashtag/PAGE',
    # @TODO 'url': 'circle/api/search/articles/PAGE',
    # @TODO 'url': 'circle/api/search/users/PAGE',
    # @TODO 'url': 'circle/api/search/pages/PAGE',
    # @TODO 'url': 'circle/api/search/groups/PAGE',
    # @TODO 'url': 'circle/api/search/events/PAGE',
    # @TODO 'url': 'circle/api/messages',
    # @TODO 'url': 'circle/api/messages/CONVERSATION_ID',
    # @TODO 'url': 'circle/api/messages/CONVERSATION_ID/MESSAGE_ID',
    # @TODO 'url': 'circle/api/groups',
    # @TODO 'url': 'circle/api/groups/PAGE',
    # @TODO 'url': 'circle/api/groups/joined/PAGE',
    # @TODO 'url': 'circle/api/groups/manage/PAGE',
    # @TODO 'url': 'circle/api/groups/GROUP_NAME',
    # @TODO 'url': 'circle/api/groups/GROUP_NAME/timeline',
    # @TODO 'url': 'circle/api/groups/GROUP_NAME/timeline/PAGE',
    # @TODO 'url': 'circle/api/groups/GROUP_NAME/photos/PAGE',
    # @TODO 'url': 'circle/api/groups/GROUP_NAME/albums/PAGE',
    # @TODO 'url': 'circle/api/groups/GROUP_NAME/videos/PAGE',
    # @TODO 'url': 'circle/api/groups/GROUP_NAME/members/PAGE',
    # @TODO 'url': 'circle/api/events',
    # @TODO 'url': 'circle/api/events/PAGE',
    # @TODO 'url': 'circle/api/events/going/PAGE',
    # @TODO 'url': 'circle/api/events/interested/PAGE',
    # @TODO 'url': 'circle/api/events/invited/PAGE',
    # @TODO 'url': 'circle/api/events/manage/PAGE',
    # @TODO 'url': 'circle/api/events/EVENT_NAME',
    # @TODO 'url': 'circle/api/events/EVENT_NAME/timeline',
    # @TODO 'url': 'circle/api/events/EVENT_NAME/timeline/PAGE',
    # @TODO 'url': 'circle/api/events/EVENT_NAME/photos/PAGE',
    # @TODO 'url': 'circle/api/events/EVENT_NAME/albums/PAGE',
    # @TODO 'url': 'circle/api/events/EVENT_NAME/videos/PAGE',
    # @TODO 'url': 'circle/api/events/EVENT_NAME/going/PAGE',
    # @TODO 'url': 'circle/api/events/EVENT_NAME/interested/PAGE',
    # @TODO 'url': 'circle/api/events/EVENT_NAME/invited/PAGE',
    # @TODO 'url': 'circle/api/pages',
    # @TODO 'url': 'circle/api/pages/PAGE',
    # @TODO 'url': 'circle/api/pages/liked/PAGE',
    # @TODO 'url': 'circle/api/pages/manage/PAGE',
    # @TODO 'url': 'circle/api/pages/PAGE_NAME',
    # @TODO 'url': 'circle/api/pages/PAGE_NAME/timeline',
    # @TODO 'url': 'circle/api/pages/PAGE_NAME/timeline/PAGE',
    # @TODO 'url': 'circle/api/pages/PAGE_NAME/photos/PAGE',
    # @TODO 'url': 'circle/api/pages/PAGE_NAME/videos/PAGE',
    # @TODO 'url': 'circle/api/people/PAGE',
    # @TODO 'url': 'circle/api/people/friend_requests/PAGE',
    # @TODO 'url': 'circle/api/people/friend_requests/sent/PAGE',
    # @TODO 'url': 'circle/api/blogs',
    # @TODO 'url': 'circle/api/blogs/PAGE',
    # @TODO 'url': 'circle/api/blogs/category/CATEGORY_ID/PAGE',
    # @TODO 'url': 'circle/api/blogs/post/POST_ID',
    # @TODO 'url': 'circle/api/market',
    # @TODO 'url': 'circle/api/market/PAGE',
    # @TODO 'url': 'circle/api/market/category/CATEGORY_ID/PAGE',
    # @TODO 'url': 'circle/api/market/post/POST_ID',
    # @TODO 'url': 'circle/api/USER_NAME',
    {
        'url': 'circle/api/USER_NAME',
        'label': 'profile',
        'GET': {
            '200': {
                'load profile': {
                    'path': {
                        'USER_NAME': 'akelinhans',
                    },
                },
            },
            '404': {
                'alex profile normal': {
                    'path': {
                        'USER_NAME': '****',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME/timeline',
    {
        'url': 'circle/api/USER_NAME/timeline',
        'label': 'cir_pro_tim', #DONE
        'POST': {
            '200': {
                # DONE
                'post to profile timline': {
                    'path': {
                        'USER_NAME': 'DrPib',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '400': {
                # DONE
                'post to profile timline (invalid post)': {
                    'path': {
                        'USER_NAME': 'DrPib',
                    },
                    'data': POST_EXAMPLES['invalid_media_bad_url'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                # DONE
                'post to profile timline (bad/no session_id)': {
                    'path': {
                        'USER_NAME': 'DrPib',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': 'Fake Session ID',
                    },
                },
            },
        },
        'GET': {
            '405': {
                # DONE
                'get profile timeline without specifying a page': {
                    'path': {
                        'USER_NAME': 'DrPib',
                    },
                },
            },
        },
    },
    # @TODO 'url': 'circle/api/USER_NAME/timeline/PAGE',
    # @TODO 'url': 'circle/api/USER_NAME/friends/PAGE',
    # @TODO 'url': 'circle/api/USER_NAME/following/PAGE',
    # @TODO 'url': 'circle/api/USER_NAME/followers/PAGE',
    # @TODO 'url': 'circle/api/USER_NAME/photos/PAGE',
    # @TODO 'url': 'circle/api/USER_NAME/albums/PAGE',
    # @TODO 'url': 'circle/api/USER_NAME/videos/PAGE',
    # @TODO 'url': 'circle/api/USER_NAME/groups/PAGE',
    # @TODO 'url': 'circle/api/USER_NAME/events/PAGE',
    # @TODO 'url': 'atrium/api/_index',
    # @TODO 'url': 'atrium/api/timeline',
    # @TODO 'url': 'atrium/api/timeline/PAGE',
    # @TODO 'url': 'atrium/api/post/POST_ID',
    # @TODO 'url': 'atrium/api/messages',
    # @TODO 'url': 'atrium/api/messages/CONVERSATION_ID',
    # @TODO 'url': 'atrium/api/messages/CONVERSATION_ID/MESSAGE_ID',
    # @TODO 'url': 'atrium/api/trending/PAGE',
    # @TODO 'url': 'atrium/api/explore/PAGE',
    # @TODO 'url': 'atrium/api/explore/hashtag/PAGE',
    # @TODO 'url': 'atrium/api/explore/articles/PAGE',
    # @TODO 'url': 'atrium/api/explore/users/PAGE',
    # @TODO 'url': 'atrium/api/bookmarks',
    # @TODO 'url': 'atrium/api/bookmarks/BOOKMARK_ID',
    # @TODO 'url': 'atrium/api/bookmarks/PAGE',
    # @TODO 'url': 'atrium/api/blogs',
    # @TODO 'url': 'atrium/api/blogs/PAGE',
    # @TODO 'url': 'atrium/api/blogs/category/CATEGORY_ID/PAGE',
    # @TODO 'url': 'atrium/api/blogs/post/POST_ID',
    # @TODO 'url': 'atrium/api/USER_NAME',
    # @TODO 'url': 'atrium/api/USER_NAME/timeline',
    # @TODO 'url': 'atrium/api/USER_NAME/timeline/PAGE',
    # @TODO 'url': 'atrium/api/USER_NAME/following/PAGE',
    # @TODO 'url': 'atrium/api/USER_NAME/followers/PAGE',
    # @TODO 'url': 'atrium/api/USER_NAME/photos/PAGE',
    # @TODO 'url': 'atrium/api/USER_NAME/albums/PAGE',
    # @TODO 'url': 'atrium/api/USER_NAME/videos/PAGE',
    # @TODO 'url': 'ads/api/_index',
    # @TODO 'url': 'ads/api/wallet',
    # @TODO 'url': 'ads/api/campaigns',
    # @TODO 'url': 'ads/api/promoted',
    # @TODO 'url': 'ads/api/promoted/pages',
    # @TODO 'url': 'ads/api/promoted/posts',
]

import requests
import sys
import json

BASE_URL = 'http://localhost:8000/'

def print_test(url, method, result, test_name, wanted, status_code, data, text, minimal=False):
    try:
        text = json.dumps(json.loads(text), indent=4)
    except:
        text = "\tUNIT TEST\n\tEXCEPTION: API Responded with a non-JSON response."

    if minimal == True:
        print('--------------------------------------------------------------------------------')
        print('test:   ' + test_name)
        print('url:    ' + url)
        print('method: ' + method)
        print('wanted: ' + str(wanted))
        print('result: ' + result)
    else:
        print('--------------------------------------------------------------------------------')
        print('test:   ' + test_name)
        print('method: ' + method)
        print('url:    ' + url)
        print('')
        print('wanted: ' + str(wanted))
        print('got:    ' + str(status_code))
        print('result: ' + result)
        print('--------------------------------------------------------------------------------')
        print('')
        print('- - - - - - - - - - - - - - - - - - - - - - ')
        print('method:   ' + method)
        print('status:   ' + str(status_code))
        print('request:  ' + test_name)
        print('- - - - - - - - - - - - - - - - - - - - - - ')
        print('')
        print(json.dumps(data, indent=4))
        print('')
        print('- - - - - - - - - - - - - - - - - - - - - - ')
        print('status:    ' + str(status_code))
        print('response:')
        print('- - - - - - - - - - - - - - - - - - - - - - ')
        print('')
        print(text)
        print('')
    with open('runs.txt', 'a') as f:
        f.write('%s: %s %s %s\n' % (result, label, method, status))
        f.close()

def run_tests(chosen_label, chosen_method, chosen_status, minimal=True):
    
    # Count tests run.
    tests_run = 0

    # You need to choose a test label.
    if chosen_label is None:
        print('No label specified. Aborting.')
        exit()

    # Filiter all tests with matching label.
    tests = list(filter(lambda test:
        test.get('label') == chosen_label, TESTS))
    if len(tests) == 0:
        print('no tests with that label')
        exit()

    # For all tests...
    for test in tests:
        URL = BASE_URL + test['url']
        method = chosen_method.upper()
        if len(method) == 1:
            if method == 'G':
                method = 'GET'
            if method == 'P':
                method = 'POST'
            if method == 'D':
                method = 'DELETE'
        METHOD = test.get(method)

        if METHOD is not None:
            status = chosen_status
            if len(status) == 1:
                status += '00'
            METHOD_STATUSs = METHOD.get(status)

            if METHOD_STATUSs is not None:

                for test_name, METHOD_STATUS in METHOD_STATUSs.items():

                    path_vars = METHOD_STATUS.get('path')
                    if path_vars is not None:
                        for key, val in path_vars.items():
                            URL = URL.replace(key, val)

                    data = METHOD_STATUS.get('data')
                    cookies = METHOD_STATUS.get('cookies')
                    status_code = None
                    text = None

                    if method == 'POST':
                        response = requests.post(URL, data, cookies=cookies)
                    elif method == 'GET':
                        response = requests.get(URL, data, cookies=cookies)
                    elif method == 'DELETE':
                        response = requests.delete(URL, data, cookies=cookies)
                    else:
                        raise Exception("Unknown HTTP request method '%s'." % method)

                    status_code = response.status_code
                    text = response.text

                    if str(status_code) == status:
                        print_test(URL, method, '\033[92mPASSED\033[0m', test_name, status, status_code, data, text,
                                minimal=minimal)
                        tests_run += 1
                    else:
                        print_test(URL, method, '\033[91mFAILED\033[0m', test_name, status, status_code, data, text,
                                minimal=minimal)
                        tests_run += 1

    if minimal == False:
        print('--------------------------------------------------------------------------------')
        print('--------------------------------------------------------------------------------')
        print("Finshed\n\t%s test requests made." % tests_run)

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("test [label] +| ([method|status] [status|method])")
        exit()

    label = sys.argv[1]

    if len(sys.argv) == 2:
        tests_run = 0
        tests_failed = 0
        tests_passed = 0
        print("Running all tests for label '%s'." % label)
        print('--------------------------------------------------------------------------------')
        print(chr(27) + "[2J")
        tests = list(filter(lambda test:
            test.get('label') == label, TESTS))
        for test in tests:
            for method, val in test.items():
                if method in ['POST','GET','DELETE']:
                    for status, test in val.items():
                        run_tests(label, method, status, minimal=True)
                        tests_run += 1
        print('--------------------------------------------------------------------------------')
        print('--------------------------------------------------------------------------------')
        print("Finshed\n\t%s test requests made." % tests_run)
        exit()

    if len(sys.argv) < 4:
        print("test [label] +| ([method|status] [status|method])")
        exit()

    label = sys.argv[1]

    one = sys.argv[2]
    two = sys.argv[3]

    if one[0] in ['2','4']:
        status = one
        method = two
    else:
        method  = one
        status = two

    print(chr(27) + "[2J")
    run_tests(label, method, status, minimal=False)
