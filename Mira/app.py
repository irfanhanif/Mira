# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import os
import re
import json
import unicodedata
import mysql.connector
import numpy as np
import tensorflow as tf

from gensim import utils
from keras.models import load_model

import errno
import sys
import tempfile
import random
from argparse import ArgumentParser

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', "983f4e07978f12f097c5edc8ed1db78f")
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', "bB6h4NmV07M3Dn5waUnHgQ4JnHY3QYPazqIk41b29lMQRHnsjzrculn+9nfvDtLzrVfS4fUtIYkDeRAW5JOkgsNkhJbudF6A0ZnAXVf1TDyWm/KqQzfFGRLm6LwIdlCi6CliEcGEiI9/VV4GKTXasAdB04t89/1O/w1cDnyilFU=")
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

#connect to database
db = mysql.connector.connect(user="root", password='namamuran', database="glove-300")
cursor = db.cursor(buffered=True)

# load cnn model
model = load_model("./cnn_final_model.h5")

def getWordEmbedding(word, cursor):
#     word = word.replace("'", "''")
    sql = """select vec from term where term like %s"""
    cursor.execute(sql, (str(word),))
    data = cursor.fetchall()
    if len(data) > 0:
        decoded_vec = json.JSONDecoder().decode(data[0][0])
        vec = np.asarray(decoded_vec, dtype=np.float32)
        return True, vec
    else:
        return False, data

def myTokenizer(content, lower=True):
    raw = content.split(' ')
    remover = re.compile("[^a-zA-Z-]")

    token = []

    for i in raw:
        term = remover.sub('', i)
        if lower == True:
            term = term.lower()
        token.append(term)
    tokenized = filter(None, token)

    return tokenized

def toSentenceEmbd(string):
    string = string.replace('\n', '')
    string = np.array(myTokenizer(string))

    begin = True
    for word in string:
        stat, vec = getWordEmbedding(word, cursor)
        if not stat:
            continue
        if begin:
            begin = False
            feature = vec
        else:
            feature += vec
            # feature = np.concatenate([feature, vec])

    feature = feature/np.linalg.norm(feature)
    feature = np.array(feature)

    return feature

def getPrediction(doc):
    vec = toSentenceEmbd(doc)
    vec = vec.reshape((1, 300, 1))
    prediction = model.predict([vec])[0]
    print prediction
    argmax = np.argmax(prediction)
    if prediction[argmax] < 0.7:
        print "DOUBT"
        ids = []
        for i in range(3):
            prediction[argmax] = -1
            ids.append(argmax+1)
            argmax = np.argmax(prediction)
        ids.append(23)
        return ids
    else:
        return [argmax+1]

def getAnswer(dictionary):
    dictionary = str(dictionary)
    with open('messages.json', 'r') as data_file:
        data = json.load(data_file, strict=False)
    return random.choice(data[dictionary])

def isDirectFaq(text):
    with open("answercls.json", 'r') as answercls:
        data = json.load(answercls, strict=False)

    for key, val in data.iteritems():
        if text == val[0]:
            answercls.close()
            return True, [key]
    answercls.close()
    return False, [-1]

# function for create tmp dir for download content
def make_static_tmp_dir():
    try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise

@app.route("/test", methods=['GET'])
def test():
    sys.stdout.write("test request received\n")
    return "test"

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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    sys.stdout.write(text+'\n')

    isDirect, id = isDirectFaq(text)
    if not isDirect:
        id = getPrediction(text)

    if len(id) > 1:
        act = []
        with open("answercls.json", 'r') as answercls:
            data = json.load(answercls, strict=False)
        print data[str(id[1])]
        for i in id:
            i = str(i)
            t = data[i][0]
            print t
            print type(t)
            act.append(MessageTemplateAction(label=t, text=t))
        # print act
        print MessageTemplateAction(label="Jumlah Kelompok", text="Jumlah Kelompok")

        buttons_template = ButtonsTemplate(title='Hm, Kamu tanya apa sebenarnya?', text='Pilih satu ya hehehe :)', actions=act)
        print buttons_template

        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    else:
        answer = getAnswer(id[0])
        sys.stdout.write(answer+'\n')

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=5000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    # create tmp dir for download content
    make_static_tmp_dir()

    app.run(debug=options.debug, port=options.port)
