$(function () {

    var timer = null;
    var num = 0;

    ////////////轮播图开始/////////////////

    var ol = $("<ol></ol>");
    //先遍历一次给所有li添加背景图片
    $(".ban ul>li").each(function (i, e) {
        ol.append($("<li></li>"));
    });

    $(".ban").append(ol);

    //确定小圆点的位置
    var olen = $(".ban ol").width();
    $(".ban ol").css("margin-left", "-" + olen / 2 + "px");
    console.log(olen);

    //自动轮播
    timer = setInterval(bannertimer, 5000);

    //鼠标停留在图片上时,暂停播放；离开时继续
    $(".clul>li").on("mouseenter", function () {
        clearInterval(timer);
    })
        .on("mouseleave", function () {
            clearInterval(timer);
            timer = setInterval(bannertimer, 5000);
        });

    //默认选中第一个ol li
    $(".ban ol>li").eq(0).addClass("current");

    //点击小圆点切换图片
    $(".ban ol>li").on("click", function () {

        $(this).addClass("current").siblings("li").removeClass("current");
        $(".ban ul>li").eq($(this).index()).fadeIn().siblings().fadeOut();

        //获取当前选中的圆点索引值，然后继续从该位置开始轮播
        var cls = $(".ban ol>li.current").index();
//		console.log(cls);
        num = cls;
    });

    function bannertimer() {
        num++;
        if (num > ($(".ban ul>li").length - 1)) {
            num = 0;
        }
        $(".ban ul>li").eq(num).fadeIn(250).siblings().fadeOut(250);
        $(".ban ol>li").eq(num).addClass("current").siblings("li").removeClass("current");
    }

    ////////////轮播图结束/////////////////

});
