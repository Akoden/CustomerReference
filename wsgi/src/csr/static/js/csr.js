$(document).ready(function(){

        var $loginForm;
	$("#login-status").on('click', function(event){
	   $.get("/accounts/login/", function(result){
	        
		var $form = $(result).find("form");
		var $dlg = $("#content-inner").append("<div>").find("div").append($form);
		
		$dlg.dialog();
		
		$form.on('submit', function(evt){
		    evt.preventDefault();
		    $form.attr('action', '/accounts/login/?ajax=true').ajaxSubmit(function(response, status) {
		    	var content = $(response);
			if( !content.find('form').length ){
			    $dlg.close();
			}
		    });
		});

		// $("<div>").wrapInner(form).dialog().appendTo("#content-inner");
	   });
	   event.preventDefault();
	});
});
