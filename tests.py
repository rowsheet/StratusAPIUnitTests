from examples import EVENT_EXAMPLES
from examples import POST_EXAMPLES
from examples import PAGE_EXAMPLES
from examples import GROUP_EXAMPLES
from config import SESSION_ID

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
    # @TODO 'url': 'core/api/signup',
    # @TODO 'url': 'core/api/signup',
    # @TODO 'url': 'core/api/siginin',
    {
        'url': 'core/api/settings',
        'label': 'cor_set',
        'GET': {
            '200': {
                'read account settings': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'POST': {
            '200': {
                'update account settings': {
                    'data': {
                        'email_address': 'rowsheet.com@gmail.com',
                        'user_name': 'ThisIsMyUserName',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    {
        'url': 'core/api/settings/profile/basic',
        'label': 'cor_set_pro_bas',
        'GET': {
            '200': {
                'read profile basic': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'POST': {
            '200': {
                'update profile basic': {
                    'data': {
                        'first_name': 'Alex',
                        'last_name': 'Kleinhans',
                        'gender': 'male',
                        'relationship_status': 'single',
                        'country': 'Antarctica',
                        'website': 'https://www.stratus.co',
                        'birth_year': '1800',
                        'birth_day': '01',
                        'birth_month': '01',
                        'about_me': 'Thank you! Very cool!',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    {
        'url': 'core/api/settings/profile/work',
        'label': 'cor_set_pro_wrk',
        'GET': {
            '200': {
                'read profile work': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'POST': {
            '200': {
                'update profile work': {
                    'data': {
                        'work_title': 'Lepricon',
                        'work_place': 'Rainbows',
                        'work_website': 'https://www.bitcoin.org',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    {
        'url': 'core/api/settings/profile/location',
        'label': 'cor_set_pro_loc',
        'GET': {
            '200': {
                'read profile location': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'POST': {
            '200': {
                'update profile location': {
                    'data': {
                        'current_city': 'Tuskegee, Alabama',
                        'hometown': 'Tiananmen Square',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    {
        'url': 'core/api/settings/profile/education',
        'label': 'cor_set_pro_edu',
        'GET': {
            '200': {
                'read profile education': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'POST': {
            '200': {
                'update profile education': {
                    'data': {
                        'school': 'Yale',
                        'major': 'Corruption',
                        'graduation_class': '1984',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    {
        'url': 'core/api/settings/profile/social',
        'label': 'cor_set_pro_soc',
        'GET': {
            '200': {
                'read profile social': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'POST': {
            '200': {
                'update profile social': {
                    'data': {
                        'facebook': 'https://www.facebook.com/sneed',
                        'twitter': 'https://www.twitter.com/sneed',
                        'youtube': 'https://www.youtube.com/sneed',
                        'instagram': 'https://www.instagram.com/sneed',
                        'linkedin': 'https://www.linkedin.com/sneed',
                        'vkontakte': 'https://www.vkontakte.com/sneed',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    {
        'url': 'core/api/settings/security/password',
        'label': 'cor_set_sec_pas',
        'POST': {
            '200': {
                'update security password': {
                    'data': {
                        'current_password': 'password is very long',
                        'new_password': 'passw0rd is very long',
                        'confirm_new_password': 'passw0rd is very long',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    {
        'url': 'core/api/settings/security/sessions',
        'label': 'cor_set_sec_ses',
        'GET': {
            '200': {
                'read security sessions': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'DELETE': {
            '200': {
                'update security sessions': {
                    'data': {
                        'session_id': '12312313123',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    {
        'url': 'core/api/settings/privacy',
        'label': 'cor_set_pri',
        'GET': {
            '200': {
                'read privacy settings': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'POST': {
            '200': {
                'update privacy settings': {
                    'data': {
                        'poke': 'everyone',
                        'post_wall': 'everyone',
                        'dob': 'everyone',
                        'see_rel': 'everyone',
                        'see_basic': 'everyone',
                        'see_work': 'everyone',
                        'see_loc': 'everyone',
                        'see_edu': 'everyone',
                        'see_other': 'everyone',
                        'see_friends': 'everyone',
                        'see_photos': 'everyone',
                        'see_liked': 'everyone',
                        'see_groups': 'everyone',
                        'see_events': 'everyone',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
            '400': {
                'bad options': {
                    'data': {
                        'poke': 'everyone',
                        'post_wall': 'foo',
                        'dob': 'everyone',
                        'see_rel': 'everyone',
                        'see_basic': 'everyone',
                        'see_work': 'bar',
                        'see_loc': 'everyone',
                        'see_edu': 'everyone',
                        'see_other': 'everyone',
                        'see_friends': 'myself', # should be 'me'
                        'see_photos': 'everyone',
                        'see_liked': 'everyone',
                        'see_groups': 'everyone',
                        'see_events': 'everyone',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'core/api/settings/notifications',
        'label': 'cor_set_not',
        'GET': {
            '200': {
                'read notification settings': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'POST': {
            '200': {
                'update notification settings': {
                    'data': {
                        'sound': True,
                        'chat_sount': True,
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    # @TODO 'url': 'core/api/settings/affiliates',
    {
        'url': 'core/api/settings/verification',
        'label': 'cor_set_ver',
        'GET': {
            '200': {
                'read verification settings': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
        'POST': {
            '200': {
                'update verification settings': {
                    'data': {
                        'photo_file': 'file://me.png',
                        'passport_file': 'file://passport.png',
                        'other_info': '$eth R1ch',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    # @TODO 'url': 'core/api/settings/blocking',
    {
        'url': 'core/api/settings/delete',
        'label': 'cor_set_del',
        'POST': {
            '200': {
                'delete my account': {
                    'data': {
                        'confirmation_string': 'I am absolutley sure that I, akleinhans, want to PERMINANTLY DELETE my account, and I understand this will PERMINANTLY REMOVE all of my data FOREVER.',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {'unauthorized request': {},},
        },
    },
    {
        'url': 'circle/api/timeline',
        'label': 'cir_tim',
        'POST': {
            '200': {
                'create a post on my own timeline': {
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'create a post on my own timeline (while not logged in)': {
                    'data': POST_EXAMPLES['valid_media'],
                },
            },
        },
    },
    {
        'url': 'circle/api/timeline/PAGE',
        'label': 'cir_tim_page',
        'GET': {
            '200': {
                'read my timeline feed': {
                    'path': {
                        'PAGE': '1',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'read my timeline feed (while not logged in)': {
                    'path': {
                        'PAGE': '1',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/post/POST_ID',
        'label': 'cir_post',
        'GET': {
            '200': {
                'read my timeline feed': {
                    'path': {
                        'POST_ID': '100',
                    },
                },
            },
        },
        'POST': {
            '200': {
                'update a post': {
                    'path': {
                        'POST_ID': '100',
                    },
                    'data': POST_EXAMPLES['valid_media_post_update'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'update a post (while not logged in)': {
                    'path': {
                        'POST_ID': '100',
                    },
                    'data': POST_EXAMPLES['valid_media_post_update'],
                },
                'update a post (that I don\'t own)': {
                    'path': {
                        'POST_ID': '200',
                    },
                    'data': POST_EXAMPLES['valid_media_post_update'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
        'DELETE': {
            '200': {
                'delete a post': {
                    'path': {
                        'POST_ID': '100',
                    },
                    'data': POST_EXAMPLES['valid_media_post_update'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'delete a post (while not logged in)': {
                    'path': {
                        'POST_ID': '100',
                    },
                },
                'delete a post (that I don\'t own)': {
                    'path': {
                        'POST_ID': '200',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/popular/PAGE',
        'label': 'cir_tim_pop_page',
        'GET': {
            '200': {
                'read my popular timeline feed': {
                    'path': {
                        'PAGE': '1',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'read my popular timeline feed (while not logged in)': {
                    'path': {
                        'PAGE': '1',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/saved/PAGE',
        'label': 'cir_tim_svd_page',
        'GET': {
            '200': {
                'read my saved timeline feed': {
                    'path': {
                        'PAGE': '1',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'read my saved timeline feed (while not logged in)': {
                    'path': {
                        'PAGE': '1',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/products/PAGE',
        'label': 'cir_tim_prd_page',
        'GET': {
            '200': {
                'read my product timeline feed': {
                    'path': {
                        'PAGE': '1',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'read my product timeline feed (while not logged in)': {
                    'path': {
                        'PAGE': '1',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/articles/PAGE',
        'label': 'cir_tim_art_page',
        'GET': {
            '200': {
                'read my article timeline feed': {
                    'path': {
                        'PAGE': '1',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'read my article timeline feed (while not logged in)': {
                    'path': {
                        'PAGE': '1',
                    },
                },
            },
        },
    },
    # @TODO 'url': 'circle/api/search/PAGE',
    # @TODO 'url': 'circle/api/search/hashtag/PAGE',
    # @TODO 'url': 'circle/api/search/articles/PAGE',
    # @TODO 'url': 'circle/api/search/users/PAGE',
    # @TODO 'url': 'circle/api/search/pages/PAGE',
    # @TODO 'url': 'circle/api/search/groups/PAGE',
    # @TODO 'url': 'circle/api/search/events/PAGE',
    {
        'url': 'circle/api/messages',
        'label': 'cir_msg',
        'GET': {
            '200': {
                'read my message conversations': {
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'read my messages (while not logged in)': {
                },
            },
        },
        'POST': {
            '200': {
                'create a new message conversation': {
                    'data': {
                        'user_name': 'myFriendTom',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'create a new message conversation (while not logged in)': {
                    'data': {
                        'user_name': 'myFriendTom',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/messages/CONVERSATION_ID',
        'label': 'cir_msg_cnv',
        'GET': {
            '200': {
                'read my conversation messages': {
                    'path': {
                        'CONVERSATION_ID': '123123123',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'read my conversation messages (while not logged in).': {
                    'path': {
                        'CONVERSATION_ID': '123123123',
                    },
                },
                'read my conversation messages (to a conversation I don\'t own).': {
                    'path': {
                        'CONVERSATION_ID': '000000000000',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
        'POST': {
            '200': {
                'create a new message': {
                    'path': {
                        'CONVERSATION_ID': '123123123',
                    },
                    'data': {
                        'message_text': 'This is some message text.',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'create a new message (while not logged in).': {
                    'path': {
                        'CONVERSATION_ID': '123123123',
                    },
                    'data': {
                        'message_text': 'This is some message text.',
                    },
                },
            },
        },
        'DELETE': {
            '200': {
                'delete a conversation': {
                    'path': {
                        'CONVERSATION_ID': '123123123',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'delete a conversation (while not logged in)': {
                    'path': {
                        'CONVERSATION_ID': '123123123',
                    },
                },
                'delete a conversation (that I don\'t own).': {
                    'path': {
                        'CONVERSATION_ID': '000000000000',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/message/MESSAGE_ID',
        'label': 'cir_msg_cnv_msg',
        'POST': {
            '200': {
                'update an old message': {
                    'path': {
                        'MESSAGE_ID': '35435345',
                    },
                    'data': {
                        'message_text': 'This is some message text.',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'update an old message (while not logged in).': {
                    'path': {
                        'MESSAGE_ID': '35435345',
                    },
                    'data': {
                        'message_text': 'This is some message text.',
                    },
                },
                'update an old message (that I don\'t own).': {
                    'path': {
                        'MESSAGE_ID': '00000000000000',
                    },
                    'data': {
                        'message_text': 'This is some message text.',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
        'DELETE': {
            '200': {
                'delete an old message': {
                    'path': {
                        'MESSAGE_ID': '35435345',
                    },
                    'data': {
                        'message_text': 'This is some message text.',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'delete an old message (while not logged in).': {
                    'path': {
                        'MESSAGE_ID': '35435345',
                    },
                    'data': {
                        'message_text': 'This is some message text.',
                    },
                },
                'delete an old message (that I don\'t own).': {
                    'path': {
                        'MESSAGE_ID': '00000000000000',
                    },
                    'data': {
                        'message_text': 'This is some message text.',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups',
        'label': 'cir_grp',
        'POST': {
            '200': {
                'create a new group': {
                    'data': GROUP_EXAMPLES['valid_group'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'create a new group (while not logged in)': {
                    'path': {
                        'USER_NAME': 'akleinhans',
                    },
                },
            },
            '400': {
                'create a new group (with a missing title)': {
                    'data': GROUP_EXAMPLES['invalid_group_missing_title'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/PAGE',
        'label': 'cir_grp_page',
        'GET': {
            '200': {
                'load groups list': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/joined/PAGE',
        'label': 'cir_grp_jnd_page',
        'GET': {
            '200': {
                'load joined groups list': {
                    'path': {
                        'PAGE': '10',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load joined groups list (not logged in)': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/manage/PAGE',
        'label': 'cir_grp_man_page',
        'GET': {
            '200': {
                'load managed groups list': {
                    'path': {
                        'PAGE': '10',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load managed groups list (not logged in)': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME',
        'label': 'cir_grp_pro',
        'GET': {
            '200': {
                'load a group profile': {
                    'path': {
                        'GROUP_NAME': 'some_page_handle',
                    },
                },
            },
        },
        'POST': {
            '200': {
                'update a group': {
                    'path': {
                        'GROUP_NAME':'Example_Group',
                    },
                    'data': GROUP_EXAMPLES['valid_group_for_update'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'update a group (while not logged in)': {
                    'path': {
                        'GROUP_NAME':'FExample_Group',
                    },
                },
                'update a group (I\'m not an admin of)': {
                    'path': {
                        'GROUP_NAME':'Group_I_Dont_Admin_Foo',
                    },
                    'data': GROUP_EXAMPLES['valid_group_for_update'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
        'DELETE': {
            '200': {
                'delete a group': {
                    'path': {
                        'GROUP_NAME':'Example_Group',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'delete a group (while not logged in)': {
                    'path': {
                        'GROUP_NAME':'FExample_Group',
                    },
                },
                'delete a group (I\'m not an admin of)': {
                    'path': {
                        'GROUP_NAME':'Group_I_Dont_Admin_Foo',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/timeline',
        'label': 'cir_grp_pro_tim', 
        'POST': {
            '200': {
                'post to group timline': {
                    'path': {
                        'GROUP_NAME':'Example_Group',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '400': {
                'post to group timline (invalid post)': {
                    'path': {
                        'GROUP_NAME':'Example_Group',
                    },
                    'data': POST_EXAMPLES['invalid_media_bad_url'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'post to group timline (bad/no session_id)': {
                    'path': {
                        'GROUP_NAME':'Example_Group',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': 'Fake Session ID',
                    },
                },
                'post to group timline (I\'m not an admin of)': {
                    'path': {
                        'GROUP_NAME':'GroupThatsNotMyGroup',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
        'GET': {
            '405': {
                'get profile timeline without specifying a page': {
                    'path': {
                        'GROUP_NAME':'Example_Group',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/timeline/PAGE',
        'label': 'cir_grp_pro_tim_page',
        'GET': {
            '200': { 
                'read group profile timeline': {
                    'path': {
                        'GROUP_NAME': 'SomeGroup',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/members/PAGE',
        'label': 'cir_grp_pro_mbr_page',
        'GET': {
            '200': { 
                'read group members list': {
                    'path': {
                        'GROUP_NAME': 'SomeGroup',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/photos/PAGE',
        'label': 'cir_grp_pro_photos',
        'GET': {
            '200': { 
                'read group profile photos': {
                    'path': {
                        'GROUP_NAME': 'SomeGroup',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/albums/PAGE',
        'label': 'cir_grp_pro_albums',
        'GET': {
            '200': { 
                'read group profile albums': {
                    'path': {
                        'GROUP_NAME': 'SomeGroup',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/videos/PAGE',
        'label': 'cir_grp_pro_videos',
        'GET': {
            '200': { 
                'read group profile videos': {
                    'path': {
                        'GROUP_NAME': 'SomeGroup',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events',
        'label': 'cir_evt',
        'POST': {
            '200': {
                'create a new event': {
                    'data': EVENT_EXAMPLES['valid_event'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'create a new event (while not logged in)': {
                    'path': {
                        'USER_NAME': 'akleinhans',
                    },
                },
            },
            '400': {
                'create a new event (with a missing title)': {
                    'data': EVENT_EXAMPLES['invalid_event_missing_title'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/PAGE',
        'label': 'cir_evt_page',
        'GET': {
            '200': {
                'load events list': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/going/PAGE',
        'label': 'cir_evt_gng_page',
        'GET': {
            '200': {
                'load going events list': {
                    'path': {
                        'PAGE': '10',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load going events list (not logged in)': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/interested/PAGE',
        'label': 'cir_evt_int_page',
        'GET': {
            '200': {
                'load interested events list': {
                    'path': {
                        'PAGE': '10',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load interested events list (not logged in)': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/invited/PAGE',
        'label': 'cir_evt_ivt_page',
        'GET': {
            '200': {
                'load invited events list': {
                    'path': {
                        'PAGE': '10',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load invited events list (not logged in)': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/manage/PAGE',
        'label': 'cir_evt_man_page',
        'GET': {
            '200': {
                'load managed events list': {
                    'path': {
                        'PAGE': '10',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load managed events list (not logged in)': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME',
        'label': 'cir_evt_pro',
        'GET': {
            '200': {
                'load a event profile': {
                    'path': {
                        'EVENT_NAME': 'some_page_handle',
                    },
                },
            },
        },
        'POST': {
            '200': {
                'update a event': {
                    'path': {
                        'EVENT_NAME':'TheGretaReset',
                    },
                    'data': EVENT_EXAMPLES['valid_event_for_update'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'update a event (while not logged in)': {
                    'path': {
                        'EVENT_NAME':'FExample_Event',
                    },
                },
                'update a event (I\'m not an admin of)': {
                    'path': {
                        'EVENT_NAME':'Event_I_Dont_Admin_Foo',
                    },
                    'data': EVENT_EXAMPLES['valid_event_for_update'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
        'DELETE': {
            '200': {
                'delete a event': {
                    'path': {
                        'EVENT_NAME':'TheGretaReset',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'delete a event (while not logged in)': {
                    'path': {
                        'EVENT_NAME':'FExample_Event',
                    },
                },
                'delete a event (I\'m not an admin of)': {
                    'path': {
                        'EVENT_NAME':'Event_I_Dont_Admin_Foo',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/timeline',
        'label': 'cir_evt_pro_tim', 
        'POST': {
            '200': {
                'post to event timline': {
                    'path': {
                        'EVENT_NAME':'TheGretaReset',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '400': {
                'post to event timline (invalid post)': {
                    'path': {
                        'EVENT_NAME':'Example_Event',
                    },
                    'data': POST_EXAMPLES['invalid_media_bad_url'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'post to event timline (bad/no session_id)': {
                    'path': {
                        'EVENT_NAME':'Example_Event',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': 'Fake Session ID',
                    },
                },
                'post to event timline (I\'m not an admin of)': {
                    'path': {
                        'EVENT_NAME':'EventThatsNotMyEvent',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
        'GET': {
            '405': {
                'get profile timeline without specifying a page': {
                    'path': {
                        'EVENT_NAME':'Example_Event',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/timeline/PAGE',
        'label': 'cir_evt_pro_tim_page',
        'GET': {
            '200': { 
                'read event profile timeline': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/interested/PAGE',
        'label': 'cir_evt_pro_int_page',
        'GET': {
            '200': { 
                'read event interested list': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/invited/PAGE',
        'label': 'cir_evt_pro_inv_page',
        'GET': {
            '200': { 
                'read event invited list': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/going/PAGE',
        'label': 'cir_evt_pro_gng_page',
        'GET': {
            '200': { 
                'read event going list': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/photos/PAGE',
        'label': 'cir_evt_pro_photos',
        'GET': {
            '200': { 
                'read event profile photos': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/albums/PAGE',
        'label': 'cir_evt_pro_albums',
        'GET': {
            '200': { 
                'read profile albums': {
                    'path': {
                        'EVENT_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/videos/PAGE',
        'label': 'cir_evt_pro_videos',
        'GET': {
            '200': { 
                'read event profile videos': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages',
        'label': 'cir_pag',
        'POST': {
            '200': {
                'create a new page': {
                    'data': PAGE_EXAMPLES['valid_page'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'create a new page (while not logged in)': {
                    'path': {
                        'USER_NAME': 'akleinhans',
                    },
                },
            },
            '400': {
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
    {
        'url': 'circle/api/pages/PAGE',
        'label': 'cir_pag_page',
        'GET': {
            '200': {
                'load pages list': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages/liked/PAGE',
        'label': 'cir_pag_lik_page',
        'GET': {
            '200': {
                'load liked pages list': {
                    'path': {
                        'PAGE': '10',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load liked pages list (not logged in)': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages/manage/PAGE',
        'label': 'cir_pag_man_page',
        'GET': {
            '200': {
                'load managed pages list': {
                    'path': {
                        'PAGE': '10',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load managed pages list (not logged in)': {
                    'path': {
                        'PAGE': '10',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages/PAGE_NAME',
        'label': 'cir_pag_pro',
        'GET': {
            '200': {
                'load a page profile': {
                    'path': {
                        'PAGE_NAME': 'some_page_handle',
                    },
                },
            },
        },
        'POST': {
            '200': {
                'update a page': {
                    'path': {
                        'PAGE_NAME':'Example_Page',
                    },
                    'data': PAGE_EXAMPLES['valid_page_for_update'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'update a page (while not logged in)': {
                    'path': {
                        'PAGE_NAME':'FExample_Page',
                    },
                },
                'update a page (I\'m not an admin of)': {
                    'path': {
                        'PAGE_NAME':'Page_I_Dont_Admin_Foo',
                    },
                    'data': PAGE_EXAMPLES['valid_page_for_update'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
        'DELETE': {
            '200': {
                'delete a page': {
                    'path': {
                        'PAGE_NAME':'Example_Page',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'delete a page (while not logged in)': {
                    'path': {
                        'PAGE_NAME':'FExample_Page',
                    },
                },
                'delete a page (I\'m not an admin of)': {
                    'path': {
                        'PAGE_NAME':'Page_I_Dont_Admin_Foo',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages/PAGE_NAME/timeline',
        'label': 'cir_pag_pro_tim', 
        'POST': {
            '200': {
                'post to page timline': {
                    'path': {
                        'PAGE_NAME':'Example_Page',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '400': {
                'post to page timline (invalid post)': {
                    'path': {
                        'PAGE_NAME':'Example_Page',
                    },
                    'data': POST_EXAMPLES['invalid_media_bad_url'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'post to page timline (bad/no session_id)': {
                    'path': {
                        'PAGE_NAME':'Example_Page',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': 'Fake Session ID',
                    },
                },
                'post to page timline (I\'m not an admin of)': {
                    'path': {
                        'PAGE_NAME':'PageThatsNotMyPage',
                    },
                    'data': POST_EXAMPLES['valid_media'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
        'GET': {
            '405': {
                'get profile timeline without specifying a page': {
                    'path': {
                        'PAGE_NAME':'Example_Page',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages/PAGE_NAME/timeline/PAGE',
        'label': 'cir_pag_pro_tim_page',
        'GET': {
            '200': { 
                'read page profile timeline': {
                    'path': {
                        'PAGE_NAME': 'SomePage',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages/PAGE_NAME/photos/PAGE',
        'label': 'cir_pag_pro_photos',
        'GET': {
            '200': { 
                'read page profile photos': {
                    'path': {
                        'PAGE_NAME': 'SomePage',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages/PAGE_NAME/videos/PAGE',
        'label': 'cir_pag_pro_videos',
        'GET': {
            '200': { 
                'read page profile videos': {
                    'path': {
                        'PAGE_NAME': 'SomePage',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
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
    {
        'url': 'circle/api/market/post/POST_ID',
        'label': 'cir_mar_post', 
        'GET': {
            '200': {
                'view market post': {
                    'path': {
                        'POST_ID': '100',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME',
        'label': 'cir_pro',
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
        'POST': {
            '405': {
                'anththing': {
                    'path': {
                        'USER_NAME': 'akleinhans',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/timeline',
        'label': 'cir_pro_tim', 
        'POST': {
            '200': {
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
                'get profile timeline without specifying a page': {
                    'path': {
                        'USER_NAME': 'DrPib',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/timeline/PAGE',
        'label': 'cir_pro_tim_page',
        'GET': {
            '200': { 
                'read profile timeline': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/friends/PAGE',
        'label': 'cir_pro_tim_fr',
        'GET': {
            '200': { 
                'read profile friend list': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/following/PAGE',
        'label': 'cir_pro_fing',
        'GET': {
            '200': { 
                'read profile following': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/followers/PAGE',
        'label': 'cir_pro_frs',
        'GET': {
            '200': { 
                'read profile followers': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/photos/PAGE',
        'label': 'cir_pro_photos',
        'GET': {
            '200': { 
                'read profile photos': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/albums/PAGE',
        'label': 'cir_pro_albums',
        'GET': {
            '200': { 
                'read profile albums': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/videos/PAGE',
        'label': 'cir_pro_videos',
        'GET': {
            '200': { 
                'read profile videos': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/groups/PAGE',
        'label': 'cir_pro_groups',
        'GET': {
            '200': { 
                'read profile groups': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/events/PAGE',
        'label': 'cir_pro_events',
        'GET': {
            '200': { 
                'read profile events': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': '3',
                    },
                },
            },
        },
    },
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
    # @TODO 'url': 'ads/api/wallet',
    # @TODO 'url': 'ads/api/campaigns',
    # @TODO 'url': 'ads/api/promoted',
    # @TODO 'url': 'ads/api/promoted/pages',
    # @TODO 'url': 'ads/api/promoted/posts',
]

