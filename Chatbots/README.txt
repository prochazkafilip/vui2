

Before installing the needed libraries and packages, make sure you have pip3 (or pip) available at your OS. 

1. create virtualenv (virtual environment) named as "venv" :

https://sourabhbajaj.com/mac-setup/Python/virtualenv.html

2. Activate your venv:

source venv/bin/activate

3. and with pip install requirements.txt as follows:

pip3 install -r requirements.txt

4. Install rasa x (gui for Rasa):

pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple

5. Enter "my_rasa" folder and type "rasa x" and local mode for rasa will be opened in your web browser at 5005 port.

6. Open another shell window and type "rasa run actions" to run action server at 5055 port.


*/ ---------------------------- */

https://rasa.com/docs/rasa/installation/

COVID-19 dataset resources:

https://github.com/benoitalvarez/Covid-19-QBox-ChatbotModel/blob/master/Models/Rasa/Covid19%20Bot_RASA.json

https://www.transperfect.com/dataforce/covid-19-chatbot

https://medium.com/qbox-nlp-performance-tooling/new-model-for-rapid-deployment-of-covid-19-trained-chatbots-8806fb94a8ff

https://github.com/Archish27/nora-covid-19-bot/blob/master/actions/actions.py

