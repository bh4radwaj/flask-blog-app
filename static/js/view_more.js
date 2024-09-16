function get(){
    document.getElementById("view-m").remove();
    xhr = new XMLHttpRequest();
    xhr.open("POST","/viewmore",true);
    xhr.onload = function(){
        // console.log(xhr.responseText);
        var resp = JSON.parse(xhr.responseText);
        // console.log(resp);
        if(resp.length>0){
            for(var i=0;i<resp.length;i++){
                if(resp[i].like_ok){
                    if(resp[i].img){
                        var d = document.createElement('div');
                        d.innerHTML = `
                    
                        <br>
                        <div class="container shadow-lg" style="height: 100%;">
                            <br>
                            <p>
                                <img src="/static/profile_imgs/${resp[i].prof_img}" alt="" style="height:11%;width:11%;border-radius: 50%;">
                                <h3 style="margin-left: 18%;margin-top:-11%;margin-bottom: 5%;">${resp[i].uid}</h3>
                                <div style="margin-top:-15%;margin-left:70%" class="float-right">
                                    <button id="" class="btn btn-default"><a href="/dashboard/posts/edit/${resp[i].id}"><img src="/static/other_imgs/edit.png" alt="" style="height: 35%;width:35%;border-radius: 50%;"></a></button>
                                    <button onclick="del('${resp[i].id}');" id="${resp[i].id}" class="btn btn-default"><img src="/static/other_imgs/delete.png" alt="" style="height: 35%;width:35%;border-radius: 50%;"></button>
                                </div>
                            </p>
                            <hr>
                            <h2>${resp[i].title}</h2>
                            <div class="text-center">
                                <img src="/static/post_imgs/${resp[i].img}" alt="" style="height: 40%;width:90%;">
                            </div>
                            <br>
                            <h5 class="text-center">${resp[i].body}</h5>
                            <h6>created on ${resp[i].date}</h6>
                            <p> 
                                <h5 class="btn btn-info float-left">${resp[i].likes } Likes</h5>
                                <button name="${resp[i].id}" onclick="goto_like("${resp[i].id}")" class="btn btn-default float-right" style="margin-left: 65%;margin-top:-14%;"><img src="/static/other_imgs/love.png" alt="" style="height:40%;width:40%"></button>
                            </p>              
                            <br><br>
                            <a href="/dashboard/comment/${resp[i].id}">add a comment</a>
                            <br><br>

                        </div>
                        <br>`;
                        document.getElementById("main").appendChild(d);
                    }
                    else{
                        var d = document.createElement('div');
                        d.innerHTML = `
                    
                        <br>
                        <div class="container shadow-lg" style="height: 100%;">
                            <br>
                            <p>
                                <img src="/static/profile_imgs/${resp[i].prof_img}" alt="" style="height:11%;width:11%;border-radius: 50%;">
                                <h3 style="margin-left: 18%;margin-top:-11%;margin-bottom: 5%;">${resp[i].uid}</h3>
                                <div style="margin-top:-15%;margin-left:70%" class="float-right">
                                    <button id="" class="btn btn-default"><a href="/dashboard/posts/edit/${resp[i].id}"><img src="/static/other_imgs/edit.png" alt="" style="height: 35%;width:35%;border-radius: 50%;"></a></button>
                                    <button onclick="del('${resp[i].id}');" id="${resp[i].id}" class="btn btn-default"><img src="/static/other_imgs/delete.png" alt="" style="height: 35%;width:35%;border-radius: 50%;"></button>
                                </div>
                            </p>
                            <hr>
                            <h2>${resp[i].title}</h2>
                            <br>
                            <h5 class="text-center">${resp[i].body}</h5>
                            <h6>created on ${resp[i].date}</h6>
                            <p> 
                                <h5 class="btn btn-info float-left">${resp[i].likes } Likes</h5>
                                <button name="${resp[i].id}" onclick="goto_like("${resp[i].id}")" class="btn btn-default float-right" style="margin-left: 65%;margin-top:-14%;"><img src="/static/other_imgs/love.png" alt="" style="height:40%;width:40%"></button>
                            </p>              
                            <br><br>
                            <a href="/dashboard/comment/${resp[i].id}">add a comment</a>
                            <br><br>

                        </div>
                        <br>`;
                        document.getElementById("main").appendChild(d);
                    }
                }
                else{
                    if(resp[i].img){
                        var d = document.createElement('div');
                        d.innerHTML = `
                    
                        <br>
                        <div class="container shadow-lg" style="height: 100%;">
                            <br>
                            <p>
                                <img src="/static/profile_imgs/${resp[i].prof_img}" alt="" style="height:11%;width:11%;border-radius: 50%;">
                                <h3 style="margin-left: 18%;margin-top:-11%;margin-bottom: 5%;">${resp[i].uid}</h3>
                                <div style="margin-top:-15%;margin-left:70%" class="float-right">
                                    <button id="" class="btn btn-default"><a href="/dashboard/posts/edit/${resp[i].id}"><img src="/static/other_imgs/edit.png" alt="" style="height: 35%;width:35%;border-radius: 50%;"></a></button>
                                    <button onclick="del('${resp[i].id}');" id="${resp[i].id}" class="btn btn-default"><img src="/static/other_imgs/delete.png" alt="" style="height: 35%;width:35%;border-radius: 50%;"></button>
                                </div>
                            </p>
                            <hr>
                            <h2>${resp[i].title}</h2>
                            <div class="text-center">
                                <img src="/static/post_imgs/${resp[i].img}" alt="" style="height: 40%;width:90%;">
                            </div>
                            <br>
                            <h5 class="text-center">${resp[i].body}</h5>
                            <h6>created on ${resp[i].date}</h6>
                            <p> 
                                <h5 class="btn btn-info float-left">${resp[i].likes } Likes</h5>
                                <button name="${resp[i].id}" onclick="goto_dislike('${resp[i].id}');" class="btn btn-default float-right" style="margin-left: 65%;margin-top:-14%;"><img src="/static/other_imgs/unlove.png" alt="" style="height:40%;width:40%"></button>
                            </p>              
                            <br><br>
                            <a href="/dashboard/comment/${resp[i].id}">add a comment</a>
                            <br><br>
                        </div>
                        <br>        
                        
                        `;
                        document.getElementById("main").appendChild(d);
                    }
                    else{
                        var d = document.createElement('div');
                        d.innerHTML = `
                    
                        <br>
                        <div class="container shadow-lg" style="height: 100%;">
                            <br>
                            <p>
                                <img src="/static/profile_imgs/${resp[i].prof_img}" alt="" style="height:11%;width:11%;border-radius: 50%;">
                                <h3 style="margin-left: 18%;margin-top:-11%;margin-bottom: 5%;">${resp[i].uid}</h3>
                                <div style="margin-top:-15%;margin-left:70%" class="float-right">
                                    <button id="" class="btn btn-default"><a href="/dashboard/posts/edit/${resp[i].id}"><img src="/static/other_imgs/edit.png" alt="" style="height: 35%;width:35%;border-radius: 50%;"></a></button>
                                    <button onclick="del('${resp[i].id}');" id="${resp[i].id}" class="btn btn-default"><img src="/static/other_imgs/delete.png" alt="" style="height: 35%;width:35%;border-radius: 50%;"></button>
                                </div>
                            </p>
                            <hr>
                            <h2>${resp[i].title}</h2>
                            <br>
                            <h5 class="text-center">${resp[i].body}</h5>
                            <h6>created on ${resp[i].date}</h6>
                            <p> 
                                <h5 class="btn btn-info float-left">${resp[i].likes } Likes</h5>
                                <button name="${resp[i].id}" onclick="goto_dislike('${resp[i].id}');" class="btn btn-default float-right" style="margin-left: 65%;margin-top:-14%;"><img src="/static/other_imgs/unlove.png" alt="" style="height:40%;width:40%"></button>
                            </p>              
                            <br><br>
                            <a href="/dashboard/comment/${resp[i].id}">add a comment</a>
                            <br><br>
                        </div>
                        <br>        
                        
                        `;
                        document.getElementById("main").appendChild(d);
                        
                    }


                }    
            }
            var bt_div = document.createElement('div');
            bt_div.innerHTML = `
                <button class="float-left btn btn-info" id="view-m" onclick="get();">view More</button>
            `;
            document.getElementById("main").appendChild(bt_div);
        }
        else{
            var bt_div = document.createElement('div');
            bt_div.className = "text-center"
            bt_div.innerHTML = `
                <h4>posts completed</h4>
            `;
            document.getElementById("main").appendChild(bt_div);
        }

    }
    xhr.send();
}


