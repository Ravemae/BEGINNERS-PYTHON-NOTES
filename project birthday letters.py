def open_files():
  name = []
  print("Hello there welcome to project birthday letters")
  print("please note that this version can only allow you to  send to 6 people at once")
  while True:
    user_input = input("write a name of the person you would like to invite to your birthday party: ")
    add_to_list = name.append(user_input)
    if len(name) < 6:
      more = input(" would you like to add someone else: ")
    else:
      print("You have reached yout limit please try again later")
      break
    if more == "yes" or more == "yeah"  or more == "sure":
      open_files
    else:
      print("ok")
      break
  files_names  = ['demo.txt','demo1.txt', 'demo2.txt','demo3.txt','demo4.txt','demo5.txt', 'demo6.txt']
  for  i in range (0,len(name)):    
    with open(files_names[i], mode='a') as file:
      file.write(f"Hi {name[i]},\n I want you to come to my birthday party. Hope to see you soon\n Best regards,\n David")
open_files()
  