let chartInstance = null;

async function predict() {
    let hours = document.getElementById("hours").value;
    let attendance = document.getElementById("attendance").value;

    if (!hours || !attendance) {
        alert("Fill all fields!");
        return;
    }

    document.getElementById("result").innerText = "⏳ Predicting...";

    let response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            hours: hours,
            attendance: attendance
        })
    });

    let data = await response.json();

    let prediction = data.prediction;

    document.getElementById("result").innerText =
        "📈 Predicted Marks: " + prediction;

    drawChart(hours, attendance, prediction);
}

/* Chart function */
function drawChart(hours, attendance, marks) {
    let ctx = document.getElementById("chart").getContext("2d");

    if (chartInstance) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Hours", "Attendance", "Marks"],
            datasets: [{
                label: "Student Data",
                data: [hours, attendance, marks]
            }]
        }
    });
}

/* Theme toggle */
function toggleTheme() {
    document.body.classList.toggle("light");
}