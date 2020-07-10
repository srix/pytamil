grammar புணர்ச்சி;

புணர்ச்சி: விதி (',' விதி)* ;

விதி: நிலைமொழி_மாற்றம் கூட்டல் வருமொழி_மாற்றம் ;

நிலைமொழி_மாற்றம்: நிலைமொழி மாற்றல் ;

// nilaimozhiexpression = nilaimozhi {filters} ;

// (* # any character except '|' or '+' *)
நிலைமொழி: [^|+]* ;
    

வருமொழி_மாற்றம்: {filters}* வருமொழி ;

// (* # any character except '|' *)
வருமொழி: [^,]* ;  
    
    
filters: 
    | '|' @:filter
    | @:filter '|'
    ;


filter: filtername param | filtername ;

param: '(' @:value ')' ;

filtername: 'உடம்படுமெய்' | 'இரட்டுதல்' | 'திரிதல்' | 'சும்மா' ;

// (* # any character except ')' *)
value: [^)]*; 

கூட்டல்: '+இயல்பு+' | '+' ;


// get right tamil word
// writes the grammar
// write listener
// replace புணர்ச்சிசெய்
