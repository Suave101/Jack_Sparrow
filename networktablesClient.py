import codecs, hashlib, json

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

lock = True
usalt = b"a97789618bd9221692ae84115675b88aa9bc30362c22883c"
lockHashes = json.loads(codecs.decode(open("ntc.lock", "rb").read().decode("utf_7"), "rot_13"))
# tabPerms = {11: ["My Account", "Clocks", "Manage Accounts Below10", "Toggle Idiot Proofing", "Safe PSI Limit",
#                  "Disable Brownout Messages", "Toggle Brownout Sustain Disabled", "CAN Devices Type", "CAN IDs",
#                  "Welcome"],
#             10: ["My Account", "Manage Accounts Below10", "Toggle Idiot Proofing", "Safe PSI Limit",
#                  "Disable Brownout Messages", "Toggle Brownout Sustain Disabled", "CAN Devices Type", "CAN IDs",
#                  "Welcome"],
#             9: ["CAN Devices Type", "CAN IDs", "Welcome"],
#             8: ["CAN IDs", "Welcome"],
#             1: ["Welcome"]}
tabPerms_info = {11: {'My Account': {'Name': 'My Account', 'JSON': '[{"type": "title", "title": "My Account"}, {"type": "color", "title": "Background Color", "section": "My Account", "key": "key2"}]', 'Values': {'key2': '000000'}}, 'Clocks': {'Name': 'Clocks', 'JSON': '[{"type": "title", "title": "Clocks"}, {"type": "bool", "title": "Server Down", "section": "Clocks", "key": "key2"}, {"type": "string", "title": "Server Down Message", "section": "Clocks", "key": "key3"}]', 'Values': {'key2': 'false', 'key3': 'Robot Network Error'}}, 'Safety Bypass': {'Name': 'Safety Bypass', 'JSON': '[{"type": "title", "title": "Safety Bypass"}, {"type": "bool", "title": "Idiot Proofing", "section": "Safety Bypass", "key": "key2"}, {"type": "bool", "title": "Enable Brownout Warnings", "section": "Safety Bypass", "key": "key3"}, {"type": "bool", "title": "Brownout Sustain", "desc": "When brownout is detected, leave robot in disabled until reset or battery changed.", "section": "Safety Bypass", "key": "key4"}, {"type": "numeric", "title": "Safe PSI Limit", "desc": "Pneumatic tanks will charge up to this value. The robot will not let the PSI go over 200. FRC regulation states PSI must not go above 120.", "section": "Safety Bypass", "key": "key5"}]', 'Values': {'key2': False, 'key3': False, 'key4': False, 'key5': 100}}, 'CAN Types': {'Name': 'CAN Types', 'JSON': '[{"type": "title", "title": "CAN Types"}, {"type": "bool", "title": "Work in Progress", "section": "CAN Types", "key": "key2"}]', 'Values': {'key2': True}}, 'CAN IDs': {'Name': 'CAN IDs', 'JSON': '[{"type": "title", "title": "CAN IDs"}, {"type": "bool", "title": "Work in Progress", "section": "CAN IDs", "key": "key2"}]', 'Values': {'key2': True}}}, 10: {'My Account': {'Name': 'My Account', 'JSON': '[{"type": "title", "title": "My Account"}, {"type": "color", "title": "Background Color", "section": "My Account", "key": "key2"}]', 'Values': {'key2': '000000'}}, 'Safety Bypass': {'Name': 'Safety Bypass', 'JSON': '[{"type": "title", "title": "Safety Bypass"}, {"type": "bool", "title": "Idiot Proofing", "section": "Safety Bypass", "key": "key2"}, {"type": "bool", "title": "Enable Brownout Warnings", "section": "Safety Bypass", "key": "key3"}, {"type": "bool", "title": "Brownout Sustain", "desc": "When brownout is detected, leave robot in disabled until reset or battery changed.", "section": "Safety Bypass", "key": "key4"}, {"type": "numeric", "title": "Safe PSI Limit", "desc": "Pneumatic tanks will charge up to this value. The robot will not let the PSI go over 200. FRC regulation states PSI must not go above 120.", "section": "Safety Bypass", "key": "key5"}]', 'Values': {'key2': False, 'key3': False, 'key4': False, 'key5': 100}}, 'CAN Types': {'Name': 'CAN Types', 'JSON': '[{"type": "title", "title": "CAN Types"}, {"type": "bool", "title": "Work in Progress", "section": "CAN Types", "key": "key2"}]', 'Values': {'key2': True}}, 'CAN IDs': {'Name': 'CAN IDs', 'JSON': '[{"type": "title", "title": "CAN IDs"}, {"type": "bool", "title": "Work in Progress", "section": "CAN IDs", "key": "key2"}]', 'Values': {'key2': True}}}, 9: {'CAN IDs': {'Name': 'CAN IDs', 'JSON': '[{"type": "title", "title": "CAN IDs"}, {"type": "bool", "title": "Work in Progress", "section": "CAN IDs", "key": "key2"}]', 'Values': {'key2': True}}}, 8: {'CAN IDs': {'Name': 'CAN IDs', 'JSON': '[{"type": "title", "title": "CAN IDs"}, {"type": "bool", "title": "Work in Progress", "section": "CAN IDs", "key": "key2"}]', 'Values': {'key2': True}}}, 1: {}}


class Login(App):

    def build(self):
        global lock

        def checkPassword(instance):
            global lockHashes, usalt, lock
            nonlocal username_input, password_input
            if username_input.text in lockHashes.keys():
                _ptemp = []
                for val in lockHashes.values():
                    _ptemp.append(val[0])
                if str(hashlib.pbkdf2_hmac(hash_name="sha256", password=password_input.text.encode("utf-8"), salt=usalt,
                                           iterations=69420)) in _ptemp:
                    lock = lockHashes[username_input.text][1]
                    self.stop()
                del _ptemp

        self.title = "NTC - Login"
        layout = GridLayout(cols=1, padding=200)
        welcome_label = Label(text='Login', font_size='35sp', padding=(100, 100))
        username_input = TextInput(hint_text="Username", halign="center")
        password_input = TextInput(hint_text="Password", password=True, password_mask="?", halign="center")
        button = Button(text='Login')
        button.bind(on_release=checkPassword)
        layout.add_widget(welcome_label)
        layout.add_widget(username_input)
        layout.add_widget(password_input)
        layout.add_widget(button)
        return layout


class Main(App):
    def build_config(self, config):
        for item in tabPerms_info[lock]:
            config.setdefaults(item, tabPerms_info[lock][item]['Values'])

    def build_settings(self, settings):
        for item in tabPerms_info[lock]:
            settings.add_json_panel(item, self.config, data=tabPerms_info[lock][item]['JSON'])

    def build(self):
        global tabPerms
        ntcSettingsButton = Button(text="Settings")
        ntcSettingsButton.bind(on_press=self.open_settings)
        launchCodeButton = Button()
        if lock == 11:
            mainLayout = GridLayout(cols=3, padding=500)
            mainLayout.add_widget(ntcSettingsButton)
        elif lock == 10:
            mainLayout = GridLayout(cols=2, padding=500)
            mainLayout.add_widget(ntcSettingsButton)
        elif lock == (9 or 8):
            mainLayout = GridLayout(cols=2, padding=500)
            mainLayout.add_widget(ntcSettingsButton)
        else:
            mainLayout = GridLayout(cols=1, padding=500)
        return mainLayout


if __name__ == '__main__':
    Login().run()
    lock = 10
    Main().run()
    if type(lock) == type(int):
        Main().run()
