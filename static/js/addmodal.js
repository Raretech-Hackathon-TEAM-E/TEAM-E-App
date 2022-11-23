// チャンネル追加モーダル取得
const addChannelModal = document.getElementById("add-channel-modal");
console.log(addChannelModal);
// チャンネル追加モーダルを開くボタン取得
const addChannelBtn = document.getElementById("add-channel-btn");
console.log(addChannelBtn);
// 追加モーダルクローズボタン取得
const buttonClose = document.getElementById("add-page-close-btn");


// モーダルを開く
// <button id="add-channel-btn">チャンネル追加</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", modalOpen);
function modalOpen() {
  addChannelModal.style.display = "block";
}

buttonClose.addEventListener("click", modalClose);
function modalClose() {
  addChannelModal.style.display = "none";
}

addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == addChannelModal) {
    addChannelModal.style.display = "none";
  }
}