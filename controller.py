from config import *
from models import *
from forms import *
import time

def check_for_kick():
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("login"))

#custom routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    services = ["Web Development","Api Desigining","Micro-Services","Pentesting(Application-security)","Web-Designing"]
    return render_template('services.html',services=services)

#backend routes
@app.route('/register',methods=['POST','GET'])
def register():
    form = register_form()
    if request.method == 'POST':
        email = form.email.data
        uid = form.username.data
        if User.query.filter_by(uid=uid).first():
            flash("uid already taken,use another","danger")
        else:
            if User.query.filter_by(uid=uid).first():
                flash("email already taken,use another","danger")
            else:
                if form.password.data != form.confirm.data:
                    flash("uid already taken,use another","danger")
                else:
                    password = form.password.data
                    print(f"email:{email},uid:{uid},password:{password}")
                    password = sha256_crypt.encrypt(str(password))
                    usr = User(email=email,uid=uid,password=password)
                    db.session.add(usr)
                    db.session.commit()
                    usr = User.query.filter_by(uid=uid).first()
                    prof = Profile(user_id=usr.id)
                    db.session.add(prof)
                    db.session.commit()
                    flash("Account Succefully crated.you can login now","success")
                    return redirect(url_for("login"))

    return render_template('register.html',form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    form = login_form()
    if request.method == 'POST':
        uid = form.username.data
        pword = form.password.data

        if User.query.filter_by(uid=uid).first():
            usr_ = User.query.filter_by(uid=uid).first()
            if sha256_crypt.verify(pword,usr_.password):
                flash("You Have Logged In!!","success")
                session['uid'] = uid
                session['logged_in'] = True
                return redirect(url_for('dashboard'))
            else:
                flash("Wrong Password","warning")
        else:
            flash("invalid Data","warning")
    return render_template('login.html',form=form)

@app.route('/dashboard')
def dashboard():

    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))

    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    session.clear()
    flash("You have been logged out","success")
    return redirect(url_for("index"))

def save_img(img):
    random_hex = secrets.token_hex(8)
    fname,fext = os.path.splitext(img.filename)
    print(f"ext:{fext}")
    allowed = ['.jpg','.png','.gif','.jpeg','.webp']
    if fext not in allowed:
        return "not_allowed"
    fullf = random_hex+fext
    fullpath = os.path.join(app.root_path,'static/post_imgs',fullf)
    img.save(fullpath)
    return fullf

def save_prof_img(img):
    random_hex = secrets.token_hex(8)
    fname,fext = os.path.splitext(img.filename)
    print(f"ext:{fext}")
    allowed = ['.jpg','.png','.gif','.jpeg','.webp']
    if fext not in allowed:
        return "not_allowed"
    fullf = random_hex+fext
    fullpath = os.path.join(app.root_path,'static/profile_imgs',fullf)
    img.save(fullpath)
    return fullf

def save_album(img):
    random_hex = secrets.token_hex(8)
    fname,fext = os.path.splitext(img.filename)
    print(f"ext:{fext}")
    allowed = ['.jpg','.png','.gif','.jpeg','.webp']
    if fext not in allowed:
        return False
    fullf = random_hex+fext
    fullpath = os.path.join(app.root_path,'static/album',fullf)
    img.save(fullpath)
    return fullf


@app.route('/dashboard/addpost',methods=['POST','GET'])
def addpost():
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    form = post_form()
    if request.method == 'POST':
        uid = session['uid']
        title = form.title.data
        body = form.body.data
        if request.files['img']:
            img = request.files['img']
            img_name = save_img(img)
            print(f"img:{img_name}::saved")
            if img_name == "not_allowed":
                img_name = ""
        else:
            img_name = ""
        usr = User.query.filter_by(uid=uid).first()
        pst = Post(title=title,body=body,img=img_name,user_id=usr.id)
        db.session.add(pst)
        db.session.commit()
        flash("Post Succesfully added","success")
        return redirect(url_for("profile"))
    return render_template('add-post.html',form=form,ckeditor=ckeditor)

