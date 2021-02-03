SESSION_ID = '8okfl9z8yftehjw8btj3codtbuy46db1'
PAGE_EXAMPLES = {
    'valid_page': {
        'page_name': 'Exampe_Page',
        'title': 'Exampe Page',
        'description': 'Descriptin of my Page',
        'category': 'abalian',
        # Optional
        'company': 'Page, LLC',
        'phone_number': '911',
        'website': 'https://www.example.com',
        'photo': 'https://cdn1.stratus.co/231123141312312312.png',
        'pinned_post': '100',
        'location': 'Exampe Page',
        'action_text': 'Some Action Text',
        'action_url': 'https://www.example.com',
        'action_color': 'primary',
        'facebook_link': 'https://www.facebook.com/thispage',
        'twitter_link': 'https://www.twitter.com/thispage',
        'youtube_link': 'https://www.youtube.com/thispage',
        'instagram_link': 'https://www.instagram.com/thispage',
        'linkedin_link': 'https://www.linkedin.com/thispage',
        'vkontate_link': 'https://www.example.com/thispage',
    },
    'invalid_page_bad_socials': {
        'page_name': 'Exampe_Page',
        'description': 'Descriptin of my Page',
        'category': 'abalian',
        'facebook_link': 'BAD URL',
        'twitter_link': 'https://www.twitter.com/thispage',
        'youtube_link': 'BAD URL',
        'instagram_link': 'https://www.instagram.com/thispage',
        'linkedin_link': 'https://www.linkedin.com/thispage',
        'vkontate_link': 'https://www.example.com/thispage',
    },
    'invalid_page_missing_title': {
        'page_name': 'Exampe_Page',
        'description': 'Descriptin of my Page',
        'category': 'abalian',
        # Optional
        'company': 'Page, LLC',
        'phone_number': '911',
        'website': 'https://www.example.com',
        'photo': 'https://cdn1.stratus.co/231123141312312312.png',
        'pinned_post': '100',
        'location': 'Exampe Page',
        'action_text': 'Some Action Text',
        'action_url': 'https://www.example.com',
        'action_color': 'primary',
        'facebook_link': 'https://www.facebook.com/thispage',
        'twitter_link': 'https://www.twitter.com/thispage',
        'youtube_link': 'https://www.youtube.com/thispage',
        'instagram_link': 'https://www.instagram.com/thispage',
        'linkedin_link': 'https://www.linkedin.com/thispage',
        'vkontate_link': 'https://www.example.com/thispage',
    },
}   
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
    {
        'url': 'circle/api/pages',
        'label': 'cir_pag',
        'POST': {
            '200': {
                # DONE
                'create a new page': {
                    'data': PAGE_EXAMPLES['valid_page'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                # DONE
                'create a new page (while not logged in)': {
                    'path': {
                        'USER_NAME': 'akleinhans',
                    },
                },
            },
            '400': {
                # DONE
                'create a new page (with a missing title)': {
                    'data': PAGE_EXAMPLES['invalid_page_missing_title'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
                'create a new page (bad social links)': {
                    'data': PAGE_EXAMPLES['invalid_page_bad_socials'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
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
    # @DONE 'url': 'circle/api/market/post/POST_ID',
    {
        'url': 'circle/api/market/post/POST_ID',
        'label': 'cir_mar_post', #DONE
        'GET': {
            '200': {
                # DONE
                'view market post': {
                    'path': {
                        'POST_ID': '100',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME',
    {
        'url': 'circle/api/USER_NAME',
        'label': 'cir_pro',
        'GET': {
            '200': {
                # DONE
                'load profile': {
                    'path': {
                        'USER_NAME': 'akelinhans',
                    },
                },
            },
            '404': {
                # DONE
                'alex profile normal': {
                    'path': {
                        'USER_NAME': '****',
                    },
                },
            },
        },
        'POST': {
            '405': {
                # DONE
                'anththing': {
                    'path': {
                        'USER_NAME': 'akleinhans',
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
    # @DONE 'url': 'circle/api/USER_NAME/timeline/PAGE',
    {
        'url': 'circle/api/USER_NAME/timeline/PAGE',
        'label': 'cir_pro_tim_page',
        'GET': {
            '200': { #DONE
                'read profile timeline': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME/friends/PAGE',
    {
        'url': 'circle/api/USER_NAME/friends/PAGE',
        'label': 'cir_pro_tim_fr',
        'GET': {
            '200': { #DONE
                'read profile friend list': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME/following/PAGE',
    {
        'url': 'circle/api/USER_NAME/following/PAGE',
        'label': 'cir_pro_fing',
        'GET': {
            '200': { #DONE
                'read profile following': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME/followers/PAGE',
    {
        'url': 'circle/api/USER_NAME/followers/PAGE',
        'label': 'cir_pro_frs',
        'GET': {
            '200': { #DONE
                'read profile followers': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME/photos/PAGE',
    {
        'url': 'circle/api/USER_NAME/photos/PAGE',
        'label': 'cir_pro_photos',
        'GET': {
            '200': { #DONE
                'read profile photos': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME/albums/PAGE',
    {
        'url': 'circle/api/USER_NAME/albums/PAGE',
        'label': 'cir_pro_albums',
        'GET': {
            '200': { #DONE
                'read profile albums': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME/videos/PAGE',
    {
        'url': 'circle/api/USER_NAME/videos/PAGE',
        'label': 'cir_pro_videos',
        'GET': {
            '200': { #DONE
                'read profile videos': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME/groups/PAGE',
    {
        'url': 'circle/api/USER_NAME/groups/PAGE',
        'label': 'cir_pro_groups',
        'GET': {
            '200': { #DONE
                'read profile groups': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    # @DONE 'url': 'circle/api/USER_NAME/events/PAGE',
    {
        'url': 'circle/api/USER_NAME/events/PAGE',
        'label': 'cir_pro_events',
        'GET': {
            '200': { #DONE
                'read profile events': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
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
        f.write('%s: %s %s %s\n' % (result, label, method, status_code))
        f.close()

def print_summary(tests_run, tests_passed, tests_failed):
    print('--------------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------------')
    if tests_run == 0:
        print('\033[91mno matching tests found\033[0m')
    elif tests_failed == 0:
        print("""Finshed
    tests ran:      %s
    \033[92mPASSED\033[0m          %s
    FAILED:         0""" % (tests_run, tests_passed))
        print('\033[92mAll tests PASSED\033[0m')
    else:
        print("""Finshed
    tests ran:      %s
    PASSED:         %s
    \033[91mFAILED:         %s \033[0m
        """ % (tests_run, tests_passed, tests_failed))

def run_method_status(chosen_label, chosen_method, chosen_status, minimal=True):
    
    # Count tests run.
    tests_run = 0
    tests_failed = 0
    tests_passed = 0

    # You need to choose a test label.
    if chosen_label is None:
        print('No label specified. Aborting.')
        return

    # Filiter all tests with matching label.
    tests = list(filter(lambda test:
        test.get('label') == chosen_label, TESTS))
    if len(tests) == 0:
        print('no tests with that label')
        return

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
                        tests_passed += 1
                    else:
                        print_test(URL, method, '\033[91mFAILED\033[0m', test_name, status, status_code, data, text,
                                minimal=minimal)
                        tests_run += 1
                        tests_failed += 1

    # Don't print if we're running multiple tests because
    # the summary will print at the end.
    if minimal == False:
        print_summary(tests_run, tests_passed, tests_failed)

    return tests_run, tests_passed, tests_failed

# Run all of the tests with this label (for all specified
# HTTP methods and HTTP status codes). 
def run_label(label, minimal=True):
    tests_run = 0
    tests_failed = 0
    tests_passed = 0
    tests = list(filter(lambda test:
        test.get('label') == label, TESTS))
    for test in tests:
        for method, val in test.items():
            if method in ['POST','GET','DELETE']:
                for status, test in val.items():
                    _tests_run, _tests_passed, _tests_failed = run_method_status(
                        label, method, status, minimal=True)
                    tests_run += _tests_run
                    tests_passed += _tests_passed
                    tests_failed += _tests_failed
    if minimal == False:
        print_summary(tests_run, tests_passed, tests_failed)
    return tests_run, tests_passed, tests_failed

# All the tests I've already done.
DONE_LIST = ['cir_pro_tim','cir_pro','cir_pro_tim_page',
        'cir_pro_fr',
        'cir_pro_fing',
        'cir_pro_frs',
        'cir_pro_photos',
        'cir_pro_albums',
        'cir_pro_videos',
        'cir_pro_groups',
        'cir_pro_events',
        'cir_pag',
        ]

if __name__ == '__main__':

    print(chr(27) + "[2J")
    # Print args
    if len(sys.argv) == 1:
        print("test [label] +| ([method|status] [status|method])")
        exit()

    # Get the label you want to run. 
    label = sys.argv[1]

    # Run all previously done tests.
    if label == 'donelist':
        tests_run = 0
        tests_failed = 0
        tests_passed = 0
        for _label in DONE_LIST:
            _tests_run, _tests_passed, _tests_failed = run_label(_label)
            tests_run += _tests_run
            tests_passed += _tests_passed
            tests_failed += _tests_failed
        print_summary(tests_run, tests_passed, tests_failed)
        exit()
    # Not specifying an HTTP method or status will run all tests with that label.
    if len(sys.argv) == 2:
        run_label(label)

    # Print args again if missuse.
    if len(sys.argv) < 4:
        print("test [label] +| ([method|status] [status|method])")
        exit()

    # Parse the next args, but let them swap order. Allow the arguments
    # 2 and 4 to be short for the common 200 and 400 http codes.
    # For example:
    #
    #       $test label POST 200
    #
    # can also be run as:
    #
    #       $test label p 2
    #       $test label 2 p
    # 
    # Anything more specific must specify either 'post','get','delete' and
    # the exact HTTP status code, i.e. 405, 401, etc. Other HTTP methods
    # are not supported.
    one = sys.argv[2]
    two = sys.argv[3]
    if one[0] in ['2','4']:
        status = one
        method = two
    else:
        method  = one
        status = two

    # Run the tests.
    run_method_status(label, method, status, minimal=False)
