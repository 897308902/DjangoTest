$(document).ready(function() {
	//弹出登录对话框
	$("#login_link").click(function() {
		$("#mask").css("display", "block");
	});

	$("#login").click(function() {
		$("#mask").css("display", "none");
	});

	//<!--固定搜索栏-->
	var tops = 0;
	var f_tops=$("#fixd_search").offset().top;
	var le=$("#fixd_search").offset().left;
	
//	$(window).scroll(function() {
//
//		tops = $(document).scrollTop();
//
//		if(tops >= f_tops) {
//			$("#fixd_search").addClass("fixd");
//			$("#fixd_search").css("left",le);
//			//防止跳动
//			$(".menu").css("margin-top",100);
//		} else {
//			$("#fixd_search").removeClass("fixd");
//			$(".menu").css("margin-top",0);
//		}
//	});

	//关闭长图
	$("#close_btn").click(function() {
		$("#topbanner").css("display", "none");
	});
	
	//轮播图的
	$("#slider").mouseenter(function(){
		//鼠标经过图片时,左右按钮显示,离开时还是要隐藏
		$("#arrow").css("display","block");
	})
	$("#slider").mouseleave(function(){
		//鼠标经过图片时,左右按钮显示,离开时还是要隐藏
		$("#arrow").css("display","none");
	})
	$("#circle li").first().addClass("current");
	
	$("#circle li").mouseenter(function(){
		$(this).eq($(this).index()).addClass("current").siblings("li").removeClass("current");
		$("#slider_pic").attr("src","static/img/slider"+($(this).index()+1)+".jpg");
	})
	//右侧部分12个图标
	
	$("#pic12 i").each(function(i,e){
		$(this).css("background-position","0 "+(-25*i)+"px");
	});
	
	$("#pic12  li").mouseenter(function(){
		$(this).children("a").children("i").css("background-position","right "+(-25*$(this).index())+"px");
	});
	$("#pic12  li").mouseleave(function(){
		$(this).children("a").children("i").css("background-position","0 "+(-25*$(this).index())+"px");
	});
});
