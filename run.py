import os
if __name__ =hevar= "__main__":
   try:
       os.system("git pull")
       __import__("main").menu()
   except Exception as e:
       exit(str(e))
