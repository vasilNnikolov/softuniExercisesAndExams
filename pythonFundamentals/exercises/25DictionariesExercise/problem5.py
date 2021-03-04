n = int(input())
registrations = {} # key is username, license plate number is value

for _ in range(n):
    tokens = input().split(' ')
    if tokens[0] == 'register':
        username, licenseNumber = tokens[1], tokens[2]
        if username not in registrations:
            registrations[username] = licenseNumber
            print(f'{username} registered {licenseNumber} successfully')
        else:
            print(f'ERROR: already registered with plate number {registrations[username]}')
    elif tokens[0] == 'unregister':
        username = tokens[1]
        if username in registrations:
            print(f'{username} unregistered successfully')
            registrations.pop(username)
        else:
            print(f'ERROR: user {username} not found')

for user, number in registrations.items():
    print(f'{user} => {number}')
