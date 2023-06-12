from prefect_email import EmailServerCredentials
def create_email_creds():
    credentials = EmailServerCredentials(
        username="my_mail@gmail.com",
        password="my_pass",  # must be an app password
    )
    credentials.save("email-block")


#EmailServerCredentials.load("BLOCK_NAME_PLACEHOLDER")

if __name__ == "__main__":
    create_email_creds()