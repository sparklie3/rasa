from transformers import pipeline

from typing import Any, Dict, List, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import us_state_abbrev

class quote_form(FormAction):
    def name(self):
        return "quote_form"

@staticmethod
    def required_slots(tracker):
        if tracker.get_slot('states_abbrev')
        # return ["date_of_birth","gender","nicotine","states","coverage_amount","coverage_length"]
        return ["date_of_birth","gender","nicotine","state_abbrev"]
  
@staticmethod
    # what happens after all the form data is filled
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message("Thanks, great job!")
        return []


# check if the state user is getting quote is supported

class action_validate_state(Action):
    def name(self):
        return "action_validate_state"

    

