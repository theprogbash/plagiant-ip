$(document).ready(function(){
    $('#physical_Account').click(function(){
        if($(this).prop("checked") == true){
            $("#university_name").css("display", "none");
        }
        else{
            $("#university_name").css("display", "block");
        }
    });
});