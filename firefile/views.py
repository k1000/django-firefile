# -*- coding: utf-8 -*-
import base64
from urlparse import urlparse

from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

version = "0.8.3";

def _get_file_path( url ):
    return "%s%s"% ( settings.PROJECT_PATH, urlparse(url).path )
    
def saveFile(uri, contents):
    try:
        f = open( _get_file_path(uri) , 'w')
        f.write(contents)
        f.close()
        return True
    except:
        return False

@staff_member_required
def get_respond(request):
    if request.method == "POST":
        action = request.POST.get("action", False)
        if action:
            result = authorizeAction(request);
            
            if not request.FILES : return endError("no_file_specified")
            sfile = base64.b64decode(request.FILES['file'])
            if substr(sfile, -4) != ".css": return endError("invalid_file_extension")

            # CHECK STYLESHEET DATA
            stylesheet =  request.POST.get("stylesheet", False)
            if not stylesheet: return endError("no_stylesheet_attached")
            if len(stylesheet) < 10: return endError("stylesheet_too_short")

            # DECODE
            stylesheet_content = base64.b64decode(stylesheet);
            if not saveFile(_get_file_path( url ), stylesheet_content): return endError("save_error")
                
            index = request.POST("index", "")
            response = """<?xml version='1.0' encoding='ISO-8859-1'?> 
            <firefilestatus success='true' msg='FilesSuccessfullySaved' styleindex='%s' />""" % index
            
            return HttpResponse(response)
            
    return HttpResponse("<h1>Firefile</h1>")



def endError( index ):
    return HttpResponse( """<?xml version='1.0' encoding='ISO-8859-1'?>
    <firefilestatus success='false' msg='FileErrors' styleindex='%s' />""" % index )

