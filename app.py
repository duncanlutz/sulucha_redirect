from flask import Flask, redirect
app = Flask(__name__)

@app.route('/', methods=["GET"])
def redirect_user():
    return redirect('https://bestattorneys.com', 301)

if __name__ == '__main__':
    app.run()