              
var ctx = document.getElementById('myChart').getContext('2d');
chartData.datasets[0]["backgroundColor"]="Lightblue"
var myChart = new Chart(ctx, {
    type: 'bar',
    data: chartData,
    options: {
        maintainAspectRatio: false,
      plugins: {
        datalabels: {
          anchor: 'end',
          align: 'end',
          labels: {
            value: {
              color: 'Red',
            }
          }

        }
      }
    },
    
}); 



$(document).ready(function() {
  $("#test_ajax").click(function(e) {
    e.preventDefault();
    $.ajax({
      type: "GET",
      dataType: 'text',
      url: "/sales",
      success: function(res) {
       document.querySelector("#c2").innerHTML = '<canvas id="myChart2">  </canvas>';
       var ctx1 = document.getElementById('myChart2').getContext('2d');
       
       var myChart1 = new Chart(ctx1, {
                type: 'pie',
                data: JSON.parse(res),
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
       
          
      
      },
      error: function(res) {
        alert("error");
      }
    });
  });
});