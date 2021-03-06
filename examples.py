VARIABLES =  {
    'EXAMPLE_PAGE_NAME': 'APITest_ExamplePage',
    'EXAMPLE_PAGE_NAME_CHANGE': 'APITest_ExamplePage_Change',
    'FAMOUS_PAGE': 'PresidentTrumpNewsFeed',

    'EXAMPLE_GROUP_NAME': 'APITest_ExampleGroup',
    'EXAMPLE_GROUP_NAME_CHANGE': 'APITest_ExampleGroup',
    'FAMOUS_GROUP': 'apollofintech',

    # This variable is for PAGINATION, not Page related!
    'PAGE': '1',
}
EVENT_EXAMPLES = {
    'valid_event': {
        'event_name': 'TheGretaReset',
        'title': 'A Brave New World',
        'description': 'Don\' forget you\'re here forever.',
        'category': 'CompositionOfMorphisms',
        'timestamp_start': '1984-01-01T00:00:00+0000',
        'timestamp_end': '2077-11-05T23:58:20+0000',
        'location': 'Above',
        # Optional
        'photo': 'https://cdn1.stratus.co/09F911029D74E35BD84156C5635688C0.png',
        'pinned_post': '100',
    },
    'valid_event_for_update': {
        'event_name': 'abelian',
        'title': 'As Above',
        'location': 'Bellow',
        'description': 'Ideas Worth Sharing',
        'category': 'CompositionOfMorphisms',
    },
    'invalid_event_not_own_by_req_user': {
        'event_name': 'nonAbelian',
        'title': 'As Above',
        'description': 'Deus Ex',
        'category': 'ThisStatementIsFalse',
    },
    'invalid_event_missing_title': {
        'event_name': 'incompleteness',
        'description': 'No consistent system of axioms whose theorems can be listed by an effective procedure is capable of proving all truths about the arithmetic of natural numbers',
        'category': 'Entscheidungsproblem',
    },
    'invalid_event_invalid_date': {
        'event_name': 'Have_We',
        'title': '4got What 1t',
        'timestamp_start': '2077-11-05T23:58:20+0000',
        'timestamp_end': '1984-01-01T00:00:00+0000',
        'description': 'means 2B',
        'category': 'human',
    },
    'invalid_event_invalid_location': {
        'event_name': 'IMustStop',
        'title': 'Falling In Love',
        'description': 'with every girl who',
        'location': 'F*#$s',
        'category': 'me',
    },
}
GROUP_EXAMPLES = {
    'valid_group': {
        'group_name': 'Example_Group',
        'title': 'Exampe Group',
        'description': 'Descriptin of my Group',
        'category': 'CompositionOfMorphisms',
        # Optional
        'photo': 'https://cdn1.stratus.co/231123141312312312.png',
        'pinned_post': '100',
    },
    'valid_group_for_update': {
        'group_name': 'New_Name',
        'title': 'A New Title',
        'category': 'othercatagory',
        'photo': 'https://cdn1.stratus.co/WH4000.png',
        'pinned_post': '45',
    },
    'invalid_group_not_own_by_req_user': {
        'group_name': 'a_group_i_dont_own',
        'title': 'Exampe Group',
        'description': 'Descriptin of my Group',
        'category': 'CompositionOfMorphisms',
    },
    'invalid_group_missing_title': {
        'group_name': 'Exampe_Group',
        'description': 'Descriptin of my Group',
        'category': 'CompositionOfMorphisms',
    },
}   
PAGE_EXAMPLES = {
    'valid_page': {
        'page_name': VARIABLES['EXAMPLE_PAGE_NAME'],
        'title': 'Exampe Page',
        'description': 'Descriptin of my Page',
        'category': 'CompositionOfMorphisms',
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
        'vkontakte_link': 'https://www.example.com/thispage',
    },
    'valid_page_update_info': {
        'page_name': VARIABLES['EXAMPLE_PAGE_NAME'],
        'title': 'A New Title',
        'category': 'othercatagory',
        'action_text': 'Some New Action Text',
        'twitter_link': 'https://www.twitter.com/newthing',
    },
    'valid_page_update_profile_pic': {
        'page_name': VARIABLES['EXAMPLE_PAGE_NAME'],
        'photo': 'https://cdn1.stratus.co/231123141312312312.png',
    },
    'valid_page_update_handle': {
        'page_name': VARIABLES['EXAMPLE_PAGE_NAME_CHANGE'],
        'photo': 'https://cdn1.stratus.co/231123141312312312.png',
    },
    'invalid_page_not_own_by_req_user': {
        'page_name': 'a_page_i_dont_own',
        'title': 'Exampe Page',
        'description': 'Descriptin of my Page',
        'category': 'CompositionOfMorphisms',
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
        'vkontakte_link': 'https://www.example.com/thispage',
    },
    'invalid_page_bad_socials': {
        'page_name': 'Exampe_Page',
        'description': 'Descriptin of my Page',
        'category': 'CompositionOfMorphisms',
        'facebook_link': 'BAD URL',
        'twitter_link': 'https://www.twitter.com/thispage',
        'youtube_link': 'BAD URL',
        'instagram_link': 'https://www.instagram.com/thispage',
        'linkedin_link': 'https://www.linkedin.com/thispage',
        'vkontakte_link': 'https://www.example.com/thispage',
    },
    'invalid_page_missing_title': {
        'page_name': 'Exampe_Page',
        'description': 'Descriptin of my Page',
        'category': 'CompositionOfMorphisms',
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
        'vkontakte_link': 'https://www.example.com/thispage',
    },
}   
POST_EXAMPLES = {
    #---------------------------------------------------------------------------
    # INVALID POSTS 
    #---------------------------------------------------------------------------
    'valid_media': {
        'post_type': 'media',
        'src_text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'src_url': 'https://google.com/?no=matter&how=fast&i=run',
        'src_provider': 'Breitbart Media Outlet',
        'src_type': 'photo',
        'src_title': 'Title of my post',
        'src_html': '<html>how to meet ladies</html>',
    },
    'valid_media_post_update': {
        'post_type': 'media',
        'src_text': 'Im changing the text of this post',
        'src_url': 'https://google.com/?no=matter&how=fast&i=run',
        'src_provider': 'Breitbart Media Outlet',
        'src_type': 'photo',
        'src_title': 'Title of my post',
        'src_html': '<html>how to meet ladies</html>',
    },
    #---------------------------------------------------------------------------
    # INVALID POSTS
    #---------------------------------------------------------------------------
    'invalid_post_type': {
        'post_type': 'foo',
    },
    'invalid_media_bad_url': {
        'post_type': 'media',
        'src_url': 'THIS IS NOT A URL',
        'src_provider': 'Breitbart Media Outlet',
        'src_type': 'photo',
        'src_title': 'Title of my post',
        'src_text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'src_html': '<html>how to meet ladies</html>',
    },
    'invalid_media_missing_provider': {
        'post_type': 'media',
        'src_url': 'https://google.com/?no=matter&how=fast&i=run',
        'src_type': 'photo',
        'src_title': 'Title of my post',
        'src_text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'src_html': '<html>how to meet ladies</html>',
    },
    'invalid_media_invalid_type': {
        'post_type': 'media',
        'src_url': 'https://google.com/?no=matter&how=fast&i=run',
        'src_provider': 'Breitbart Media Outlet',
        'src_type': 'NOT A VALID TYPE',
        'src_title': 'Title of my post',
        'src_text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'src_html': '<html>how to meet ladies</html>',
    },
    'invalid_media_missing_title': {
        'post_type': 'media',
        'src_url': 'https://google.com/?no=matter&how=fast&i=run',
        'src_provider': 'Breitbart Media Outlet',
        'src_type': 'photo',
        'src_title': 'Title of my post',
        'src_text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'src_html': '<html>how to meet ladies</html>',
    },
    'invalid_media_invalid_title': {
        'post_type': 'media',
        'src_url': 'https://google.com/?no=matter&how=fast&i=run',
        'src_provider': 'Breitbart Media Outlet',
        'src_type': 'photo',
        'src_title': '****INVALID TITLE CHARACTERS******',
        'src_text': 'The joke is that both the words ending in the same sylable that rhyme.',
        'src_html': '<html>how to meet ladies</html>',
    },
}