function del(id){
    var conf = confirm("Do you Want To Delete This Post?");
    if(conf){
        xhr = new XMLHttpRequest();
        xhr.open("POST","/delete/"+id,true);
        xhr.onload = function(){
            console.log(xhr.responseText);
        }
        xhr.send();
        var el = document.getElementById(id);
        el.parentElement.parentElement.remove();
    }
}

function log(){
    // document.getElementById('head').innerHTML = "";
    var text = document.getElementById("filter").value;
    if(text!==""){
        document.getElementById('main-c').innerHTML = "<br><br>";
        document.getElementById('load').innerHTML = "Loading ...";
        xhr = new XMLHttpRequest();
        xhr.open("POST","/search/"+text,true);
        xhr.onload = function(){
            document.getElementById('load').innerHTML = "";
            var resp = JSON.parse(xhr.responseText);
            if(resp){
                console.log(resp.length);
                console.log(resp);
                var div = document.createElement('div');
                var html = "";
                for(var i=0;i<resp.length;i++){
                    html+=`
                        <a href="/dashboard/profiles/${resp[i].uid}" style="text-decoration:none">
                            <div class="container shadow-lg" style="border-radius:15px;width:40%;padding-top:1%">
                                <img src="/static/profile_imgs/${resp[i].prof_img}" alt="" class="float-left" style="height:13%;width:13%;border-radius: 50%;padding:2px;border:1px red dotted">
                                <div>
                                    <h4 style="margin-left:20%;">${resp[i].uid}</h4>
                                    <h6 style="margin-left:20%;">${resp[i].email}</h6>
                                </div>
                                <br>
                            </div>
                            <br>
                        </a>
                    `;
                }
                div.innerHTML = html;
                // document.getElementById('head').innerHTML+=text;
                document.getElementById('main-c').appendChild(div);
            }
            if(resp.length==0){
                document.getElementById('load').innerHTML = "no users found";
            }
        };
        xhr.send();
    }
}







