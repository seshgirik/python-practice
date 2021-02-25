def has_facebook_account(user_email):
    print('calling Facebook service')
    return False

def has_github_account(user_email):
    print('calling Github service')
    return True

def has_twitter_account(user_email):
    print('calling Twitter service')
    return True

def has_social_media_account(user_email):
    print('Checking social media apps...')
    # Python's `any` receives an Iterable
    # and returns True when the first truthy clause is found.
    response = has_facebook_account(user_email) or has_github_account(user_email) or has_twitter_account(user_email)
    # response = any([
    #     has_facebook_account(user_email),  # This is False
    #     has_github_account(user_email),  # This is True
    #     has_twitter_account(user_email),  # This is True
    # ])
    print('Done!')
    return response


has_social_media_account('fake@email.com')