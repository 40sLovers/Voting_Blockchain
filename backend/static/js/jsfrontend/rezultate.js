// Chart.js
var chart = document.getElementById('chart_voturi').getContext('2d');

// Luam date
let vot_itemi;
async function luam_date()
{
    vot_itemi = await fetch("http://127.0.0.1:5000/getPoolResults?pool_id=123&order_by=a");
    vot_itemi = await vot_itemi.json();
}
luam_date();


// Creare tabel
/*
    Aici sunt valori PLACEHOLDER
    Este doar o simulare pentru afisarea rezultatelor
    Datele trebuie luate din backend

    (Momentan datele sunt stocate intr-o lista de dictionare. Nu stiu cum vor fi memorate in final...)
*/


let votesChart = new Chart(chart, {
    type:'bar',
    data:{
        labels:[],
        datasets:[{
            label:'Voturi',
            data:[],

            backgroundColor: [
                'rgba(89, 133, 255, 0.5)',
                'rgba(255, 89, 133, 0.5)',
            ],
        }],
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Rezultatele votului',
                font:{size:18},
                padding:{top:30, bottom:20},
                color:'#182552'
            },
            legend:{
                display:false
            }
        }
    }
})

// Calcule pentru voturi
async function calcul_nr_total_voturi()
{
    var nrTotalVoturi = 
    vot_itemi.map((el)=> Object.values(el)[0])
    .reduce((prev,curr)=>prev+curr,0);
    document.getElementById("nrTotalVoturi").innerText = String(nrTotalVoturi);
}

async function calcul_castigatori()
{
    var nrMaximVoturi = -1;
    var castigatori = "";
    nrMaximVoturi = Math.max(...vot_itemi.map((el)=>Object.values(el)[0]))

    castigatori = 
    vot_itemi.filter((el)=> Object.values(el)[0] == nrMaximVoturi)
    .map((el)=>Object.keys(el)[0])
    document.getElementById("castigatori").innerText = String(castigatori);
}

// Updatarea tabelului
async function updatare_tabel()
{
    console.log(vot_itemi)
    votesChart["data"]["labels"]= vot_itemi.map((el)=>Object.keys(el)[0])
    votesChart["data"]["datasets"][0]["data"]=vot_itemi.map((el)=>Object.values(el)[0])
    votesChart.update();
}

// Functie
async function javascript_chart()
{
    // Luam date
    await luam_date();

    // Updatare tabel
    updatare_tabel();

    // Calcularea voturilor;
    calcul_nr_total_voturi();
    calcul_castigatori();
}

javascript_chart();
setInterval(javascript_chart, 2000);