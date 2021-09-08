
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: chartData,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
}); 



$(document).ready(function() {
  $("#test_ajax").click(function(e) {
    e.preventDefault();
    $.ajax({
      type: "GET",
      dataType: 'text',
      url: "/sales",
      success: function(res) {
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