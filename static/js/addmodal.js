const Modal = document.querySelector(".modal");
const addChannelBtn = document.querySelector("#add-channel-btn");
const buttonClose = document.querySelector(".modalClose");
const deleteChannelBtn = document.querySelector(".delete-channel-btn");

// モーダルを開く
// <button id="add-channel-btn">チャンネル追加</button>ボタンがクリックされた時
addChannelBtn.addEventListener('click', modalOpen);
function modalOpen() {
  modal.style.display = 'block';
}

buttonClose.addEventListener('click', modalClose);
function modalClose() {
  modal.style.display = 'none';
}

addEventListener('click', outsideClose);
function outsideClose(e) {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
}