@app.route('/dashboard/profile',methods=['POST','GET'])
def profile():
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    if request.method == 'POST':
        if request.files:
            img = request.files['album']
            img_name = save_album(img)
            if img_name:
                usr = User.query.filter_by(uid=session['uid']).first()
                albums = usr.prof[0].albums
                if albums=='':
                    usr.prof[0].albums = "#2#$2"+img_name
                    db.session.commit()
                    flash("new album added","success")
                    return redirect(url_for('profile'))
                else:
                    albums = albums.split("#2#$2")
                    albums.append(img_name)
                    st = "#2#$2".join(albums)
                    usr.prof[0].albums = st
                    db.session.commit()
                    flash("new album added","success")
                    return redirect(url_for('profile'))


    usr = User.query.filter_by(uid=session['uid']).first()
    prof_img = usr.prof[0].prof_img
    albums = usr.prof[0].albums.split('#2#$2')
    albums.remove('')
    albums.reverse()
    print(f"reversed:{albums}")
    albums = list(albums)
    print(type(albums))
    followers = usr.prof[0].followers
    following = usr.prof[0].following
    posts = list(usr.posts)


    new_posts = []
    for post in posts:
        d = dict()
        d['id'] = post.id
        d['title'] = post.title
        d['body'] = post.body
        d['img'] = post.img
        d['date'] = post.date
        d['likes'] = post.likes
        d['liked'] = post.liked
        new_posts.append(d)

    like_ok = []
    for post in posts:
        liked = post.liked
        liked = liked.split("#$%12!")
        user_id = User.query.filter_by(uid=session['uid']).first().id
        if str(user_id) in liked:
            like_ok.append(False)
        else:
            like_ok.append(True)

    like_ok = like_ok.__iter__()
    for post in new_posts:
        post['like_ok'] = next(like_ok)

    print(f"lastsss:{new_posts}")

    new_posts.reverse()
    # print(posts)
    posts=list(new_posts)
    total_posts = len(posts)
    session['curr_'] = 0
    session['next_'] = 2
    return render_template("profile.html",prof_img=prof_img,posts=new_posts[session['curr_']:session['next_']],uid=session['uid'],email=usr.email,followers=followers,following=following,total_posts=total_posts,albums=albums)

@app.route('/dashboard/profile/album/<string:img>',methods=['POST','GET'])
def album(img):
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    if request.method == 'POST':
        subprocess.run(['rm','/home/bnk/progs/flask/test/static/albums/'+img])
        usr = User.query.filter_by(uid=session['uid']).first()
        albums = usr.prof[0].albums.split('#2#$2')
        albums.remove(img)
        st = "#2#$2".join(albums)
        usr.prof[0].albums = st
        db.session.commit()
        flash("album removed","success")
        return redirect(url_for('profile'))

    return render_template('album.html',img=img)

@app.route('/go/<string:id>',methods=['POST','GET'])
def go(id):
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    return redirect(url_for("edit_post",id=id))


@app.route('/dashboard/posts/edit/<string:id>',methods=['POST','GET'])
def edit_post(id):
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))

    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("Invalid post","warning")
        return redirect(url_for("dashboard"))
    if post.author.uid != session['uid']:
        flash("Accesssing Unauthorized Post","danger")
        return redirect(url_for("profile"))
    form = post_edit_form()
    form.title.data = post.title
    form.body.data = post.body

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        post.title = title
        post.body = body
        
        if form.dont_want_image.data:
            post.img = ""
        else:
            if request.files['img']:
                img_name = save_img(request.files['img'])
                post.img = img_name
        
        db.session.commit()
        flash("Post updated","success")
        return redirect(url_for("profile"))

    return render_template("edit-post.html",form=form)

