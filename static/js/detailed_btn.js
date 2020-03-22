$(document).ready(function(){
    $(".show-more-report-btn").click(function(){
        $("#find-by-fives-detailed").fadeToggle("slow", function(){
            if($('#find-by-fives-detailed').css('display') == 'block'){
                $(".show-more-report-btn").html("Bağla");
            }
            else {
                $(".show-more-report-btn").html("Ətraflı");
            }
        });
    });
});