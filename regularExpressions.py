import re

print("regularExpressions.py")
pattern = r"Part"

text = '''This article is about the pre-1947 history of Pakistan. For post-1947 history, see History of Pakistan (1947–present).
Part of a series on the
History of Pakistan
Statue of an Indus priest or king found in Mohenjodaro, 1927
Timeline
Ancient
Classical
Medieval
Early modern
Modern
History of provinces
 Category Portal
vte
Part of a series on the
Culture of Pakistan

History
People
Languages
Traditions
Folklore
Cuisine
Festivals
Religion
Art
Literature
Music and Performing arts
Media
Sport
Monuments
Symbols
flag Pakistan portal
vte
History of South Asia
South Asia (orthographic projection)
Outline
National histories
Regional histories
Specialised histories
vte

A map outlining historical sites in Pakistan
The history of Pakistan preceding the country's independence in 1947[1] is shared with that of Afghanistan, India, and Iran. Spanning the western expanse of the Indian subcontinent and the eastern borderlands of the Iranian plateau, the region of present-day Pakistan served both as the fertile ground of a major civilization and as the gateway of South Asia to Central Asia and the Near East.[2][3]

Situated on the first coastal migration route of Homo sapiens out of Africa, the region was inhabited early by modern humans.[4][5] The 9,000-year history of village life in South Asia traces back to the Neolithic (7000–4300 BCE) site of Mehrgarh in Pakistan,[6][7][8] and the 5,000-year history of urban life in South Asia to the various sites of the Indus Valley Civilization, including Mohenjo Daro and Harappa.[9][10]


'''


# print(re.search(pattern,text))
results = re.finditer(pattern,text)
# print(type(result))

for result in results:
    print(result)