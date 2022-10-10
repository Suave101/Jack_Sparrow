import codecs, hashlib, json

usalt = b"a97789618bd9221692ae84115675b88aa9bc30362c22883c"

password_table = {"Suave101": ["ChErOkEe2007aPd923252648482007202588224646", 11],
                  "LynB": ["cfc84ec8f9e7b2458a001", 10],
                  "flintseal": ["60dc4c24fc98e595", 10],
                  "Jordan": ["efff4b2d494", 10],
                  "SlyPirate": ["81b1e1f134eb902b", 9],
                  "MechanicalSpy": ["c0b7d0e8f6ea1", 8],
                  "Guest": ["1234", 1]}
for item in password_table:
    password_table[item][0] = str(hashlib.pbkdf2_hmac(hash_name="sha256", password=password_table[item][0].encode("utf-8"), salt=usalt, iterations=69420))

with open("ntc.lock", "rb") as password_file:
    print(json.loads(codecs.decode(password_file.read().decode("utf_7"), "rot_13")))

with open("ntc.lock", "wb") as password_file:
    password_file.write(codecs.encode(json.dumps(password_table), "rot_13").encode("utf_7"))
