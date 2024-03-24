// script.js
function getRecommendations() {
    var prompt = document.getElementById("prompt").value;
    $.ajax({
        type: "POST",
        url: "/recommend",
        data: { prompt: prompt },
        success: function(response) {
            document.getElementById("result").innerHTML = "<h2>Recommended Food:</h2><p>" + response + "</p>";
        }
    });
}
