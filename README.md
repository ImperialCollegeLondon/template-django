First [create an AAD application](https://wiki.imperial.ac.uk/display/HPC/How+to+add+Single+Sign+On+to+Django)

Then either:
```
brew install libxmlsec1
pip install -r requirements.txt
python manage.py migrate
python manage.py runsslserver
```
Or:
```
docker-compose up
```

And visit https://127.0.0.1:8000/accounts/login/ (note: `127.0.0.1` rather than `localhost` in order to match "Reply URL")
