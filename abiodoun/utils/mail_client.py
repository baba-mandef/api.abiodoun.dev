import smtplib
from email.mime.text import MIMEText
from django.conf import settings


class Email_Message():
    """
    Simple email client for sending emails using the Zoho mail service.

    Attributes:
        recipient (list): A list of email addresses of the recipients.
        subject (str): The subject of the email.
        message (str): The body/content of the email.
    """

    def __init__(self, recipient, subject, message):
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.sender = settings.DEFAULT_ZOHO_EMAIL
        self.host = settings.ZOHO_HOST
        self.login = settings.ZOHO_LOGIN
        self.password = settings.ZOHO_PASSWORD

    @property
    def _message(self) -> MIMEText:
        """
        Generate the email message in MIMEText format.

        Returns:
            MIMEText: The email message in MIMEText format.
        """
        email_message = MIMEText(self.message)
        email_message['Subject'] = self.subject
        email_message['From'] = self.sender
        email_message['To'] = ', '.join(self.recipient)

        return email_message

    @property
    def _server(self) -> smtplib.SMTP_SSL:
        """
        Create an SMTP server for sending emails using the SSL protocol.

        Returns:
            smtplib.SMTP_SSL: The SMTP_SSL server instance.
        """
        return smtplib.SMTP_SSL(self.host, 465)

    def send(self):
        """
        Send the email using the Zoho mail service.
        """
        server = self._server
        login = self.login
        password = self.password
        sender = self.sender
        recipient = ', '.join(self.recipient)

        server.login(login, password)
        server.sendmail(sender, recipient, self._message.as_string())
        server.quit()
