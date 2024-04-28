import string, sys, time, hashlib, keyboard, os, fileinput, bcrypt, getpass, pyperclip, random, string, sys, time

os.system('cls')
RanNum = random.randint(1, 5)

number_list = ['1', '2', '3', '5', '6', '7', '8', '9']
r1 = random.choice(number_list)

letter_list = ['B', 'D', 'F']
r2 = random.choice(letter_list)

r3 = r2 + r1


os.system('color ' + r3)

os.system('color 2')



u = getpass.getpass("Enter a password: ")

os.system('cls')

# Hashing the password
hashed = hashlib.md5(u.encode('utf-8')).hexdigest()
 

 
# printing the hashed
print("Hashed Using MD5: ")
print(hashed)

pyperclip.copy(hashed)
hash = input("Press \" Ctrl + V \" to paste the hash: ")

st = time.time()

f = open(r'rockyou.txt', 'r+', encoding = 'iso-8859-15')

yesno = ""

for line in f:
   line=line.rstrip()
   
   h= hashlib.md5(line.encode('iso-8859-15')).hexdigest()
   
   if h == hash:
     
      et = time.time()
      print("Original Password: ", line)
      print("This is a very insecure password that can easily be breached.")
      elapsed_time = et - st
      round(elapsed_time)
      print('Execution time:', elapsed_time, 'seconds')
     
      yesno = (input("Would you like to enter a more secure password? \" Y \" for yes, \" N \" for no: "))  


      if yesno == "N" or yesno == "n":
         
         print('Bye, Have a Great Day')
         exit()

      elif yesno == "Y" or yesno =="y":
         
         u = getpass.getpass("Enter a password: ")

         os.system('cls')

         # Hashing the password
         hashed = hashlib.md5(u.encode('utf-8')).hexdigest()
 

 
# printing the hashed
         print("Hashed Using MD5: ")
         print(hashed)

         pyperclip.copy(hashed)
         hash = input("Press \" Ctrl + V \" to paste the hash: ")

         f = open(r'rockyou.txt', 'r+', encoding = 'iso-8859-15')



         for line in f:
            line=line.rstrip()
   
            h= hashlib.md5(line.encode('iso-8859-15')).hexdigest()
   
            if h == hash:
             et = time.time()
             print("Original Password: ", line)
             print("This is a very insecure password that can easily be breached.")
             elapsed_time = et - st
             round(elapsed_time)
             print('Execution time:', elapsed_time, 'seconds')
             
             exit()


         else:
            print("Nice Password, it may take a second to crack it")

            f3 = open(r'passwords.txt', 'r+', encoding = 'iso-8859-15')
         
     
            for line in f3:
                  line=line.rstrip()
                  h= hashlib.md5(line.encode('iso-8859-15')).hexdigest()
                     
                  if h == hash:
         
                    et = time.time()  
                    print("Original Password: ", line)
                    print("This is a very insecure password that can easily be breached.")
                    elapsed_time = et - st
                    round(elapsed_time)
                    print('Execution time:', elapsed_time, 'seconds')
                   
                    exit()
               
            else:
           
                  print("Awesome password, I couldn't breach it!")
                  exit()

else:
 
   print("Nice Password, It make take a second to crack it")
   
   f3 = open(r'passwords.txt', 'r+', encoding = 'iso-8859-15')
         
   for line in f3:
      line=line.rstrip()
      h= hashlib.md5(line.encode('iso-8859-15')).hexdigest()
                     
      if h == hash:
         
         et = time.time()
         print("Original Password: ", line)
         print("This is a very insecure password that can easily be breached.")
         elapsed_time = et - st
         round(elapsed_time)
         print('Execution time:', elapsed_time, 'seconds')
         
         exit()
         
   else:
           
      print("Awesome password, I couldn't breach it!")
      exit()
