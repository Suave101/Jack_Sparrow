"""
import json
settings = {11: [{'type': 'title', 'title': 'Security Level 11 Settings'}, {'type': 'numeric', 'title': 'My Account', 'desc': 'Description of My Account', 'section': 'My Account', 'key': 'key2'}, {'type': 'numeric', 'title': 'Clocks', 'desc': 'Description of Clocks', 'section': 'Clocks', 'key': 'key2'}, {'type': 'numeric', 'title': 'Manage_Accounts_Below10', 'desc': 'Description of Manage_Accounts_Below10', 'section': 'Manage_Accounts_Below10', 'key': 'key2'}, {'type': 'numeric', 'title': 'Toggle_Idiot_Proofing', 'desc': 'Description of Toggle_Idiot_Proofing', 'section': 'Toggle_Idiot_Proofing', 'key': 'key2'}, {'type': 'numeric', 'title': 'Safe_PSI_Limit', 'desc': 'Description of Safe_PSI_Limit', 'section': 'Safe_PSI_Limit', 'key': 'key2'}, {'type': 'numeric', 'title': 'Disable_Brownout_Messages', 'desc': 'Description of Disable_Brownout_Messages', 'section': 'Disable_Brownout_Messages', 'key': 'key2'}, {'type': 'numeric', 'title': 'Toggle_Brownout_Sustain_Disabled', 'desc': 'Description of Toggle_Brownout_Sustain_Disabled', 'section': 'Toggle_Brownout_Sustain_Disabled', 'key': 'key2'}, {'type': 'numeric', 'title': 'CAN_Devices_Type', 'desc': 'Description of CAN_Devices_Type', 'section': 'CAN_Devices_Type', 'key': 'key2'}, {'type': 'numeric', 'title': 'CAN_IDs', 'desc': 'Description of CAN_IDs', 'section': 'CAN_IDs', 'key': 'key2'}, {'type': 'numeric', 'title': 'Welcome', 'desc': 'Description of Welcome', 'section': 'Welcome', 'key': 'key2'}], 10: [{'type': 'title', 'title': 'Security Level 10 Settings'}, {'type': 'numeric', 'title': 'My Account', 'desc': 'Description of My Account', 'section': 'My Account', 'key': 'key2'}, {'type': 'numeric', 'title': 'Manage_Accounts_Below10', 'desc': 'Description of Manage_Accounts_Below10', 'section': 'Manage_Accounts_Below10', 'key': 'key2'}, {'type': 'numeric', 'title': 'Toggle_Idiot_Proofing', 'desc': 'Description of Toggle_Idiot_Proofing', 'section': 'Toggle_Idiot_Proofing', 'key': 'key2'}, {'type': 'numeric', 'title': 'Safe_PSI_Limit', 'desc': 'Description of Safe_PSI_Limit', 'section': 'Safe_PSI_Limit', 'key': 'key2'}, {'type': 'numeric', 'title': 'Disable_Brownout_Messages', 'desc': 'Description of Disable_Brownout_Messages', 'section': 'Disable_Brownout_Messages', 'key': 'key2'}, {'type': 'numeric', 'title': 'Toggle_Brownout_Sustain_Disabled', 'desc': 'Description of Toggle_Brownout_Sustain_Disabled', 'section': 'Toggle_Brownout_Sustain_Disabled', 'key': 'key2'}, {'type': 'numeric', 'title': 'CAN_Devices_Type', 'desc': 'Description of CAN_Devices_Type', 'section': 'CAN_Devices_Type', 'key': 'key2'}, {'type': 'numeric', 'title': 'CAN_IDs', 'desc': 'Description of CAN_IDs', 'section': 'CAN_IDs', 'key': 'key2'}, {'type': 'numeric', 'title': 'Welcome', 'desc': 'Description of Welcome', 'section': 'Welcome', 'key': 'key2'}], 9: [{'type': 'title', 'title': 'Security Level 9 Settings'}, {'type': 'numeric', 'title': 'CAN_Devices_Type', 'desc': 'Description of CAN_Devices_Type', 'section': 'CAN_Devices_Type', 'key': 'key2'}, {'type': 'numeric', 'title': 'CAN_IDs', 'desc': 'Description of CAN_IDs', 'section': 'CAN_IDs', 'key': 'key2'}, {'type': 'numeric', 'title': 'Welcome', 'desc': 'Description of Welcome', 'section': 'Welcome', 'key': 'key2'}], 8: [{'type': 'title', 'title': 'Security Level 8 Settings'}, {'type': 'numeric', 'title': 'CAN_IDs', 'desc': 'Description of CAN_IDs', 'section': 'CAN_IDs', 'key': 'key2'}, {'type': 'numeric', 'title': 'Welcome', 'desc': 'Description of Welcome', 'section': 'Welcome', 'key': 'key2'}], 1: [{'type': 'title', 'title': 'Security Level 1 Settings'}, {'type': 'numeric', 'title': 'Welcome', 'desc': 'Description of Welcome', 'section': 'Welcome', 'key': 'key2'}]}

for item in settings:
    settings[item] = json.dumps(settings[item])

print(settings)
"""
import json

