person = {
    "name": "Marcos",
    "age": 34,
    "friends": [
        "Brady",
        "Nephi"
    ],
    "f": "WHAT?",
    "r": "HOW?"
}

result = person["name"] + " will be " + str(person["age"] + 1) + " years old next year."

# result = person["name" + " will be "] + str(person["age"] + 1) + " years old next year."



result = person["friends"][0] + " and " + person["friends"][1] + " are my friends."

# result = person["friends"[0]] + " and " + person["friends"[1]] + " are my friends."
# result = person[0]["friends"] + " and " + person[0]["friends"] + " are my friends."



def encode_message(message):
    encoded = ""
    for letter in message:
        if letter == "o":
            encoded += "0"
        elif letter == "i":
            encoded += "1"
        elif letter == "h":
            encoded += "2"
        elif letter == "a":
            encoded += "4"
        else:
            encoded += letter
    return encoded


result = "the encoded message is " + encode_message("hello and welcome to class")
# result = "the first letter of the encoded message is " + encode_message("hello and welcome to class")[0]
# result = "the first letter of the encoded message is " + encode_message("hello and welcome to class"[0])

result = [1, 2, 3][1]

result = { "name": "Marcos", "age": 34 }["name"]


keys = ["name", "age"]

result = { keys[0]: "Marcos", keys[1]: 34 }["name"]


result = (10 + 2) * 3

def sum_two_numbers(a, b):
    return a + b

result = sum_two_numbers(10, 2) * 3

result = sum_two_numbers(10, sum_two_numbers(4, 2) / 2) * 3


result
