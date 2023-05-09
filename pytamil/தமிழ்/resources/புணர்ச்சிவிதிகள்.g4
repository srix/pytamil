grammar புணர்ச்சிவிதிகள்;

புணர்ச்சிவிதிகள்: விதி (',' விதி)* ;

விதி: நிலைமொழி_மாற்றம்  கூட்டல்  வருமொழி_மாற்றம் ;

நிலைமொழி_மாற்றம்: 'நிலைமொழி' filters*;

வருமொழி_மாற்றம்: filters* 'வருமொழி' ;
    
    
filters
        :  '|' fil 
        | fil  '|' ;


fil: filtername param  ;

param: '(' value ')' ;

filtername: 'உடம்படுமெய்' | 'இரட்டுதல்' | 'திரிதல்' | 'சும்மா' ;

// (* # any character except ')' *)
// VALUE: '~')'+'; 
// VALUE: 'வ்'+; 
value:( 'வ்' | 'ய்')+; 
// value: .+?; 


கூட்டல் :  '+' ;


// get right tamil word
// writes the grammar
// write listener`
// replace புணர்ச்சிசெய்
