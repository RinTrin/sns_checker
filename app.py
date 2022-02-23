from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

token = "zq9xGG0hEAaHzRePZnxioIzvknXYUH247mb1Q3NVPTlHx1fKlQHVfYCz3t9rgT6N8FpS/ZasVuoxuXdLD5UgPxNXua69RGblPlH1IVQQXTSPs9C0iPzkSdIL+65zMksUNm09FlsqMA3WyQavk28YKAdB04t89/1O/w1cDnyilFU="
handle_token = "d9c88b4a751dfefc0040715d11b8410a"
line_bot_api = LineBotApi(token)
handler = WebhookHandler(handle_token)

app = Flask(__name__)

@app.route("/")
def say_hello():
    return "Hello"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()