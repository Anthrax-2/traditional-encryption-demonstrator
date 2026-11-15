"use strict"

const methods = document.querySelector("#methods")
const input = document.querySelector("#input")
const key = document.querySelector("#key")
const output = document.querySelector("#output")

const enterBtn = document.querySelector("#enter")
const swapBtn = document.querySelector("#swap")
const clearAll = document.querySelector("#clear-all")

const errorField = document.querySelector("#error")

const clearInput = document.querySelector("#clear-input")
const clearKey = document.querySelector("#clear-key")
const clearOutput = document.querySelector("#clear-output")


enterBtn.addEventListener("click", async () => {

    const mode = document.querySelector("input[name = 'mode']:checked")

    try {
        const message = {
        method: methods.value,
        input: input.value,
        key: key.value,
        mode: mode.value
        }
        const response = await fetch("/api/process", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(message)
        })
        const data = await response.json()

        if (response.ok) {
            output.value = data["result"]
            errorField.textContent = ""
        } else {
            errorField.textContent = data["error"]
        }
    } catch (error) {

        errorField.textContent = "Cannot reach the server. Check connection."
        errorField.style.color = "rgb(177, 194, 22)"
    }    
})

swapBtn.addEventListener("click", () => {
    input.value = output.value
    output.value = ""
})

clearInput.addEventListener("click", () => {
    input.value = ""
})

clearKey.addEventListener("click", () => {
    key.value = ""
})

clearOutput.addEventListener("click", () => {
    output.value = ""
})

clearAll.addEventListener("click", () => {
    input.value = ""
    key.value = ""
    output.value = ""
})