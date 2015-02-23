
%%module dgtal

%%{
% for i in includes :
#include "${i}"
% endfor
%%}

% for i in includes :
%%include "${i}"
% endfor

% for t in templates :
%%template (${t['instanceName']}) ${t['instance']};
% endfor
