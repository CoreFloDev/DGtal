#!/usr/bin/python2
#This will be the python script generating the SWIG interfaces
# vim: set fileencoding=utf-8

# This script requires the following packages :
# * libclang-3.6-dev
# * python-clang-3.6

import clang.cindex
import sys
import os
import pprint
import traceback
from mako.template import Template

LIB_CLANG = '/usr/lib/llvm-3.6/lib/libclang.so'
MAKO_PATH = 'swig.mako'
OUTPUT_FILE = 'src/SWIG/dgtal_output.i'
SOURCE_PATH = 'src/DGtal/arithmetic/LighterSternBrocot.h'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# function to parse AST
def traverse(node,parent,filename):

    ret = {}

    try:
        # do compute here
        if node.location.file.name == filename:

            # All templates
            if node.kind == CK.CLASS_TEMPLATE:
                parameterOfTemplate = [] 
                for child in node.get_children():
                    if child.kind in [CK.TEMPLATE_TYPE_PARAMETER,CK.TEMPLATE_TEMPLATE_PARAMETER,CK.TEMPLATE_NON_TYPE_PARAMETER]:
                        parameterOfTemplate.append(child.displayname)
                ret[node.spelling] = parameterOfTemplate

    except:
        pass

    for child_node in node.get_children():
        trav = traverse(child_node,node,filename)
        ret = dict(ret.items() + trav.items())
        
    return ret
#end traverse


# load Clang
clang.cindex.Config.set_library_file(LIB_CLANG)
index = clang.cindex.Index.create()

allowedExt = ['.h','.cpp','.ih']
CK = clang.cindex.CursorKind


types = {"TInteger"  : {"Type":"int","Renommage":"i64"},
         "TQuotient" : {"Type":"int","Renommage":"i64"}}


print bcolors.OKGREEN+"--- Starting swig generation ---"+bcolors.ENDC

# test with only one source
translation_unit = index.parse(SOURCE_PATH, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])
templateFound = traverse(translation_unit.cursor,None,SOURCE_PATH)
templates = []
includes = [SOURCE_PATH]


# generate template name and template instance
for t in templateFound:
    instance = t+"<"
    instanceName = t
    parameters = templateFound[t]
    for p in parameters:
    
        if instanceName != t:
            instance = instance+","
        instance = instance + types[p]["Type"]
        instanceName = instanceName + types[p]["Renommage"]

        # if the type require include, we add them
        if types[p].has_key("requireInclude"):
            for i in types[p]["requireInclude"]:
                if i not in includes:
                    includes.append(i)

    instance = instance + ">"
    templates.append({"instance":instance,"instanceName":instanceName})

# generate the swig interface
tpl = Template(filename=MAKO_PATH)
output = tpl.render(templates=templates,
                    includes=includes)
print output

 
f = open(OUTPUT_FILE,'w')
f.write(output)
f.close()
