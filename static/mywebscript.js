function RunSentimentAnalysis() {

    const textInput = document.getElementById("textToAnalyze");
    const resultBox = document.getElementById("system_response");
    const button = document.getElementById("analyzeButton");
    const buttonText = document.getElementById("buttonText");

    const textToAnalyze = textInput.value.trim();

    if (textToAnalyze === "") {
        resultBox.innerHTML = `
            <div class="empty-result">
                <div class="empty-icon">⚠</div>
                <h3>Please enter some text</h3>
                <p>Write a statement before running the emotion analysis.</p>
            </div>
        `;
        return;
    }

    button.disabled = true;
    buttonText.textContent = "Analyzing...";

    resultBox.innerHTML = `
        <div class="empty-result">
            <div class="empty-icon">◌</div>
            <h3>Analyzing your statement...</h3>
            <p>Watson NLP is processing your text.</p>
        </div>
    `;

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {

        if (this.readyState === 4) {

            button.disabled = false;
            buttonText.textContent = "Analyze Emotion";

            if (this.status === 200) {
                resultBox.innerHTML = this.responseText;
            } else {
                resultBox.innerHTML = `
                    <div class="empty-result">
                        <div class="empty-icon">⚠</div>
                        <h3>Something went wrong</h3>
                        <p>Unable to analyze the statement. Please try again.</p>
                    </div>
                `;
            }
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" +
        encodeURIComponent(textToAnalyze),
        true
    );

    xhttp.send();
}


/* Character counter */

document.addEventListener("DOMContentLoaded", function () {

    const textInput = document.getElementById("textToAnalyze");
    const counter = document.getElementById("characterCount");

    textInput.addEventListener("input", function () {
        counter.textContent = `${textInput.value.length} characters`;
    });

});
