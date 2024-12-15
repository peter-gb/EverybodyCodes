words = "THE FLAME SHIELDED THE HEART OF THE KINGS"
runic = words.split(",")

inscr = "POWE PO WER P OWE R"


def extract_runicwords(runic,inscr):
    words_ins = inscr.split(" ")
    matches = [runic_word for runic_word in runic if any(runic_word in word for word in words_ins)]
    return matches

matches = extract_runicwords(runic,inscr)

print(len(matches))