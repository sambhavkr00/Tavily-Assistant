sap.ui.define(
  ["sap/ui/core/mvc/Controller", "sap/ui/model/json/JSONModel"],
  function (Controller, JSONModel) {
    "use strict";

    return Controller.extend("curiousai.frontend.controller.App", {
      onInit: function () {
        // Set a default model for the view
        var oModel = new JSONModel({
          prompt: "",
          response: "",
        });
        this.getView().setModel(oModel);
        // Generate a unique session ID for the user
        this.sSessionId = this._generateUUID();
      },

      _generateUUID: function () {
        // A simple UUID generator
        return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(
          /[xy]/g,
          function (c) {
            var r = (Math.random() * 16) | 0,
              v = c === "x" ? r : (r & 0x3) | 0x8;
            return v.toString(16);
          }
        );
      },

      onSendPress: function () {
        var oView = this.getView();
        var oModel = oView.getModel();
        var sPrompt = oView.byId("promptInput").getValue();
        var oLoadingBox = oView.byId("loadingBox");
        var oLoadingStatus = oView.byId("loadingStatus");

        if (!sPrompt) {
          return;
        }

        oModel.setProperty("/response", "");
        oView.byId("responseText").setContent("");
        oLoadingBox.setVisible(true);

        var that = this;
        var i = 0;
        var messages = [
          "Processing request...",
          "Thinking...",
          "Searching...",
          "Extracting information...",
          "Analyzing data...",
          "Compiling results...",
          "Formulating response...",
          "Generating response...",
        ];
        this._interval = setInterval(function () {
          if (i < messages.length) {
            oLoadingStatus.setText(messages[i]);
            i++;
          }
        }, 2000);

        var sBackendUrl = "/api/invoke/";

        fetch(sBackendUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            prompt: sPrompt,
            session_id: this.sSessionId,
          }),
        })
          .then((response) => {
            if (!response.ok) {
              // Handle HTTP errors (like 500) by reading the response text
              return response.text().then(text => {
                throw new Error(`HTTP error! Status: ${response.status}, Body: ${text}`);
              });
            }
            return response.json();
          })
          .then((data) => {
            // Add a fallback to prevent marked() from getting undefined
            var sResponse = data.output ?? data.error ?? "An empty or invalid response was received from the server.";
            var sHtmlResponse = marked.parse(sResponse);
            oModel.setProperty("/response", sHtmlResponse);
          })
          .catch((error) => {
            console.error("Fetch failed:", error);
            var sErrorResponse = marked.parse("Error: " + error.message);
            oModel.setProperty("/response", sErrorResponse);
          })
          .finally(function () {
            clearInterval(that._interval);
            oLoadingBox.setVisible(false);
          });
      },
    });
  }
);
