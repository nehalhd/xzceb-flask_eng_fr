import machinetranslation 
from machinetranslation import translator
from flask import Flask, render_template, request
import json

from . import english_to_french, french_to_english

# import sys
# sys.path.append('../machinetranslation/translator')

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=['POST'])
def englishToFrench():
    english_text = request.form.get('english_text')
    # Write your code here
    french_text = english_to_french(english_text)

    return french_text

@app.route("/frenchToEnglish", methods=['POST'])
def frenchToEnglish():
    french_text = request.form.get('french_text')
    # Write your code here
    english_text = french_to_english(french_text)

    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
