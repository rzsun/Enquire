var numPos = 0;
var numNeg = 0;
var areaChartData = [];
areaChartData[0] = ['Time', 'Positive', 'Negative'];
var scatterChartData = [];
scatterChartData[0] = ['Polarity', 'Followers'];

for (i = 0; i < tweets.length; i++) {
	if (tweets[i].sent == "pos") {
	    numPos++;
	}
	if (tweets[i].sent == "neg") {
	    numNeg++;
	}
	areaChartData[i + 1] = [tweets[i].time, tweets[i].posindex, tweets[i].negindex];
	scatterChartData[i + 1] = [(tweets[i].posindex - tweets[i].negindex), tweets[i].followercount];
}

function drawPieChart() {
    var data = google.visualization.arrayToDataTable([
        ['Sentiment', 'Number'],
        ['Negative', numNeg],
        ['Postive', numPos]
    ]);
    var options = {
        title: 'Overall Sentiment',
        backgroundColor: '#F0F0F0',
        colors: ['#FE7569', '#00CC33']
    };
    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
}

function drawAreaChart() {
    var data = google.visualization.arrayToDataTable(areaChartData);
    var options = {
        title: 'Sentiment Across Time',
        hAxis: {title: 'Time', titleTextStyle: {color: '#333'}, textPosition: 'none'},
        vAxis: {minValue: 0},
        backgroundColor: '#F0F0F0',
        colors: ['#00CC33', '#FE7569'],
    };
    var chart = new google.visualization.AreaChart(document.getElementById('areachart'));
    chart.draw(data, options);
}

function drawScatterChart() {
    var data = google.visualization.arrayToDataTable(scatterChartData);

    var options = {
        title: 'Polarity vs. Followers',
        hAxis: {
        	title: 'Polarity',
        	minValue: 0,
        	maxValue: 1,
        	gridlines: {count : 0}
        },
        vAxis: {
		    title: 'Followers', 
		    minValue: 0, 
		    maxValue: 30000,
		    gridlines: {count : 0},
		    logScale: true
        },
        legend: 'none',
        backgroundColor: '#F0F0F0',
        pointSize: 3,
        colors: ['#3399FF'],
    };

    var chart = new google.visualization.ScatterChart(document.getElementById('scatterchart'));
    chart.draw(data, options);
}

google.load("visualization", "1", {packages: ["corechart"]});
google.setOnLoadCallback(drawScatterChart);
google.setOnLoadCallback(drawPieChart);
google.setOnLoadCallback(drawAreaChart);
