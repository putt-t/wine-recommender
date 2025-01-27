// Wait for DOM to load
document.addEventListener("DOMContentLoaded", async () => {
    try {
      await generateForm();
    } catch (error) {
      console.error("Error generating form:", error);
    }
  });
  
  async function fetchFormData() {
    try {
      const response = await fetch("/form-data");
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error("Error fetching form data:", error);
      throw error;
    }
  }
  
  async function generateForm() {
    const formData = await fetchFormData();
    const form = document.getElementById("preferencesForm");
  
    if (!form) {
      console.error("Form element not found!");
      return;
    }
  
    // Add form elements
    for (const [key, value] of Object.entries(formData)) {
      const formGroup = document.createElement("div");
      formGroup.className = "form-group";
  
      const label = document.createElement("label");
      label.setAttribute("for", key);
      label.textContent = key + ":";
  
      let input;
      if (Array.isArray(value)) {
        input = document.createElement("select");
        input.setAttribute("id", key);
        input.setAttribute("name", key);
        value.forEach((option) => {
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
  
      formGroup.appendChild(label);
      formGroup.appendChild(input);
      form.appendChild(formGroup);
    }
  
    // Add submit button
    const submitButton = document.createElement("button");
    submitButton.setAttribute("type", "submit");
    submitButton.setAttribute("id", "submitButton");
    submitButton.textContent = "Submit";
    form.appendChild(submitButton);
  
    // Add form submit handler
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const formData = new FormData(form);
      const preferences = Object.fromEntries(formData.entries());
      console.log("User Preferences:", preferences);
      alert("Preferences submitted!");
    });
  }
  