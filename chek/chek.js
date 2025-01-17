var startDate = new Date("1999-11-01");
var endDate = new Date("2024-04-24");

endDate.setDate(endDate.getDate() + 30);

// Array to hold the dates within the range
var dateRange = [];

// Loop through the dates from start to end and push them to the array
var currentDate = new Date(startDate);
while (currentDate <= endDate) {
    dateRange.push(new Date(currentDate));
    currentDate.setDate(currentDate.getDate() + 1); // Increment to the next day
}

console.log(dateRange[8973])