function close(){
    console.log("closed");
    document.getElementById("flashed").parentElement.remove();
}





function goto_like(id){
    xhr = new XMLHttpRequest();
    xhr.open('POST','/like/'+id,true);
    xhr.send();
    var bt = document.getElementsByName(id)[0];
    bt.childNodes[0].attributes.src.nodeValue = "/static/other_imgs/unlove.png";
    bt.attributes.onclick.nodeValue = `goto_dislike(${id})`;
    var div = bt.parentElement;
    var tag_like = div.childNodes[23].innerHTML;
    var new_tag = (parseInt(tag_like.split(" ")[0])+1)+" likes";
    div.childNodes[23].innerHTML = new_tag;
}

function goto_dislike(id){
    xhr = new XMLHttpRequest();
    xhr.open('POST','/dislike/'+id,true);
    xhr.send();
    var bt = document.getElementsByName(id)[0];
    bt.childNodes[0].attributes.src.nodeValue = "/static/other_imgs/love.png";
    bt.attributes.onclick.nodeValue = `goto_like(${id})`;
    var div = bt.parentElement;
    var tag_like = div.childNodes[23].innerHTML;
    var new_tag = (parseInt(tag_like.split(" ")[0])-1)+" likes";
    div.childNodes[23].innerHTML = new_tag;
}


function comm_delete(id){
    var check = confirm('are you sure');
    if(check){
        document.getElementById(id).remove();
        xhr = new XMLHttpRequest();
        xhr.open('POST','/comm-delete/'+id,true);
        xhr.send();
    } 
}