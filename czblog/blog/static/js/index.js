$(document).ready(function () {
    // 默认选中第一个
    $("#navs").children().eq(0).addClass("active").siblings("li").removeClass("active");


	// $("#navs>li").on("click",function(){
    //
	// 	$(this).addClass("active").siblings("li").removeClass("active");
	// });

});