from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation 
from translator import english_to_french, french_to_english

import sys
sys.path.append('/path/to/translator')

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=['POST'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = english_to_french(textToTranslate)

    return "Translated text to French"

@app.route("/frenchToEnglish", methods=['POST'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = french_to_english(textToTranslate)

    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
