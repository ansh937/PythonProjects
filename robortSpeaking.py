import os

if __name__== "__main__":
  print("Welcome to the Robort speaker 2.0")
  while True:
      word=input("Enter any thing then it will convert your words to the voice: ")
      if word.lower()=="q":
        os.system(f"say {"Bye Bye friend"}")#(f"say 'Bye bye friend'")
        break
      command=f"say {word}" #*Here the say is the command used to pronounce the name typed by the user 
                            #*if we donoot mention the word (say)then the error will occour
      os.system(command)