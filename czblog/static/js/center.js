$(function () {
    // 显示弹框
    $('#information').click(function () {
        $("#other_info").css('display', 'block')
    });
    // 关闭弹框
    $("#cls").click(function () {
        $("#other_info").css('display', 'none')
    });
});
