$(function(){
	
	var timer=null;
	var num=0;
	
	
	//点击列表切换内容
	$(".ulist li").on("click",function(i,e){
		$(this).addClass("current").siblings("li").removeClass("current");
		$(".p_about").eq($(this).index()).css("display","block").siblings().css("display","none");
		
		//右上角的文字也要变换
		$(".dlnews label").text($(this).children("a").children("h3").text());
	})
	
	//第三栏，点击标题隐藏内容
	var f=true;
	$(".international").click(function(){
		if(f){
			$(".content").eq(0).hide();
			f=false;
		}else{
			$(".content").eq(0).show();
			f=true;
		}
	});
	var p=true;
	$(".partners").click(function(){
		if(p){
			$(".content").eq(1).hide();
			p=false;
		}else{
			$(".content").eq(1).show();
			p=true;
		}
	});
	
	//企业文化中的图片
	$(".culture li").each(function(i,e){
		$(this).children(".culicon").children("i").css("background-position","0 -"+($(this).index()*250)+"px");
	})
	.last().css({"border-bottom":"0","margin-bottom":"0"});
	
});

