from rest_framework.viewsets import ModelViewSet
from abiodoun.message.serializers import MessageSerializer
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from telegram.ext import ApplicationBuilder, ContextTypes
from django.conf import settings
from abiodoun.utils.mail_client import Email_Message


class MessageViewSet(ModelViewSet):

    serializer_class = MessageSerializer
    http_method_names = ['post']

    def create(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        sender = serializer.validated_data.get('sender')
        sender_email = serializer.validated_data.get('sender_email')
        body = serializer.validated_data.get('body')

        message = Email_Message(
            [sender_email],
            f"Merci de nous avoir contacter cher(e) {sender} !",
            body
        )
        message.send()

        """ async def new_message(context: ContextTypes.DEFAULT_TYPE):
            await context.bot.send_message(chat_id=settings.CHAT,
                                           text=f'Nouveau message de : {sender} | {sender_email}\n {body}'
                                           ) """
        # application = ApplicationBuilder().token(settings.TOKEN).build()
        # application.job_queue.run_once(new_message)

        return Response("Sucess", HTTP_201_CREATED)
