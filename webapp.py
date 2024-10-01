from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    
    animal = request.args['sellist1']
    if animal == "hay":
        reply1 = "horse"
        reply2 = "horse.jfif"
    elif animal == "meat":
        reply1 = "wolf"
        reply2 = "wolf.jfif"
    elif animal == "peanuts":
        reply1 = "elephant"
        reply2 = "elephant.jfif"
    elif animal == "sludge":
        reply1 = "pleasing fungus beatle"
        reply2 = "disgusting.jpg"
    return render_template('page2.html',name = request.args["name"],sellist1 = request.args["sellist1"],sellist2 = request.args["sellist2"],sellist3 = request.args["sellist3"],sellist4 = request.args["sellist4"],sellist5 = request.args["sellist5"],animal = reply1,picture = reply2)
    
if __name__=="__main__":
    app.run(debug=False)
