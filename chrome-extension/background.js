chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "runAutomation",
        title: "Run Automation",
        contexts: ["all"]
    });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "runAutomation") {
        fetch("http://127.0.0.1:5000/run-automation")
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error("Error:", error));
    }
});
