
$(document).ready(function(){

        var $loginDialog = $("#content-inner").append("<div>").find("div").dialog("hide");

	$("#login-status").on('click', function(event){
	   $.get("/accounts/login/", function(result){
	        
		var $form = $(result).find("form");
		$loginDialog.clear().append($form).dialog('show');
		
		$form.on('submit', function(evt){

		    evt.preventDefault();
		    
		    var url = '/accounts/login/.json';
		    var fieldsData = $form.serialize();
		    var callback =  function(json, status) {
		        if( json['result'] == 'success' ){
			    $("#login-status").text(json['username']);
			    $("#logout-link").css({'visibility':'visible'});
			    $loginDialog.dialog('hide');
			}
		    };

		    $.ajax({
  			url: url,
  			dataType: 'json',
  			data: fieldsData,
  			success: callback,
			type: 'POST'
		    });
              });
	   });
	   event.preventDefault();
	});
});
