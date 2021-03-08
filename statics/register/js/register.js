$(function () {
    var check_username;
    var check_email;
    var check_password1;
    var check_password2;

    $("input[name='username']").blur(function () {
        var username = $("#inpuUsername").val();
        var u = $("#username_span");
        u.empty();
        if (username == "") {
            u.append('用户名不能为空！');
            check_username = false;
            return false;
        }
        if (username != '') {
            var reg = /^[^\d]*$/;
            isok = reg.test(username);
            if (!isok) {
                u.append('用户名不能包括数字！');
                check_username = false;
                return false;
            }
        }
        if (username.length < 3 || username.length > 8) {
            u.append('用户名必须在 3 - 8 为之间！');
            check_username = false;
            return false;
        }
        check_username = true
    });


    $("#inputEmail3").blur(function () {
        var email = $("#inputEmail3").val();
        var e = $("#email_span");
        e.empty();
        if (email == '') {
            e.append("请输入您的邮箱!");
            check_email = false;
            return false;
        } else if (email != "") {
            var reg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
            isok = reg.test(email);
            if (!isok) {
                e.append("邮箱格式不正确，请重新输入！")
                check_email = false;
                return false;
            }
        }
        check_email = true;
    });


    $("#inputPassword3").blur(function () {
        var password1 = $("#inputPassword3").val();
        console.log(password1);
        var p1 = $("#password1_span");
        p1.empty();
        if (password1 == '') {
            p1.append("请输入密码!");
            check_password1 = false;
            return false;
        }

        // if (password1.getBytes().length != password1.length()) {
        //     p1.append("密码不能含有中文");
        // }

        if (password1.length < 6 || password1.length > 64) {
            p1.append('密码必须在 6 - 64 为之间！');
            check_password1 = false;
            return false;
        }
        check_password1 = true;
    });

    $("#inputPassword4").blur(function () {
        var password1 = $("#inputPassword3").val();
        var password2 = $("#inputPassword4").val();
        var p2 = $("#password2_span");

        p2.empty();
        if (password1 != password2) {
            p2.append("两次密码输入不一致，请重新输入！");
            check_password2 = false;
            return false;
        }
        check_password2 = true;
    });

    $("#but").click(function () {
        if (check_username && check_email && check_password1 && check_password2) {
            var username = $("#inpuUsername").val();
            var email = $("#inputEmail3").val();
            var password = $("#inputPassword3").val();

            var countdown = 30;
            settime(countdown, this);
            $.ajax({
                type: "post",
                url: "/register/",
                data: {
                    'username': username,
                    'email': email,
                    'password': password
                },
                dataType: "json",
                success: function (data) {
                    if (data['code'] == '200') {
                        swal("已向您的邮箱发送激活链接！", "注意查收,请在五分钟内激活!", "success", {
                            button: "Aww yiss!",
                        });
                    } else {
                        swal("邮件发送失败!", '请保持网络畅通', 'warning');
                    }
                }
            });
        } else {
            swal('表单信息不完整!', "", "error")
        }

    });
})

function settime(countdown, val) {
    console.log(val)
    if (countdown == 0) {
        var username = $("#inpuUsername").val();
        var email = $("#inputEmail3").val();
        var password1 = $("#inputPassword3").val();

        val.removeAttribute("disabled");
        val.innerText = "立刻注册";
        countdown = 60;
    } else {
        val.setAttribute("disabled", true);
        console.log(countdown)
        val.innerText = "重新发送(" + countdown + ")";
        countdown--;
        setTimeout(function () {
            settime(countdown, val)
        }, 1000)
    }
}