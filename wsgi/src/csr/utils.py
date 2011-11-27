

from django.shortcuts import render, render_to_response
import simplejson
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound


def default_encoder(obj):
    return str(obj)

def render_ext(view_id, viewmap={}):
    def decorator(target):
        def inner(httpRequest, *args):
	    raw_result = target(httpRequest, *args);
	    ## special results
	    result = raw_result[0] 
	    if result == 'render':
	        data = raw_result[2] if len(raw_result) > 2 else {}
		data['view_id'] = view_id
		data['user'] = httpRequest.user if httpRequest.user.is_authenticated() else None
	        return render_to_response(raw_result[1], data)
	    if result == 'redirect':
	    	return HttpResponseRedirect(raw_result[1])
            if result == 'not-found':
                return HttpResponseNotFound("Not Found")
	    ##
	    result, resultData = raw_result 
	    rpath = httpRequest.path
	    extension = rpath.split("/")[-1].split(".")[-1]
	    if not extension:
	        extension = "html"	    
	    result_spec = viewmap.get(result)
	    if not result_spec:
	        raise Exception("result [%s] has not been specified" % result)	    
            resultData['user'] = httpRequest.user if httpRequest.user.is_authenticated() else None
	    if extension == "html":
	        template_location = result_spec.get('location')
		if not template_location:
		    raise Exception("attribute 'location' is required in viewmap for result of type %s" % extension)
	        resultData['view_id'] = view_id
		return render(httpRequest, template_location, resultData)
            if extension == "json":
	        resultData["result"] = result
	        return HttpResponse(simplejson.dumps(resultData, default=default_encoder), mimetype='application/json')	   
	   # resultMap['view_id'] = view_id
	    return resultData
	return inner
    return decorator




