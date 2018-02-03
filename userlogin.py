def logins(command):
    """Gets usernames and password from input in format: {username} -> {password}
     and store them to dicrionary"""
    login_dict = {}
    while True:
        login = input()
        if login == command:
            break
        login = login.split(' -> ')
        login_dict[login[0]] = login[1]
    return login_dict


user_logins = logins('login')
failed_logins = 0

# If the password matches with the user’s password, print “{username}: logged in successfully”.
# If the user doesn’t exist, or the password doesn’t match the user, print “{username}: login failed”.
# When you receive the command “end”, print the count of unsuccessful login attempts, using the format
# “unsuccessful login attempts: {count}”.

while True:
    login_try = input()
    if login_try == 'end':
        print('unsuccessful login attempts:', failed_logins)
        break
    login_try = login_try.split(' -> ')
    username = login_try[0]
    password = login_try[1]
    if username in user_logins and user_logins[username] == password:
        print(username + ': logged in successfully')
    else:
        print(username + ': login failed')
        failed_logins += 1

