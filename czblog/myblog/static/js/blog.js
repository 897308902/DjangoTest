$(document).ready(function () {
    // 默认选中第一个
    // $("#navs").children().eq(1).addClass("active").siblings("li").removeClass("active");


	// $("#navs>li").on("click",function(){
    //
	// 	$(this).addClass("active").siblings("li").removeClass("active");
	// });
    // 我的博客，分页
    $('#pageBtn').click(function () {
        var nu = $("#gotoPage").val();
        console.log(nu);
        if (nu<1){
            nu=1
        }
        $(this).attr('href','?page='+nu);

    });
});