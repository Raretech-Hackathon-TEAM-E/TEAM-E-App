const updateButton = document.getElementById("channel-update");
const updateChannelModal = document.getElementById("update-channel-modal");
const updatePageButtonClose = document.getElementById("update-page-close-btn");

const updateChannel = () => {
  if (uid !== channel.uid) {
    return;
  } else {
    modalOpen("update");
  }
};

function modalOpen(mode) {
  if (mode === "update") {
    updateChannelModal.style.display = "block";
  }
}


updateButton.addEventListener("click", updateChannel);



updatePageButtonClose.addEventListener("click", () => {
  modalClose("update");
});

function modalClose(mode) {
  if (mode === "update") {
    updateChannelModal.style.display = "none"; 
  }
}

addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == updateChannelModal) {
    updateChannelModal.style.display = "none";
  }
}