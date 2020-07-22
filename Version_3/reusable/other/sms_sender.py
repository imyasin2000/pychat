import ghasedak

def sms_sender(from_c,send_to):
    sms = ghasedak.Ghasedak("a953ba30854130502559586ca6b93e0f81de604661d4bd0ec858e162330f8a76")
    sms.send({ 'message':str(from_c) +' invited you to chat on PyChat.\n\nYou can download PyChat with the link below : \n\n' + "http://8upload.ir/uploads/f74418985.zip",  'receptor' : str(send_to),  'linenumber': '10008566' })



sms_sender("Dr.mostafa bastam ","09113187038")