@app.route('/viewmore',methods=['POST','GET'])
def viewmore():
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    if request.method == 'POST':
        session['curr_']+=2
        session['next_']+=2
        usr = User.query.filter_by(uid=session['uid']).first()
        prof_img = usr.prof[0].prof_img
        posts = usr.posts

        new_posts = []
        for post in posts:
            d = dict()
            d['prof_img'] = prof_img
            d['uid'] = session['uid']
            d['id'] = post.id
            d['title'] = post.title
            d['body'] = post.body
            d['img'] = post.img
            d['date'] = post.date
            d['likes'] = post.likes
            d['liked'] = post.liked
            new_posts.append(d)

        like_ok = []
        for post in posts:
            liked = post.liked
            liked = liked.split("#$%12!")
            user_id = User.query.filter_by(uid=session['uid']).first().id
            if str(user_id) in liked:
                like_ok.append(False)
            else:
                like_ok.append(True)

        like_ok = like_ok.__iter__()
        for post in new_posts:
            post['like_ok'] = next(like_ok)

        new_posts.reverse()
        posts=list(new_posts)
        resp = posts[session['curr_']:session['next_']]
        print(resp)
        # resp = []
        # for post in posts:
        #     d = dict()
        #     d['id'] = post.id
        #     d['uid'] = session['uid']
        #     d['prof_img'] = prof_img
        #     d['title'] = post.title
        #     d['body'] = post.body
        #     if post.img:
        #         d['img'] = post.img
        #     d['date'] = post.date
        #     d['likes'] = post.likes
        #     resp.append(d)

        return jsonify(resp),200 
        
@app.route('/delete/<string:id>',methods=['POST','GET'])
def delete(id):
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    if request.method == 'POST':
        post = Post.query.filter_by(id=id).first()
        if not post:
            flash("Invalid post","warning")
            return redirect(url_for("dashboard"))

        # print(post)
        if post.author.uid != session['uid']:
            flash("Unauthorized Post!! Never Do That Again","danger")
        else:
            db.session.delete(post)
            db.session.commit()
            if post.img:
                subprocess.run(['rm','/home/bnk/progs/flask/test/static/post_imgs/'+post.img])
            flash("Post Deleted!","success")
        return str(id)+" deleted",200

@app.route('/search/<string:text>',methods=['POST','GET'])
def search(text):
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        text = "%"+text+"%"
        res = cur.execute("SELECT * FROM users WHERE uid LIKE %s",[text])
        result = cur.fetchall()
        print(f"typr:{type(result)}")
        res = list(result)

        imgs = []
        for usr in res:
            user = User.query.filter_by(uid=usr['uid']).first()
            imgs.append(user.prof[0].prof_img)
        imgs = imgs.__iter__()
        for usr in res:
            usr['prof_img'] = next(imgs)
        print(res)
        time.sleep(3)
        return jsonify(res),200

@app.route('/dashboard/profiles')
def users_profiles():
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    return render_template('search.html')

@app.route('/dashboard/profiles/<string:text>')
def user_profile(text):
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    if not User.query.filter_by(uid=text).first():
        flash("No Matched Users sorryy,try the better way","warning")
        return redirect(url_for("users_profiles"))

    session['visited_user'] = text
    session['users_curr_'] = 0
    session['users_next_'] = 2
    usr = User.query.filter_by(uid=text).first()
    prof_img = usr.prof[0].prof_img
    albums = usr.prof[0].albums.split('#2#$2')
    albums.remove('')
    albums.reverse()
    print(f"reversed:{albums}")
    albums = list(albums)
    print(type(albums))
    followers = usr.prof[0].followers
    following = usr.prof[0].following

    posts = list(usr.posts)


    new_posts = []
    for post in posts:
        d = dict()
        d['id'] = post.id
        d['title'] = post.title
        d['body'] = post.body
        d['img'] = post.img
        d['date'] = post.date
        d['likes'] = post.likes
        d['liked'] = post.liked
        new_posts.append(d)

    like_ok = []
    for post in posts:
        liked = post.liked
        liked = liked.split("#$%12!")
        user_id = User.query.filter_by(uid=session['uid']).first().id
        if str(user_id) in liked:
            like_ok.append(False)
        else:
            like_ok.append(True)

    like_ok = like_ok.__iter__()
    for post in new_posts:
        post['like_ok'] = next(like_ok)


    new_posts.reverse()
    new_posts = list(new_posts)
    total_posts = len(posts)
    # session['curr_'] = 0
    # session['next_'] = 2
    return render_template("users_profile.html",prof_img=prof_img,posts=new_posts[session['users_curr_']:session['users_next_']],uid=text,email=usr.email,followers=followers,following=following,total_posts=total_posts,albums=albums)


