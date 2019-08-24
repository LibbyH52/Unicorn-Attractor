$( document ).ready(function() {
    var endpoint = '/api/graphs/'
    var labels = []
    var count = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(data){
            bug_labels = data.bug_labels
            bug_count = data.bug_count

            feature_labels = data.feature_labels
            feature_count = data.feature_count

            var ctx = $("#myPieChart")[0].getContext('2d');
            var myPieChart = new Chart(ctx, {
                type: "pie",
                data: {
                    labels: bug_labels,
                    datasets: [
                        {
                            data: bug_count,
                            backgroundColor: ["#ff6e54", "#dd5182", "#955196"]
                        }
                    ]
                },
                options: {
                    legend: {
                        display: true,
                        position: 'left',
                        labels: {
                            fontColor: '#f1f1f1',
                            fontSize: 18,
                        }
                    }
                }
            });

            var ctx = $("#myPieChart2")[0].getContext('2d');
            var myPieChart = new Chart(ctx, {
                type: "pie",
                data: {
                    labels: feature_labels,
                    datasets: [
                        {
                            data: feature_count,
                            backgroundColor: ["#ff6e54", "#dd5182", "#955196"]
                        }
                    ]
                },
                options: {
                    legend: {
                        display: true,
                        position: 'left',
                        labels: {
                            fontColor: '#f1f1f1',
                            fontSize: 18,
                        }
                    }
                }
            });   
        },

        
        error: function(error_data){
            console.log('error')
            console.log(error_data)
        }
    })
});