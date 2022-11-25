// チャンネル追加モーダル取得
const addChannelModal = document.getElementById("add-channel-modal");
// チャンネル追加モーダルを開くボタン取得
const addChannelBtn = document.getElementById("add-channel-btn");
// 追加モーダルクローズボタン取得
const addPageButtonClose = document.getElementById("add-page-close-btn");

// チャンネル削除モーダル取得
const deleteChannelModal = document.getElementById("delete-channel-modal");
// チャンネル削除モーダルを開くボタン取得
const deleteChannelBtn = document.getElementById("delete-channel-btn");
// 削除モーダルクローズボタン取得
const deletePageButtonClose = document.getElementById("delete-page-close-btn");

//update


addChannelBtn.addEventListener("click", () => {
  modalOpen("add");
});

function modalOpen(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "block";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "block";
  } else if (mode === "update") {
    updateChannelModal.style.display = "block";
  }
}

// モーダル内のバツ印がクリックされた時
addPageButtonClose.addEventListener("click", () => {
  modalClose("add");
});
deletePageButtonClose.addEventListener("click", () => {
  modalClose("delete");
});
updatePageButtonClose.addEventListener("click", () => {
  modalClose("update");
});

function modalClose(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "none";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "none";
  } else if (mode === "update") {
    updateChannelModal.style.display = "none";
  }
}

/*
// モーダルを開く
// <button id="add-channel-btn">チャンネル追加</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", modalOpen);
function modalOpen() {
  addChannelModal.style.display = "block";
}


deleteChannelBtn.addEventListener("click", modalOpen);
function modalOpen() {
  deleteChannelModal.style.display = "block";
}
*/


// モーダルコンテンツ以外がクリックされた時
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == addChannelModal) {
    addChannelModal.style.display = "none";
  } else if (e.target == deleteChannelModal) {
    deleteChannelModal.style.display = "none";
  }
}