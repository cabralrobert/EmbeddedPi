$(function() {
        var $document = $(document);
        var selector = '[data-rangeslider]';
        var $element = $(selector);

        var textContent = ('textContent' in document) ? 'textContent' : 'innerText';
        
        function valueOutput(element) {
            var value = element.value;
            var output = element.parentNode.getElementsByTagName('output')[0] || element.parentNode.parentNode.getElementsByTagName('output')[0];
            output[textContent] = value;
        }
        $document.on('input', 'input[type="range"], ' + selector, function(e) {
            valueOutput(e.target);
        });
        
        $document
            .on('click', '#js-example-hidden button[data-behaviour="toggle"]', function(e) {
                var $container = $(e.target.previousElementSibling);
                $container.toggle();
            });
        
        $element.rangeslider({
        
            polyfill: false,
        
            onInit: function() {
                valueOutput(this.$element[0]);
            }
        });
    });

    function test(){
    	var $document = $(document);
        var selector = '[data-rangeslider]';
        var $element = $(selector);        

        var temp = $("#testeee").val();


        var selectedVal = "";
		var selected = $("#radioDiv input[type='radio']:checked");
		if (selected.length > 0) {
		    selectedVal = selected.val();
		}

		$.ajax( {
               method: 'POST',
               url: 'ar.php',
               dataType: 'json',
               data: {temp:temp,
               		  velo:selectedVal,
               		  swing:'n',
                    poweroff: "-1"},

               success: function(result) {
                   console.log(result);
               },
               error: function(result){
                   console.log(result);
               }
        });	

    }

    function processForm(){
    	var x=$("#switch-shadow").is(":checked");

    	$.ajax( {
               method: 'POST',
               url: 'ar.php',
               dataType: 'json',
               data: {temp:0,
               		  velo:0,
               		  swing:x,
                    poweroff: "-1"},

               success: function(result) {
                   console.log(result);
               },
               error: function(result){
                   console.log(result);
               }
        });	


    }

    function poweroff(){

    $.ajax( {
               method: 'POST',
               url: 'ar.php',
               dataType: 'json',
               data: {temp:0,
                    velo:0,
                    swing:"n",
                    poweroff: "1"},

               success: function(result) {
                   console.log(result);
               },
               error: function(result){
                   console.log(result);
               }
           });

}

