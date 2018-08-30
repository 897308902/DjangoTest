$(document).ready(function () {

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