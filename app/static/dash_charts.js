function dynamicColors() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgba(" + r + "," + g + "," + b + ", 0.5)";
}

function poolColors(a) {
    var pool = [];
    for(i = 0; i < a; i++) {
        pool.push(dynamicColors());
    }
    return pool;
}

function create_chart(chart_id,canvas_id,data,chart_type="bar",color=null){
    document.querySelector("#"+chart_id).innerHTML = '<canvas id='+canvas_id+'>  </canvas>';
       var ctx1 = document.getElementById(canvas_id).getContext('2d');
       if (chart_type=="pie"){
            data.datasets[0]["backgroundColor"]=poolColors(data.datasets[0].data.length);
       }
       else if (chart_type=="bar" && color!=null){
            data.datasets[0]["backgroundColor"] = color;
       }

       var myChart1 = new Chart(ctx1, {
                type: chart_type,
                data: data,
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
            }
        });
    return 1;
}



create_chart("c1","myChart",chartData,"bar","Lightblue");

function create_stacked_chart(chart_id,canvas_id,data,chart_type="bar",color=null){
    document.querySelector("#"+chart_id).innerHTML = '<canvas id='+canvas_id+'>  </canvas>';
        var ctx1 = document.getElementById(canvas_id).getContext('2d');
        var myChart1 = new Chart(ctx1,{
          type: 'bar',
          data: data,
          options: {
            plugins: {
              title: {
                display: true,
                text: 'Users Subscriptions'
              },
            },
            responsive: true,
            scales: {
              x: {
                stacked: true,
              },
              y: {
                stacked: true
              }
            }
          }
        });
}


$(document).ready(function() {
  $("#test_ajax").click(function(e) {
    e.preventDefault();
    $.ajax({
      type: "GET",
      dataType: 'text',
      url: "/users",
      success: function(res) {
       var res_data = JSON.parse(res);
        create_stacked_chart("c2","users",res_data["users"]);
        create_stacked_chart("c3","sub_type",res_data["sub_type"]);
      },
      error: function(res) {
        alert("error");
      }
    });
  });
});