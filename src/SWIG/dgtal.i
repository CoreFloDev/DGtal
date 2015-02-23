%module dgtal

%feature("flatnested");

%{
#include "../DGtal/arithmetic/LighterSternBrocot.h"
%}

%include "../DGtal/arithmetic/LighterSternBrocot.h"

%template (LightSternBrocot) DGtal::LighterSternBrocot<int,int>;
%rename (Fraction) LightSternBrocot::Fraction;
%rename (Node) LightSternBrocot::Node;
