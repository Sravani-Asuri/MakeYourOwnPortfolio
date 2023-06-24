from flask import Flask,render_template, request,session
import uuid
import os

app = Flask(__name__)
app.secret_key="SecretKey"
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form/<string:design>",methods=["GET","POST"])
def form(design):
    session["design_sess"]=design
    return render_template("form.html")

@app.route("/upload", methods = ["GET","POST"])
def upload():
    design_upload=session.get("design_sess")
    if design_upload=="design1":
        design_name="design1.html"
    elif design_upload=="design2":
        design_name="design2.html"
    
    if request.method == "POST":
        name = request.form.get("firstname")
        lastname = request.form.get("lastname")
        school = request.form.get("school")
        college = request.form.get("college")
        phone = request.form.get("phone")
        email = request.form.get("email")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        about = request.form.get("about")
        git= request.form.get("github")
        insta = request.form.get("instagram")
        key=uuid.uuid1()
        img=request.files["dp"]
        img.save(f"static/images/{img.filename}")
        img_new_name=f"{key}{img.filename}"
        os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")
   
        
    return render_template(design_name,dname = name,dlname = lastname,dsch = school,img=img_new_name, dcol = college,dph = phone,demail = email,ds1 = skill1,ds2 = skill2,ds3 =skill3,ds4 = skill4,dabout = about,g=git,i=insta)

        
if __name__ == "__main__":
    app.run(debug=True)
