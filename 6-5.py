text = "X-DSPAM-Confidence:    0.8475"

atpos = text.find('0')
txt = text[atpos:atpos+6]
txt = float(txt)
print(txt)