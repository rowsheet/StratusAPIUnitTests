from examples import EVENT_EXAMPLES
from examples import POST_EXAMPLES
from examples import PAGE_EXAMPLES
from examples import GROUP_EXAMPLES
from examples import VARIABLES
from config import SESSION_ID

TESTS = [
    #---------------------------------------------------------------------------
    {
        'url': 'core/api/signup',
        'label': 'cor_signup',
        'POST': {
            '200': {
                'create a new account': {
                    'data': {
                        'user_name': 'new_api_test_user',
                        'first_name': 'Firstname',
                        'last_name': 'Lastname',
                        'email_address': 'email@email.com',
                        'password': 'somethinglongerthan12characters',
                        'confirm_password': 'somethinglongerthan12characters',
                        'newsletter': False,
                        'terms': True,
                    },
                },
            },
            '400': {
                'create a new account (username taken)': {
                    'data': {
                        'user_name': 'api_test_user',
                        'first_name': 'Firstname',
                        'last_name': 'Lastname',
                        'email_address': 'email@email.com',
                        'password': 'somethinglongerthan12characters',
                        'confirm_password': 'somethinglongerthan12characters',
                        'newsletter': False,
                        'terms': True,
                    },
                },
                'create a new account (email already used)': {
                    'data': {
                        'user_name': 'new_api_test_user',
                        'first_name': 'Firstname',
                        'last_name': 'Lastname',
                        'email_address': 'Apolloc2020@gmail.com',
                        'password': 'somethinglongerthan12characters',
                        'confirm_password': 'somethinglongerthan12characters',
                        'newsletter': False,
                        'terms': True,
                    },
                },
                'create a new account (disagree terms)': {
                    'data': {
                        'user_name': 'new_api_test_user',
                        'first_name': 'Firstname',
                        'last_name': 'Lastname',
                        'email_address': 'email@email.com',
                        'password': 'somethinglongerthan12characters',
                        'confirm_password': 'somethinglongerthan12characters',
                        'newsletter': False,
                        'terms': False,
                    },
                },
                'create a new account (bad password match)': {
                    'data': {
                        'user_name': 'new_api_test_user',
                        'first_name': 'Firstname',
                        'last_name': 'Lastname',
                        'email_address': 'email@email.com',
                        'password': 'somethinglongerthan12characters',
                        'confirm_password': 'doesnt match password',
                        'newsletter': False,
                        'terms': True,
                    },
                },
            },
        },
    },
    {
        'url': 'core/api/siginin',
        'label': 'cor_signin',
        'POST': {
            '200': {
                'login': {
                    'data': {
                        'user_name': 'new_api_test_user',
                        'password': 'somethinglongerthan12characters',
                    },
                },
            },
            '400': {
                'login': {
                    'data': {
                        'user_name': 'new_api_test_user',
                        'password': 'invlid password',
                    },
                },
            },
        },
    },
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
        'url': 'circle/api/post/POST_ID/action/ACTION',
        'label': 'cir_post_act',
        'POST': {
            '200': {
                'like a post': {
                    'path': {
                        'POST_ID': '100',
                        'ACTION': 'like',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
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
                'read my a post': {
                    'path': {
                        'POST_ID': '4675',
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
    {
        'url': 'circle/api/search/PAGE',
        'label': 'cir_sch_pos',
        'GET': {
            '200': {
                'search posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some search',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/search/hashtag/PAGE',
        'label': 'cir_sch_hsh',
        'GET': {
            '200': {
                'search posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some search',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/search/articles/PAGE',
        'label': 'cir_sch_art',
        'GET': {
            '200': {
                'search posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some search',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/search/users/PAGE',
        'label': 'cir_sch_usr',
        'GET': {
            '200': {
                'search posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some search',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/search/pages/PAGE',
        'label': 'cir_sch_pag',
        'GET': {
            '200': {
                'search posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some search',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/search/groups/PAGE',
        'label': 'cir_sch_grp',
        'GET': {
            '200': {
                'search posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some search',
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/search/events/PAGE',
        'label': 'cir_sch_evt',
        'GET': {
            '200': {
                'search posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some search',
                    },
                },
            },
        },
    },
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load joined groups list (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load managed groups list (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
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
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                    },
                },
            },
        },
        'POST': {
            '200': {
                'update a group': {
                    'path': {
                        'GROUP_NAME': VARIABLES['EXAMPLE_GROUP_NAME'],
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
                        'GROUP_NAME': VARIABLES['EXAMPLE_GROUP_NAME'],
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
                        'GROUP_NAME': VARIABLES['EXAMPLE_GROUP_NAME'],
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
                        'GROUP_NAME': VARIABLES['EXAMPLE_GROUP_NAME'],
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
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
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
                        'GROUP_NAME': VARIABLES['EXAMPLE_GROUP_NAME'],
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
                        'GROUP_NAME': VARIABLES['EXAMPLE_GROUP_NAME'],
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/action/ACTION',
        'label': 'cir_grp_pro_act_join',
        'POST': {
            '200': { 
                'join a group': {
                    'path': {
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                        'ACTION': 'join',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/action/ACTION',
        'label': 'cir_grp_pro_act_unjoin',
        'POST': {
            '200': { 
                'unjoin a group': {
                    'path': {
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                        'ACTION': 'unjoin',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/action/ACTION',
        'label': 'cir_grp_pro_act_like',
        'POST': {
            '200': { 
                'like a group': {
                    'path': {
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                        'ACTION': 'like',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/groups/GROUP_NAME/action/ACTION',
        'label': 'cir_grp_pro_act_unlike',
        'POST': {
            '200': { 
                'like a group': {
                    'path': {
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                        'ACTION': 'like',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
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
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                        'PAGE': '9',
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
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                        'PAGE': VARIABLES['PAGE'],
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
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                        'PAGE': VARIABLES['PAGE'],
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
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                        'PAGE': VARIABLES['PAGE'],
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
                        'GROUP_NAME': VARIABLES['FAMOUS_GROUP'],
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load going events list (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load interested events list (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load invited events list (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load managed events list (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
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
        'url': 'circle/api/events/EVENT_NAME/action/ACTION',
        'label': 'cir_evt_pro_act_going',
        'POST': {
            '200': { 
                'going a event': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'ACTION': 'going',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/action/ACTION',
        'label': 'cir_evt_pro_act_ungoing',
        'POST': {
            '200': { 
                'ungoing a event': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'ACTION': 'ungoing',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/action/ACTION',
        'label': 'cir_evt_pro_act_interested',
        'POST': {
            '200': { 
                'interested a event': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'ACTION': 'interested',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/action/ACTION',
        'label': 'cir_evt_pro_act_uninterested',
        'POST': {
            '200': { 
                'uninterested a event': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'ACTION': 'uninterested',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/action/ACTION',
        'label': 'cir_evt_pro_act_like',
        'POST': {
            '200': { 
                'like a event': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'ACTION': 'like',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/events/EVENT_NAME/action/ACTION',
        'label': 'cir_evt_pro_act_unlike',
        'POST': {
            '200': { 
                'like a event': {
                    'path': {
                        'EVENT_NAME': 'SomeEvent',
                        'ACTION': 'like',
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    # CREATE A NEW PAGE
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
    # UPDATE A PAGE
    {
        'url': 'circle/api/pages/PAGE_NAME',
        'label': 'cir_pag_pro',
        'GET': {
            '200': {
                'load a page profile': {
                    'path': {
                        'PAGE_NAME':VARIABLES['FAMOUS_PAGE'],
                    },
                },
            },
        },
        'POST': {
            '200': {
                'update a page\'s info': {
                    'path': {
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME'],
                    },
                    'data': PAGE_EXAMPLES['valid_page_update_info'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
                'update a page profile picture': {
                    'path': {
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME'],
                    },
                    'data': PAGE_EXAMPLES['valid_page_update_profile_pic'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
                'update a page handle': {
                    'path': {
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME'],
                    },
                    'data': PAGE_EXAMPLES['valid_page_update_handle'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
                'update a page restore': {
                    'path': {
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME_CHANGE'],
                    },
                    'data': PAGE_EXAMPLES['valid_page'],
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'update a page (while not logged in)': {
                    'path': {
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME'],
                    },
                },
                'update a page (I\'m not an admin of)': {
                    'path': {
                        'PAGE_NAME':'Page_I_Dont_Own',
                    },
                    'data': PAGE_EXAMPLES['valid_page_update_info'],
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
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME'],
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
    # READ PAGES
    {
        'url': 'circle/api/pages/PAGE',
        'label': 'cir_pag_page',
        'GET': {
            '200': {
                'load pages list': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load liked pages list (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'load managed pages list (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages/PAGE_NAME/action/ACTION',
        'label': 'cir_pag_pro_act_like',
        'POST': {
            '200': { 
                'like a page': {
                    'path': {
                        'PAGE_NAME': 'SomePage',
                        'ACTION': 'like',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/pages/PAGE_NAME/action/ACTION',
        'label': 'cir_pag_pro_act_unlike',
        'POST': {
            '200': { 
                'like a page': {
                    'path': {
                        'PAGE_NAME': 'SomePage',
                        'ACTION': 'like',
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
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME'],
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
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME'],
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
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME'],
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
                        'PAGE_NAME':VARIABLES['EXAMPLE_PAGE_NAME'],
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
                        'PAGE_NAME':VARIABLES['FAMOUS_PAGE'],
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE_NAME':VARIABLES['FAMOUS_PAGE'],
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE_NAME':VARIABLES['FAMOUS_PAGE'],
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/people/PAGE',
        'label': 'cir_pep_page',
        'GET': {
            '200': { 
                'list other profiles': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/people/friend_requests/PAGE',
        'label': 'cir_pep_frn_req_page',
        'GET': {
            '200': { 
                'list your firend requests': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'list your firend requests (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/people/friend_requests/sent/PAGE',
        'label': 'cir_pep_frn_req_snt_page',
        'GET': {
            '200': { 
                'list your firend requests sent': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
            '401': {
                'list your firend requests sent (not logged in)': {
                    'path': {
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
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
        'url': 'circle/api/USER_NAME/action/ACTION',
        'label': 'cir_pro_act_report',
        'POST': {
            '200': { 
                'report a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'report',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/action/ACTION',
        'label': 'cir_pro_act_poke',
        'POST': {
            '200': { 
                'poke a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'poke',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/action/ACTION',
        'label': 'cir_pro_act_block',
        'POST': {
            '200': { 
                'block a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'block',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/action/ACTION',
        'label': 'cir_pro_act_unfollow',
        'POST': {
            '200': { 
                'unfollow a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'unfollow',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/action/ACTION',
        'label': 'cir_pro_act_follow',
        'POST': {
            '200': { 
                'follow a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'follow',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/action/ACTION',
        'label': 'cir_pro_act_frn_req',
        'POST': {
            '200': { 
                'friend request a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'friend_request',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/action/ACTION',
        'label': 'cir_pro_act_unfrn_req',
        'POST': {
            '200': { 
                'cancel a friend request': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'cancel_friend_request',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'circle/api/USER_NAME/action/ACTION',
        'label': 'cir_pro_act_frn_req_conf',
        'POST': {
            '200': { 
                'confirm a friend request': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'confirm_friend_request',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
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
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/timeline',
        'label': 'atr_tim',
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
        'url': 'atrium/api/timeline/PAGE',
        'label': 'atr_tim_page',
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
        'url': 'atrium/api/post/POST_ID/action/ACTION',
        'label': 'atr_post_act',
        'POST': {
            '200': {
                'like a post': {
                    'path': {
                        'POST_ID': '100',
                        'ACTION': 'like',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/post/POST_ID',
        'label': 'atr_post',
        'GET': {
            '200': {
                'read a post': {
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
        'url': 'atrium/api/messages',
        'label': 'atr_msg',
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
        'url': 'atrium/api/messages/CONVERSATION_ID',
        'label': 'atr_msg_cnv',
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
        'url': 'atrium/api/message/MESSAGE_ID',
        'label': 'atr_msg_cnv_msg',
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
        'url': 'atrium/api/trending/PAGE',
        'label': 'atr_trn',
        'GET': {
            '200': { 
                'read trending': {
                    'path': {
                        'PAGE': '1',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/bookmarks/PAGE',
        'label': 'atr_bkm',
        'GET': {
            '200': { 
                'read bookmarks': {
                    'path': {
                        'PAGE': '1',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/explore/PAGE',
        'label': 'atr_sch_pos',
        'GET': {
            '200': {
                'explore posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some query',
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/explore/hashtag/PAGE',
        'label': 'atr_sch_hsh',
        'GET': {
            '200': {
                'explore posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some query',
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/explore/articles/PAGE',
        'label': 'atr_sch_art',
        'GET': {
            '200': {
                'explore posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some query',
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/explore/users/PAGE',
        'label': 'atr_sch_usr',
        'GET': {
            '200': {
                'explore posts': {
                    'path': {
                        'PAGE': '1',
                    },
                    'data': {
                        'q': 'some query',
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME',
        'label': 'atr_pro',
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
        'url': 'atrium/api/USER_NAME/action/ACTION',
        'label': 'atr_pro_act_report',
        'POST': {
            '200': { 
                'report a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'report',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/action/ACTION',
        'label': 'atr_pro_act_poke',
        'POST': {
            '200': { 
                'poke a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'poke',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/action/ACTION',
        'label': 'atr_pro_act_block',
        'POST': {
            '200': { 
                'block a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'block',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/action/ACTION',
        'label': 'atr_pro_act_unfollow',
        'POST': {
            '200': { 
                'unfollow a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'unfollow',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/action/ACTION',
        'label': 'atr_pro_act_follow',
        'POST': {
            '200': { 
                'follow a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'follow',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/action/ACTION',
        'label': 'atr_pro_act_frn_req',
        'POST': {
            '200': { 
                'friend request a user': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'friend_request',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/action/ACTION',
        'label': 'atr_pro_act_unfrn_req',
        'POST': {
            '200': { 
                'cancel a friend request': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'cancel_friend_request',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/action/ACTION',
        'label': 'atr_pro_act_frn_req_conf',
        'POST': {
            '200': { 
                'confirm a friend request': {
                    'path': {
                        'USER_NAME': 'SomeUser',
                        'ACTION': 'confirm_friend_request',
                    },
                    'cookies': {
                        'sessionid': SESSION_ID,
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/timeline',
        'label': 'atr_pro_tim', 
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
        'url': 'atrium/api/USER_NAME/timeline/PAGE',
        'label': 'atr_pro_tim_page',
        'GET': {
            '200': { 
                'read profile timeline': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/friends/PAGE',
        'label': 'atr_pro_tim_fr',
        'GET': {
            '200': { 
                'read profile friend list': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/following/PAGE',
        'label': 'atr_pro_fing',
        'GET': {
            '200': { 
                'read profile following': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/followers/PAGE',
        'label': 'atr_pro_frs',
        'GET': {
            '200': { 
                'read profile followers': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/photos/PAGE',
        'label': 'atr_pro_photos',
        'GET': {
            '200': { 
                'read profile photos': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/albums/PAGE',
        'label': 'atr_pro_albums',
        'GET': {
            '200': { 
                'read profile albums': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    {
        'url': 'atrium/api/USER_NAME/videos/PAGE',
        'label': 'atr_pro_videos',
        'GET': {
            '200': { 
                'read profile videos': {
                    'path': {
                        'USER_NAME': 'DrPib',
                        'PAGE': VARIABLES['PAGE'],
                    },
                },
            },
        },
    },
    # @TODO 'url': 'ads/api/wallet',
    # @TODO 'url': 'ads/api/campaigns',
    # @TODO 'url': 'ads/api/promoted',
    # @TODO 'url': 'ads/api/promoted/pages',
    # @TODO 'url': 'ads/api/promoted/posts',
]
""" # We're not doing these right now.
    # @TODO 'url': 'circle/api/blogs',
    # @TODO 'url': 'circle/api/blogs/PAGE',
    # @TODO 'url': 'circle/api/blogs/category/CATEGORY_ID/PAGE',
    # @TODO 'url': 'circle/api/blogs/post/POST_ID',
    # @TODO 'url': 'circle/api/market',
    # @TODO 'url': 'circle/api/market/PAGE',
    # @TODO 'url': 'circle/api/market/category/CATEGORY_ID/PAGE',
    # @TODO 'url': 'circle/api/market/post/POST_ID',
    # @TODO 'url': 'atrium/api/blogs',
    # @TODO 'url': 'atrium/api/blogs/PAGE',
    # @TODO 'url': 'atrium/api/blogs/category/CATEGORY_ID/PAGE',
    # @TODO 'url': 'atrium/api/blogs/post/POST_ID',
"""
