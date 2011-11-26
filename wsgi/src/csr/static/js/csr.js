/* ******************************************************************
 * This is the main js script file for the CustomerReference project
 * Use jQuery API
 * Author : theo@akoden.com
 * ************************ ****************************************/

$(document).ready(function(){
        
    var $loginDialog;
    
    $("#login-status").on('click', function(event){
	
	$.get("/accounts/login/", function(result){


	    if($loginDialog != null){
		$loginDialog.dialog('close');
		$loginDialog = null;
	    }

	    $loginDialog = $("#content-inner").append("<div>").find("div").dialog();
	    
	    var $form = $(result).find("form");
	    $loginDialog.append($form);
	    
	    $form.on('submit', function(evt){

		evt.preventDefault();
		
		var url = '/accounts/login/.json';
		var fieldsData = $form.serialize();
		var callback =  function(json, status) {
		    if( json['result'] == 'success' ){
			$("#login-status").text(json['username']);
			$("#logout-link").css({'visibility':'visible'});
			$loginDialog.dialog('close');
			$loginDialog = null;
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

