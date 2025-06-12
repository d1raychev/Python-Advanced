class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email_len = 5
valid_domains = ['.com', '.bg', '.org', '.net']

while True:
    email = input()
    if email == "End":
        break

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split('@')[0]) < email_len:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email.split('.')[-1]
    if f'.{domain}' not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')

