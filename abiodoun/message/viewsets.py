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
        Cher {str(sender)},
        Votre message a bien été reçu et je vous en suis reconnaissant.
        Je souhaite vous informer que votre message a été enregistré 
        dans ma boîte de réception et que je prends très au sérieux 
        toutes les demandes que je reçois. Je vais étudier attentivement
        votre message et je vous répondrai dans les plus brefs délais.

        Si votre demande est urgente ou si vous avez besoin d'une réponse
        rapide, je vous conseille de me contacter directement par
        téléphone au +229 66173930.

        Encore une fois, merci de l'intérêt que vous portez à mon travail.
        Je suis ravi de pouvoir échanger avec vous et j'espère que nous
        pourrons collaborer ensemble.

        Cordialement,
        Abiodoun Paraïso
        Développeur web
        """
        message = Email_Message(
            [sender_email],
            f"Merci de nous avoir contacter cher(e) {str(sender)} !",
            message
        )
        message.send()

        message = Message.objects.create(**serializer.validated_data)

        """ async def new_message(context: ContextTypes.DEFAULT_TYPE):
            await context.bot.send_message(chat_id=settings.CHAT,
                                           text=f'Nouveau message de : {sender} | {sender_email}\n {body}'
                                           ) 
        application = ApplicationBuilder().token(settings.TOKEN).build()
        application.job_queue.run_once(new_message) """
        """ async def new_message(context: ContextTypes.DEFAULT_TYPE):
            await context.bot.send_message(chat_id=settings.CHAT,
                                           text=f'Nouveau message de : {sender} | {sender_email}\n {body}'
                                           ) """
        # application = ApplicationBuilder().token(settings.TOKEN).build()
        # application.job_queue.run_once(new_message)

        return Response("Sucess", HTTP_201_CREATED)
