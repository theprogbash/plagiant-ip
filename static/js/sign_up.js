$(document).ready(function(){
    $("#university_name option[selected]").html("Universitet").attr("disabled", "disabled");
    $("#university_name").css("color", "#9B9B9B");
    $("#password").attr("type", "password");

    $('#id_isPhysicalAccount').click(function(){
        if($(this).prop("checked") == true){
            $("#university_name").css("display", "none");
        }
        else{
            $("#university_name").css("display", "block");
        }
    });
});
