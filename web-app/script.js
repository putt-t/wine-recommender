
async function fetchFormData() {
    const response = await fetch("/form-data");
    return await response.json();
}


async function generateForm() {
    const formData = await fetchFormData();
    const form = document.getElementById("preferencesForm");

    for (const [key, value] of Object.entries(formData)) {
        const label = document.createElement("label");
        label.setAttribute("for", key);
        label.textContent = key + ":";

        let input;
        if (Array.isArray(value)) {
            input = document.createElement("select");
            input.setAttribute("id", key);
            input.setAttribute("name", key);
            value.forEach(option => {
                const optionElement = document.createElement("option");
                optionElement.value = option;
                optionElement.textContent = option;
                input.appendChild(optionElement);
            });
        } else if (typeof value === "object") {
            input = document.createElement("input");
            input.setAttribute("type", "range");
            input.setAttribute("id", key);
            input.setAttribute("name", key);
            input.setAttribute("min", value.min);
            input.setAttribute("max", value.max);
            input.setAttribute("step", value.step);
            input.setAttribute("value", (value.min + value.max) / 2);
        }

        form.appendChild(label);
        form.appendChild(input);
        form.appendChild(document.createElement("br"));
    }
}


document.getElementById("submitButton").addEventListener("click", () => {
    const form = document.getElementById("preferencesForm");
    const formData = new FormData(form);
    const preferences = {};
    for (const [key, value] of formData.entries()) {
        preferences[key] = value;
    }
    console.log("User Preferences:", preferences);
    alert("Preferences submitted!");
});


generateForm();