tabPerms = {11: ["My Account", "Welcome", "Clocks", "Safety Bypass", "CAN Types", "CAN IDs"],
            10: ["My Account", "Welcome", "Safety Bypass", "CAN Types", "CAN IDs"],
            9: ["Welcome", "CAN Devices Type", "CAN IDs"],
            8: ["Welcome", "CAN IDs"],
            1: ["Welcome"]}

tab_panels = {}

for level in tabPerms:
    _tab_panels = {}
    for item in tabPerms[level]:
        if item == "My Account":
            _temp = [{"type": "title", "title": item},
                     {"type": "color",
                      "title": "Background Color",
                      "section": item,
                      "key": "key2"}]
            _temp2 = {"key2": "000000"}
            _tab_panels[item] = {"Name": item, "JSON": json.dumps(_temp), "Values": _temp2}
        if item == "Clocks":
            # Manage_All_Accounts DownForRepairs Disable_Account Access_NTC_Code Create_Special_Access_Codes Create_Launch_Codes
            _temp = [{"type": "title", "title": item},
                     {"type": "bool",
                      "title": "Server Down",
                      "section": item,
                      "key": "key2"},
                     {"type": "string",
                      "title": "Server Down Message",
                      "section":  item,
                      "key": "key3"}
                     ]
            _temp2 = {"key2": "false", "key3": "Robot Network Error"}
            _tab_panels[item] = {"Name": item, "JSON": json.dumps(_temp), "Values": _temp2}
        if item == "Safety Bypass":
            _temp = [{"type": "title", "title": item},
                     {"type": "bool",
                      "title": "Idiot Proofing",
                      "section":  item,
                      "key": "key2"},
                     {"type": "bool",
                      "title": "Enable Brownout Warnings",
                      "section":  item,
                      "key": "key3"},
                     {"type": "bool",
                      "title": "Brownout Sustain",
                      "desc": "When brownout is detected, leave robot in disabled until reset or battery changed.",
                      "section":  item,
                      "key": "key4"},
                     {"type": "numeric",
                      "title": "Safe PSI Limit",
                      "desc": "Pneumatic tanks will charge up to this value. The robot will not let the PSI go over 200."
                              " FRC regulation states PSI must not go above 120.",
                      "section":  item,
                      "key": "key5"}
                     ]
            _temp2 = {"key2": False, "key3": False, "key4": False, "key5": 100}
            _tab_panels[item] = {"Name": item, "JSON": json.dumps(_temp), "Values": _temp2}
        if item == "CAN Types":
            _temp = [{"type": "title", "title": item},
                     {"type": "bool",
                      "title": "Work in Progress",
                      "section":  item,
                      "key": "key2"}]
            _temp2 = {"key2": True}
            _tab_panels[item] = {"Name": item, "JSON": json.dumps(_temp), "Values": _temp2}
        if item == "CAN IDs":
            _temp = [{"type": "title", "title": item},
                     {"type": "bool",
                      "title": "Work in Progress",
                      "section":  item,
                      "key": "key2"}]
            _temp2 = {"key2": True}
            _tab_panels[item] = {"Name": item, "JSON": json.dumps(_temp), "Values": _temp2}
    tab_panels[level] = _tab_panels
    del _tab_panels

print(tab_panels)
