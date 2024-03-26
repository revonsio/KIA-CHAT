# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction

class ActionFeedbackWelcome(Action):
    def name(self) -> Text:
        return "action_feedback_welcome"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        submenu = tracker.get_slot("submenu")
        option2action_name =   {"main": {
                                    1: "action_handle_berat_badan",
                                    2: "action_handle_tinggi_badan",
                                    3: "action_handle_tumbuh_kembang",
                                    4: "action_handle_lainnya"}
                                }

        try:
            option = int(tracker.get_slot("option"))
        except ValueError:
            dispatcher.utter_message(text=f"Jawaban harus berupa angka!")
            return [SlotSet('option', None)]
        try:
            next_action = option2action_name[submenu][option]
        except KeyError:
            dispatcher.utter_message(text=f"Maaf, opsi tidak tersedia")
            return [SlotSet('option', None)]

        dispatcher.utter_message(text=f"Anda telah memilih menu {option}")

        if type(next_action) is tuple:
            return [SlotSet('option', None),
                    SlotSet('suboption', next_action[1]),
                    FollowupAction(name=next_action[0])]
        else:
            return [SlotSet('option', None),
                    FollowupAction(name=next_action)]
    
class ActionHandleBeratBadan(Action):

    def name(self) -> Text:
        return "action_handle_berat_badan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Menu Berat Badan."""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleTinggiBadan(Action):

    def name(self) -> Text:
        return "action_handle_tinggi_badan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Menu Tinggi Badan."""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleTumbuhKembang(Action):

    def name(self) -> Text:
        return "action_handle_tumbuh_kembang"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Menu Tumbuh Kembang."""
        dispatcher.utter_message(text=message)

        return []
    
class ActionHandleLainnya(Action):

    def name(self) -> Text:
        return "action_handle_lainnya"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Menu Lainnya."""
        dispatcher.utter_message(text=message)

        return []

class ActionDataBeratbadan(Action):
    def name(self):
        return "action_data_beratbadan"

    def run(self, dispatcher, tracker, domain):

        jenis_kelamin = tracker.get_slot("jenis_kelamin")
        umur = tracker.get_slot("umur")
        berat_badan = tracker.get_slot("berat_badan")

        if jenis_kelamin == True:
            dispatcher.utter_message(text="Jenis Kelamin: Laki-laki\n")
        else:
             dispatcher.utter_message(text="Jenis Kelamin: Perempuan\n")
        
        if umur & berat_badan > 0:
            dispatcher.utter_message(text="Menyala Abangkuuhh\n")
        else:
            dispatcher.utter_message(text="Input invalid\n")

        return[]


class ActionFeedbackChecklistfirst(Action):
    def name(self):
        return "action_feedback_checklistfirst"

    def run(self, dispatcher, tracker, domain):

        question11 = tracker.get_slot("question11")
        question12 = tracker.get_slot("question12")
        question13 = tracker.get_slot("question13")
        question14 = tracker.get_slot("question14")
        question15 = tracker.get_slot("question15")
        question16 = tracker.get_slot("question16")
        question17 = tracker.get_slot("question17")
        question18 = tracker.get_slot("question18")
        question19 = tracker.get_slot("question19")
        question110 = tracker.get_slot("question110")
        
        
        if question11 == False:
            dispatcher.utter_message(response="utter_response_question11")
        if question12 == False:
            dispatcher.utter_message(response="utter_response_question12")
        if question13 == False:
            dispatcher.utter_message(response="utter_response_question13")
        if question14 == False:
            dispatcher.utter_message(response="utter_response_question14")
        if question15 == False:
            dispatcher.utter_message(response="utter_response_question15")
        if question16 == False:
            dispatcher.utter_message(response="utter_response_question16")
        if question17 == False:
            dispatcher.utter_message(response="utter_response_question17")
        if question18 == False:
            dispatcher.utter_message(response="utter_response_question18")
        if question19 == False:
            dispatcher.utter_message(response="utter_response_question19")
        if question110 == False:
            dispatcher.utter_message(response="utter_response_question110")
            
            return []
    
class ActionFeedbackChecklistsecond(Action):
    def name(self):
        return "action_feedback_checklistsecond"

    def run(self, dispatcher, tracker, domain):

        question21 = tracker.get_slot("question21")
        question22 = tracker.get_slot("question22")
        question23 = tracker.get_slot("question23")
        question24 = tracker.get_slot("question24")
        question25 = tracker.get_slot("question25")
        question26 = tracker.get_slot("question26")
        question27 = tracker.get_slot("question27")
        question28 = tracker.get_slot("question28")
        question29 = tracker.get_slot("question29")
        question210 = tracker.get_slot("question210")
                
        if question21 == False:
            dispatcher.utter_message(response="utter_response_question21")

        if question22 == False:
            dispatcher.utter_message(response="utter_response_question22")

        if question23 == False:
            dispatcher.utter_message(response="utter_response_question23")

        if question24 == False:
            dispatcher.utter_message(response="utter_response_question24")

        if question25 == False:
            dispatcher.utter_message(response="utter_response_question25")

        if question26 == False:
            dispatcher.utter_message(response="utter_response_question26")

        if question27 == False:
            dispatcher.utter_message(response="utter_response_question27")

        if question28 == False:
            dispatcher.utter_message(response="utter_response_question28")

        if question29 == False:
            dispatcher.utter_message(response="utter_response_question29")

        if question210 == False:
            dispatcher.utter_message(response="utter_response_question210")

            return []

# class ValidateChecklistfirstForm(FormValidationAction):
#   def name(self) -> Text:
#       return "validate_checklistfirst_form"

#   @staticmethod
#   def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ):

#         question11 = tracker.get_slot("question11")

#         if question11 == False:
#             return [dispatcher.utter_message(text="Q1 Tidak Normal")]

#         return []

# class ActionSetChecklist(Action):
#     def name(self):
#         return "action_set_checklist"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         intent = tracker.latest_message["intent"].get("name")

#         if intent == "deny":
#             return [dispatcher.utter_message(text="Tidak Normal")]
#         elif intent == "affirm":
#             return [dispatcher.utter_message(text="Normal")]
#         return []
    

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
