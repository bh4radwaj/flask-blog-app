function goto_u_like(id){
    xhr = new XMLHttpRequest();
    xhr.open('POST','/like/'+id,true);
    xhr.send();
    var bt = document.getElementsByName(id)[0];
    bt.childNodes[0].attributes.src.nodeValue = "/static/other_imgs/unlove.png";
    bt.attributes.onclick.nodeValue = `goto_u_dislike(${id})`;
    var div = bt.parentElement;
    var tag_like = div.childNodes[21].innerHTML;
    var new_tag = (parseInt(tag_like.split(" ")[0])+1)+" likes";
    div.childNodes[21].innerHTML = new_tag;
}

function goto_u_dislike(id){
    xhr = new XMLHttpRequest();
    xhr.open('POST','/dislike/'+id,true);
    xhr.send();
    var bt = document.getElementsByName(id)[0];
    bt.childNodes[0].attributes.src.nodeValue = "/static/other_imgs/love.png";
    bt.attributes.onclick.nodeValue = `goto_u_like(${id})`;
    var div = bt.parentElement;
    var tag_like = div.childNodes[21].innerHTML;
    var new_tag = (parseInt(tag_like.split(" ")[0])-1)+" likes";
    div.childNodes[21].innerHTML = new_tag;
    console.log("dislike");
}



function users_get(){
    document.getElementById("view-m").remove();
    xhr = new XMLHttpRequest();
    xhr.open("POST","/viewmore_users",true);
    xhr.onload = function(){
        // console.log(xhr.responseText);
        var resp = JSON.parse(xhr.responseText);
        // console.log(resp);
        if(resp.length>0){
            console.log(resp);
            for(var i=0;i<resp.length;i++){
                if(resp[0].like_ok){
                    if(resp[i].img){
                        var d = document.createElement('div');
                        d.innerHTML = `
                    
                        <br>
                        <div class="container shadow-lg" style="height: 100%;">
                            <br>
                            <p>
                                <img src="/static/profile_imgs/${resp[i].prof_img}" alt="" style="height:11%;width:11%;border-radius: 50%;">
                                <h3 style="margin-left: 18%;margin-top:-11%;margin-bottom: 5%;">${resp[i].uid}</h3>
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
                                <button name="${resp[i].id}" onclick="goto_u_like('${resp[i].id}');" class="btn btn-default float-right" style="margin-left: 65%;margin-top:-14%;"><img src="/static/other_imgs/love.png" alt="" style="height:40%;width:40%"></button>
                            </p>              
                            <br><br>
                        </div>
                        <br>        
                        
                        `
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
                            </p>
                            <hr>
                            <h2>${resp[i].title}</h2>
                            <br>
                            <h5 class="text-center">${resp[i].body}</h5>
                            <h6>created on ${resp[i].date}</h6>
                            <p> 
                                <h5 class="btn btn-info float-left">${resp[i].likes } Likes</h5>
                                <button name="${resp[i].id}" onclick="goto_u_like('${resp[i].id}');" class="btn btn-default float-right" style="margin-left: 65%;margin-top:-14%;"><img src="/static/other_imgs/love.png" alt="" style="height:40%;width:40%"></button>
                            </p>              
                            <br><br>
                        </div>
                        <br>        
                        
                        `;
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
                                <button name="${resp[i].id}" onclick="goto_u_dislike('${resp[i].id}');" class="btn btn-default float-right" style="margin-left: 65%;margin-top:-14%;"><img src="/static/other_imgs/unlove.png" alt="" style="height:40%;width:40%"></button>
                            </p>              
                            <br><br>
                        </div>
                        <br>        
                        
                        `
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
                            </p>
                            <hr>
                            <h2>${resp[i].title}</h2>
                            <br>
                            <h5 class="text-center">${resp[i].body}</h5>
                            <h6>created on ${resp[i].date}</h6>
                            <p> 
                                <h5 class="btn btn-info float-left">${resp[i].likes } Likes</h5>
                                <button name="${resp[i].id}" onclick="goto_u_dislike('${resp[i].id}');" class="btn btn-default float-right" style="margin-left: 65%;margin-top:-14%;"><img src="/static/other_imgs/unlove.png" alt="" style="height:40%;width:40%"></button>
                            </p>              
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
                <button class="float-left btn btn-info" id="view-m" onclick="users_get();">view More</button>
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
    };
    xhr.send();
}
