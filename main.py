from clockwork import clockwork

api = clockwork.API('6dbd7ee0c11c49d41c298bbb4cf84edea3eda846')

message = clockwork.SMS(
    to = '14196356328',
    message = 'Test Message - Steven Kast')

response = api.send(message)

if response.success:
    print ('Success ' + response.id)
else:
    print (response.error_code)
    print (response.error_message)
