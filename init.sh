pip3 install -r ./cyberhead/requirements.txt
yarn --cwd ./cyberhead/web/ install

python3 ./cyberhead/database.py
python3 ./startup.py
