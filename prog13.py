from flask import Flask, jsonify
app=Flask(__name__)
@app.route("/")
def home():
    return jsonify({
        "message":"Hello! python backend is working."
    })
@app.route("/about")
def about():
    return jsonify({
        "name":"my application",
        "backend":"python flask"
    })
if __name__=="__main__":
    app.run(debug=True)