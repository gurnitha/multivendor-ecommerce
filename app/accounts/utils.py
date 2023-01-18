# app/accounts/utils.py

def detect_user(user):

    if user.role == 1:
        redirectUrl = 'vendor_dashboard'
        # redirectUrl = 'vendor_dashboard' # this did not work because of i used: app/accounts
        redirectUrl = '../vendor_dashboard' # this works
        return redirectUrl

    elif user.role == 2:
        redirectUrl = 'custumer_dashboard'
        # redirectUrl = 'custDashboard'   # this did not work because of i used: app/accounts
        redirectUrl = '../custumer_dashboard'  # this works
        return redirectUrl

    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'