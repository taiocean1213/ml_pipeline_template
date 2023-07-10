## Python Project

-getting started:
navigate to the project root directory in the terminal and type
`pip install -r requirements.txt`

-package the app



# Pushing to remotes
dvc remote add -d myremote gdrive://1dtuVBTTqiuw4weaAPAqBDBEBzAq6Jfe-?usp=sharing

dvc add assets/data/digits.csv assets/models/model.joblib

dvc commit

dvc push

git add .

git commit -a -m "Updated Model"

git push

# Pulling from remotes
git clone <git-repo-url>

dvc remote add -d myremote gdrive://1dtuVBTTqiuw4weaAPAqBDBEBzAq6Jfe-?usp=sharing

dvc pull myremote

git checkout <versionHash>

dvc checkout

