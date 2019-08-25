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

            upvote_labels = data.upvote_labels
            upvote_count = data.upvote_count
            
            view_labels = data.view_labels
            view_count = data.view_count

            var ctx = $("#myPieChart")[0].getContext('2d');
            var myPieChart = new Chart(ctx, {
                type: "pie",
                data: {
                    labels: bug_labels,
                    datasets: [
                        {
                            data: bug_count,
                            backgroundColor: ["#bad0af", "#f0b8b8", "#83af70"]
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
                            backgroundColor: ["#bad0af", "#f0b8b8", "#83af70"]
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
            
            var ctx = $('#myBarChart')[0].getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: upvote_labels,
                    datasets: [{
                        label: '# of Votes',
                        data: upvote_count,
                        backgroundColor: [
                            '#488f31',
                            '#f0b8b8',
                            '#83af70',
                            '#e67f83',
                            '#bad0af',
                        ],
                    }]
                },
                options: {
                    legend: {
                        labels: {
                            fontColor: '#f1f1f1'
                        }
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                fontColor: '#f1f1f1',
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                fontColor: '#f1f1f1',
                            }
                        }]
                    },
                }
            }); 

            var ctx = $('#myBarChart2')[0].getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: view_labels,
                    datasets: [{
                        label: '# of Views',
                        data: view_count,
                        backgroundColor: [
                            '#488f31',
                            '#f0b8b8',
                            '#83af70',
                            '#e67f83',
                            '#bad0af',
                        ],
                    }]
                },
                options: {
                    legend: {
                        labels: {
                            fontColor: '#f1f1f1'
                        }
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                fontColor: '#f1f1f1',
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                fontColor: '#f1f1f1',
                            }
                        }]
                    },

                }
            }); 
        },

        
        error: function(error_data){
            console.log('error')
            console.log(error_data)
        }
    })
});