@app.route('/viewmore_users',methods=['POST','GET'])
def viewmore_users():
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    if request.method == 'POST':
        session['users_curr_']+=2
        session['users_next_']+=2
        usr = User.query.filter_by(uid=session['visited_user']).first()
        prof_img = usr.prof[0].prof_img
        posts = usr.posts

        new_posts = []
        for post in posts:
            d = dict()
            d['id'] = post.id
            d['title'] = post.title
            d['prof_img'] = prof_img
            d['uid'] = session['visited_user']
            d['body'] = post.body
            d['img'] = post.img
            d['date'] = post.date
            d['likes'] = post.likes
            d['liked'] = post.liked
            new_posts.append(d)

        like_ok = []
        for post in posts:
            liked = post.liked
            liked = liked.split("#$%12!")
            user_id = User.query.filter_by(uid=session['uid']).first().id
            if str(user_id) in liked:
                like_ok.append(False)
            else:
                like_ok.append(True)

        like_ok = like_ok.__iter__()
        for post in new_posts:
            post['like_ok'] = next(like_ok)

        new_posts.reverse()
        posts=list(new_posts)
        resp = posts[session['users_curr_']:session['users_next_']]



        # posts.reverse()
        # posts=list(posts)
        # posts = posts[session['users_curr_']:session['users_next_']]

        # resp = []
        # for post in posts:
        #     d = dict()
        #     d['id'] = post.id
        #     d['uid'] = session['visited_user']
        #     d['prof_img'] = prof_img
        #     d['title'] = post.title
        #     d['body'] = post.body
        #     if post.img:
        #         d['img'] = post.img
        #     d['date'] = post.date
        #     d['likes'] = post.likes
        #     resp.append(d)

        return jsonify(resp),200


@app.route('/dashboard/edit-profile',methods=['POST','GET'])
def edit_profile():
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    form = prof_edit_form()
    form.username.data = session['uid']

    if request.method == 'POST':
        if request.files['img']:
            img_name = save_prof_img(request.files['img'])
            User.query.filter_by(uid=session['uid']).first().prof[0].prof_img = img_name
            db.session.commit()
            flash("profile updated","success")
            # return redirect(url_for("edit_profile"))

        uid = request.form['username']
        if uid==session['uid']:
            pass
        else:
            if User.query.filter_by(uid=uid).first():
                flash("User id already taken please try another","warning")
                return redirect(url_for("edit_profile"))
            else:
                User.query.filter_by(uid=session['uid']).first().uid = uid
                db.session.commit()
                session['uid'] = uid

        if request.form['password']:
            if not len(request.form['password']) >=8:
                flash("Password length atleast 8 chrecters","warning")
                return redirect(url_for("edit_profile"))
            else:
                if request.form['password']!=request.form['confirm']:
                    flash("Passwords Dont match","warning")
                    return redirect(url_for("edit_profile"))

                pword = sha256_crypt.encrypt(str(request.form['password']))
                User.query.filter_by(uid=session['uid']).first().password = pword
                db.session.commit()
                flash("profile Updated","success")
                return redirect(url_for("edit_profile"))

    return render_template('edit-profile.html',form=form,prof_img=User.query.filter_by(uid=session['uid']).first().prof[0].prof_img)

