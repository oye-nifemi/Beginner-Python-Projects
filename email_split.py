def main():
    email = input("Enter your email address: ")
    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
main()