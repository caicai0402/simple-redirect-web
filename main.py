from flask import Flask, redirect, url_for
import random

app = Flask(__name__)

@app.route("/", methods=['GET'])
def redirect_to_form():
    form_links = [
        "https://www.surveycake.com/s/wvBBO",
        "https://www.surveycake.com/s/xwQxz",
        "https://www.surveycake.com/s/7Zpyn",
        "https://www.surveycake.com/s/9eDAx",
        "https://www.surveycake.com/s/OkQ3G",
        "https://www.surveycake.com/s/4mn47",             
    ]
    selected_link = random.choice(form_links)
    return redirect(selected_link)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1126, debug=True)
    # link: https://reurl.cc/d1OE2M
