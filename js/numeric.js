var spins = document.getElementsByClassName("spin");
for (var i = 0, len = spins.length; i < len; i++) {
    var spin = spins[i],
        span = spin.getElementsByTagName("span"),
        input = spin.getElementsByTagName("input")[0];
    
    input.onchange = function() { input.value = +input.value || 0; };
    span[0].onclick = function() { input.value = Math.max(0, input.value - 1); };
    span[1].onclick = function() { input.value -= -1; };
}