// Step 1: Initialize Tooltip
var toolTip = d3.tip()
.attr("class", "tooltip")
.offset([80, -60])
.html(function(d) {
  return (`<strong>${(d.pounds)}<strong><hr>${d.candy}
  `);
});

// Step 2: Create the tooltip in chartGroup.
svg.call(toolTip);

// Step 3: Create "mouseover" event listener to display tooltip
arc.on("mouseover", function(d) {
toolTip.show(d, this);
})
// Step 4: Create "mouseout" event listener to hide tooltip
.on("mouseout", function(d) {
  toolTip.hide(d);
});
