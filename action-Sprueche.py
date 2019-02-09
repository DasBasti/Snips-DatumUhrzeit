#!/usr/bin/env python3

from hermes_python.hermes import Hermes
import datetime
import random

sprueche = open('sprueche.txt').read().splitlines()
fragen = open('fragen.txt').read().splitlines()
stop = open('stop.txt').read().splitlines()

USERNAME_INTENTS = "BastiN"


def user_intent(intentname):
    return USERNAME_INTENTS + ":" + intentname


def subscribe_intent_callback(hermes, intent_message):
    intentname = intent_message.intent.intent_name

    if intentname == user_intent("Random"):
        result_sentence = random.choice(sprueche)
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Next"):
        result_sentence = random.choice(sprueche)
        result_sentence += '\n'
        result_sentence += random.choice(fragen)
        current_session_id = intent_message.session_id
        hermes.publish_continue_session(current_session_id, result_sentence)

    elif intentname == user_intent("Stop"):
        result_sentence = random.choice(stop)
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Help"):
        result_sentence = "Heute schon geschmunzelt? Frage deinen Assistenten einfach nach dem Spruch des Tages."
        current_session_id = intent_message.session_id
        hermes.publish_continue_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intents(subscribe_intent_callback).start()
