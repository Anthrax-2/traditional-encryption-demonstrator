"use strict"


const methods = document.querySelector("#methods")
const input = document.querySelector("#input")
const key = document.querySelector("#key")
const output = document.querySelector("#output")

const enterBtn = document.querySelector("#enter")

const errorField = document.querySelector("#error")


enterBtn.addEventListener("click", async () => {

    const mode = document.querySelector("input[name = 'mode']:checked")

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
        errorField.innerHTML = ""
    } else {
        errorField.innerHTML = data["error"]
    }
    
})