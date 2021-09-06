import pywhatkit as kit
                # pip install pywhatkit

phone_no = "+91 phone_no"
                # '+91 phone no' enter phone number in this format

message = "hello this whatsapp automated message dont reply"
                # pass the message you want to send


kit.sendwhatmsg(phone_no,message,14,3,wait_time=35)
                # pass phone number and meassge variable
                # then pass time in hours , time in seconds
                # set wait time by default 35 seconds


print("your message is deileverd")