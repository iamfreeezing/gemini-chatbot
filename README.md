<h2>Steps to run the app locally:</h2>

1. Create your own virtual environment by using: **python -m venv nocode_env**

2. Activate:

        nocode_env\Scripts\activate.bat (Windows)
        
        source nocode_env/bin/activate (Mac/Linux)
    
3. Install all dependencies using requirements.txt (**pip install -r requirements.txt**)

4. Install: **https://cloud.google.com/sdk/docs/install**

5. Authenticate via: **gcloud auth application-default login**. You have to click on the link in the terminal and sign in.

6. Run Django server via: **python manage.py runserver**

Step 4 can be skipped (maybe). But do it just to be sure.gi
