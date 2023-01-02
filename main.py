alphabet = [
  "ა", "ბ", "გ", "დ", "ე", "ვ", "ზ", "თ", "ი", "კ", "ლ", "მ", "ნ", "ო", "პ",
  "ჟ", "რ", "ს", "ტ", "უ", "ფ", "ქ", "ღ", "ყ", "შ", "ჩ", "ც", "ძ", "წ", "ჭ",
  "ხ", "ჯ", "ჰ"
]

match = [
  "1", "2", "3", "4", "5", "6", "7", "9", "10", "20", "30", "40", "50", "70",
  "80", "90", "100", "200", "300", "400", "500", "600", "700", "800", "900",
  "1000", "2000", "3000", "4000", "5000", "6000", "8000", "9000"
]

shemotanili = input("შემოიტანე სიტყვა/სიტყვები და დააჭირე Enter'ს: ")

final_result = ""
for letter in shemotanili:
  for element in alphabet:
    if element == letter:
      indeqsi = alphabet.index(element)
      final_result += match[indeqsi]
      break
  else:
    print("Daviqsirda shecdoma, cade tavidan getayva")
print(final_result)
