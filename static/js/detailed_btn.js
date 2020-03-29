$(document).ready(function(){
    $(".show-more-report-btn_5").click(function(){
        $("#find-by-fives-detailed").fadeToggle("slow", function(){
            if($('#find-by-fives-detailed').css('display') == 'block'){
                $(".show-more-report-btn_5").html("Bağla");
            }
            else {
                $(".show-more-report-btn_5").html("Ətraflı");
            }
        });
    });
    $(".show-more-report-btn_20").click(function(){
        $("#find-by-twenties-detailed").fadeToggle("slow", function(){
            if($('#find-by-twenties-detailed').css('display') == 'block'){
                $(".show-more-report-btn_20").html("Bağla");
            }
            else {
                $(".show-more-report-btn_20").html("Ətraflı");
            }
        });
    });
});