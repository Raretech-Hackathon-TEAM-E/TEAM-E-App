// チャンネル追加モーダル取得
const addChannelModal = document.getElementById("add-channel-modal");
console.log(addChannelModal);
// チャンネル追加モーダルを開くボタン取得
const addChannelBtn = document.getElementById("add-channel-btn");
console.log(addChannelBtn);
// 追加モーダルクローズボタン取得
const buttonClose = document.getElementById("add-page-close-btn");
// チャンネル削除モーダル取得
/* 削除機能いったんコメントアウト
const deleteChannelModal = document.getElementById("delete-channel-modal");
// チャンネル削除モーダルを開くボタン取得
const deleteChannelBtn = document.getElementById("delete-channel-btn");
// 削除モーダルクローズボタン取得
const deleteClose = document.getElementById("delete-page-close-btn");

*/

// モーダルを開く
// <button id="add-channel-btn">チャンネル追加</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", modalOpen);
function modalOpen() {
  addChannelModal.style.display = "block";
}

/*
deleteChannelBtn.addEventListener("click", modalOpen);
function modalOpen() {
  deleteChannelModal.style.display = "block";
}
*/

buttonClose.addEventListener("click", modalClose);
function modalClose() {
  addChannelModal.style.display = "none";
}

/*
deleteClose.addEventListener("click", modalClose);
function modalClose() {
  deleteChannelModal.style.display = "none";
}
*/

addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == addChannelModal) {
    addChannelModal.style.display = "none";
  }
}