

def render_ext(view_id):
    def decorator(target):
        def decorator_logic(*args, **kwargs):
	    resultMap = target(args, kwargs)
	    resultMap['view_id'] = view_id
	    return resultMap
	return decorator_logic
    return decorator




