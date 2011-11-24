$(document).ready(function(){

        var $loginForm;
	$("#login-status").on('click', function(event){
	   $.get("/accounts/login/", function(result){
	        
		var $form = $(result).find("form");
		var $dlg = $("#content-inner").append("<div>").find("div").append($form);
		
		$dlg.dialog();
		
		$form.on('submit', function(evt){

		    evt.preventDefault();
		    
		    var url = '/accounts/login/?ajax=true';
		    var fieldsData = $form.serialize();
		    var callback =  function(json, status) {
		        if( json['result'] == 'success' ){
			    $("#login-status").text(json['username']);
			    $dlg.dialog('close');
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
