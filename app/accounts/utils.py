# app/accounts/utils.py

def detect_user(user):

    if user.role == 1:
        redirectUrl = 'vendor-dashboard'
        # redirectUrl = 'vendor-dashboard' # this did not work because of i used: app/accounts
        redirectUrl = '../vendor-dashboard' # this works
        return redirectUrl

    elif user.role == 2:
        redirectUrl = 'customer-dashboard'
        # redirectUrl = 'customer-dashboard'   # this did not work because of i used: app/accounts
        redirectUrl = '../customer-dashboard'  # this works
        return redirectUrl

    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'