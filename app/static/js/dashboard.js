// Career Readiness

const readinessChart=document.getElementById("readinessChart");

if(readinessChart){

new Chart(readinessChart,{

type:"doughnut",

data:{

labels:["Completed","Remaining"],

datasets:[{

data:[readiness,100-readiness],

backgroundColor:[

"#2563EB",

"#E5E7EB"

],

borderWidth:0

}]

},

options:{

responsive:true,

plugins:{

legend:{

position:"bottom"

}

}

}

});

}

// Skills

const skillsChart=document.getElementById("skillsChart");

if(skillsChart){

new Chart(skillsChart,{

type:"bar",

data:{

labels:["Matched","Missing"],

datasets:[{

data:[matched,missing],

backgroundColor:[

"#22C55E",

"#EF4444"

]

}]

},

options:{

responsive:true,

plugins:{

legend:{

display:false

}

},

scales:{

y:{

beginAtZero:true

}

}

}

});

}