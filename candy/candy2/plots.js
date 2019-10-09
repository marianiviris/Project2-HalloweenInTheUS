
var mainData;
var promises = [];
function init() {
  promises.push(d3.csv("state-candy.csv"));
  Promise.all(promises).then(function (fullData) {
    mainData = fullData[0];
    mainData.forEach(d => {
      d["Top Candy pounds"] = +d["Top Candy pounds"];
      console.log(d["Top Candy pounds"]);
      d["2nd Candy pounds"] = +d["2nd Candy pounds"];
      d["3rd Candy pounds"] = +d["3rd Candy pounds"];
      //The next four don't change anything so are redundant.
      //mainData["State"] = mainData["State"];
      //mainData["Top Candy"] = mainData["Top Candy"];
      //mainData["2nd Place"] = mainData["2nd Place"];
      //mainData["3rd Place"] = mainData["3rd Place"];
    });

    // Initializes the page with a default plot
    var trace1 = {
      x: GetArrayFromMainData("State"),
      y: GetArrayFromMainData("Top Candy pounds"),
      type: "scatter",
      mode: "markers"
    };
    var data = [trace1];
    Plotly.newPlot("plot", data);
  });
};

// Call updatePlotly() when a change takes place to the DOM
d3.selectAll("#selDataset").on("change", updatePlotly);

// This function is called when a dropdown menu item is selected
function updatePlotly() {
  // Use D3 to select the dropdown menu
  var dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  var dataset = dropdownMenu.property("value");
  console.log(dataset);

  // Initialize x and y arrays
  //var x = [];
  var y = [];

  if (dataset == 'dataset1') {
    //x = GetArrayFromMainData("State");
    y = GetArrayFromMainData("Top Candy pounds");
  }

  if (dataset == 'dataset2') {
    //x = GetArrayFromMainData("State");
    y = GetArrayFromMainData("2nd Place pounds");
  }

  if (dataset == 'dataset3') {
    //x = GetArrayFromMainData("State");
    y = GetArrayFromMainData("3rd Place pounds");
  }
  // Note the extra brackets around 'x' and 'y'
  //Plotly.restyle("plot", "x", [x]);
  var update = { y: [y] };
  Plotly.restyle("plot", update);
}

function GetArrayFromMainData(field) {
  var arr = [];
  mainData.forEach(d => {
    arr.push(d[field]);
  });
  return arr;
};

init();
