from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
import audio
import video
import webcam
app=Flask(__name__)
cors=CORS(app)
def emotion(msg):
    emotion=[5,48,56,87]
    return emotion
def detectText(msg):
    return "positive"
##@app.route('/login',methods=['POST','GET'])
##def login():
##    if request.method =='POST':
##        email=request.form['username']
##        pa=request.form['password']
##        return logging_in(email,pa)
##    else:
##        email = request.args.get('username')
##        pa = request.args.get('pa')
##        return logging_in(email, pa)
@app.route("/msg",methods=["POST"])
def main2():
    print(request.get_json())
    print(request.get_text())
    if(request.method=="POST"):
        print(123)
        return jsonify(detectText(request.form['text']))
@app.route("/msg/<msg>")
def main(msg):
##    per=emotion(msg)
##    print(per)
    print(msg)
    return jsonify(detectText(msg))
##    return jsonify({'happy':per[0],'sad':per[1],'suprising':per[2],'afraid':per[3]})
@app.route("/a")
def m():
    return render_template("index.html")
@app.route("/audio/<file>")
def audioMethod(file):
    data=audio.file("C:/Users/Angel/Downloads/"+file)
    print(data)
    return jsonify("positive")
@app.route("/listen")
def listen():
    print(audio.listen())
    return jsonify("positive")
@app.route("/live")
def live():
    return jsonify(webcam.live())
@app.route("/endlive")
def endlive():
    return(webcam.stop())
@app.route("/ok",methods=["POST","GET"])
def ok():
    print("helo")
    if(request.method=="POST"):
        print(request.files["audio"].filename)
        return jsonify(audio.file(request.files["audio"]))
if(__name__)=="__main__":
    app.run(port=5000)
