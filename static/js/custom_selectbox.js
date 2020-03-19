$(document).ready(function(){
    $("#university option[selected]").html("Universitet").attr("disabled", "disabled");
    $("#university").css("color", "#9B9B9B");
    $("#password").attr("type", "password");

    $('#id_isPhysicalAccount').click(function(){
        if($(this).prop("checked") == true){
            $("#university").css("display", "none");
        }
        else{
            $("#university").css("display", "block");
        }
    });
});
