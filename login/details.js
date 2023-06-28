const  chartData = {
    labels:["ToTal D'heures", "ToTal D'absence Justfie: ", "ToTAl D'absence Non Justfie"],
    data:[80,10,10],
};

const myChart= document.querySelector(".my-chart");

new Chart(myChart,{
    type:"doughnut",
    data:{
        labels: chartData.labels,
        datasets:[
            {
                label:"Heure",
                data:chartData.data,
            }
        ]
    }
});