var numPos = 0;
var numNeg = 0;
var areaChartData = [];
areaChartData[0] = ['Time', 'Positive', 'Negative'];
var scatterChartData = [];
scatterChartData[0] = ['Polarity', 'Followers'];

var scatterChartData2 = [];
scatterChartData2[0] = ['Polarity', 'Retweets'];

var scatterChartData3 = [];
scatterChartData3[0] = ['Polarity', 'Favorites'];

for (i = 0; i < tweets.length; i++) {
	if (tweets[i].sent == "pos") {
	    numPos++;
	}
	if (tweets[i].sent == "neg") {
	    numNeg++;
	}
	areaChartData[i + 1] = [tweets[i].time, parseFloat(tweets[i].posindex.toFixed(2)), parseFloat(tweets[i].negindex.toFixed(2))];
	scatterChartData[i + 1] = [parseFloat((tweets[i].posindex - tweets[i].negindex).toFixed(2)), tweets[i].followercount];
	scatterChartData2[i + 1] = [parseFloat((tweets[i].posindex - tweets[i].negindex).toFixed(2)), tweets[i].retweetcount];
	scatterChartData3[i + 1] = [parseFloat((tweets[i].posindex - tweets[i].negindex).toFixed(2)), tweets[i].favoritecount];
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
    console.log(tweets[2]["time"]);
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

function drawScatterChart2() {
    var data = google.visualization.arrayToDataTable(scatterChartData2);

    var options = {
        title: 'Polarity vs. Retweets',
        hAxis: {
        	title: 'Polarity',
        	minValue: 0,
        	maxValue: 1,
        	gridlines: {count : 0}
        },
        vAxis: {
		    title: 'Retweets', 
		    minValue: 0, 
		    maxValue: 30000,
		    gridlines: {count : 0},
		    logScale: true
        },
        legend: 'none',
        backgroundColor: '#F0F0F0',
        pointSize: 3,
        colors: ['#ff9999'],
    };

    var chart = new google.visualization.ScatterChart(document.getElementById('scatterchart2'));
    chart.draw(data, options);
}

function drawScatterChart3() {
    var data = google.visualization.arrayToDataTable(scatterChartData3);

    var options = {
        title: 'Polarity vs. Favorites',
        hAxis: {
        	title: 'Polarity',
        	minValue: 0,
        	maxValue: 1,
        	gridlines: {count : 0}
        },
        vAxis: {
		    title: 'Favorites', 
		    minValue: 0, 
		    maxValue: 30000,
		    gridlines: {count : 0},
		    logScale: true
        },
        legend: 'none',
        backgroundColor: '#F0F0F0',
        pointSize: 3,
        colors: ['#fecc66'],
    };

    var chart = new google.visualization.ScatterChart(document.getElementById('scatterchart3'));
    chart.draw(data, options);
}

function drawComparisonChart() {
	var numPosList = new Array();
	var numNegList = new Array();

	// get all chart keys
	for(var i = 0; i < tweets.length; i++) {
		var chartKey = tweets[i].chartKey;
		if(!(chartKey in numPosList)) {
		    numPosList[chartKey] = 0;
		}
		if(!(chartKey in numNegList)) {
		    numNegList[chartKey] = 0;
		}
	}

	if(numPosList.length != numNegList.length) {
		throw { name: 'FatalError', message: 'Number of items of both charts are different, should not happen!' };
	}

	// count based on chart keys
	for(var i = 0; i < tweets.length; i++) {
		var chartKey = tweets[i].chartKey;
		if(tweets[i].sent == "pos") {
		    if(chartKey in numPosList) {
		        numPosList[chartKey]++;
		    }
		} else if(tweets[i].sent == "neg") {
		    if(chartKey in numNegList) {
		        numNegList[chartKey]++;
		    }
		}
	}
	
	var dataArray = new Array();
    dataArray.push(['Product', 'Positive', 'Negative']);
    for(var key in numPosList) {
        var posPer = parseInt(numPosList[key]) / (parseInt(numPosList[key]) + parseInt(numNegList[key]));
        var negPer = parseInt(numNegList[key]) / (parseInt(numPosList[key]) + parseInt(numNegList[key]));
		posPer = parseFloat(posPer.toFixed(2));
		negPer = parseFloat(negPer.toFixed(2));
		
        dataArray.push([key, posPer, negPer]);
    }
    
    var data = google.visualization.arrayToDataTable(dataArray);

    var options = {
      title: 'Comparison Chart',
      vAxis: {maxValue: 1.0, minValue: 0.0},
      backgroundColor: '#F0F0F0',
      colors: ['#00CC33', '#FE7569']
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('comparisonchart'));

    chart.draw(data, options);
      	
}


google.load("visualization", "1", {packages: ["corechart"]});
google.setOnLoadCallback(drawScatterChart);
google.setOnLoadCallback(drawScatterChart2);
google.setOnLoadCallback(drawScatterChart3);
google.setOnLoadCallback(drawPieChart);
google.setOnLoadCallback(drawAreaChart);
google.setOnLoadCallback(drawComparisonChart);
