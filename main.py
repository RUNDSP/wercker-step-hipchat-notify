import sys
import hipchat

if len(sys.argv) < 7 :
  print 'There should be 7 arguments'
  sys.exit(1)

token = str(sys.argv[1])
room_id = str(sys.argv[2])
from_name  = str(sys.argv[3])
message  = str(sys.argv[4])
color = str(sys.argv[5])

notify = '0'
if str(sys.argv[6]) == 'true':
    notify = '1'

print "token: " + token
print "room_id: " + room_id
print "message: " + message
print "color: " + color
print "notify: " + notify

hipster = hipchat.HipChat(token=token)

hipster.method('rooms/message', method='POST', parameters={'room_id': room_id, 'from': from_name, 'message': message, 'color': color, 'notify': notify})