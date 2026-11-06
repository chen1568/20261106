list_message = input().split(" ")
message = []
for i in range(len(list_message)):
    list_message[i] = int(list_message[i])
    message.append(chr(list_message[i]))
print("「解碼結果： {}」".format(message))``