@app.route('/like/<string:id>',methods=['POST','GET'])
def like(id):
    post = Post.query.filter_by(id=id).first()
    user_id = User.query.filter_by(uid=session['uid']).first().id
    liked = post.liked.split('#$%12!')
    if str(user_id) in liked:
        return 'mm..dont try to mess with me',200
    else:
        post.likes+=1
        liked.append(str(user_id))
        liked = "#$%12!".join(liked)
        post.liked = liked
        db.session.commit()
        return 'ok',200

@app.route('/dislike/<string:id>',methods=['POST','GET'])
def dislike(id):
    post = Post.query.filter_by(id=id).first()
    user_id = User.query.filter_by(uid=session['uid']).first().id
    liked = post.liked.split('#$%12!')
    if str(user_id) not in liked:
        return 'mm..dont try to mess with me',200
    else:
        post.likes-=1
        liked.remove(str(user_id))
        liked = "#$%12!".join(liked)
        post.liked = liked
        db.session.commit()
        return 'ok',200

@app.route('/dashboard/comment/<string:id>',methods=['POST','GET'])
def comment(id):
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    try:
        form = comment_form()
        post = Post.query.filter_by(id=id).first()
        prof_img = post.author.prof[0].prof_img 
        uid = post.author.uid
        comments = post.comments
        print(comments)
            # nums = range(0,len(comments))
        prof_imgs = []
        for i in range(0,len(comments)):
            print(i)
            prof_imgs.append(comments[i].author.prof[0].prof_img)
        print(prof_imgs)

        comms = []
        prof_imgs = iter(prof_imgs)
        for comment in comments:
            d = dict()
            d['uid'] = comment.author.uid
            d['comment'] = comment.comment
            d['prof_img'] = next(prof_imgs)
            d['id'] = comment.id
            comms.append(d)
        comms.reverse()
        comms = list(comms)
        user_id = User.query.filter_by(uid=session['uid']).first().id
        if request.method == 'POST':
            comment = form.body.data
            if(len(comment)==1):
                flash('at least 2 char long comment please!','warning')
                return redirect(url_for('comment',id=id))
            com1 = Comment(comment=comment,post_id=id,author_id=user_id)
            db.session.add(com1)
            db.session.commit()
            flash('comment added','success')
            return redirect(url_for('comment',id=id))

        return render_template('comment.html',post=post,comments=comms,uid=uid,prof_img=prof_img,form=form)
    except:
         flash('invalid post','warning')
         return redirect(url_for('profile'))

@app.route('/comm-delete/<string:id>',methods=['POST','GET'])
def comm_delete(id):
    try:
        a = session['uid']
    except:
            flash("ooo..Dont touch those Unauthorized pages.login first","danger")
            return redirect(url_for("index"))
    if request.method == 'POST':
        comment = Comment.query.filter_by(id=id).first()
        if(comment.author.uid!=session['uid']):
            flash('accessing unouthorized comments')
            session.clear()
            return redirect(url_for('index'))
        db.session.delete(comment)
        db.session.commit()

        return "ok",200

# @app.route('/api/test',methods=['POST','GET'])
# def api_test():
#     print(request.authorization)
#     return request.authorization

@app.route('/resp',methods=['POST','GET'])
def resp():
    if request.method == 'POST':
        if request.json:
            print(f'json:{request.json}')
        if request.args:
            print(f'args:{request.args}')
        if request.authorization:
            print(f'auth:{request.authorization}')
        if request.cookies:
            print(dir(request.cookies))
            greet = request.cookies
            print(greet.get('greetings'))

    data = (
        {
            "id":1,
            "title":"post 1",
            "body":"first post"
        },
                {
            "id":2,
            "title":"post 2",
            "body":"second post"
        },
                {
            "id":3,
            "title":"post 3",
            "body":"third post"
        }
    )
    # resp_ = make_response(render_template('index.html'))
    resp_ = make_response(jsonify(data),200)
    resp_.headers['whoami'] = 'bnk'
    resp_.set_cookie(
        'greetings',
        value="hope you are fine!",
        max_age=None,
        expires=None,
        path=request.path,
        domain=None,
        secure=False
    )
    return resp_
