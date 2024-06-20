     import os

     bind = "0.0.0.0:" + os.environ.get("PORT", "8000")
     workers = 2  # Adjust based on your needs 

     # Specify the correct module and callable
     wsgi_app = "bot.main:app"
