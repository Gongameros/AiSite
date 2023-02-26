from revChatGPT.V1 import Chatbot
from flask import Flask, render_template

chatbot = Chatbot(config={
  "email": "your password",
  "password": "your password"
})

prompt = 2+4
response = ""

for data in chatbot.ask(
  prompt
):
    response = data["message"]

app = Flask(__name__)
@app.route("/")
def ArtistAI():
    return render_template('ArtistAI.html', gpt_output = response)

if __name__ == '__main__':
    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
