%module dgtal

%feature("flatnested");

%{
#include "/home/florent/projet/DGtal/src/DGtal/arithmetic/LighterSternBrocot.h"
using namespace DGtal;
%}

%include "/home/florent/projet/DGtal/src/DGtal/arithmetic/LighterSternBrocot.h"

%template (LightSternBrocot) DGtal::LighterSternBrocot<int,int>;
%rename (Fraction) LightSternBrocot::Fraction;
%rename (Node) LightSternBrocot::Node;
