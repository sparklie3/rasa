# from transformers import pipeline, AutoTokenizer, AutoModelWithLMHead

# tokenizer = AutoTokenizer.from_pretrained("gpt2")

# model = AutoModelWithLMHead.from_pretrained("gpt2")

from typing import Any, Dict, List, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# Respond with a career response
class action_find_career_response(Action):
    # def name(self) -> Text:
    def name(self):
        return "action_find_career_response"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: "Tracker",
        domain: Dict[Text, Any]):

        bot = ("Reaching out to a human agent")
        dispatcher.utter_message(bot)

        dispatcher.utter_message("say hello")
        return []

