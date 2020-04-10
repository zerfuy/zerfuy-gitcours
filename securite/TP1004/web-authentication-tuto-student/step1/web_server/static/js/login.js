console.log("login js loaded");

post_auth=function(){
    let uname=$('#iptusername')[0].value;
    let pwd=$('#iptpwd')[0].value;

    $.ajax({
        type: "POST",
        beforeSend: function(request) {
          request.setRequestHeader("Authority", 'test');
        },
        url: "/auth/login",
        data: {"username":uname, "password":pwd},

        success: function(msg) {
          console.log("Server answer... "+msg)
        }
      });
};



$('#btnsubmit').click(post_auth);