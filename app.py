print("Title of program: yay encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be better,  feeling sad is being human")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling, live life happily and make every moment your best part")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
 patch-1
      encouragement_list.append("you are stronger than you think, dont give up, life is like a marathon and its okay to be slow")
      counter += 1 

      encouragement_list.append("you are stronger than you think, don't give up, life is like a marathon and its okay to be slow")
      counter += 1
    if each_word == "hyper":
      feelings_list.append("hyper")
      encouragement_list.append("you can do whatever you want and have fun haha! It's fun to be highh!")
      counter += 1
 main
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Go occupy yourself, spend time with you loved ones. Life is short, make the most of it.")
      counter += 1
   if each_word == "hopeless":
      feelings_list.append("hopeless")
      encouragement_list.append("cheer up, dont give up")
      counter += 1
 patch-1

    if each_word == "angry"
       feelings_list.append("angry")
       encouragement_list.append("Anger only makes you feel horrible. Keep calm and smile, do not do anything you will regret!")
       counter += 1
      
main
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
