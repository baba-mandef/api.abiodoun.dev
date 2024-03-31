from rest_framework.viewsets import ModelViewSet
from abiodoun.message.serializers import MessageSerializer
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from telegram.ext import ApplicationBuilder, ContextTypes
from abiodoun.utils.mail_client import Email_Message
from django.conf import settings
from django.template.loader import render_to_string
from abiodoun.utils.mail_client import Email_Message
from abiodoun.message.models import Message
from abiodoun.message.signature import signature


class MessageViewSet(ModelViewSet):

    serializer_class = MessageSerializer
    http_method_names = ['post']

    def create(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        sender = serializer.validated_data.get('sender_name')
        sender_email = serializer.validated_data.get('sender_email')
        body = serializer.validated_data.get('body')
        message =  f"""
       <!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mail de réponse</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #000a40;  padding: 20px;">

<div style="background-color: #ff7624; padding: 10px; border-radius: 5px;">
    <h2 style="color: #ffffff;">Réponse à votre message</h2>
</div>

<div style="margin-top: 20px;">
    <h3 style="color: #ff7624; ">Cher(e) {str(sender)},</h3>

    <p>Merci pour votre message, qui a été reçu avec attention.</p>

    <p>Votre demande a été enregistrée et sera traitée dans les plus brefs délais. Je prends très au sérieux chaque demande que je reçois et je m'engage à vous fournir une réponse dans les meilleurs délais.</p>

    <p>Si votre demande est urgente ou nécessite une réponse immédiate, je vous invite à me contacter directement par téléphone au <b> <a style="text-decoration:none; color:#000a40;" href="tel:+22998879049">229 98879049</a> </b> <p>

    <p>Encore une fois, merci de l'intérêt que vous portez à mon travail. Je suis impatient(e) de pouvoir collaborer avec vous.</p>

    <p style="margin-top: 20px;">Cordialement.</p>
</div>

</body>
</html>

 {str(signature)}
        """
        message = Email_Message(
            [sender_email],
            f"Merci de nous avoir contacter cher(e) {str(sender)} !",
            message
        )
        message.send()

        message = Message.objects.create(**serializer.validated_data)

        # application = ApplicationBuilder().token(settings.TOKEN).build()
        # application.job_queue.run_once(new_message)

        return Response("Sucess", HTTP_201_CREATED)
