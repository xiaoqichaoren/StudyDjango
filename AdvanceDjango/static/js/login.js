$(function () {
    $("img").click(function () {
        $(this).attr("src", "/third/yanzheng/?t="+Date.now());
    });
});