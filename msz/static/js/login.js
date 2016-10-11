/**
 * Created by Administrator on 2015/11/19.
 */
$(function () {
    // $("input[type='text'], input[type='password']").keyup(function () {
    //     var _this = $(this);
    //     _this.parents("td").find(".error").html("");
    // });
    $("body").on("submit", '#form_login', function (e) {
        e.preventDefault();
        var form = $(this);
        var _userName = $.trim($("#id_username").val());
        var _passWord = $.trim($("#id_password").val());
        var _nextUrl = window.location.search.replace(/^\?next=/, '');
        var params = form.serializeArray();

        var userError = $("#error_username");
        var passError = $("#error_password");
        var _this = $(this);

        if (_this.hasClass("posting")) {
            return false;
        }
        if (_userName == "") {
            userError.html("请输入用户名！");
            return false;
        }
        if (_passWord == '') {
            passError.html("请输入密码！");
            return false;
        }
        _this.addClass("posting");
        params.push({name: 'next', value: _nextUrl});
        $.ajax({
            url: "/accounts/login/",
            data: params,
            dataType: "json",
            type: "POST",
            success: function (resp) {
                if (resp.state) {
                    window.location.href = resp.redirect_url;
                } else {
                    _this.removeClass("posting");
                    var error = resp.error;
                    for (var name in error) {
                        $("#error_" + name).html(error[name][0]);
                    }
                }
            },
            error: function (err) {
                if (err.status == 403){
                    _this.removeClass("posting");
                    alert("您已登录了");
                } else if (err.statusText !== 'abort') {
                    _this.removeClass("posting");
                    alert("系统错误");
                }
            }
        })
    });
});

